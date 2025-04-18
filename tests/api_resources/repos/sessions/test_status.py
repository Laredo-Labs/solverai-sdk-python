# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from solver_api import SolverAPI, AsyncSolverAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_stream(self, client: SolverAPI) -> None:
        status_stream = client.repos.sessions.status.stream(
            repo="repo",
            provider="github",
            org="org",
        )
        status_stream.response.close()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_stream_with_all_params(self, client: SolverAPI) -> None:
        status_stream = client.repos.sessions.status.stream(
            repo="repo",
            provider="github",
            org="org",
            session_filter=["string"],
        )
        status_stream.response.close()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_stream(self, client: SolverAPI) -> None:
        response = client.repos.sessions.status.with_raw_response.stream(
            repo="repo",
            provider="github",
            org="org",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_stream(self, client: SolverAPI) -> None:
        with client.repos.sessions.status.with_streaming_response.stream(
            repo="repo",
            provider="github",
            org="org",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_path_params_stream(self, client: SolverAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org` but received ''"):
            client.repos.sessions.status.with_raw_response.stream(
                repo="repo",
                provider="github",
                org="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.repos.sessions.status.with_raw_response.stream(
                repo="",
                provider="github",
                org="org",
            )


class TestAsyncStatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_stream(self, async_client: AsyncSolverAPI) -> None:
        status_stream = await async_client.repos.sessions.status.stream(
            repo="repo",
            provider="github",
            org="org",
        )
        await status_stream.response.aclose()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncSolverAPI) -> None:
        status_stream = await async_client.repos.sessions.status.stream(
            repo="repo",
            provider="github",
            org="org",
            session_filter=["string"],
        )
        await status_stream.response.aclose()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncSolverAPI) -> None:
        response = await async_client.repos.sessions.status.with_raw_response.stream(
            repo="repo",
            provider="github",
            org="org",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncSolverAPI) -> None:
        async with async_client.repos.sessions.status.with_streaming_response.stream(
            repo="repo",
            provider="github",
            org="org",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_path_params_stream(self, async_client: AsyncSolverAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org` but received ''"):
            await async_client.repos.sessions.status.with_raw_response.stream(
                repo="repo",
                provider="github",
                org="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.repos.sessions.status.with_raw_response.stream(
                repo="",
                provider="github",
                org="org",
            )
