# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileDeleteResponse"]


class FileDeleteResponse(BaseModel):
    """Response from deleting a file.

    Following the OpenAI API convention for delete responses.
    """

    id: str
    """The unique identifier of the deleted file."""

    deleted: Literal[True]
    """Whether the file was successfully deleted."""

    object: Literal["file"]
    """The object type, which is always 'file'."""
