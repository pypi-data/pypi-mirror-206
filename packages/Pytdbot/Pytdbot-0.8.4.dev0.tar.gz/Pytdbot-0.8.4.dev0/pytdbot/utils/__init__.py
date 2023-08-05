__all__ = [
    "escape_markdown",
    "escape_html",
    "bold",
    "italic",
    "underline",
    "strikethrough",
    "spoiler",
    "hyperlink",
    "mention",
    "code",
    "pre",
    "pre_code",
    "is_type"
]

from .escape import escape_markdown, escape_html
from .text_format import (
    bold,
    italic,
    underline,
    strikethrough,
    spoiler,
    hyperlink,
    mention,
    code,
    pre,
    pre_code,
)

def is_type(obj, cls) -> bool:
    """
    Returns True if the type of the given object matches the specified class, False otherwise

    Args:
        obj: The object to check
        cls: The class to compare the object against

    Returns:
        A boolean indicating whether the type of the object matches the specified class

    . warning::

        This function should only be used on trusted values, since it relies on comparing the string names of the object's and class's types.
        It is possible for someone to create a custom class with the same name as a built-in or trusted class, which could lead to unexpected results
    """
    return obj.__class__.__name__ == cls.__class__.__name__
