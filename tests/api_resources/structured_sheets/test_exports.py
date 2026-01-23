# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from deeptable import DeepTable, AsyncDeepTable
from deeptable._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_sqlite(self, client: DeepTable, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/structured-sheets/ss_01abc2def3ghjkmnpqrs4uvwxy/exports/sqlite").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        export = client.structured_sheets.exports.download_sqlite(
            "ss_01abc2def3ghjkmnpqrs4uvwxy",
        )
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download_sqlite(self, client: DeepTable, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/structured-sheets/ss_01abc2def3ghjkmnpqrs4uvwxy/exports/sqlite").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        export = client.structured_sheets.exports.with_raw_response.download_sqlite(
            "ss_01abc2def3ghjkmnpqrs4uvwxy",
        )

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert export.json() == {"foo": "bar"}
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download_sqlite(self, client: DeepTable, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/structured-sheets/ss_01abc2def3ghjkmnpqrs4uvwxy/exports/sqlite").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.structured_sheets.exports.with_streaming_response.download_sqlite(
            "ss_01abc2def3ghjkmnpqrs4uvwxy",
        ) as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, StreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download_sqlite(self, client: DeepTable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `structured_sheets_id` but received ''"):
            client.structured_sheets.exports.with_raw_response.download_sqlite(
                "",
            )


class TestAsyncExports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_sqlite(self, async_client: AsyncDeepTable, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/structured-sheets/ss_01abc2def3ghjkmnpqrs4uvwxy/exports/sqlite").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        export = await async_client.structured_sheets.exports.download_sqlite(
            "ss_01abc2def3ghjkmnpqrs4uvwxy",
        )
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download_sqlite(self, async_client: AsyncDeepTable, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/structured-sheets/ss_01abc2def3ghjkmnpqrs4uvwxy/exports/sqlite").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        export = await async_client.structured_sheets.exports.with_raw_response.download_sqlite(
            "ss_01abc2def3ghjkmnpqrs4uvwxy",
        )

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await export.json() == {"foo": "bar"}
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download_sqlite(
        self, async_client: AsyncDeepTable, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/structured-sheets/ss_01abc2def3ghjkmnpqrs4uvwxy/exports/sqlite").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.structured_sheets.exports.with_streaming_response.download_sqlite(
            "ss_01abc2def3ghjkmnpqrs4uvwxy",
        ) as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download_sqlite(self, async_client: AsyncDeepTable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `structured_sheets_id` but received ''"):
            await async_client.structured_sheets.exports.with_raw_response.download_sqlite(
                "",
            )
