# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    limit: int
    """Maximum number of files to return."""

    starting_after: Optional[str]
    """Cursor for pagination. Use the ID of the last file from the previous page."""
