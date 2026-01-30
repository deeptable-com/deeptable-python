# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TableResponse"]


class TableResponse(BaseModel):
    """Response representing a table extracted from a structured sheet.

    This is returned from GET (retrieve) and list table endpoints.
    Table names use a composite format: {normalized_sheet_name}__{table_name}.
    """

    id: str
    """The unique identifier for this table."""

    created_at: datetime
    """The timestamp when this table was created."""

    name: str
    """Composite table name: {normalized_sheet_name}\\__\\__{table_name}.

    Uses lowercase snake_case. Aggregation tables end with '**aggregations'. Two
    special metadata tables exist per structured sheet:
    '**deeptable_workbook_metadata' (workbook provenance info) and
    '**deeptable_table_overview' (summary of all tables). Example:
    'staffing**head_count' or 'staffing**head_count**aggregations'.
    """

    object: Literal["table"]
    """The object type, which is always 'table'."""

    sheet_name: str
    """The original Excel sheet name this table came from."""

    structured_sheet_id: str
    """The ID of the structured sheet this table belongs to."""

    type: Literal["relational", "aggregation", "tableless", "metadata"]
    """The type of table (relational, aggregation, tableless, or metadata)."""
