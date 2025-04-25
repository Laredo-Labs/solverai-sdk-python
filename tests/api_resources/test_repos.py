# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from solverai import Solver, AsyncSolver
from tests.utils import assert_matches_type
from solverai.types import RepoListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRepos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Solver) -> None:
        repo = client.repos.list(
            "github",
        )
        assert_matches_type(RepoListResponse, repo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Solver) -> None:
        response = client.repos.with_raw_response.list(
            "github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = response.parse()
        assert_matches_type(RepoListResponse, repo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Solver) -> None:
        with client.repos.with_streaming_response.list(
            "github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = response.parse()
            assert_matches_type(RepoListResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRepos:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncSolver) -> None:
        repo = await async_client.repos.list(
            "github",
        )
        assert_matches_type(RepoListResponse, repo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSolver) -> None:
        response = await async_client.repos.with_raw_response.list(
            "github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = await response.parse()
        assert_matches_type(RepoListResponse, repo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSolver) -> None:
        async with async_client.repos.with_streaming_response.list(
            "github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = await response.parse()
            assert_matches_type(RepoListResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True
