"""
Utilities for managing compat between notebook versions.

Taken from: https://github.com/quantopian/pgcontents/blob/master/pgcontents/utils/ipycompat.py
"""

from ipython_genutils.importstring import import_item
from ipython_genutils.py3compat import string_types
from nbformat import from_dict, reads, writes
from nbformat.v4.nbbase import (
    new_code_cell,
    new_markdown_cell,
    new_notebook,
    new_raw_cell,
)
from nbformat.v4.rwbase import strip_transient
from jupyter_server.services.contents.checkpoints import (
    Checkpoints,
    GenericCheckpointsMixin,
)
from jupyter_server.services.contents.filecheckpoints import GenericFileCheckpoints
from jupyter_server.services.contents.filemanager import FileContentsManager
from jupyter_server.services.contents.manager import ContentsManager
from jupyter_server.utils import to_os_path
from traitlets import (
    Any,
    Bool,
    Dict,
    HasTraits,
    Instance,
    Integer,
    TraitError,
    Unicode,
    validate,
)
from traitlets.config import Config


__all__ = [
    "Any",
    "Bool",
    "Checkpoints",
    "Config",
    "ContentsManager",
    "Dict",
    "FileContentsManager",
    "GenericCheckpointsMixin",
    "GenericFileCheckpoints",
    "HasTraits",
    "Instance",
    "Integer",
    "TraitError",
    "Unicode",
    "from_dict",
    "import_item",
    "new_code_cell",
    "new_markdown_cell",
    "new_notebook",
    "new_raw_cell",
    "reads",
    "string_types",
    "strip_transient",
    "to_os_path",
    "validate",
    "writes",
]
