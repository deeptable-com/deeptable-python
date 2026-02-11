# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    after: Optional[str]
    """A cursor for pagination.

    Use the `last_id` from a previous response to fetch the next page.
    """

    limit: int
    """Maximum number of files to return."""
