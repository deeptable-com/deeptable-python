# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import structured_sheet_list_params, structured_sheet_create_params
from .exports import (
    ExportsResource,
    AsyncExportsResource,
    ExportsResourceWithRawResponse,
    AsyncExportsResourceWithRawResponse,
    ExportsResourceWithStreamingResponse,
    AsyncExportsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.structured_sheet_response import StructuredSheetResponse
from ...types.structured_sheet_list_response import StructuredSheetListResponse

__all__ = ["StructuredSheetsResource", "AsyncStructuredSheetsResource"]


class StructuredSheetsResource(SyncAPIResource):
    @cached_property
    def exports(self) -> ExportsResource:
        return ExportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> StructuredSheetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/deeptable-python#accessing-raw-response-data-eg-headers
        """
        return StructuredSheetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StructuredSheetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/deeptable-python#with_streaming_response
        """
        return StructuredSheetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file_id: str,
        sheet_names: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StructuredSheetResponse:
        """Start converting a spreadsheet workbook into structured data.

        This initiates an
        asynchronous conversion process. Poll the returned resource using the `id` to
        check completion status.

        Args:
          file_id: The unique identifier of the file to convert.

          sheet_names: List of sheet names to convert. If None, all sheets will be converted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/structured-sheets",
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "sheet_names": sheet_names,
                },
                structured_sheet_create_params.StructuredSheetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StructuredSheetResponse,
        )

    def retrieve(
        self,
        structured_sheets_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StructuredSheetResponse:
        """
        Get the status and details of a structured sheets conversion.

        Args:
          structured_sheets_id: The unique identifier of the structured sheets conversion.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not structured_sheets_id:
            raise ValueError(
                f"Expected a non-empty value for `structured_sheets_id` but received {structured_sheets_id!r}"
            )
        return self._get(
            f"/v1/structured-sheets/{structured_sheets_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StructuredSheetResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        starting_after: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StructuredSheetListResponse:
        """List all structured sheets conversions for the authenticated user.

        Results are
        paginated using cursor-based pagination.

        Args:
          limit: Maximum number of results to return per page.

          starting_after: Cursor for pagination. Use the `next_cursor` from a previous response to fetch
              the next page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/structured-sheets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "starting_after": starting_after,
                    },
                    structured_sheet_list_params.StructuredSheetListParams,
                ),
            ),
            cast_to=StructuredSheetListResponse,
        )

    def delete(
        self,
        structured_sheets_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a structured sheets conversion and its associated exports.

        This action
        cannot be undone.

        Args:
          structured_sheets_id: The unique identifier of the structured sheets conversion.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not structured_sheets_id:
            raise ValueError(
                f"Expected a non-empty value for `structured_sheets_id` but received {structured_sheets_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/structured-sheets/{structured_sheets_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncStructuredSheetsResource(AsyncAPIResource):
    @cached_property
    def exports(self) -> AsyncExportsResource:
        return AsyncExportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStructuredSheetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/deeptable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStructuredSheetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStructuredSheetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/deeptable-python#with_streaming_response
        """
        return AsyncStructuredSheetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file_id: str,
        sheet_names: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StructuredSheetResponse:
        """Start converting a spreadsheet workbook into structured data.

        This initiates an
        asynchronous conversion process. Poll the returned resource using the `id` to
        check completion status.

        Args:
          file_id: The unique identifier of the file to convert.

          sheet_names: List of sheet names to convert. If None, all sheets will be converted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/structured-sheets",
            body=await async_maybe_transform(
                {
                    "file_id": file_id,
                    "sheet_names": sheet_names,
                },
                structured_sheet_create_params.StructuredSheetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StructuredSheetResponse,
        )

    async def retrieve(
        self,
        structured_sheets_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StructuredSheetResponse:
        """
        Get the status and details of a structured sheets conversion.

        Args:
          structured_sheets_id: The unique identifier of the structured sheets conversion.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not structured_sheets_id:
            raise ValueError(
                f"Expected a non-empty value for `structured_sheets_id` but received {structured_sheets_id!r}"
            )
        return await self._get(
            f"/v1/structured-sheets/{structured_sheets_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StructuredSheetResponse,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        starting_after: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StructuredSheetListResponse:
        """List all structured sheets conversions for the authenticated user.

        Results are
        paginated using cursor-based pagination.

        Args:
          limit: Maximum number of results to return per page.

          starting_after: Cursor for pagination. Use the `next_cursor` from a previous response to fetch
              the next page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/structured-sheets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "starting_after": starting_after,
                    },
                    structured_sheet_list_params.StructuredSheetListParams,
                ),
            ),
            cast_to=StructuredSheetListResponse,
        )

    async def delete(
        self,
        structured_sheets_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a structured sheets conversion and its associated exports.

        This action
        cannot be undone.

        Args:
          structured_sheets_id: The unique identifier of the structured sheets conversion.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not structured_sheets_id:
            raise ValueError(
                f"Expected a non-empty value for `structured_sheets_id` but received {structured_sheets_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/structured-sheets/{structured_sheets_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class StructuredSheetsResourceWithRawResponse:
    def __init__(self, structured_sheets: StructuredSheetsResource) -> None:
        self._structured_sheets = structured_sheets

        self.create = to_raw_response_wrapper(
            structured_sheets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            structured_sheets.retrieve,
        )
        self.list = to_raw_response_wrapper(
            structured_sheets.list,
        )
        self.delete = to_raw_response_wrapper(
            structured_sheets.delete,
        )

    @cached_property
    def exports(self) -> ExportsResourceWithRawResponse:
        return ExportsResourceWithRawResponse(self._structured_sheets.exports)


class AsyncStructuredSheetsResourceWithRawResponse:
    def __init__(self, structured_sheets: AsyncStructuredSheetsResource) -> None:
        self._structured_sheets = structured_sheets

        self.create = async_to_raw_response_wrapper(
            structured_sheets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            structured_sheets.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            structured_sheets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            structured_sheets.delete,
        )

    @cached_property
    def exports(self) -> AsyncExportsResourceWithRawResponse:
        return AsyncExportsResourceWithRawResponse(self._structured_sheets.exports)


class StructuredSheetsResourceWithStreamingResponse:
    def __init__(self, structured_sheets: StructuredSheetsResource) -> None:
        self._structured_sheets = structured_sheets

        self.create = to_streamed_response_wrapper(
            structured_sheets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            structured_sheets.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            structured_sheets.list,
        )
        self.delete = to_streamed_response_wrapper(
            structured_sheets.delete,
        )

    @cached_property
    def exports(self) -> ExportsResourceWithStreamingResponse:
        return ExportsResourceWithStreamingResponse(self._structured_sheets.exports)


class AsyncStructuredSheetsResourceWithStreamingResponse:
    def __init__(self, structured_sheets: AsyncStructuredSheetsResource) -> None:
        self._structured_sheets = structured_sheets

        self.create = async_to_streamed_response_wrapper(
            structured_sheets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            structured_sheets.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            structured_sheets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            structured_sheets.delete,
        )

    @cached_property
    def exports(self) -> AsyncExportsResourceWithStreamingResponse:
        return AsyncExportsResourceWithStreamingResponse(self._structured_sheets.exports)
