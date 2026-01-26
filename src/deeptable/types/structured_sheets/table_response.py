# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TableResponse"]


class TableResponse(BaseModel):
    """Response representing a table extracted from a structured sheet.

    This is returned from GET (retrieve) and list table endpoints.
    Table names use SQL naming conventions (e.g., monthly_head_count).
    """

    id: str
    """The unique identifier for this table."""

    created_at: datetime
    """The timestamp when this table was created."""

    name: str
    """The name of the table using SQL naming conventions."""

    sheet_name: str
    """The original Excel sheet name this table came from."""

    sheet_name_normalized: str
    """
    Normalized sheet name for use in SQLite table names and export filenames
    (lowercase, snake_case).
    """

    structured_sheet_id: str
    """The ID of the structured sheet this table belongs to."""

    type: Literal["relational", "aggregation", "tableless"]
    """The type of table (relational, aggregation, or tableless)."""

    object: Optional[Literal["table"]] = None
    """The object type, which is always 'table'."""
