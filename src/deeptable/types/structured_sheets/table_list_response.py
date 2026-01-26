# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .table_response import TableResponse

__all__ = ["TableListResponse"]


class TableListResponse(BaseModel):
    """Paginated response for listing tables from a structured sheet.

    Uses cursor-based pagination for efficient iteration through results.
    """

    data: List[TableResponse]
    """List of tables."""

    has_more: bool
    """Whether there are more results available after this page."""

    first_id: Optional[str] = None
    """Unique identifier for a table."""

    last_id: Optional[str] = None
    """Unique identifier for a table."""

    object: Optional[Literal["list"]] = None
    """The object type, which is always 'list'."""
