# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .file import File
from .._models import BaseModel

__all__ = ["FileListResponse"]


class FileListResponse(BaseModel):
    """Paginated response for listing files.

    Uses cursor-based pagination for efficient iteration through results.
    """

    data: List[File]
    """List of files."""

    has_more: bool
    """Whether there are more results available after this page."""

    next_cursor: Optional[str] = None
    """Unique identifier for a file."""

    object: Optional[Literal["list"]] = None
    """The object type, which is always 'list'."""
