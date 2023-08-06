# -*- coding: utf-8 -*-
#
#  sourceform.py
#  This file is part of FORD.
#
#  Copyright 2014 Christopher MacMackin <cmacmackin@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

from collections import defaultdict
from dataclasses import dataclass
import sys
import re
import os.path
import copy
import textwrap
from typing import List, Tuple, Optional, Union, Sequence, Dict
from itertools import chain

# Python 2 or 3:
if sys.version_info[0] > 2:
    from urllib.parse import quote
else:
    from urllib import quote

import toposort
from pygments import highlight
from pygments.lexers import FortranLexer, FortranFixedLexer, guess_lexer_for_filename
from pygments.formatters import HtmlFormatter

import ford.reader
import ford.utils
from ford.intrinsics import INTRINSICS

VAR_TYPE_STRING = r"^integer|real|double\s*precision|character|complex|double\s*complex|logical|type|class|procedure|enumerator"
VARKIND_RE = re.compile(r"\((.*)\)|\*\s*(\d+|\(.*\))")
KIND_RE = re.compile(r"kind\s*=\s*([^,\s]+)", re.IGNORECASE)
KIND_SUFFIX_RE = re.compile(r"(?P<initial>.*)_(?P<kind>[a-z]\w*)", re.IGNORECASE)
CHAR_KIND_SUFFIX_RE = re.compile(r"(?P<kind>[a-z]\w*)_(?P<initial>.*)", re.IGNORECASE)
LEN_RE = re.compile(r"(?:len\s*=\s*(\w+|\*|:|\d+)|(\d+))", re.IGNORECASE)
ATTRIBSPLIT_RE = re.compile(r",\s*(\w.*?)::\s*(.*)\s*")
ATTRIBSPLIT2_RE = re.compile(r"\s*(::)?\s*(.*)\s*")
ASSIGN_RE = re.compile(r"(\w+\s*(?:\([^=]*\)))\s*=(?!>)(?:\s*([^\s]+))?")
POINT_RE = re.compile(r"(\w+\s*(?:\([^=>]*\)))\s*=>(?:\s*([^\s]+))?")
EXTENDS_RE = re.compile(r"extends\s*\(\s*([^()\s]+)\s*\)", re.IGNORECASE)
DOUBLE_PREC_RE = re.compile(r"double\s+precision", re.IGNORECASE)
DOUBLE_CMPLX_RE = re.compile(r"double\s+complex", re.IGNORECASE)
QUOTES_RE = re.compile(r"\"([^\"]|\"\")*\"|'([^']|'')*'", re.IGNORECASE)
PARA_CAPTURE_RE = re.compile(r"<p>.*?</p>", re.IGNORECASE | re.DOTALL)
COMMA_RE = re.compile(r",(?!\s)")
NBSP_RE = re.compile(r" (?= )|(?<= ) ")
DIM_RE = re.compile(r"^\w+\s*(\(.*\))\s*$")


base_url = ""


class FortranBase:
    """
    An object containing the data common to all of the classes used to represent
    Fortran data.
    """

    IS_SPOOF = False

    POINTS_TO_RE = re.compile(r"\s*=>\s*", re.IGNORECASE)
    SPLIT_RE = re.compile(r"\s*,\s*", re.IGNORECASE)
    SRC_CAPTURE_STR = r"^[ \t]*([\w(),*: \t]+?[ \t]+)?{0}([\w(),*: \t]+?)?[ \t]+{1}[ \t\n,(].*?end[ \t]*{0}[ \t]+{1}[ \t]*?(!.*?)?$"

    # ~ this regex is not working for the LINK and DOUBLE_LINK types

    base_url = ""
    pretty_obj = {
        "proc": "procedures",
        "type": "derived types",
        "sourcefile": "source files",
        "program": "programs",
        "module": "modules and submodules",
        "submodule": "modules and submodules",
        "interface": "abstract interfaces",
        "blockdata": "block data units",
    }

    def __init__(
        self, source, first_line, parent=None, inherited_permission="public", strings=[]
    ):
        self.visible = False
        self.permission = inherited_permission.lower()
        self.strings = strings
        self.parent = parent
        if self.parent:
            self.parobj = self.parent.obj
            self.display = self.parent.display
            self.settings = self.parent.settings
        else:
            self.parobj = None
            self.display = None
            self.settings = None
        self.obj = type(self).__name__[7:].lower()
        if (
            self.obj == "subroutine"
            or self.obj == "function"
            or self.obj == "submoduleprocedure"
        ):
            self.obj = "proc"
        self._initialize(first_line)
        del self.strings
        self.doc = []
        line = source.__next__()
        while line[0:2] == "!" + self.settings["docmark"]:
            self.doc.append(line[2:])
            line = source.__next__()
        source.pass_back(line)
        self.hierarchy = []
        cur = self.parent
        while cur:
            self.hierarchy.append(cur)
            cur = cur.parent
        self.hierarchy.reverse()

    @property
    def filename(self) -> str:
        """Name of the file containing this entity"""
        # If `hierarchy` is empty, it's probably because it's a source
        # file, so we can use its name directly
        return self.hierarchy[0].name if self.hierarchy else self.name

    def get_dir(self) -> Optional[str]:
        if isinstance(
            self,
            (
                FortranSourceFile,
                FortranProgram,
                FortranModule,
                GenericSource,
                FortranBlockData,
            ),
        ) or (
            isinstance(
                self,
                (
                    FortranType,
                    FortranInterface,
                    FortranProcedure,
                    FortranSubmoduleProcedure,
                ),
            )
            and isinstance(
                self.parent,
                (
                    FortranSourceFile,
                    FortranProgram,
                    FortranModule,
                    FortranSubmodule,
                    FortranBlockData,
                ),
            )
        ):
            return self.obj

        return None

    def get_url(self):
        if hasattr(self, "external_url"):
            return self.external_url
        outstr = "{0}/{1}/{2}.html"
        loc = self.get_dir()
        if loc:
            return outstr.format(self.base_url, loc, quote(self.ident))
        if isinstance(
            self,
            (
                FortranBoundProcedure,
                FortranCommon,
                FortranVariable,
                FortranEnum,
                FortranFinalProc,
            ),
        ):
            parent_url = self.parent.get_url()
            if parent_url:
                return f"{parent_url}#{self.anchor}"
            return None
        return None

    def lines_description(self, total, total_all=0, obj=None):
        if not obj:
            obj = self.obj
        description = "{:4.1f}% of total for {}.".format(
            float(self.num_lines) / total * 100, self.pretty_obj[obj]
        )
        if total_all:
            description = (
                "<p>"
                + description
                + "</p>Including implementation: {} statements, {:4.1f}% of total for {}.".format(
                    self.num_lines_all,
                    float(self.num_lines_all) / total_all * 100,
                    self.pretty_obj[obj],
                )
            )
        return description

    @property
    def ident(self) -> str:
        """Return a unique identifier for this object"""
        return namelist.get_name(self)

    @property
    def anchor(self) -> str:
        """Return a string suitable for an HTML anchor link"""
        return f"{self.obj}-{quote(self.ident)}"

    def __str__(self):
        url = self.get_url()
        if url and getattr(self, "visible", True):
            name = self.name or "<em>unnamed</em>"
            return f"<a href='{url}'>{name}</a>"
        return self.name or ""

    def __lt__(self, other):
        """
        Compare two Fortran objects. Needed to make toposort work.
        """
        return self.ident < other.ident

    def _ensure_meta_key_set(self, key: str, transform=None, default=None):
        """Ensure that ``key`` is set in ``self.meta``, after applying
        an optional ``transform``.

        Use ``default`` if ``key`` is not in ``self.settings``.
        """
        value = self.meta.get(key, self.settings.get(key, default))
        if transform:
            self.meta[key] = transform(value)
        else:
            self.meta[key] = value

    def markdown(self, md, project):
        """
        Process the documentation with Markdown to produce HTML.
        """
        if len(self.doc) > 0:
            # Remove any common leading whitespace from the docstring
            # so that the markdown conversion is a bit more robust
            self.doc = textwrap.dedent("\n".join(self.doc)).splitlines()

            if len(self.doc) == 1 and ":" in self.doc[0]:
                words = self.doc[0].split(":")[0].strip()
                if words.lower() not in [
                    "author",
                    "date",
                    "license",
                    "version",
                    "category",
                    "summary",
                    "deprecated",
                    "display",
                    "graph",
                ]:
                    self.doc.insert(0, "")
                self.doc.append("")
            self.doc = "\n".join(self.doc)
            self.doc = md.reset().convert(self.doc)
            self.meta = md.Meta
        else:
            if (
                self.settings["warn"]
                and self.obj != "sourcefile"
                and self.obj != "genericsource"
            ):
                # TODO: Add ability to print line number where this item is in file
                print(
                    "Warning: Undocumented {} {} in file {}".format(
                        self.obj, self.name, self.hierarchy[0].name
                    )
                )
            self.doc = ""
            self.meta = {}

        if self.parent:
            self.display = self.parent.display

        # ~ print (self.meta)
        for key in self.meta:
            # ~ print(key, self.meta[key])
            if key == "display":
                tmp = [item.lower() for item in self.meta[key]]
                if type(self) == FortranSourceFile:
                    while "none" in tmp:
                        tmp.remove("none")
                if len(tmp) == 0:
                    pass
                elif "none" in tmp:
                    self.display = []
                elif (
                    "public" not in tmp
                    and "private" not in tmp
                    and "protected" not in tmp
                ):
                    pass
                else:
                    self.display = tmp
            elif len(self.meta[key]) == 1:
                self.meta[key] = self.meta[key][0]
            elif key == "summary":
                self.meta[key] = "\n".join(self.meta[key])
        if hasattr(self, "num_lines"):
            self.meta["num_lines"] = self.num_lines

        self.doc = ford.utils.sub_macros(ford.utils.sub_notes(self.doc))

        if self.meta.get("summary", None) is not None:
            self.meta["summary"] = md.convert(self.meta["summary"])
            self.meta["summary"] = ford.utils.sub_macros(
                ford.utils.sub_notes(self.meta["summary"])
            )
        elif PARA_CAPTURE_RE.search(self.doc):
            if self.get_url() is None:
                # There is no stand-alone webpage for this item (e.g.,
                # an internal routine in a routine, so make the whole
                # doc blob appear, without the link to "more..."
                self.meta["summary"] = self.doc
            else:
                self.meta["summary"] = PARA_CAPTURE_RE.search(self.doc).group()
        else:
            self.meta["summary"] = ""
        if self.meta["summary"].strip() != self.doc.strip():
            self.meta[
                "summary"
            ] += '<a href="{}" class="pull-right"><emph>Read more&hellip;</emph></a>'.format(
                self.get_url()
            )

        self._ensure_meta_key_set("graph", ford.utils.str_to_bool)
        self._ensure_meta_key_set("graph_maxdepth")
        self._ensure_meta_key_set("graph_maxnodes")
        self._ensure_meta_key_set("deprecated", ford.utils.str_to_bool, False)

        if self.obj in ["proc", "type", "program"]:
            self._ensure_meta_key_set("source", ford.utils.str_to_bool)
            if self.meta["source"]:
                if self.obj == "proc":
                    obj = self.proctype.lower()
                else:
                    obj = self.obj
                regex = re.compile(
                    self.SRC_CAPTURE_STR.format(obj, self.name),
                    re.IGNORECASE | re.DOTALL | re.MULTILINE,
                )
                if match := regex.search(self.hierarchy[0].raw_src):
                    self.src = highlight(match.group(), FortranLexer(), HtmlFormatter())
                else:
                    self.src = ""
                    if self.settings["warn"]:
                        print(
                            "Warning: Could not extract source code for {} {} in file {}".format(
                                self.obj, self.name, self.hierarchy[0].name
                            )
                        )

        if self.obj == "proc":
            self._ensure_meta_key_set("proc_internals", ford.utils.str_to_bool)

        # Create Markdown
        for item in self.children:
            if isinstance(item, FortranBase):
                item.markdown(md, project)

    def sort_components(self):
        """Sorts components using the method specified in the object
        meta/project settings

        """

        def permission(item):
            permission_type = getattr(item, "permission", "default")
            sorting = {"default": 0, "public": 1, "protected": 2, "private": 3}
            return sorting[permission_type]

        def fortran_type_name(item):
            if item.obj == "variable":
                retstr = item.vartype
                if retstr == "class":
                    retstr = "type"
                if item.kind:
                    retstr += f"-{item.kind}"
                if item.strlen:
                    retstr += f"-{item.strlen}"
                if item.proto:
                    retstr += f"-{item.proto[0]}"
                return retstr
            if item.obj == "proc":
                return_var = (
                    f"-{fortran_type_name(item.retvar)}"
                    if item.proctype == "Function"
                    else ""
                )
                return f"{item.proctype.lower()}{return_var}"

            return item.obj

        SORT_KEY_FUNCTIONS = {
            "alpha": lambda item: item.name,
            "permission": permission,
            "permission-alpha": lambda item: f"{permission(item)}-{item.name}",
            "type": fortran_type_name,
            "type-alpha": lambda item: f"{fortran_type_name(item)}-{item.name}",
            "src": None,
        }

        sort_key = SORT_KEY_FUNCTIONS[self.settings["sort"].lower()]
        if sort_key is None:
            return

        for entities in [
            "variables",
            "modules",
            "submodules",
            "common",
            "subroutines",
            "modprocedures",
            "functions",
            "interfaces",
            "absinterfaces",
            "types",
            "programs",
            "blockdata",
            "boundprocs",
            "finalprocs",
        ]:
            entity = getattr(self, entities, [])
            entity.sort(key=sort_key)

    def make_links(self, project):
        """
        Process intra-site links to documentation of other parts of the program.
        """
        self.doc = ford.utils.sub_links(self.doc, project)
        if self.meta.get("summary", None) is not None:
            self.meta["summary"] = ford.utils.sub_links(self.meta["summary"], project)

        # Create links in the project
        for item in self.children:
            if isinstance(item, FortranBase) and hasattr(item, "doc"):
                item.make_links(project)

    @property
    def routines(self):
        """Iterator returning all procedures"""
        return self.iterator("functions", "subroutines", "modprocedures")

    def iterator(self, *argv):
        """Iterator returning any list of elements via attribute lookup in ``self``

        This iterator retains the order of the arguments"""
        for arg in argv:
            if hasattr(self, arg):
                for item in getattr(self, arg):
                    yield item

    @property
    def children(self):
        """Iterator over all child entities"""

        non_list_children = ["constructor", "procedure", "retvar"]

        return chain(
            self.iterator(
                "absinterfaces",
                "args",
                "blockdata",
                "bindings",
                "boundprocs",
                "common",
                "enums",
                "finalprocs",
                "functions",
                "interfaces",
                "modprocedures",
                "modules",
                "programs",
                "submodules",
                "subroutines",
                "types",
                "variables",
            ),
            filter(None, (getattr(self, item, None) for item in non_list_children)),
        )

    def _should_display(self, item) -> bool:
        """Return True if item should be displayed"""
        if self.settings["hide_undoc"] and not item.doc:
            return False
        return item.permission in self.display

    def filter_display(self, collection: Sequence) -> List:
        """Remove items from collection if they shouldn't be displayed"""

        return [obj for obj in collection if self._should_display(obj)]


class FortranContainer(FortranBase):
    """
    A class on which any classes requiring further parsing are based.
    """

    ATTRIB_RE = re.compile(
        r"^(asynchronous|allocatable|bind\s*\(.*\)|data|dimension|external|intent\s*\(\s*\w+\s*\)|optional|parameter|"
        r"pointer|private|protected|public|save|target|value|volatile)(?:\s+|\s*::\s*)((/|\(|\w).*?)\s*$",
        re.IGNORECASE,
    )
    END_RE = re.compile(
        r"^end\s*(?:(module|submodule|subroutine|function|procedure|program|type|interface|enum|block\sdata|block|associate)(?:\s+(\w.*))?)?$",
        re.IGNORECASE,
    )
    BLOCK_RE = re.compile(r"^(\w+\s*:)?\s*block\s*$", re.IGNORECASE)
    BLOCK_DATA_RE = re.compile(r"^block\s*data\s*(\w+)?\s*$", re.IGNORECASE)
    ASSOCIATE_RE = re.compile(r"^(\w+\s*:)?\s*associate\s*\((.+)\)\s*$", re.IGNORECASE)
    ENUM_RE = re.compile(r"^enum\s*,\s*bind\s*\(.*\)\s*$", re.IGNORECASE)
    MODPROC_RE = re.compile(
        r"^(module\s+)?procedure\s*(?:::|\s)\s*(\w.*)$", re.IGNORECASE
    )
    MODULE_RE = re.compile(r"^module(?:\s+(\w+))?$", re.IGNORECASE)
    SUBMODULE_RE = re.compile(
        r"""^submodule\s*
        \(\s*(?P<ancestor_module>\w+)\s*         # Non-optional ancestor module
        (?::\s*(?P<parent_submod>\w+))?\s*\)  # Optional parent submodule
        \s*(?P<name>\w+)                      # This submodule's name
        $""",
        re.IGNORECASE | re.VERBOSE,
    )
    PROGRAM_RE = re.compile(r"^program(?:\s+(\w+))?$", re.IGNORECASE)
    SUBROUTINE_RE = re.compile(
        r"""^\s*(?:(?P<attributes>.+?)\s+)?     # Optional attributes
        subroutine\s+(?P<name>\w+)\s*           # Required subroutine name
        (?P<arguments>\([^()]*\))?              # Optional arguments
        (?:\s*bind\s*\(\s*(?P<bindC>.*)\s*\))?$ # Optional C-binding""",
        re.IGNORECASE | re.VERBOSE,
    )
    FUNCTION_RE = re.compile(
        r"""^(?:(?P<attributes>.+?)\s+)?               # Optional attributes (including type)
        function\s+(?P<name>\w+)\s*                    # Required function name
        (?P<arguments>\([^()]*\))?                     # Required arguments
        (?=(?:.*result\s*\(\s*(?P<result>\w+)\s*\))?)  # Optional result name
        (?=(?:.*bind\s*\(\s*(?P<bindC>.*)\s*\))?).*$   # Optional C-binding""",
        re.IGNORECASE | re.VERBOSE,
    )
    TYPE_RE = re.compile(
        r"^type(?:\s+|\s*(,.*)?::\s*)((?!(?:is\s*\())\w+)\s*(\([^()]*\))?\s*$",
        re.IGNORECASE,
    )
    INTERFACE_RE = re.compile(r"^(abstract\s+)?interface(?:\s+(.+))?$", re.IGNORECASE)
    BOUNDPROC_RE = re.compile(
        r"""^(?P<generic>generic|procedure)\s*  # Required keyword
        (?P<prototype>\([^()]*\))?\s*           # Optional interface name
        (?:,\s*(?P<attributes>\w[^:]*))?        # Optional list of attributes
        (?:\s*::)?\s*                           # Optional double-colon
        (?P<names>\w.*)$                        # Required name(s)
        """,
        re.IGNORECASE | re.VERBOSE,
    )
    COMMON_RE = re.compile(r"^common(?:\s*/\s*(\w+)\s*/\s*|\s+)(\w+.*)", re.IGNORECASE)
    COMMON_SPLIT_RE = re.compile(r"\s*(/\s*\w+\s*/)\s*", re.IGNORECASE)
    FINAL_RE = re.compile(r"^final\s*::\s*(\w.*)", re.IGNORECASE)
    USE_RE = re.compile(
        r"^use(?:\s*(?:,\s*(?:non_)?intrinsic\s*)?::\s*|\s+)(\w+)\s*($|,.*)",
        re.IGNORECASE,
    )
    ARITH_GOTO_RE = re.compile(r"go\s*to\s*\([0-9,\s]+\)", re.IGNORECASE)
    CALL_RE = re.compile(
        r"(?:^|[^a-zA-Z0-9_% ]\s*(?:\w+%)?)(\w+)(?=\s*\(\s*(?:.*?)\s*\))", re.IGNORECASE
    )
    SUBCALL_RE = re.compile(
        r"^(?:if\s*\(.*\)\s*)?call\s+(?:\w+%)?(\w+)\s*(?:\(\s*(.*?)\s*\))?$",
        re.IGNORECASE,
    )
    FORMAT_RE = re.compile(r"^[0-9]+\s+format\s+\(.*\)", re.IGNORECASE)

    VARIABLE_STRING = (
        r"^(integer|real|double\s*precision|character|complex|double\s*complex|logical|type(?!\s+is)|class(?!\s+is|\s+default)|"
        r"procedure|enumerator{})\s*((?:\(|\s\w|[:,*]).*)$"
    )

    def __init__(
        self, source, first_line, parent=None, inherited_permission="public", strings=[]
    ):
        self.num_lines = 0
        if not isinstance(self, FortranSourceFile):
            self.num_lines += 1
        if type(self) != FortranSourceFile:
            FortranBase.__init__(
                self, source, first_line, parent, inherited_permission, strings
            )
        incontains = False
        if type(self) is FortranSubmodule:
            self.permission = "private"

        typestr = ""
        for vtype in self.settings["extra_vartypes"]:
            typestr = typestr + "|" + vtype
        self.VARIABLE_RE = re.compile(
            self.VARIABLE_STRING.format(typestr), re.IGNORECASE
        )

        # This is a little bit confusing, because `permission` here is sort of
        # overloaded for "permission for this entity", and "permission for child
        # entities". For example, the former doesn't apply to modules or programs,
        # while for procedures _only_ the first applies. For things like types, we
        # need to keep track of these meanings separately. Also note that
        # `child_permission` for types can be different for components and bound
        # procedures, but luckily they cannot be mixed in the source, so we don't
        # need to actually track `child_permission` separately for them both
        child_permission = (
            "public" if isinstance(self, FortranType) else self.permission
        )

        blocklevel = 0
        associatelevel = 0
        for line in source:
            if line[0:2] == "!" + self.settings["docmark"]:
                self.doc.append(line[2:])
                continue
            if line.strip() != "":
                self.num_lines += 1

            # Temporarily replace all strings to make the parsing simpler
            self.strings = []
            search_from = 0
            while quote := QUOTES_RE.search(line[search_from:]):
                self.strings.append(quote.group())
                line = line[0:search_from] + QUOTES_RE.sub(
                    '"{}"'.format(len(self.strings) - 1), line[search_from:], count=1
                )
                search_from += QUOTES_RE.search(line[search_from:]).end(0)

            # Cache the lowercased line
            line_lower = line.lower()

            if self.settings["lower"]:
                line = line_lower

            # Check the various possibilities for what is on this line
            if line_lower == "contains":
                if not incontains and isinstance(self, _can_have_contains):
                    incontains = True
                    if isinstance(self, FortranType):
                        child_permission = "public"
                elif incontains:
                    self.print_error(line, "Multiple CONTAINS statements present")
                else:
                    self.print_error(line, "Unexpected CONTAINS statement")
            elif line_lower in ["public", "private", "protected"]:
                child_permission = line_lower
                if not isinstance(self, FortranType):
                    self.permission = line_lower
            elif line_lower == "sequence":
                if type(self) == FortranType:
                    self.sequence = True
            elif self.FORMAT_RE.match(line):
                # There's nothing interesting for us in a format statement
                continue
            elif (match := self.ATTRIB_RE.match(line)) and blocklevel == 0:
                attr = match.group(1).lower().replace(" ", "")
                if len(attr) >= 4 and attr[0:4].lower() == "bind":
                    attr = attr.replace(",", ", ")
                if hasattr(self, "attr_dict"):
                    if attr == "data":
                        pass
                    elif attr in ["dimension", "allocatable", "pointer"]:
                        names = ford.utils.paren_split(",", match.group(2))
                        for name in names:
                            name = name.strip().lower()
                            try:
                                open_parenthesis = name.index("(")
                                var_name = name[:open_parenthesis]
                                dimensions = name[open_parenthesis:]
                            except ValueError:
                                var_name = name
                                dimensions = ""

                            self.attr_dict[var_name].append(attr + dimensions)
                    else:
                        stmnt = match.group(2)
                        if attr == "parameter":
                            stmnt = stmnt[1:-1].strip()
                        names = ford.utils.paren_split(",", stmnt)
                        search_from = 0
                        while QUOTES_RE.search(attr[search_from:]):
                            num = int(
                                QUOTES_RE.search(attr[search_from:]).group()[1:-1]
                            )
                            attr = attr[0:search_from] + QUOTES_RE.sub(
                                self.strings[num], attr[search_from:], count=1
                            )
                            search_from += QUOTES_RE.search(attr[search_from:]).end(0)
                        for name in names:
                            if attr == "parameter":
                                split = ford.utils.paren_split("=", name)
                                name = split[0].strip().lower()
                                self.param_dict[name] = split[1]
                            name = name.strip().lower()
                            self.attr_dict[name].append(attr)

                elif attr.lower() == "data" and self.obj == "sourcefile":
                    # TODO: This is just a fix to keep FORD from crashing on
                    # encountering a block data structure. At some point I
                    # should actually implement support for them.
                    continue
                else:
                    self.print_error(line, f"Unexpected {attr.upper()} statement")

            elif match := self.END_RE.match(line):
                if isinstance(self, FortranSourceFile):
                    self.print_error(
                        line,
                        "END statement outside of any nesting",
                        describe_object=False,
                    )
                endtype = match.group(1)
                if endtype and endtype.lower() == "block":
                    blocklevel -= 1
                elif endtype and endtype.lower() == "associate":
                    associatelevel -= 1
                else:
                    self._cleanup()
                    return

            elif (match := self.MODPROC_RE.match(line)) and (
                match.group(1) or isinstance(self, FortranInterface)
            ):
                if hasattr(self, "modprocs"):
                    # Module procedure in an INTERFACE
                    self.modprocs.extend(get_mod_procs(source, match, self))
                elif hasattr(self, "modprocedures"):
                    # Module procedure implementing an interface in a SUBMODULE
                    self.modprocedures.append(
                        FortranSubmoduleProcedure(source, match, self, self.permission)
                    )
                    self.num_lines += self.modprocedures[-1].num_lines - 1
                else:
                    self.print_error(line, "Unexpected MODULE PROCEDURE")

            elif match := self.BLOCK_DATA_RE.match(line):
                if hasattr(self, "blockdata"):
                    self.blockdata.append(FortranBlockData(source, match, self))
                    self.num_lines += self.blockdata[-1].num_lines - 1
                else:
                    self.print_error(line, "Unexpected BLOCK DATA")
            elif self.BLOCK_RE.match(line):
                blocklevel += 1
            elif self.ASSOCIATE_RE.match(line):
                associatelevel += 1
            elif match := self.MODULE_RE.match(line):
                if hasattr(self, "modules"):
                    self.modules.append(FortranModule(source, match, self))
                    self.num_lines += self.modules[-1].num_lines - 1
                else:
                    self.print_error(line, "Unexpected MODULE")

            elif match := self.SUBMODULE_RE.match(line):
                if hasattr(self, "submodules"):
                    self.submodules.append(FortranSubmodule(source, match, self))
                    self.num_lines += self.submodules[-1].num_lines - 1
                else:
                    self.print_error(line, "Unexpected SUBMODULE")

            elif match := self.PROGRAM_RE.match(line):
                if hasattr(self, "programs"):
                    self.programs.append(FortranProgram(source, match, self))
                    self.num_lines += self.programs[-1].num_lines - 1
                else:
                    self.print_error(line, "Unexpected PROGRAM")
                if len(self.programs) > 1:
                    self.print_error(
                        line,
                        "Multiple PROGRAM units in same source file",
                        describe_object=False,
                    )

            elif match := self.SUBROUTINE_RE.match(line):
                if isinstance(self, FortranCodeUnit) and not incontains:
                    self.print_error(line, "Unexpected SUBROUTINE")
                elif hasattr(self, "subroutines"):
                    self.subroutines.append(
                        FortranSubroutine(source, match, self, self.permission)
                    )
                    self.num_lines += self.subroutines[-1].num_lines - 1
                else:
                    self.print_error(line, "Unexpected SUBROUTINE")

            elif match := self.FUNCTION_RE.match(line):
                if isinstance(self, FortranCodeUnit) and not incontains:
                    self.print_error(line, "Unexpected FUNCTION")
                elif hasattr(self, "functions"):
                    self.functions.append(
                        FortranFunction(source, match, self, self.permission)
                    )
                    self.num_lines += self.functions[-1].num_lines - 1
                else:
                    self.print_error(line, "Unexpected FUNCTION")

            elif (match := self.TYPE_RE.match(line)) and blocklevel == 0:
                if hasattr(self, "types"):
                    self.types.append(FortranType(source, match, self, self.permission))
                    self.num_lines += self.types[-1].num_lines - 1
                else:
                    self.print_error(line, "Unexpected derived TYPE")

            elif (match := self.INTERFACE_RE.match(line)) and blocklevel == 0:
                if hasattr(self, "interfaces"):
                    intr = FortranInterface(source, match, self, self.permission)
                    self.num_lines += intr.num_lines - 1
                    if intr.abstract:
                        self.absinterfaces.extend(intr.contents)
                    elif intr.generic:
                        self.interfaces.append(intr)
                    else:
                        self.interfaces.extend(intr.contents)
                else:
                    self.print_error(line, "Unexpected INTERFACE")

            elif (match := self.ENUM_RE.match(line)) and blocklevel == 0:
                if hasattr(self, "enums"):
                    self.enums.append(FortranEnum(source, match, self, self.permission))
                    self.num_lines += self.enums[-1].num_lines - 1
                else:
                    self.print_error(line, "Unexpected ENUM")

            elif (match := self.BOUNDPROC_RE.match(line)) and incontains:
                if not hasattr(self, "boundprocs"):
                    self.print_error(line, "Unexpected type-bound procedure")
                    continue

                names = match["names"].split(",")
                # Generic procedures or single name
                if match["generic"].lower() == "generic" or len(names) == 1:
                    self.boundprocs.append(
                        FortranBoundProcedure(source, match, self, child_permission)
                    )
                    continue

                # For multiple procedures, parse each one as if it
                # were on a line by itself
                for bind in reversed(names):
                    pseudo_line = self.BOUNDPROC_RE.match(
                        line[: match.start("names")] + bind
                    )
                    self.boundprocs.append(
                        FortranBoundProcedure(
                            source, pseudo_line, self, child_permission
                        )
                    )

            elif match := self.COMMON_RE.match(line):
                if hasattr(self, "common"):
                    split = self.COMMON_SPLIT_RE.split(line)
                    if len(split) > 1:
                        for i in range(len(split) // 2):
                            pseudo_line = (
                                split[0]
                                + " "
                                + split[2 * i + 1]
                                + " "
                                + split[2 * i + 2].strip()
                            )
                            if pseudo_line[-1] == ",":
                                pseudo_line = pseudo_line[:-1]
                            self.common.append(
                                FortranCommon(
                                    source,
                                    self.COMMON_RE.match(pseudo_line),
                                    self,
                                    "public",
                                )
                            )
                        for i in range(len(split) // 2):
                            self.common[-i - 1].doc = self.common[
                                -len(split) // 2 + 1
                            ].doc
                    else:
                        self.common.append(FortranCommon(source, match, self, "public"))
                else:
                    self.print_error(line, "Unexpected COMMON statement")

            elif (match := self.FINAL_RE.match(line)) and incontains:
                if hasattr(self, "finalprocs"):
                    procedures = self.SPLIT_RE.split(match.group(1).strip())
                    finprocs = [
                        FortranFinalProc(proc, self) for proc in procedures[:-1]
                    ]
                    finprocs.append(FortranFinalProc(procedures[-1], self, source))
                    self.finalprocs.extend(finprocs)
                else:
                    self.print_error(line, "Unexpected finalization procedure")

            elif self.VARIABLE_RE.match(line) and blocklevel == 0:
                if hasattr(self, "variables"):
                    self.variables.extend(
                        line_to_variables(source, line, child_permission, self)
                    )
                else:
                    self.print_error(line, "Unexpected variable")

            elif match := self.USE_RE.match(line):
                if hasattr(self, "uses"):
                    self.uses.append(list(match.groups()))
                else:
                    self.print_error(line, "Unexpected USE statement")
            else:
                if self.CALL_RE.search(line):
                    if hasattr(self, "calls"):
                        # Arithmetic GOTOs looks little like function references:
                        # "goto (1, 2, 3) i".  But even in free-form source we're
                        # allowed to use a space: "go to (1, 2, 3) i".  Our CALL_RE
                        # expression doesn't catch that so we first rule such a
                        # GOTO out.
                        if not self.ARITH_GOTO_RE.search(line):
                            callvals = self.CALL_RE.findall(line)
                            for val in callvals:
                                if (
                                    val.lower() not in self.calls
                                    and val.lower() not in INTRINSICS
                                ):
                                    self.calls.append(val.lower())
                    else:
                        pass
                        # Not raising an error here as too much possibility that something
                        # has been misidentified as a function call
                if match := self.SUBCALL_RE.match(line):
                    # Need this to catch any subroutines called without argument lists
                    if hasattr(self, "calls"):
                        callval = match.group(1).lower()
                        if callval not in self.calls and callval not in INTRINSICS:
                            self.calls.append(callval)
                    else:
                        self.print_error(line, "Unexpected procedure call")

        if not isinstance(self, FortranSourceFile):
            raise Exception("File ended while still nested.")

    def _cleanup(self):
        raise NotImplementedError()

    def print_error(self, line, error, describe_object=True) -> None:
        description = f" in {self.obj} '{self.name}'" if describe_object else ""
        message = f"ERROR in file '{self.filename}': {error}{description}:\n\t{line}"
        if self.settings["dbg"]:
            return print(message)

        if self.settings["force"]:
            return
        raise ValueError(message)


class FortranCodeUnit(FortranContainer):
    """
    A class on which programs, modules, functions, and subroutines are based.
    """

    def correlate(self, project):
        # Add procedures, interfaces and types from parent to our lists
        if hasattr(self.parent, "all_procs"):
            self.all_procs.update(self.parent.all_procs)
        self.all_absinterfaces = getattr(self.parent, "all_absinterfaces", {})
        for ai in self.absinterfaces:
            self.all_absinterfaces[ai.name.lower()] = ai
        self.all_types = getattr(self.parent, "all_types", {})
        for dt in self.types:
            self.all_types[dt.name.lower()] = dt
        self.all_vars = getattr(self.parent, "all_vars", {})
        for var in self.variables:
            self.all_vars[var.name.lower()] = var

        if type(getattr(self, "ancestor", "")) not in [str, type(None)]:
            self.ancestor.descendants.append(self)
            self.all_procs.update(self.parent_submodule.all_procs)
            self.all_absinterfaces.update(self.parent_submodule.all_absinterfaces)
            self.all_types.update(self.parent_submodule.all_types)
        elif type(getattr(self, "ancestor_module", "")) not in [str, type(None)]:
            self.ancestor_module.descendants.append(self)
            self.all_procs.update(self.ancestor_module.all_procs)
            self.all_absinterfaces.update(self.ancestor_module.all_absinterfaces)
            self.all_types.update(self.ancestor_module.all_types)

        # Module procedures will be missing (some/all?) metadata, so
        # now we copy it from the interface
        if isinstance(self, FortranModule):
            for proc in filter(lambda p: p.module, self.routines):
                intr = self.all_procs.get(proc.name.lower(), None)
                if (
                    intr
                    and intr.proctype.lower() == "interface"
                    and not intr.generic
                    and not intr.abstract
                    and intr.procedure.module is True
                ):
                    proc.module = intr
                    intr.procedure.module = proc

                    if isinstance(proc, FortranSubmoduleProcedure):
                        proc.attribs = intr.procedure.attribs
                        proc.args = intr.procedure.args
                        if hasattr(intr.procedure, "retvar"):
                            proc.retvar = intr.procedure.retvar
                        proc.proctype = intr.procedure.proctype

        def should_be_public(name: str) -> bool:
            """Is name public?"""
            return self.permission == "public" or name in self.public_list

        def filter_public(collection: dict) -> dict:
            """Return a new dict of only the public objects from collection"""
            return {
                name: obj for name, obj in collection.items() if should_be_public(name)
            }

        # Add procedures and types from USED modules to our lists
        for mod, extra in self.uses:
            if type(mod) is str:
                continue
            procs, absints, types, variables = mod.get_used_entities(extra)
            if self.obj == "module":
                self.pub_procs.update(filter_public(procs))
                self.pub_absints.update(filter_public(absints))
                self.pub_types.update(filter_public(types))
                self.pub_vars.update(filter_public(variables))
            self.all_procs.update(procs)
            self.all_absinterfaces.update(absints)
            self.all_types.update(types)
            self.all_vars.update(variables)
        self.uses = set([m[0] for m in self.uses])

        typelist = {}
        for dtype in self.types:
            if dtype.extends and dtype.extends.lower() in self.all_types:
                dtype.extends = self.all_types[dtype.extends.lower()]
                typelist[dtype] = set([dtype.extends])
            else:
                typelist[dtype] = set([])
        typeorder = toposort.toposort_flatten(typelist)

        # Match up called procedures
        if hasattr(self, "calls"):
            tmplst = []
            for call in self.calls:
                call_low = call.lower()
                argname = False
                for a in getattr(self, "args", []):
                    # Consider allowing procedures passed as arguments to be included in callgraphs
                    argname |= call_low == a.name.lower()
                if hasattr(self, "retvar"):
                    argname |= call_low == self.retvar.name.lower()
                if (
                    not argname
                    and call_low not in self.all_vars
                    and (call_low not in self.all_types or call_low in self.all_procs)
                ):
                    tmplst.append(call)
            self.calls = tmplst

            procedures = (
                {proc.name.lower(): proc for proc in self.parent.routines}
                if self.parobj == "sourcefile"
                else {}
            )
            procedures.update({proc.name.lower(): proc for proc in project.procedures})
            procedures.update(self.all_procs)

            for i, call in enumerate(self.calls):
                try:
                    self.calls[i] = procedures[call.lower()]
                except KeyError:
                    pass

        if self.obj == "submodule":
            self.ancestry = []
            item = self
            while item.parent_submodule:
                item = item.parent_submodule
                self.ancestry.insert(0, item)
            self.ancestry.insert(0, item.ancestor_module)

        # Recurse
        for dtype in typeorder:
            if dtype in self.types:
                dtype.correlate(project)
        for entity in self.iterator(
            "functions",
            "subroutines",
            "interfaces",
            "absinterfaces",
            "variables",
            "common",
            "modprocedures",
        ):
            entity.correlate(project)
        if hasattr(self, "args") and not getattr(self, "mp", False):
            for arg in self.args:
                arg.correlate(project)
        if hasattr(self, "retvar") and not getattr(self, "mp", False):
            self.retvar.correlate(project)

        self.sort_components()

        # Separate module subroutines/functions from normal ones
        if self.obj == "submodule":
            self.modfunctions = [func for func in self.functions if func.module]
            self.functions = [func for func in self.functions if not func.module]
            self.modsubroutines = [sub for sub in self.subroutines if sub.module]
            self.subroutines = [sub for sub in self.subroutines if not sub.module]

    def process_attribs(self):
        """Attach standalone attributes to the correct object, and compute the
        list of public objects
        """

        # IMPORTANT: Make sure types processed before interfaces--import when
        # determining permissions of derived types and overridden constructors
        for item in self.iterator(
            "functions", "subroutines", "types", "interfaces", "absinterfaces"
        ):
            for attr in self.attr_dict[item.name.lower()]:
                if attr in ["public", "private", "protected"]:
                    item.permission = attr
                elif attr[0:4] == "bind":
                    if hasattr(item, "bindC"):
                        item.bindC = attr[5:-1]
                    elif getattr(item, "procedure", None):
                        item.procedure.bindC = attr[5:-1]
                    else:
                        item.attribs.append(attr)
                else:
                    item.attribs.append(attr)
            try:
                del self.attr_dict[item.name.lower()]
            except KeyError:
                pass

        for var in self.variables:
            for attr in self.attr_dict[var.name.lower()]:
                if attr in ["public", "private", "protected"]:
                    var.permission = attr
                elif attr[0:6] == "intent":
                    var.intent = attr[7:-1]
                elif DIM_RE.match(attr) and (
                    "pointer" in attr or "allocatable" in attr
                ):
                    i = attr.index("(")
                    var.attribs.append(attr[0:i])
                    var.dimension = attr[i:]
                elif attr == "parameter":
                    var.attribs.append(attr)
                    var.initial = self.param_dict[var.name.lower()]
                else:
                    var.attribs.append(attr)
            try:
                del self.attr_dict[var.name.lower()]
            except KeyError:
                pass

        # Now we want a list of all the objects we've declared, plus
        # any we've imported that have a "public" attribute
        self.public_list = [
            item.name.lower()
            for item in self.iterator(
                "functions",
                "subroutines",
                "types",
                "interfaces",
                "absinterfaces",
                "variables",
            )
            if item.permission == "public"
        ] + [item for item, attr in self.attr_dict.items() if "public" in attr]

        del self.attr_dict

    def prune(self):
        """
        Remove anything which shouldn't be displayed.
        """

        if self.obj == "proc" and not self.meta["proc_internals"]:
            self.functions = []
            self.subroutines = []
            self.types = []
            self.interfaces = []
            self.absinterfaces = []
            self.variables = []
            return

        self.functions = self.filter_display(self.functions)
        self.subroutines = self.filter_display(self.subroutines)
        self.types = self.filter_display(self.types)
        self.interfaces = self.filter_display(self.interfaces)
        self.absinterfaces = self.filter_display(self.absinterfaces)
        self.variables = self.filter_display(self.variables)
        if self.obj == "submodule":
            self.modprocedures = self.filter_display(self.modprocedures)
            self.modsubroutines = self.filter_display(self.modsubroutines)
            self.modfunctions = self.filter_display(self.modfunctions)

        # Recurse
        for obj in self.iterator(
            "absinterfaces",
            "interfaces",
        ):
            obj.visible = True

        for obj in self.iterator(
            "functions",
            "subroutines",
            "types",
            "modprocedures",
            "modfunctions",
            "modsubroutines",
        ):
            obj.visible = True
            obj.prune()


class FortranSourceFile(FortranContainer):
    """
    An object representing individual files containing Fortran code. A project
    will consist of a list of these objects. In turn, SourceFile objects will
    contains lists of all of that file's contents
    """

    def __init__(self, filepath, settings, preprocessor=None, fixed=False, **kwargs):
        # Hack to prevent FortranBase.__str__ to generate an anchor link to the source file in HTML output.
        self.visible = kwargs.get("incl_src", True)
        self.path = filepath.strip()
        self.name = os.path.basename(self.path)
        self.settings = settings
        self.fixed = fixed
        self.parent = None
        self.modules = []
        self.submodules = []
        self.functions = []
        self.subroutines = []
        self.programs = []
        self.blockdata = []
        self.doc = []
        self.hierarchy = []
        self.obj = "sourcefile"
        self.display = settings["display"]
        self.encoding = kwargs.get("encoding", True)
        self.permission = "public"

        source = ford.reader.FortranReader(
            self.path,
            settings["docmark"],
            settings["predocmark"],
            settings["docmark_alt"],
            settings["predocmark_alt"],
            fixed,
            settings["fixed_length_limit"],
            preprocessor,
            settings["macro"],
            settings["include"],
            settings["encoding"],
        )

        super().__init__(source, "")
        with open(self.path, "r", encoding=settings["encoding"]) as readobj:
            self.raw_src = readobj.read()

        lexer = FortranFixedLexer() if self.fixed else FortranLexer()
        self.src = highlight(
            self.raw_src, lexer, HtmlFormatter(lineanchors="ln", cssclass="hl")
        )


class FortranModule(FortranCodeUnit):
    """
    An object representing individual modules within your source code. These
    objects contains lists of all of the module's contents, as well as its
    dependencies.
    """

    ONLY_RE = re.compile(r"^\s*,\s*only\s*:\s*(?=[^,])", re.IGNORECASE)
    RENAME_RE = re.compile(r"(\w+)\s*=>\s*(\w+)", re.IGNORECASE)

    def _initialize(self, line):
        self.name = line.group(1)
        self.uses = []
        self.variables = []
        self.enums = []
        self.public_list = []
        self.private_list = []
        self.protected_list = []
        self.subroutines = []
        self.functions = []
        self.modprocedures = []
        self.interfaces = []
        self.absinterfaces = []
        self.types = []
        self.descendants = []
        self.common = []
        self.visible = True
        self.attr_dict = defaultdict(list)
        self.param_dict = dict()

    def _cleanup(self):
        """Create list of all local procedures. Ones coming from other modules
        will be added later, during correlation."""
        self.all_procs = {}
        for p in self.routines:
            self.all_procs[p.name.lower()] = p

        for var in self.variables:
            # Count procedure pointers and dummy procedures
            if var.vartype == "procedure":
                self.all_procs[var.name.lower()] = var

        for interface in self.interfaces:
            if not interface.abstract:
                self.all_procs[interface.name.lower()] = interface
            if interface.generic:
                for proc in interface.iterator("subroutines", "functions"):
                    self.all_procs[proc.name.lower()] = proc
        self.process_attribs()
        self.variables = [v for v in self.variables if "external" not in v.attribs]

        def should_be_public(item: FortranBase) -> bool:
            return item.permission in ["public", "protected"]

        def filter_public(collection: list) -> dict:
            return {
                obj.name.lower(): obj for obj in collection if should_be_public(obj)
            }

        self.pub_procs = filter_public(self.all_procs.values())
        self.pub_vars = filter_public(self.variables)
        self.pub_types = filter_public(self.types)
        self.pub_absints = filter_public(self.absinterfaces)

    def get_used_entities(self, use_specs):
        """
        Returns the entities which are imported by a use statement. These
        are contained in dicts.
        """
        if len(use_specs.strip()) == 0:
            return (self.pub_procs, self.pub_absints, self.pub_types, self.pub_vars)

        only = bool(self.ONLY_RE.match(use_specs))
        use_specs = self.ONLY_RE.sub("", use_specs)
        # The used names after possible renaming
        used_names = {}
        for item in map(str.strip, use_specs.split(",")):
            if match := self.RENAME_RE.search(item):
                used_names[match.group(2).lower()] = match.group(1).lower()
            else:
                used_names[item.lower()] = item.lower()

        def used_objects(object_type: str, only: bool) -> dict:
            """Get the objects that are actually used"""
            result = {}
            object_collection = getattr(self, object_type)
            for name, obj in object_collection.items():
                name = name.lower()
                if only:
                    if name in used_names:
                        result[used_names[name]] = obj
                else:
                    result[name] = obj
            return result

        ret_procs = used_objects("pub_procs", only)
        ret_absints = used_objects("pub_absints", only)
        ret_types = used_objects("pub_types", only)
        ret_vars = used_objects("pub_vars", only)
        return (ret_procs, ret_absints, ret_types, ret_vars)


class FortranSubmodule(FortranModule):
    def _initialize(self, line):
        FortranModule._initialize(self, line)
        self.name = line["name"]
        self.parent_submodule = line["parent_submod"]
        self.ancestor_module = line["ancestor_module"]
        self.modprocedures = []
        del self.public_list
        del self.private_list
        del self.protected_list

    def _cleanup(self):
        # Create list of all local procedures. Ones coming from other modules
        # will be added later, during correlation.
        self.process_attribs()
        self.variables = [v for v in self.variables if "external" not in v.attribs]
        self.all_procs = {p.name.lower(): p for p in self.routines}
        for interface in self.interfaces:
            if not interface.abstract:
                self.all_procs[interface.name.lower()] = interface
            if interface.generic:
                for proc in interface.iterator("subroutines", "functions"):
                    self.all_procs[proc.name.lower()] = proc

    def get_dir(self):
        return "module"


def _list_of_procedure_attributes(
    attribute_string: Optional[str],
) -> Tuple[List[str], str]:
    """Convert a string of attributes into a list of attributes"""
    if not attribute_string:
        return [], ""

    attribute_list = []
    attribute_string = attribute_string.lower()

    for attribute in [
        "impure",
        "pure",
        "elemental",
        "non_recursive",
        "recursive",
        "module",
    ]:
        if attribute in attribute_string:
            attribute_list.append(attribute)
            attribute_string = re.sub(
                attribute, "", attribute_string, flags=re.IGNORECASE
            )

    return attribute_list, attribute_string.replace(" ", "")


def implicit_type(name: str) -> str:
    """Map names to implicit types"""

    if name[0].lower() in "ijklmn":
        return "integer"
    return "real"


class FortranProcedure(FortranCodeUnit):
    """Base class for subroutines and functions for common functionality"""

    def _procedure_initialize(
        self,
        name: str,
        arguments: Optional[str],
        attributes: Optional[str],
        bindC: Optional[str],
        **kwargs,
    ) -> str:
        self.name = name
        self.attribs, attribstr = _list_of_procedure_attributes(attributes)
        self.mp = False
        self.module = "module" in self.attribs

        self.args = []
        if arguments:
            # Empty argument lists will contain the empty string, so we need to remove it
            self.args = [
                arg for arg in self.SPLIT_RE.split(arguments[1:-1].strip()) if arg
            ]

        self._parse_bind_C(bindC)
        self.variables: List[FortranVariable] = []
        self.enums: List[FortranEnum] = []
        self.uses = []
        self.calls = []
        self.subroutines: List[FortranSubroutine] = []
        self.functions: List[FortranFunction] = []
        self.interfaces: List[FortranInterface] = []
        self.absinterfaces: List[FortranInterface] = []
        self.types: List[FortranType] = []
        self.common: List[FortranCommon] = []
        self.attr_dict: Dict[str, List[str]] = defaultdict(list)
        self.param_dict: Dict[str, str] = dict()
        self.associate_blocks = []

        return attribstr

    def _parse_bind_C(self, bind_C_text: Optional[str]):
        """Parses a `bind(...)` attribute"""

        if bind_C_text is None:
            self.bindC = None
            return

        # Shouldn't have parentheses in, but just to be safe, let's
        # remove any
        if "(" in bind_C_text or ")" in bind_C_text:
            bind_C_text = ford.utils.get_parens(bind_C_text, -1)

        self.bindC = bind_C_text

        # Now we have to replace any quoted text that has previously
        # been removed
        search_from = 0
        while quote := QUOTES_RE.search(self.bindC[search_from:]):
            num = int(quote.group()[1:-1])
            self.bindC = self.bindC[0:search_from] + QUOTES_RE.sub(
                self.parent.strings[num], self.bindC[search_from:], count=1
            )
            if not (next_match := QUOTES_RE.search(self.bindC[search_from:])):
                raise ValueError(
                    f"Unexpected missing quotes in '{self.bindC[search_from:]}'"
                )
            search_from += next_match.end(0)

    @property
    def is_interface_procedure(self) -> bool:
        """Is this procedure just an interface?"""
        return isinstance(self.parent, FortranInterface) and not self.parent.generic

    @property
    def permission(self):
        """Permission (public/private) of this procedure"""
        if self.is_interface_procedure:
            return self.parent.permission

        return self._permission

    @permission.setter
    def permission(self, value):
        self._permission = value

    @property
    def ident(self) -> str:
        """Return a unique identifier for this object"""
        if self.is_interface_procedure:
            return namelist.get_name(self.parent)
        return super().ident

    def get_dir(self) -> Optional[str]:
        if self.is_interface_procedure:
            return "interface"

        return super().get_dir()

    def _cleanup(self):
        """Convert all child entities to object instances"""

        self.all_procs = {p.name.lower(): p for p in self.routines}
        for interface in self.interfaces:
            if not interface.abstract:
                self.all_procs[interface.name.lower()] = interface
            if interface.generic:
                for proc in interface.routines:
                    self.all_procs[proc.name.lower()] = proc

        for i, arg in enumerate(self.args):
            # Is there a variable declaration for this argument?
            for var in self.variables:
                if arg.lower() == var.name.lower():
                    arg = var
                    self.variables.remove(var)
                    break

            # Otherwise, is it a procedure with an interface?
            if isinstance(arg, str):
                for intr in self.interfaces:
                    if intr.abstract or intr.generic:
                        continue
                    proc = intr.procedure
                    if proc.name.lower() == arg.lower():
                        arg = proc
                        arg.parent = self
                        self.interfaces.remove(intr)
                        break

            # If we've still not found it, it's an implicitly-type variable.
            # FIXME: we pay no attention to `implicit none` or other
            # `implicit` statements
            if isinstance(arg, str):
                arg = FortranVariable(arg, implicit_type(arg), self, doc="")

            self.args[i] = arg

        self.process_attribs()
        self.variables = [v for v in self.variables if "external" not in v.attribs]


class FortranSubroutine(FortranProcedure):
    """
    An object representing a Fortran subroutine and holding all of said
    subroutine's contents.
    """

    def _initialize(self, line: re.Match):
        self._procedure_initialize(**line.groupdict())
        self.proctype = "Subroutine"


class FortranFunction(FortranProcedure):
    """
    An object representing a Fortran function and holding all of said function's
    contents.
    """

    def _initialize(self, line: re.Match):
        attribstr = self._procedure_initialize(**line.groupdict())
        self.proctype = "Function"
        self.retvar = line["result"] or self.name

        try:
            parsed_type = parse_type(
                attribstr, self.strings, self.settings["extra_vartypes"]
            )
            self.retvar = FortranVariable(
                name=self.retvar,
                vartype=parsed_type.vartype,
                parent=self,
                kind=parsed_type.kind,
                strlen=parsed_type.strlen,
                proto=parsed_type.proto,
            )
        except ValueError:
            pass

    def _cleanup(self):
        if not isinstance(self.retvar, FortranVariable):
            for var in self.variables:
                if var.name.lower() == self.retvar.lower():
                    self.retvar = var
                    self.variables.remove(var)
                    break
            else:
                self.retvar = FortranVariable(
                    self.retvar, implicit_type(self.retvar), self
                )

        super()._cleanup()


class FortranSubmoduleProcedure(FortranCodeUnit):
    """
    An object representing a the implementation of a Module Function or
    Module Subroutine in a submodule.
    """

    module = True

    def _initialize(self, line):
        self.proctype = "Module Procedure"
        self.name = line.group(2)
        self.variables = []
        self.enums = []
        self.uses = []
        self.calls = []
        self.subroutines = []
        self.functions = []
        self.interfaces = []
        self.absinterfaces = []
        self.types = []
        self.attr_dict = defaultdict(list)
        self.mp = True
        self.param_dict = dict()
        self.associate_blocks = []
        self.common = []

    def _cleanup(self):
        self.process_attribs()
        self.all_procs = {p.name.lower(): p for p in self.routines}
        for interface in self.interfaces:
            if not interface.abstract:
                self.all_procs[interface.name.lower()] = interface
            if interface.generic:
                for proc in interface.iterator("subroutines", "functions"):
                    self.all_procs[proc.name.lower()] = proc
        self.variables = [v for v in self.variables if "external" not in v.attribs]


class FortranProgram(FortranCodeUnit):
    """
    An object representing the main Fortran program.
    """

    def _initialize(self, line):
        self.name = line.group(1)
        if self.name is None:
            self.name = ""
        self.variables = []
        self.enums = []
        self.subroutines = []
        self.functions = []
        self.interfaces = []
        self.types = []
        self.uses = []
        self.calls = []
        self.absinterfaces = []
        self.attr_dict = defaultdict(list)
        self.param_dict = dict()
        self.associate_blocks = []
        self.common = []

    def _cleanup(self):
        self.all_procs = {}
        for p in self.routines:
            self.all_procs[p.name.lower()] = p
        for interface in self.interfaces:
            if not interface.abstract:
                self.all_procs[interface.name.lower()] = interface
            if interface.generic:
                for proc in interface.iterator("subroutines", "functions"):
                    self.all_procs[proc.name.lower()] = proc
        self.process_attribs()
        self.variables = [v for v in self.variables if "external" not in v.attribs]


class FortranType(FortranContainer):
    """
    An object representing a Fortran derived type and holding all of said type's
    components and type-bound procedures. It also contains information on the
    type's inheritance.
    """

    def _initialize(self, line):
        self.name = line.group(2)
        self.extends = None
        self.attributes = []
        if line.group(1):
            attribstr = line.group(1)[1:].strip()
            attriblist = self.SPLIT_RE.split(attribstr.strip())
            for attrib in attriblist:
                attrib_lower = attrib.strip().lower()
                if EXTENDS_RE.search(attrib):
                    self.extends = EXTENDS_RE.search(attrib).group(1)
                elif attrib_lower in ["public", "private"]:
                    self.permission = attrib_lower
                elif attrib_lower == "external":
                    self.attributes.append("external")
                else:
                    self.attributes.append(attrib.strip())
        if line.group(3):
            paramstr = line.group(3).strip()
            self.parameters = self.SPLIT_RE.split(paramstr)
        else:
            self.parameters = []
        self.sequence = False
        self.variables = []
        self.boundprocs = []
        self.finalprocs = []
        self.constructor = None

    def _cleanup(self):
        # Match parameters with variables
        for i in range(len(self.parameters)):
            for var in self.variables:
                if self.parameters[i].lower() == var.name.lower():
                    self.parameters[i] = var
                    self.variables.remove(var)
                    break

    def correlate(self, project):
        self.all_absinterfaces = self.parent.all_absinterfaces
        self.all_types = self.parent.all_types
        self.all_procs = self.parent.all_procs
        self.num_lines_all = self.num_lines

        # Match variables as needed (recurse)
        # ~ for i in range(len(self.variables)-1,-1,-1):
        # ~ self.variables[i].correlate(project)
        for v in self.variables:
            v.correlate(project)
        # Get inherited public components
        inherited = [
            var
            for var in getattr(self.extends, "variables", [])
            if var.permission == "public"
        ]
        self.local_variables = self.variables
        for invar in inherited:
            if not hasattr(invar, "doc"):
                invar.doc = "Inherited from [[{0}]]".format(self.extends)
                invar.meta = {}
        self.variables = inherited + self.variables

        # Match boundprocs with procedures
        # FIXME: This is not at all modular because must process non-generic bound procs first--could there be a better way to do it
        for proc in self.boundprocs:
            if not proc.generic:
                proc.correlate(project)
        # Identify inherited type-bound procedures which are not overridden
        inherited = []
        inherited_generic = []
        if self.extends and type(self.extends) is not str:
            for bp in self.extends.boundprocs:
                if bp.permission == "private":
                    continue
                if all([bp.name.lower() != b.name.lower() for b in self.boundprocs]):
                    if bp.generic:
                        gen = copy.copy(bp)
                        gen.parent = self
                        inherited.append(gen)
                    else:
                        inherited.append(bp)
                elif bp.generic:
                    gen = copy.copy(bp)
                    gen.parent = self
                    inherited_generic.append(gen)
        self.boundprocs = inherited + self.boundprocs
        # Match up generic type-bound procedures to their particular bindings
        for proc in self.boundprocs:
            for bp in inherited_generic:
                if bp.name.lower() == proc.name.lower() and hasattr(bp, "bindings"):
                    proc.bindings = bp.bindings + proc.bindings
                    break
            if proc.generic:
                proc.correlate(project)
        # Match finalprocs
        for fp in self.finalprocs:
            fp.correlate(project)
        # Find a constructor, if one exists
        if self.name.lower() in self.all_procs:
            self.constructor = self.all_procs[self.name.lower()]
            self.constructor.permission = self.permission
            self.num_lines += getattr(
                self.constructor, "num_lines_all", self.constructor.num_lines
            )

        self.sort_components()

        # Get total num_lines, including implementations
        for proc in self.finalprocs:
            self.num_lines_all += proc.procedure.num_lines
        for proc in self.boundprocs:
            for bind in proc.bindings:
                if isinstance(bind, FortranProcedure):
                    self.num_lines_all += bind.num_lines
                elif isinstance(bind, FortranBoundProcedure):
                    for b in bind.bindings:
                        if isinstance(b, FortranProcedure):
                            self.num_lines_all += b.num_lines

    def prune(self):
        """
        Remove anything which shouldn't be displayed.
        """
        self.boundprocs = self.filter_display(self.boundprocs)
        self.variables = self.filter_display(self.variables)
        for obj in self.boundprocs + self.variables:
            obj.visible = True

    def __repr__(self):
        return f"FortranType('{self.name}', variables={self.variables}, boundprocs={self.boundprocs})"


class FortranEnum(FortranContainer):
    """
    An object representing a Fortran enumeration. Contains the individual
    enumerators as variables.
    """

    def _initialize(self, line):
        self.variables = []
        self.name = ""

    def _cleanup(self):
        prev_val = -1
        for var in self.variables:
            if not var.initial:
                var.initial = prev_val + 1

            initial = (
                remove_kind_suffix(var.initial)
                if isinstance(var.initial, str)
                else var.initial
            )

            try:
                prev_val = int(initial)
            except ValueError:
                raise ValueError(
                    f"Non-integer ('{var.initial}') assigned to enumerator '{var.name}'."
                )


class FortranInterface(FortranContainer):
    """An `interface` block, including generic and abstract interfaces

    Attributes
    ----------
    subroutines: list
        External subroutines
    functions: list
        External functions
    modprocs: list
        Procedures defined in this scope
    variables: list
        Procedure pointers and dummy procedures
    generic: bool
        True if this is a generic interface
    abstract: bool
        True if this is an abstract interface
    """

    def _initialize(self, line):
        self.proctype = "Interface"
        self.name = line.group(2)
        self.subroutines = []
        self.functions = []
        self.modprocs = []
        self.variables = []
        self.generic = bool(self.name)
        self.abstract = bool(line.group(1))
        if self.generic and self.abstract:
            raise Exception(f"Generic interface '{self.name}' can not be abstract")

    def correlate(self, project):
        self.all_absinterfaces = self.parent.all_absinterfaces
        self.all_types = self.parent.all_types
        self.all_procs = self.parent.all_procs
        self.num_lines_all = self.num_lines
        if self.generic:
            # Some "modprocs" are actually procedure pointers or dummy
            # args, so we need to move them to a separate lsit
            modprocs_to_pop = []
            for modproc in self.modprocs:
                try:
                    procedure = self.all_procs[modproc.name.lower()]
                except KeyError:
                    raise RuntimeError(
                        f"Could not find interface procedure '{modproc.name}' in '{self.parent.name}'. "
                        f"Known procedures are: {list(self.all_procs.keys())}"
                    )

                if isinstance(procedure, FortranVariable):
                    self.variables.append(procedure)
                    modprocs_to_pop.append(modproc)
                    continue

                modproc.procedure = procedure
                self.num_lines_all += modproc.procedure.num_lines

            for proc in modprocs_to_pop:
                self.modprocs.remove(proc)

            for proc in self.routines:
                proc.correlate(project)
        else:
            self.procedure.correlate(project)

        self.sort_components()

    def _cleanup(self):
        if not self.abstract and self.generic:
            return

        contents = []
        for proc in self.routines:
            proc.visible = False
            item = copy.copy(self)
            item.procedure = proc
            item.procedure.parent = item
            del item.functions
            del item.modprocs
            del item.subroutines
            item.name = proc.name
            item.permission = proc.permission
            contents.append(item)
        self.contents = contents


class FortranFinalProc(FortranBase):
    """
    An object representing a finalization procedure for a derived type
    within Fortran.
    """

    def __init__(self, name, parent, source=None):
        self.name = name
        self.parent = parent
        self.procedure = None
        self.obj = "finalproc"
        self.parobj = self.parent.obj
        self.display = self.parent.display
        self.settings = self.parent.settings
        self.doc = []
        if source:
            line = source.__next__()
            while line[0:2] == "!" + self.settings["docmark"]:
                self.doc.append(line[2:])
                line = source.__next__()
            source.pass_back(line)
        self.hierarchy = []
        cur = self.parent
        while cur:
            self.hierarchy.append(cur)
            cur = cur.parent
        self.hierarchy.reverse()

    def correlate(self, project):
        self.all_procs = self.parent.all_procs
        if self.name.lower() in self.all_procs:
            self.procedure = self.all_procs[self.name.lower()]


class FortranVariable(FortranBase):
    """
    An object representing a variable within Fortran.
    """

    def __init__(
        self,
        name,
        vartype,
        parent,
        attribs=[],
        intent="",
        optional=False,
        permission="public",
        parameter=False,
        kind=None,
        strlen=None,
        proto=None,
        doc=None,
        points=False,
        initial=None,
    ):
        self.name = name
        self.vartype = vartype.lower()
        self.parent = parent
        if self.parent:
            self.parobj = self.parent.obj
            self.settings = self.parent.settings
        else:
            self.parobj = None
            self.settings = None
        self.obj = type(self).__name__[7:].lower()
        self.attribs = copy.copy(attribs)
        self.intent = intent
        self.optional = optional
        self.kind = kind
        self.strlen = strlen
        self.proto = copy.copy(proto)
        self.doc = copy.copy(doc) if doc is not None else []
        self.permission = permission
        self.points = points
        self.parameter = parameter
        self.initial = initial
        self.dimension = ""
        self.meta = {}
        self.visible = False

        indexlist = []
        indexparen = self.name.find("(")
        if indexparen > 0:
            indexlist.append(indexparen)
        indexbrack = self.name.find("[")
        if indexbrack > 0:
            indexlist.append(indexbrack)
        indexstar = self.name.find("*")
        if indexstar > 0:
            indexlist.append(indexstar)

        if len(indexlist) > 0:
            self.dimension = self.name[min(indexlist) :]
            self.name = self.name[0 : min(indexlist)]

        self.hierarchy = []
        cur = self.parent
        while cur:
            self.hierarchy.append(cur)
            cur = cur.parent
        self.hierarchy.reverse()

    def correlate(self, project):
        if not self.proto:
            return

        proto_name = self.proto[0].lower()
        if proto_name == "*":
            return

        if self.vartype in ("type", "class"):
            self.proto[0] = self.parent.all_types.get(proto_name, self.proto[0])
        elif self.vartype == "procedure":
            abstract_prototype = self.parent.all_absinterfaces.get(
                proto_name, self.proto[0]
            )
            self.proto[0] = self.parent.all_procs.get(proto_name, abstract_prototype)

    @property
    def full_type(self):
        """Return the full type, including class, kind, len, and so on"""
        parameter_parts = []
        result = self.vartype

        # Wrap only kind, strlen, proto in brackets
        if self.kind:
            parameter_parts.append(f"kind={self.kind}")
        if self.strlen:
            parameter_parts.append(f"len={self.strlen}")

        # If we've got a "proto", then we probably don't have kind and strlen?
        if parameter_parts:
            result += f"({', '.join(parameter_parts)})"
        elif self.proto:
            proto = str(self.proto[0])
            if self.proto[1]:
                proto += f"({self.proto[1]})"
            result += f"({proto})"

        return result

    @property
    def full_declaration(self):
        """Return the full type declaration, including attributes, dimensions,
        kind, and so on"""

        # Add all the other attributes to a single list
        attribute_parts = copy.copy(self.attribs)
        if self.dimension:
            attribute_parts.append(self.dimension)
        if self.parameter:
            attribute_parts.append("parameter")

        # Note: not str.join because we want the leading comman too
        attributes = [f", {part}" for part in attribute_parts]
        return f"{self.full_type}{''.join(attributes)}"

    def __repr__(self):
        return f"FortranVariable('{self.name}', type='{self.full_type}', permission='{self.permission}')"


class FortranBoundProcedure(FortranBase):
    """
    An object representing a type-bound procedure, possibly overloaded.
    """

    def _initialize(self, line: re.Match):
        self.attribs = []
        self.deferred = False

        for attribute in ford.utils.paren_split(",", line["attributes"] or ""):
            attribute = attribute.strip()
            # Preserve original capitalisation -- TODO: needed?
            attribute_lower = attribute.lower()
            if attribute_lower in ["public", "private"]:
                self.permission = attribute_lower
            elif attribute_lower == "deferred":
                self.deferred = True
            else:
                self.attribs.append(attribute)

        split = self.POINTS_TO_RE.split(line["names"])
        self.name = split[0].strip()
        self.generic = line["generic"].lower() == "generic"
        self.proto = line["prototype"]
        if self.proto:
            self.proto = self.proto[1:-1].strip()
        self.bindings = []
        if len(split) > 1:
            binds = self.SPLIT_RE.split(split[1])
            for bind in binds:
                self.bindings.append(bind.strip())
        else:
            self.bindings.append(self.name)

    def correlate(self, project):
        self.all_procs = self.parent.all_procs
        self.protomatch = False
        if self.proto:
            proto_lower = self.proto.lower()
            if proto_lower in self.all_procs:
                self.proto = self.all_procs[proto_lower]
                self.protomatch = True
            elif proto_lower in self.parent.all_absinterfaces:
                self.proto = self.parent.all_absinterfaces[proto_lower]
                self.protomatch = True

        if self.generic:
            parent_boundprocs = {
                proc.name.lower(): proc for proc in self.parent.boundprocs if proc
            }

            for i, binding in enumerate(self.bindings):
                binding_name = getattr(binding, "name", binding).lower()

                try:
                    self.bindings[i] = parent_boundprocs[binding_name]
                except KeyError:
                    pass

        elif not self.deferred:
            for i in range(len(self.bindings)):
                try:
                    self.bindings[i] = self.all_procs[self.bindings[i].lower()]
                    self.bindings[i].binding = self
                except KeyError:
                    break

        self.sort_components()

    def __repr__(self):
        return f"FortranBoundProcedure('{self.name}', permission='{self.permission}')"


class FortranModuleProcedure(FortranBase):
    """
    An object representing a module procedure in an interface. Not to be
    confused with type of module procedure which is the implementation of
    a module function or module subroutine in a submodule.
    """

    def __init__(self, name, parent=None, inherited_permission=None):
        if inherited_permission is not None:
            self.permission = inherited_permission.lower()
        else:
            self.permission = None
        self.parent = parent
        if self.parent:
            self.parobj = self.parent.obj
            self.settings = self.parent.settings
        else:
            self.parobj = None
            self.settings = None
        self.obj = "moduleprocedure"
        self.name = name
        self.procedure = None
        self.doc = []
        self.hierarchy = []
        cur = self.parent
        while cur:
            self.hierarchy.append(cur)
            cur = cur.parent
        self.hierarchy.reverse()


class FortranBlockData(FortranContainer):
    """
    An object representing a block-data unit. Now obsolete due to modules,
    block data units allowed variables held in common blocks to be initialized
    outside of an executing program unit.
    """

    def _initialize(self, line):
        self.name = line.group(1)
        if not self.name:
            self.name = "<em>unnamed</em>"
        self.uses = []
        self.variables = []
        self.types = []
        self.common = []
        self.visible = True
        self.attr_dict = defaultdict(list)
        self.param_dict = dict()

    def correlate(self, project):
        # Add procedures, interfaces and types from parent to our lists
        self.all_types = {}
        for dt in self.types:
            self.all_types[dt.name.lower()] = dt
        self.all_vars = {}
        for var in self.variables:
            self.all_vars[var.name.lower()] = var
        self.all_absinterfaces = {}
        self.all_procs = {}

        # Add procedures and types from USED modules to our lists
        for mod, extra in self.uses:
            if type(mod) is str:
                continue
            procs, absints, types, variables = mod.get_used_entities(extra)
            self.all_procs.update(procs)
            self.all_absinterfaces.update(absints)
            self.all_types.update(types)
            self.all_vars.update(variables)
        self.uses = [m[0] for m in self.uses]

        typelist = {}
        for dtype in self.types:
            if dtype.extends and dtype.extends.lower() in self.all_types:
                dtype.extends = self.all_types[dtype.extends.lower()]
                typelist[dtype] = set([dtype.extends])
            else:
                typelist[dtype] = set([])
        typeorder = toposort.toposort_flatten(typelist)

        for dtype in typeorder:
            dtype.visible = True
            if dtype in self.types:
                dtype.correlate(project)
        for var in self.variables:
            var.correlate(project)
        for com in self.common:
            com.correlate(project)

        self.sort_components()

    def prune(self):
        self.types = self.filter_display(self.types)
        self.variables = self.filter_display(self.variables)
        for dtype in self.types:
            dtype.visible = True
            dtype.prune()

    def _cleanup(self):
        self.process_attribs()

    def process_attribs(self):
        for item in self.types:
            for attr in self.attr_dict[item.name.lower()]:
                if attr == "public" or attr == "private" or attr == "protected":
                    item.permission = attr
                elif attr[0:4] == "bind":
                    if hasattr(item, "bindC"):
                        item.bindC = attr[5:-1]
                    elif getattr(item, "procedure", None):
                        item.procedure.bindC = attr[5:-1]
                    else:
                        item.attribs.append(attr[5:-1])
        for var in self.variables:
            for attr in self.attr_dict[var.name.lower()]:
                if attr == "public" or attr == "private" or attr == "protected":
                    var.permission = attr
                elif attr[0:6] == "intent":
                    var.intent = attr[7:-1]
                elif DIM_RE.match(attr) and (
                    "pointer" in attr or "allocatable" in attr
                ):
                    i = attr.index("(")
                    var.attribs.append(attr[0:i])
                    var.dimension = attr[i:]
                elif attr == "parameter":
                    var.attribs.append(attr)
                    var.initial = self.param_dict[var.name.lower()]
                else:
                    var.attribs.append(attr)
        del self.attr_dict


class FortranCommon(FortranBase):
    """
    An object representing a common block. This is a legacy feature.
    """

    def _initialize(self, line):
        self.name = line.group(1)
        if not self.name:
            self.name = ""
        self.other_uses = []
        self.variables = [v.strip() for v in ford.utils.paren_split(",", line.group(2))]
        self.visible = True

    def correlate(self, project):
        for i in range(len(self.variables)):
            if self.variables[i] in self.parent.all_vars:
                self.variables[i] = self.parent.all_vars[self.variables[i]]
                try:
                    self.parent.variables.remove(self.variables[i])
                except ValueError:
                    pass
            else:
                self.variables[i] = FortranVariable(
                    self.variables[i], implicit_type(self.variables[i]), self, doc=""
                )

        if self.name in project.common:
            self.other_uses = project.common[self.name]
            self.other_uses.append(self)
        else:
            lst = [self]
            project.common[self.name] = lst
            self.other_uses = lst

        self.sort_components()


class FortranSpoof(object):
    """
    A dummy-type which is used to represent arguments, interfaces, type-bound
    procedures, etc. which lack a corresponding variable or implementation.
    """

    IS_SPOOF = True

    def __init__(self, name, parent=None, obj="ITEM"):
        self.name = name
        self.parent = parent
        self.obj = obj
        if self.parent.settings["warn"]:
            print(
                "Warning: {} {} in {} {} could not be matched to "
                "corresponding item in code (file {}).".format(
                    self.obj.upper(),
                    self.name,
                    self.parent.obj.upper(),
                    self.parent.name,
                    self.parent.hierarchy[0].name,
                )
            )

    def __getitem__(self, key):
        return []

    def __len__(self):
        return 0

    def __contains__(self, item):
        return False

    def __getattr__(self, name):
        return []

    def __str__(self):
        return self.name


class GenericSource(FortranBase):
    """
    Represent a non-Fortran source file. The contents of the file will
    not be analyzed, but documentation can be extracted.
    """

    def __init__(self, filename, settings):
        self.obj = "sourcefile"
        self.parobj = None
        self.parent = None
        self.hierarchy = []
        self.settings = settings
        self.num_lines = 0
        extra_filetypes = settings["extra_filetypes"][filename.split(".")[-1]]
        comchar = extra_filetypes[0]
        if len(extra_filetypes) > 1:
            self.lexer_str = extra_filetypes[1]
        else:
            self.lexer_str = None
        docmark = settings["docmark"]
        predocmark = settings["predocmark"]
        docmark_alt = settings["docmark_alt"]
        predocmark_alt = settings["predocmark_alt"]
        self.path = filename.strip()
        self.name = os.path.basename(self.path)
        with open(filename, "r", encoding=settings["encoding"]) as r:
            self.raw_src = r.read()
        # TODO: Get line numbers to display properly
        if self.lexer_str is None:
            lexer = guess_lexer_for_filename(self.name, self.raw_src)
        else:
            import pygments.lexers

            lexer = getattr(pygments.lexers, self.lexer_str)
        self.src = highlight(
            self.raw_src, lexer, HtmlFormatter(lineanchors="ln", cssclass="hl")
        )
        com_re = re.compile(
            r"^((?!{0}|[\"']).|(\'[^']*')|(\"[^\"]*\"))*({0}.*)$".format(
                re.escape(comchar)
            )
        )
        if docmark == docmark_alt != "":
            raise Exception("Error: docmark and docmark_alt are the same.")
        if docmark == predocmark_alt != "":
            raise Exception("Error: docmark and predocmark_alt are the same.")
        if docmark_alt == predocmark != "":
            raise Exception("Error: docmark_alt and predocmark are the same.")
        if predocmark == predocmark_alt != "":
            raise Exception("Error: predocmark and predocmark_alt are the same.")
        if len(predocmark) != 0:
            doc_re = re.compile(
                r"^((?!{0}|[\"']).|('[^']*')|(\"[^\"]*\"))*({0}(?:{1}|{2}).*)$".format(
                    re.escape(comchar), re.escape(docmark), re.escape(predocmark)
                )
            )
        else:
            doc_re = re.compile(
                r"^((?!{0}|[\"']).|('[^']*')|(\"[^\"]*\"))*({0}{1}.*)$".format(
                    re.escape(comchar), re.escape(docmark)
                )
            )
        if len(docmark_alt) != 0 and len(predocmark_alt) != 0:
            doc_alt_re = re.compile(
                r"^((?!{0}|[\"']).|('[^']*')|(\"[^\"]*\"))*({0}(?:{1}|{2}).*)$".format(
                    re.escape(comchar),
                    re.escape(docmark_alt),
                    re.escape(predocmark_alt),
                )
            )
        elif len(docmark_alt) != 0:
            doc_alt_re = re.compile(
                r"^((?!{0}|[\"']).|('[^']*')|(\"[^\"]*\"))*({0}{1}.*)$".format(
                    re.escape(comchar), re.escape(docmark_alt)
                )
            )
        elif len(predocmark_alt) != 0:
            doc_alt_re = re.compile(
                r"^((?!{0}|[\"']).|('[^']*')|(\"[^\"]*\"))*({0}{1}.*)$".format(
                    re.escape(comchar), re.escape(predocmark_alt)
                )
            )
        else:
            doc_alt_re = None
        self.doc = []
        prevdoc = False
        docalt = False
        for line in open(filename, "r", encoding=settings["encoding"]):
            line = line.strip()
            if doc_alt_re:
                match = doc_alt_re.match(line)
            else:
                match = False
            if match:
                prevdoc = True
                docalt = True
                doc = match.group(4)
                if doc.startswith(comchar + docmark_alt):
                    doc = doc[len(comchar + docmark_alt) :].strip()
                else:
                    doc = doc[len(comchar + predocmark_alt) :].strip()
                self.doc.append(doc)
                continue
            match = doc_re.match(line)
            if match:
                prevdoc = True
                if docalt:
                    docalt = False
                doc = match.group(4)
                if doc.startswith(comchar + docmark):
                    doc = doc[len(comchar + docmark) :].strip()
                else:
                    doc = doc[len(comchar + predocmark) :].strip()
                self.doc.append(doc)
                continue
            match = com_re.match(line)
            if match:
                if docalt:
                    if match.start(4) == 0:
                        doc = match.group(4)
                        doc = doc[len(comchar) :].strip()
                        self.doc.append(doc)
                    else:
                        docalt = False
                elif prevdoc:
                    prevdoc = False
                    self.doc.append("")
                continue
            # if not including any comment...
            if prevdoc:
                self.doc.append("")
                prevdoc = False
            docalt = False

    def lines_description(self, total, total_all=0):
        return ""


_can_have_contains = (
    FortranModule,
    FortranProgram,
    FortranProcedure,
    FortranType,
    FortranSubmodule,
    FortranSubmoduleProcedure,
)


def remove_kind_suffix(literal, is_character: bool = False):
    """Return the literal without the kind suffix of a numerical literal,
    or the kind prefix of a character literal"""

    kind_re = CHAR_KIND_SUFFIX_RE if is_character else KIND_SUFFIX_RE
    kind_suffix = kind_re.match(literal)
    if kind_suffix:
        return kind_suffix.group("initial")
    return literal


def line_to_variables(source, line, inherit_permission, parent):
    """
    Returns a list of variables declared in the provided line of code. The
    line of code should be provided as a string.
    """
    parsed_type = parse_type(line, parent.strings, parent.settings["extra_vartypes"])
    attribs = []
    intent = ""
    optional = False
    permission = inherit_permission
    parameter = False

    if attribmatch := ATTRIBSPLIT_RE.match(parsed_type.rest):
        attribstr = attribmatch.group(1).strip()
        declarestr = attribmatch.group(2).strip()
        tmp_attribs = [attr.strip() for attr in ford.utils.paren_split(",", attribstr)]
        for tmp_attrib in tmp_attribs:
            # Lowercase and remove whitespace so checking intent is cleaner
            tmp_attrib_lower = tmp_attrib.lower().replace(" ", "")

            if tmp_attrib_lower in ["public", "private", "protected"]:
                permission = tmp_attrib_lower
            elif tmp_attrib_lower == "optional":
                optional = True
            elif tmp_attrib_lower == "parameter":
                parameter = True
            elif tmp_attrib_lower == "intent(in)":
                intent = "in"
            elif tmp_attrib_lower == "intent(out)":
                intent = "out"
            elif tmp_attrib_lower == "intent(inout)":
                intent = "inout"
            else:
                attribs.append(tmp_attrib)
    else:
        declarestr = ATTRIBSPLIT2_RE.match(parsed_type.rest).group(2)
    declarations = ford.utils.paren_split(",", declarestr)

    doc = []
    docmark = f"!{parent.settings['docmark']}"
    while (docline := next(source)).startswith(docmark):
        doc.append(docline[2:])
    source.pass_back(docline)

    varlist = []
    for dec in declarations:
        dec = re.sub(" ", "", dec)
        split = ford.utils.paren_split("=", dec)
        if len(split) > 1:
            name = split[0]
            points = split[1][0] == ">"
            if points:
                initial = split[1][1:]
            else:
                initial = split[1]
        else:
            name = dec.strip()
            initial = None
            points = False

        if initial:
            initial = COMMA_RE.sub(", ", initial)
            # TODO: pull out into standalone function?
            search_from = 0
            while quote := QUOTES_RE.search(initial[search_from:]):
                num = int(quote.group()[1:-1])
                string = NBSP_RE.sub("&nbsp;", parent.strings[num])
                string = string.replace("\\", "\\\\")
                initial = initial[0:search_from] + QUOTES_RE.sub(
                    string, initial[search_from:], count=1
                )
                search_from += QUOTES_RE.search(initial[search_from:]).end(0)

        varlist.append(
            FortranVariable(
                name,
                parsed_type.vartype,
                parent,
                copy.copy(attribs),
                intent,
                optional,
                permission,
                parameter,
                parsed_type.kind,
                parsed_type.strlen,
                parsed_type.proto,
                doc,
                points,
                initial,
            )
        )

    return varlist


_EXTRA_TYPES_RE_CACHE: Dict[Tuple[str, ...], re.Pattern] = {}


@dataclass
class ParsedType:
    vartype: str
    rest: str
    kind: Optional[str] = None
    strlen: Optional[str] = None
    proto: Union[None, str, List[str]] = None


def parse_type(
    string: str, capture_strings: List[str], extra_vartypes: Sequence[str]
) -> ParsedType:
    """
    Gets variable type, kind, length, and/or derived-type attributes from a
    variable declaration.
    """
    extra_vartypes = tuple(extra_vartypes)
    try:
        var_type_re = _EXTRA_TYPES_RE_CACHE[extra_vartypes]
    except KeyError:
        var_type_re = re.compile(
            "|".join((VAR_TYPE_STRING, *extra_vartypes)), re.IGNORECASE
        )
        _EXTRA_TYPES_RE_CACHE[extra_vartypes] = var_type_re

    if not (match := var_type_re.match(string)):
        raise ValueError("Invalid variable declaration: {}".format(string))

    vartype = match.group().lower()
    if DOUBLE_PREC_RE.match(vartype):
        vartype = "double precision"
    if DOUBLE_CMPLX_RE.match(vartype):
        vartype = "double complex"
    rest = string[match.end() :].strip()
    kindstr = ford.utils.get_parens(rest)
    rest = rest[len(kindstr) :].strip()

    if (
        len(kindstr) < 3
        and vartype not in ["type", "class", "character"]
        and not kindstr.startswith("*")
    ):
        return ParsedType(vartype, rest)

    match = VARKIND_RE.search(kindstr)
    if not match:
        if vartype == "character":
            # This is a bare `character` declaration with no parameters
            return ParsedType(vartype, rest, strlen="1")

        raise ValueError(
            "Bad declaration of variable type {}: {}".format(vartype, string)
        )

    if match.group(1):
        star = False
        args = match.group(1).strip()
    else:
        star = True
        args = match.group(2).strip()
        if args.startswith("("):
            args = args[1:-1].strip()

    args = re.sub(r"\s", "", args)
    if vartype in ["type", "class", "procedure"]:
        PROTO_RE = re.compile(r"(\*|\w+)\s*(?:\((.*)\))?")
        try:
            proto = list(PROTO_RE.match(args).groups())
            if not proto[1]:
                proto[1] = ""
        except AttributeError:
            raise Exception(
                "Bad type, class, or procedure prototype specification: {}".format(args)
            )
        return ParsedType(vartype, rest, proto=proto)

    if vartype == "character":
        if star:
            return ParsedType(vartype, rest, strlen=args)

        args = args.split(",")

        if len(args) > 2:
            raise ValueError(
                f"Bad declaration of `character`, too many parameters: '{string}'"
            )

        # `character` has two parameters: `len` and `kind`.
        # If the parameter names are present, they can be in any order.
        # If they're missing, `len` must be first and `kind` second.
        # If there are no parameters at all, this is handled above.

        length = None
        kind = None
        for arg in args:
            if length is None and (length_match := LEN_RE.match(arg)):
                length = length_match.group(1) or length_match.group(2)
                continue

            if kind is None and (kind_match := KIND_RE.match(arg)):
                kind = kind_match.group(1)
                if match := QUOTES_RE.search(kind):
                    num = int(match.group()[1:-1])
                    kind = QUOTES_RE.sub(capture_strings[num], kind)
                continue

            if length is None:
                length = arg
                continue

            if kind is None:
                kind = arg

        # Handle default values
        if length is None:
            length = "1"

        return ParsedType(vartype, rest, kind=kind, strlen=length)

    kind = KIND_RE.match(args)
    kind = kind.group(1) if kind else args
    return ParsedType(vartype, rest, kind=kind)


def set_base_url(url):
    FortranBase.base_url = url


def get_mod_procs(source, line, parent):
    inherit_permission = parent.permission
    retlist = []
    SPLIT_RE = re.compile(r"\s*,\s*", re.IGNORECASE)
    splitlist = SPLIT_RE.split(line.group(2))
    if splitlist and len(splitlist) > 0:
        for item in splitlist:
            retlist.append(FortranModuleProcedure(item, parent, inherit_permission))
    else:
        retlist.append(
            FortranModuleProcedure(line.group(1), parent, inherit_permission)
        )

    doc = []
    docline = source.__next__()
    while docline[0:2] == "!" + parent.settings["docmark"]:
        doc.append(docline[2:])
        docline = source.__next__()
    source.pass_back(docline)
    retlist[-1].doc = doc

    return retlist


class NameSelector(object):
    """
    Object which tracks what names have been provided for different
    entities in Fortran code. It will provide an identifier which is
    guaranteed to be unique. This identifier can then me used as a
    filename for the documentation of that entity.
    """

    def __init__(self):
        self._items = {}
        self._counts = {}

    def get_name(self, item):
        """
        Return the name for this item registered with this NameSelector.
        If no name has previously been registered, then generate a new
        one.
        """
        if not isinstance(item, ford.sourceform.FortranBase):
            raise Exception(
                "{} is not of a type derived from FortranBase".format(str(item))
            )

        if item in self._items:
            return self._items[item]
        else:
            if item.get_dir() not in self._counts:
                self._counts[item.get_dir()] = {}
            if item.name in self._counts[item.get_dir()]:
                num = self._counts[item.get_dir()][item.name] + 1
            else:
                num = 1
            self._counts[item.get_dir()][item.name] = num
            name = item.name.lower()
            for symbol, replacement in {
                "<": "lt",
                ">": "gt",
                "/": "SLASH",
                "*": "ASTERISK",
            }.items():
                name = name.replace(symbol, replacement)
            if name == "":
                name = "__unnamed__"
            if num > 1:
                name = name + "~" + str(num)
            self._items[item] = name
            return name


namelist = NameSelector()


class ExternalModule(FortranModule):
    _project_list = "extModules"

    def __init__(self, name: str, url: str = "", parent=None):
        self.name = name
        self.external_url = url
        self.parent = parent
        self.obj = "module"
        self.uses = []
        self.pub_procs = {}
        self.pub_absints = {}
        self.pub_types = {}
        self.pub_vars = {}


class ExternalFunction(FortranFunction):
    _project_list = "extProcedures"

    def __init__(self, name: str, url: str = "", parent=None):
        self.name = name
        self.external_url = url
        self.parent = parent
        self.obj = "proc"
        self.proctype = "function"


class ExternalSubroutine(FortranSubroutine):
    _project_list = "extProcedures"

    def __init__(self, name: str, url: str = "", parent=None):
        self.name = name
        self.external_url = url
        self.parent = parent
        self.obj = "proc"
        self.proctype = "subroutine"


class ExternalInterface(FortranInterface):
    _project_list = "extProcedures"

    def __init__(self, name: str, url: str = "", parent=None):
        self.name = name
        self.external_url = url
        self.parent = parent
        self.obj = "proc"
        self.proctype = "interface"


class ExternalBoundProcedure(FortranBoundProcedure):
    _project_list = "extProcedures"

    def __init__(self, name: str, url: str = "", parent=None):
        self.name = name
        self.external_url = url
        self.parent = parent
        self.obj = "proc"


class ExternalType(FortranType):
    _project_list = "extTypes"

    def __init__(self, name: str, url: str = "", parent=None):
        self.name = name
        self.external_url = url
        self.parent = parent
        self.obj = "type"
        self.boundprocs = []


class ExternalVariable(FortranVariable):
    _project_list = "extVariables"

    def __init__(self, name: str, url: str = "", parent=None):
        self.name = name
        self.external_url = url
        self.parent = parent
        self.obj = "variable"


class ExternalSubmodule(FortranSubmodule):
    def __init__(self, name: str):
        self.name = name
        self.url = ""
        self.uses = []
        self.parent_submodule = None
        self.ancestor_module = ExternalModule("Parent module")


class ExternalProgram(FortranProgram):
    def __init__(self, name: str):
        self.name = name
        self.url = ""
        self.uses = []
        self.calls = []


class ExternalSourceFile(FortranSourceFile):
    def __init__(self, name: str):
        self.name = name
        self.url = ""
        self.modules = []
        self.submodules = []
        self.functions = []
        self.subroutines = []
        self.programs = []
        self.blockdata = []
