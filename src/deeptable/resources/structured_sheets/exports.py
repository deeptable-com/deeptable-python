# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["ExportsResource", "AsyncExportsResource"]


class ExportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/deeptable-com/deeptable-python#accessing-raw-response-data-eg-headers
        """
        return ExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/deeptable-com/deeptable-python#with_streaming_response
        """
        return ExportsResourceWithStreamingResponse(self)

    def download_sqlite(
        self,
        structured_sheets_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Download the structured data as a SQLite database file.

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
        extra_headers = {"Accept": "application/x-sqlite3", **(extra_headers or {})}
        return self._get(
            f"/v1/structured-sheets/{structured_sheets_id}/exports/sqlite",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncExportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/deeptable-com/deeptable-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/deeptable-com/deeptable-python#with_streaming_response
        """
        return AsyncExportsResourceWithStreamingResponse(self)

    async def download_sqlite(
        self,
        structured_sheets_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Download the structured data as a SQLite database file.

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
        extra_headers = {"Accept": "application/x-sqlite3", **(extra_headers or {})}
        return await self._get(
            f"/v1/structured-sheets/{structured_sheets_id}/exports/sqlite",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ExportsResourceWithRawResponse:
    def __init__(self, exports: ExportsResource) -> None:
        self._exports = exports

        self.download_sqlite = to_custom_raw_response_wrapper(
            exports.download_sqlite,
            BinaryAPIResponse,
        )


class AsyncExportsResourceWithRawResponse:
    def __init__(self, exports: AsyncExportsResource) -> None:
        self._exports = exports

        self.download_sqlite = async_to_custom_raw_response_wrapper(
            exports.download_sqlite,
            AsyncBinaryAPIResponse,
        )


class ExportsResourceWithStreamingResponse:
    def __init__(self, exports: ExportsResource) -> None:
        self._exports = exports

        self.download_sqlite = to_custom_streamed_response_wrapper(
            exports.download_sqlite,
            StreamedBinaryAPIResponse,
        )


class AsyncExportsResourceWithStreamingResponse:
    def __init__(self, exports: AsyncExportsResource) -> None:
        self._exports = exports

        self.download_sqlite = async_to_custom_streamed_response_wrapper(
            exports.download_sqlite,
            AsyncStreamedBinaryAPIResponse,
        )
