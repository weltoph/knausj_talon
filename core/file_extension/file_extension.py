from talon import Context, Module

from ..user_settings import get_list_from_csv

mod = Module()
mod.list("file_extension", desc="A file extension, such as .py")

_file_extensions_defaults = {
    "dot pie": ".py",
    "dot talon": ".talon",
    "dot mark down": ".md",
    "dot shell": ".sh",
    "dot vim": ".vim",
    "dot see": ".c",
    "dot bin": ".bin",
    "dot jason": ".json",
    "dot jay son": ".json",
    "dot csv": ".csv",
    "dot text": ".txt",
    "dot html": ".html",
    "dot doc": ".doc",
    "dot doc x": ".docx",
    "dot pdf": ".pdf",
    "dot zip": ".zip",
}

file_extensions = get_list_from_csv(
    "file_extensions.csv",
    headers=("File extension", "Name"),
    default=_file_extensions_defaults,
)

ctx = Context()
ctx.lists["self.file_extension"] = file_extensions
