# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["StructuredSheetListParams"]


class StructuredSheetListParams(TypedDict, total=False):
    after: Optional[str]
    """A cursor for pagination.

    Use the `last_id` from a previous response to fetch the next page of results.
    """

    limit: int
    """Maximum number of results to return per page."""
