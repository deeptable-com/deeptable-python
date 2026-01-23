# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from deeptable import DeepTable, AsyncDeepTable
from tests.utils import assert_matches_type
from deeptable.types import StructuredSheetResponse
from deeptable.pagination import SyncCursorIDPage, AsyncCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStructuredSheets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: DeepTable) -> None:
        structured_sheet = client.structured_sheets.create(
            file_id="file_01h45ytscbebyvny4gc8cr8ma2",
        )
        assert_matches_type(StructuredSheetResponse, structured_sheet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: DeepTable) -> None:
        structured_sheet = client.structured_sheets.create(
            file_id="file_01h45ytscbebyvny4gc8cr8ma2",
            sheet_names=["Sheet1", "Financials"],
        )
        assert_matches_type(StructuredSheetResponse, structured_sheet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: DeepTable) -> None:
        response = client.structured_sheets.with_raw_response.create(
            file_id="file_01h45ytscbebyvny4gc8cr8ma2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structured_sheet = response.parse()
        assert_matches_type(StructuredSheetResponse, structured_sheet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: DeepTable) -> None:
        with client.structured_sheets.with_streaming_response.create(
            file_id="file_01h45ytscbebyvny4gc8cr8ma2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structured_sheet = response.parse()
            assert_matches_type(StructuredSheetResponse, structured_sheet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: DeepTable) -> None:
        structured_sheet = client.structured_sheets.retrieve(
            "ss_01abc2def3ghjkmnpqrs4uvwxy",
        )
        assert_matches_type(StructuredSheetResponse, structured_sheet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: DeepTable) -> None:
        response = client.structured_sheets.with_raw_response.retrieve(
            "ss_01abc2def3ghjkmnpqrs4uvwxy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structured_sheet = response.parse()
        assert_matches_type(StructuredSheetResponse, structured_sheet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: DeepTable) -> None:
        with client.structured_sheets.with_streaming_response.retrieve(
            "ss_01abc2def3ghjkmnpqrs4uvwxy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structured_sheet = response.parse()
            assert_matches_type(StructuredSheetResponse, structured_sheet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: DeepTable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `structured_sheets_id` but received ''"):
            client.structured_sheets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: DeepTable) -> None:
        structured_sheet = client.structured_sheets.list()
        assert_matches_type(SyncCursorIDPage[StructuredSheetResponse], structured_sheet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: DeepTable) -> None:
        structured_sheet = client.structured_sheets.list(
            after="ss_01abc2def3ghjkmnpqrs4uvwxy",
            limit=20,
        )
        assert_matches_type(SyncCursorIDPage[StructuredSheetResponse], structured_sheet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: DeepTable) -> None:
        response = client.structured_sheets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structured_sheet = response.parse()
        assert_matches_type(SyncCursorIDPage[StructuredSheetResponse], structured_sheet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: DeepTable) -> None:
        with client.structured_sheets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structured_sheet = response.parse()
            assert_matches_type(SyncCursorIDPage[StructuredSheetResponse], structured_sheet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: DeepTable) -> None:
        structured_sheet = client.structured_sheets.delete(
            "ss_01abc2def3ghjkmnpqrs4uvwxy",
        )
        assert structured_sheet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: DeepTable) -> None:
        response = client.structured_sheets.with_raw_response.delete(
            "ss_01abc2def3ghjkmnpqrs4uvwxy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structured_sheet = response.parse()
        assert structured_sheet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: DeepTable) -> None:
        with client.structured_sheets.with_streaming_response.delete(
            "ss_01abc2def3ghjkmnpqrs4uvwxy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structured_sheet = response.parse()
            assert structured_sheet is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: DeepTable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `structured_sheets_id` but received ''"):
            client.structured_sheets.with_raw_response.delete(
                "",
            )


class TestAsyncStructuredSheets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncDeepTable) -> None:
        structured_sheet = await async_client.structured_sheets.create(
            file_id="file_01h45ytscbebyvny4gc8cr8ma2",
        )
        assert_matches_type(StructuredSheetResponse, structured_sheet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDeepTable) -> None:
        structured_sheet = await async_client.structured_sheets.create(
            file_id="file_01h45ytscbebyvny4gc8cr8ma2",
            sheet_names=["Sheet1", "Financials"],
        )
        assert_matches_type(StructuredSheetResponse, structured_sheet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDeepTable) -> None:
        response = await async_client.structured_sheets.with_raw_response.create(
            file_id="file_01h45ytscbebyvny4gc8cr8ma2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structured_sheet = await response.parse()
        assert_matches_type(StructuredSheetResponse, structured_sheet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDeepTable) -> None:
        async with async_client.structured_sheets.with_streaming_response.create(
            file_id="file_01h45ytscbebyvny4gc8cr8ma2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structured_sheet = await response.parse()
            assert_matches_type(StructuredSheetResponse, structured_sheet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDeepTable) -> None:
        structured_sheet = await async_client.structured_sheets.retrieve(
            "ss_01abc2def3ghjkmnpqrs4uvwxy",
        )
        assert_matches_type(StructuredSheetResponse, structured_sheet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDeepTable) -> None:
        response = await async_client.structured_sheets.with_raw_response.retrieve(
            "ss_01abc2def3ghjkmnpqrs4uvwxy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structured_sheet = await response.parse()
        assert_matches_type(StructuredSheetResponse, structured_sheet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDeepTable) -> None:
        async with async_client.structured_sheets.with_streaming_response.retrieve(
            "ss_01abc2def3ghjkmnpqrs4uvwxy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structured_sheet = await response.parse()
            assert_matches_type(StructuredSheetResponse, structured_sheet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDeepTable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `structured_sheets_id` but received ''"):
            await async_client.structured_sheets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDeepTable) -> None:
        structured_sheet = await async_client.structured_sheets.list()
        assert_matches_type(AsyncCursorIDPage[StructuredSheetResponse], structured_sheet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDeepTable) -> None:
        structured_sheet = await async_client.structured_sheets.list(
            after="ss_01abc2def3ghjkmnpqrs4uvwxy",
            limit=20,
        )
        assert_matches_type(AsyncCursorIDPage[StructuredSheetResponse], structured_sheet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDeepTable) -> None:
        response = await async_client.structured_sheets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structured_sheet = await response.parse()
        assert_matches_type(AsyncCursorIDPage[StructuredSheetResponse], structured_sheet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDeepTable) -> None:
        async with async_client.structured_sheets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structured_sheet = await response.parse()
            assert_matches_type(AsyncCursorIDPage[StructuredSheetResponse], structured_sheet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncDeepTable) -> None:
        structured_sheet = await async_client.structured_sheets.delete(
            "ss_01abc2def3ghjkmnpqrs4uvwxy",
        )
        assert structured_sheet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDeepTable) -> None:
        response = await async_client.structured_sheets.with_raw_response.delete(
            "ss_01abc2def3ghjkmnpqrs4uvwxy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structured_sheet = await response.parse()
        assert structured_sheet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDeepTable) -> None:
        async with async_client.structured_sheets.with_streaming_response.delete(
            "ss_01abc2def3ghjkmnpqrs4uvwxy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structured_sheet = await response.parse()
            assert structured_sheet is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDeepTable) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `structured_sheets_id` but received ''"):
            await async_client.structured_sheets.with_raw_response.delete(
                "",
            )
