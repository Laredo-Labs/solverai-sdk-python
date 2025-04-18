# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from solver_api import SolverAPI, AsyncSolverAPI
from tests.utils import assert_matches_type
from solver_api.types import RepoRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRepos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: SolverAPI) -> None:
        repo = client.repos.retrieve(
            "github",
        )
        assert_matches_type(RepoRetrieveResponse, repo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: SolverAPI) -> None:
        response = client.repos.with_raw_response.retrieve(
            "github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = response.parse()
        assert_matches_type(RepoRetrieveResponse, repo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: SolverAPI) -> None:
        with client.repos.with_streaming_response.retrieve(
            "github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = response.parse()
            assert_matches_type(RepoRetrieveResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRepos:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSolverAPI) -> None:
        repo = await async_client.repos.retrieve(
            "github",
        )
        assert_matches_type(RepoRetrieveResponse, repo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSolverAPI) -> None:
        response = await async_client.repos.with_raw_response.retrieve(
            "github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = await response.parse()
        assert_matches_type(RepoRetrieveResponse, repo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSolverAPI) -> None:
        async with async_client.repos.with_streaming_response.retrieve(
            "github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = await response.parse()
            assert_matches_type(RepoRetrieveResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True
