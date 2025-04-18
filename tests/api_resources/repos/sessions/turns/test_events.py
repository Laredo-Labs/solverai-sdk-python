# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from solver_api import SolverAPI, AsyncSolverAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_stream(self, client: SolverAPI) -> None:
        event_stream = client.repos.sessions.turns.events.stream(
            turn_id="turnId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
        )
        event_stream.response.close()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_stream(self, client: SolverAPI) -> None:
        response = client.repos.sessions.turns.events.with_raw_response.stream(
            turn_id="turnId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_stream(self, client: SolverAPI) -> None:
        with client.repos.sessions.turns.events.with_streaming_response.stream(
            turn_id="turnId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
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
            client.repos.sessions.turns.events.with_raw_response.stream(
                turn_id="turnId",
                provider="github",
                org="",
                repo="repo",
                session_id="sessionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.repos.sessions.turns.events.with_raw_response.stream(
                turn_id="turnId",
                provider="github",
                org="org",
                repo="",
                session_id="sessionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.repos.sessions.turns.events.with_raw_response.stream(
                turn_id="turnId",
                provider="github",
                org="org",
                repo="repo",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `turn_id` but received ''"):
            client.repos.sessions.turns.events.with_raw_response.stream(
                turn_id="",
                provider="github",
                org="org",
                repo="repo",
                session_id="sessionId",
            )


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_stream(self, async_client: AsyncSolverAPI) -> None:
        event_stream = await async_client.repos.sessions.turns.events.stream(
            turn_id="turnId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
        )
        await event_stream.response.aclose()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncSolverAPI) -> None:
        response = await async_client.repos.sessions.turns.events.with_raw_response.stream(
            turn_id="turnId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncSolverAPI) -> None:
        async with async_client.repos.sessions.turns.events.with_streaming_response.stream(
            turn_id="turnId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
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
            await async_client.repos.sessions.turns.events.with_raw_response.stream(
                turn_id="turnId",
                provider="github",
                org="",
                repo="repo",
                session_id="sessionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.repos.sessions.turns.events.with_raw_response.stream(
                turn_id="turnId",
                provider="github",
                org="org",
                repo="",
                session_id="sessionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.repos.sessions.turns.events.with_raw_response.stream(
                turn_id="turnId",
                provider="github",
                org="org",
                repo="repo",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `turn_id` but received ''"):
            await async_client.repos.sessions.turns.events.with_raw_response.stream(
                turn_id="",
                provider="github",
                org="org",
                repo="repo",
                session_id="sessionId",
            )
