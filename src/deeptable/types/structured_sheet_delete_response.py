# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["StructuredSheetDeleteResponse"]


class StructuredSheetDeleteResponse(BaseModel):
    """Response from deleting a structured sheet.

    Following the OpenAI API convention for delete responses.
    """

    id: str
    """The unique identifier of the deleted structured sheet."""

    deleted: Literal[True]
    """Whether the structured sheet was successfully deleted."""

    object: Literal["structured_sheet"]
    """The object type, which is always 'structured_sheet'."""
