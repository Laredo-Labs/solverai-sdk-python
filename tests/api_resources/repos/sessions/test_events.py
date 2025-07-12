# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from solverai import Solver, AsyncSolver
from tests.utils import assert_matches_type
from solverai.types.repos.sessions import TraceEvent, EventGetPatchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Solver) -> None:
        event = client.repos.sessions.events.get(
            event_id="eventId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
        )
        assert_matches_type(TraceEvent, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Solver) -> None:
        response = client.repos.sessions.events.with_raw_response.get(
            event_id="eventId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(TraceEvent, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Solver) -> None:
        with client.repos.sessions.events.with_streaming_response.get(
            event_id="eventId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(TraceEvent, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Solver) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org` but received ''"):
            client.repos.sessions.events.with_raw_response.get(
                event_id="eventId",
                provider="github",
                org="",
                repo="repo",
                session_id="sessionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.repos.sessions.events.with_raw_response.get(
                event_id="eventId",
                provider="github",
                org="org",
                repo="",
                session_id="sessionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.repos.sessions.events.with_raw_response.get(
                event_id="eventId",
                provider="github",
                org="org",
                repo="repo",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.repos.sessions.events.with_raw_response.get(
                event_id="",
                provider="github",
                org="org",
                repo="repo",
                session_id="sessionId",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_patch(self, client: Solver) -> None:
        event = client.repos.sessions.events.get_patch(
            event_id="eventId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
        )
        assert_matches_type(EventGetPatchResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_patch_with_all_params(self, client: Solver) -> None:
        event = client.repos.sessions.events.get_patch(
            event_id="eventId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
            context_lines=0,
            interhunk_lines=0,
        )
        assert_matches_type(EventGetPatchResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_patch(self, client: Solver) -> None:
        response = client.repos.sessions.events.with_raw_response.get_patch(
            event_id="eventId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventGetPatchResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_patch(self, client: Solver) -> None:
        with client.repos.sessions.events.with_streaming_response.get_patch(
            event_id="eventId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventGetPatchResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_patch(self, client: Solver) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org` but received ''"):
            client.repos.sessions.events.with_raw_response.get_patch(
                event_id="eventId",
                provider="github",
                org="",
                repo="repo",
                session_id="sessionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.repos.sessions.events.with_raw_response.get_patch(
                event_id="eventId",
                provider="github",
                org="org",
                repo="",
                session_id="sessionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.repos.sessions.events.with_raw_response.get_patch(
                event_id="eventId",
                provider="github",
                org="org",
                repo="repo",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.repos.sessions.events.with_raw_response.get_patch(
                event_id="",
                provider="github",
                org="org",
                repo="repo",
                session_id="sessionId",
            )


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncSolver) -> None:
        event = await async_client.repos.sessions.events.get(
            event_id="eventId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
        )
        assert_matches_type(TraceEvent, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncSolver) -> None:
        response = await async_client.repos.sessions.events.with_raw_response.get(
            event_id="eventId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(TraceEvent, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncSolver) -> None:
        async with async_client.repos.sessions.events.with_streaming_response.get(
            event_id="eventId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(TraceEvent, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncSolver) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org` but received ''"):
            await async_client.repos.sessions.events.with_raw_response.get(
                event_id="eventId",
                provider="github",
                org="",
                repo="repo",
                session_id="sessionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.repos.sessions.events.with_raw_response.get(
                event_id="eventId",
                provider="github",
                org="org",
                repo="",
                session_id="sessionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.repos.sessions.events.with_raw_response.get(
                event_id="eventId",
                provider="github",
                org="org",
                repo="repo",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.repos.sessions.events.with_raw_response.get(
                event_id="",
                provider="github",
                org="org",
                repo="repo",
                session_id="sessionId",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_patch(self, async_client: AsyncSolver) -> None:
        event = await async_client.repos.sessions.events.get_patch(
            event_id="eventId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
        )
        assert_matches_type(EventGetPatchResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_patch_with_all_params(self, async_client: AsyncSolver) -> None:
        event = await async_client.repos.sessions.events.get_patch(
            event_id="eventId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
            context_lines=0,
            interhunk_lines=0,
        )
        assert_matches_type(EventGetPatchResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_patch(self, async_client: AsyncSolver) -> None:
        response = await async_client.repos.sessions.events.with_raw_response.get_patch(
            event_id="eventId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventGetPatchResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_patch(self, async_client: AsyncSolver) -> None:
        async with async_client.repos.sessions.events.with_streaming_response.get_patch(
            event_id="eventId",
            provider="github",
            org="org",
            repo="repo",
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventGetPatchResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_patch(self, async_client: AsyncSolver) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org` but received ''"):
            await async_client.repos.sessions.events.with_raw_response.get_patch(
                event_id="eventId",
                provider="github",
                org="",
                repo="repo",
                session_id="sessionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.repos.sessions.events.with_raw_response.get_patch(
                event_id="eventId",
                provider="github",
                org="org",
                repo="",
                session_id="sessionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.repos.sessions.events.with_raw_response.get_patch(
                event_id="eventId",
                provider="github",
                org="org",
                repo="repo",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.repos.sessions.events.with_raw_response.get_patch(
                event_id="",
                provider="github",
                org="org",
                repo="repo",
                session_id="sessionId",
            )
