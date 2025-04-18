# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from solver_api import SolverAPI, AsyncSolverAPI
from tests.utils import assert_matches_type
from solver_api.types.repos import (
    Turn,
    Session,
    SessionListResponse,
    SessionPatchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: SolverAPI) -> None:
        session = client.repos.sessions.create(
            repo="repo",
            provider="github",
            org="org",
            user_branch_name="userBranchName",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: SolverAPI) -> None:
        session = client.repos.sessions.create(
            repo="repo",
            provider="github",
            org="org",
            user_branch_name="userBranchName",
            description="description",
            title="title",
            visibility="private",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: SolverAPI) -> None:
        response = client.repos.sessions.with_raw_response.create(
            repo="repo",
            provider="github",
            org="org",
            user_branch_name="userBranchName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: SolverAPI) -> None:
        with client.repos.sessions.with_streaming_response.create(
            repo="repo",
            provider="github",
            org="org",
            user_branch_name="userBranchName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: SolverAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org` but received ''"):
            client.repos.sessions.with_raw_response.create(
                repo="repo",
                provider="github",
                org="",
                user_branch_name="userBranchName",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.repos.sessions.with_raw_response.create(
                repo="",
                provider="github",
                org="org",
                user_branch_name="userBranchName",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: SolverAPI) -> None:
        session = client.repos.sessions.retrieve(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: SolverAPI) -> None:
        response = client.repos.sessions.with_raw_response.retrieve(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: SolverAPI) -> None:
        with client.repos.sessions.with_streaming_response.retrieve(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: SolverAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org` but received ''"):
            client.repos.sessions.with_raw_response.retrieve(
                session_id="sessionId",
                provider="github",
                org="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.repos.sessions.with_raw_response.retrieve(
                session_id="sessionId",
                provider="github",
                org="org",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.repos.sessions.with_raw_response.retrieve(
                session_id="",
                provider="github",
                org="org",
                repo="repo",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: SolverAPI) -> None:
        session = client.repos.sessions.list(
            repo="repo",
            provider="github",
            org="org",
        )
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: SolverAPI) -> None:
        session = client.repos.sessions.list(
            repo="repo",
            provider="github",
            org="org",
            only_user_owned=True,
            page_offset=0,
            page_size=0,
            sort_attribute="created",
            sort_order="ascending",
            status_filter=["pending"],
            title_filter="titleFilter",
        )
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: SolverAPI) -> None:
        response = client.repos.sessions.with_raw_response.list(
            repo="repo",
            provider="github",
            org="org",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: SolverAPI) -> None:
        with client.repos.sessions.with_streaming_response.list(
            repo="repo",
            provider="github",
            org="org",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionListResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: SolverAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org` but received ''"):
            client.repos.sessions.with_raw_response.list(
                repo="repo",
                provider="github",
                org="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.repos.sessions.with_raw_response.list(
                repo="",
                provider="github",
                org="org",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_patch(self, client: SolverAPI) -> None:
        session = client.repos.sessions.patch(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
        )
        assert_matches_type(SessionPatchResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_patch_with_all_params(self, client: SolverAPI) -> None:
        session = client.repos.sessions.patch(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
            context_lines=0,
            interhunk_lines=0,
        )
        assert_matches_type(SessionPatchResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_patch(self, client: SolverAPI) -> None:
        response = client.repos.sessions.with_raw_response.patch(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionPatchResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_patch(self, client: SolverAPI) -> None:
        with client.repos.sessions.with_streaming_response.patch(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionPatchResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_patch(self, client: SolverAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org` but received ''"):
            client.repos.sessions.with_raw_response.patch(
                session_id="sessionId",
                provider="github",
                org="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.repos.sessions.with_raw_response.patch(
                session_id="sessionId",
                provider="github",
                org="org",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.repos.sessions.with_raw_response.patch(
                session_id="",
                provider="github",
                org="org",
                repo="repo",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_solve(self, client: SolverAPI) -> None:
        session = client.repos.sessions.solve(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
            instruction="instruction",
            num_steps=0,
        )
        assert_matches_type(Turn, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_solve_with_all_params(self, client: SolverAPI) -> None:
        session = client.repos.sessions.solve(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
            instruction="instruction",
            num_steps=0,
            invocation_options={"foo": "string"},
        )
        assert_matches_type(Turn, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_solve(self, client: SolverAPI) -> None:
        response = client.repos.sessions.with_raw_response.solve(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
            instruction="instruction",
            num_steps=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Turn, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_solve(self, client: SolverAPI) -> None:
        with client.repos.sessions.with_streaming_response.solve(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
            instruction="instruction",
            num_steps=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Turn, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_solve(self, client: SolverAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org` but received ''"):
            client.repos.sessions.with_raw_response.solve(
                session_id="sessionId",
                provider="github",
                org="",
                repo="repo",
                instruction="instruction",
                num_steps=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.repos.sessions.with_raw_response.solve(
                session_id="sessionId",
                provider="github",
                org="org",
                repo="",
                instruction="instruction",
                num_steps=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.repos.sessions.with_raw_response.solve(
                session_id="",
                provider="github",
                org="org",
                repo="repo",
                instruction="instruction",
                num_steps=0,
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncSolverAPI) -> None:
        session = await async_client.repos.sessions.create(
            repo="repo",
            provider="github",
            org="org",
            user_branch_name="userBranchName",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSolverAPI) -> None:
        session = await async_client.repos.sessions.create(
            repo="repo",
            provider="github",
            org="org",
            user_branch_name="userBranchName",
            description="description",
            title="title",
            visibility="private",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSolverAPI) -> None:
        response = await async_client.repos.sessions.with_raw_response.create(
            repo="repo",
            provider="github",
            org="org",
            user_branch_name="userBranchName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSolverAPI) -> None:
        async with async_client.repos.sessions.with_streaming_response.create(
            repo="repo",
            provider="github",
            org="org",
            user_branch_name="userBranchName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncSolverAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org` but received ''"):
            await async_client.repos.sessions.with_raw_response.create(
                repo="repo",
                provider="github",
                org="",
                user_branch_name="userBranchName",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.repos.sessions.with_raw_response.create(
                repo="",
                provider="github",
                org="org",
                user_branch_name="userBranchName",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSolverAPI) -> None:
        session = await async_client.repos.sessions.retrieve(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSolverAPI) -> None:
        response = await async_client.repos.sessions.with_raw_response.retrieve(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSolverAPI) -> None:
        async with async_client.repos.sessions.with_streaming_response.retrieve(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSolverAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org` but received ''"):
            await async_client.repos.sessions.with_raw_response.retrieve(
                session_id="sessionId",
                provider="github",
                org="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.repos.sessions.with_raw_response.retrieve(
                session_id="sessionId",
                provider="github",
                org="org",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.repos.sessions.with_raw_response.retrieve(
                session_id="",
                provider="github",
                org="org",
                repo="repo",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncSolverAPI) -> None:
        session = await async_client.repos.sessions.list(
            repo="repo",
            provider="github",
            org="org",
        )
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSolverAPI) -> None:
        session = await async_client.repos.sessions.list(
            repo="repo",
            provider="github",
            org="org",
            only_user_owned=True,
            page_offset=0,
            page_size=0,
            sort_attribute="created",
            sort_order="ascending",
            status_filter=["pending"],
            title_filter="titleFilter",
        )
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSolverAPI) -> None:
        response = await async_client.repos.sessions.with_raw_response.list(
            repo="repo",
            provider="github",
            org="org",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSolverAPI) -> None:
        async with async_client.repos.sessions.with_streaming_response.list(
            repo="repo",
            provider="github",
            org="org",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionListResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncSolverAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org` but received ''"):
            await async_client.repos.sessions.with_raw_response.list(
                repo="repo",
                provider="github",
                org="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.repos.sessions.with_raw_response.list(
                repo="",
                provider="github",
                org="org",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_patch(self, async_client: AsyncSolverAPI) -> None:
        session = await async_client.repos.sessions.patch(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
        )
        assert_matches_type(SessionPatchResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_patch_with_all_params(self, async_client: AsyncSolverAPI) -> None:
        session = await async_client.repos.sessions.patch(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
            context_lines=0,
            interhunk_lines=0,
        )
        assert_matches_type(SessionPatchResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_patch(self, async_client: AsyncSolverAPI) -> None:
        response = await async_client.repos.sessions.with_raw_response.patch(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionPatchResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_patch(self, async_client: AsyncSolverAPI) -> None:
        async with async_client.repos.sessions.with_streaming_response.patch(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionPatchResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_patch(self, async_client: AsyncSolverAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org` but received ''"):
            await async_client.repos.sessions.with_raw_response.patch(
                session_id="sessionId",
                provider="github",
                org="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.repos.sessions.with_raw_response.patch(
                session_id="sessionId",
                provider="github",
                org="org",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.repos.sessions.with_raw_response.patch(
                session_id="",
                provider="github",
                org="org",
                repo="repo",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_solve(self, async_client: AsyncSolverAPI) -> None:
        session = await async_client.repos.sessions.solve(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
            instruction="instruction",
            num_steps=0,
        )
        assert_matches_type(Turn, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_solve_with_all_params(self, async_client: AsyncSolverAPI) -> None:
        session = await async_client.repos.sessions.solve(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
            instruction="instruction",
            num_steps=0,
            invocation_options={"foo": "string"},
        )
        assert_matches_type(Turn, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_solve(self, async_client: AsyncSolverAPI) -> None:
        response = await async_client.repos.sessions.with_raw_response.solve(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
            instruction="instruction",
            num_steps=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Turn, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_solve(self, async_client: AsyncSolverAPI) -> None:
        async with async_client.repos.sessions.with_streaming_response.solve(
            session_id="sessionId",
            provider="github",
            org="org",
            repo="repo",
            instruction="instruction",
            num_steps=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Turn, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_solve(self, async_client: AsyncSolverAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org` but received ''"):
            await async_client.repos.sessions.with_raw_response.solve(
                session_id="sessionId",
                provider="github",
                org="",
                repo="repo",
                instruction="instruction",
                num_steps=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.repos.sessions.with_raw_response.solve(
                session_id="sessionId",
                provider="github",
                org="org",
                repo="",
                instruction="instruction",
                num_steps=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.repos.sessions.with_raw_response.solve(
                session_id="",
                provider="github",
                org="org",
                repo="repo",
                instruction="instruction",
                num_steps=0,
            )
