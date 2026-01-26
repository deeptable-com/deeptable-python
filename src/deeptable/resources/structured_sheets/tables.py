# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.structured_sheets import table_download_params
from ...types.structured_sheets.table_response import TableResponse
from ...types.structured_sheets.table_list_response import TableListResponse

__all__ = ["TablesResource", "AsyncTablesResource"]


class TablesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TablesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/deeptable-com/deeptable-python#accessing-raw-response-data-eg-headers
        """
        return TablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TablesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/deeptable-com/deeptable-python#with_streaming_response
        """
        return TablesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        table_id: str,
        *,
        structured_sheets_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TableResponse:
        """Get details of a specific table extracted from the structured sheet.

        Only
        available when conversion status is 'completed'.

        Args:
          structured_sheets_id: The unique identifier of the structured sheets conversion.

          table_id: The unique identifier of the table.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not structured_sheets_id:
            raise ValueError(
                f"Expected a non-empty value for `structured_sheets_id` but received {structured_sheets_id!r}"
            )
        if not table_id:
            raise ValueError(f"Expected a non-empty value for `table_id` but received {table_id!r}")
        return self._get(
            f"/v1/structured-sheets/{structured_sheets_id}/tables/{table_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TableResponse,
        )

    def list(
        self,
        structured_sheets_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TableListResponse:
        """List all tables extracted from the structured sheet.

        Only available when
        conversion status is 'completed'.

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
            f"/v1/structured-sheets/{structured_sheets_id}/tables",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TableListResponse,
        )

    def download(
        self,
        table_id: str,
        *,
        structured_sheets_id: str,
        format: Literal["parquet", "csv"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Download the table data in the specified format.

        Available formats:

        - `parquet`: Apache Parquet columnar format (recommended for data analysis)
        - `csv`: Comma-separated values (compatible with any spreadsheet application)

        Args:
          structured_sheets_id: The unique identifier of the structured sheets conversion.

          table_id: The unique identifier of the table.

          format: The format to download the table data in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not structured_sheets_id:
            raise ValueError(
                f"Expected a non-empty value for `structured_sheets_id` but received {structured_sheets_id!r}"
            )
        if not table_id:
            raise ValueError(f"Expected a non-empty value for `table_id` but received {table_id!r}")
        extra_headers = {"Accept": "application/vnd.apache.parquet", **(extra_headers or {})}
        return self._get(
            f"/v1/structured-sheets/{structured_sheets_id}/tables/{table_id}/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, table_download_params.TableDownloadParams),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncTablesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTablesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/deeptable-com/deeptable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTablesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/deeptable-com/deeptable-python#with_streaming_response
        """
        return AsyncTablesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        table_id: str,
        *,
        structured_sheets_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TableResponse:
        """Get details of a specific table extracted from the structured sheet.

        Only
        available when conversion status is 'completed'.

        Args:
          structured_sheets_id: The unique identifier of the structured sheets conversion.

          table_id: The unique identifier of the table.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not structured_sheets_id:
            raise ValueError(
                f"Expected a non-empty value for `structured_sheets_id` but received {structured_sheets_id!r}"
            )
        if not table_id:
            raise ValueError(f"Expected a non-empty value for `table_id` but received {table_id!r}")
        return await self._get(
            f"/v1/structured-sheets/{structured_sheets_id}/tables/{table_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TableResponse,
        )

    async def list(
        self,
        structured_sheets_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TableListResponse:
        """List all tables extracted from the structured sheet.

        Only available when
        conversion status is 'completed'.

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
            f"/v1/structured-sheets/{structured_sheets_id}/tables",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TableListResponse,
        )

    async def download(
        self,
        table_id: str,
        *,
        structured_sheets_id: str,
        format: Literal["parquet", "csv"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Download the table data in the specified format.

        Available formats:

        - `parquet`: Apache Parquet columnar format (recommended for data analysis)
        - `csv`: Comma-separated values (compatible with any spreadsheet application)

        Args:
          structured_sheets_id: The unique identifier of the structured sheets conversion.

          table_id: The unique identifier of the table.

          format: The format to download the table data in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not structured_sheets_id:
            raise ValueError(
                f"Expected a non-empty value for `structured_sheets_id` but received {structured_sheets_id!r}"
            )
        if not table_id:
            raise ValueError(f"Expected a non-empty value for `table_id` but received {table_id!r}")
        extra_headers = {"Accept": "application/vnd.apache.parquet", **(extra_headers or {})}
        return await self._get(
            f"/v1/structured-sheets/{structured_sheets_id}/tables/{table_id}/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, table_download_params.TableDownloadParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class TablesResourceWithRawResponse:
    def __init__(self, tables: TablesResource) -> None:
        self._tables = tables

        self.retrieve = to_raw_response_wrapper(
            tables.retrieve,
        )
        self.list = to_raw_response_wrapper(
            tables.list,
        )
        self.download = to_custom_raw_response_wrapper(
            tables.download,
            BinaryAPIResponse,
        )


class AsyncTablesResourceWithRawResponse:
    def __init__(self, tables: AsyncTablesResource) -> None:
        self._tables = tables

        self.retrieve = async_to_raw_response_wrapper(
            tables.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            tables.list,
        )
        self.download = async_to_custom_raw_response_wrapper(
            tables.download,
            AsyncBinaryAPIResponse,
        )


class TablesResourceWithStreamingResponse:
    def __init__(self, tables: TablesResource) -> None:
        self._tables = tables

        self.retrieve = to_streamed_response_wrapper(
            tables.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            tables.list,
        )
        self.download = to_custom_streamed_response_wrapper(
            tables.download,
            StreamedBinaryAPIResponse,
        )


class AsyncTablesResourceWithStreamingResponse:
    def __init__(self, tables: AsyncTablesResource) -> None:
        self._tables = tables

        self.retrieve = async_to_streamed_response_wrapper(
            tables.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tables.list,
        )
        self.download = async_to_custom_streamed_response_wrapper(
            tables.download,
            AsyncStreamedBinaryAPIResponse,
        )
