# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .structured_sheet_response import StructuredSheetResponse

__all__ = ["StructuredSheetListResponse"]


class StructuredSheetListResponse(BaseModel):
    """Paginated response for listing structured sheets conversions.

    Uses cursor-based pagination for efficient iteration through results.
    """

    data: List[StructuredSheetResponse]
    """List of structured sheets conversions."""

    has_more: bool
    """Whether there are more results available after this page."""

    next_cursor: Optional[str] = None
    """Unique identifier for a structured sheets conversion."""

    object: Optional[Literal["list"]] = None
    """The object type, which is always 'list'."""
