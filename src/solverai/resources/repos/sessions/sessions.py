# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import Literal

import httpx

from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from .status import (
    StatusResource,
    AsyncStatusResource,
    StatusResourceWithRawResponse,
    AsyncStatusResourceWithRawResponse,
    StatusResourceWithStreamingResponse,
    AsyncStatusResourceWithStreamingResponse,
)
from ....types import VcsProvider
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .turns.turns import (
    TurnsResource,
    AsyncTurnsResource,
    TurnsResourceWithRawResponse,
    AsyncTurnsResourceWithRawResponse,
    TurnsResourceWithStreamingResponse,
    AsyncTurnsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.repos import (
    SessionVisibility,
    session_list_params,
    session_solve_params,
    session_create_params,
    session_get_patch_params,
)
from ...._base_client import make_request_options
from ....types.repos.turn import Turn
from ....types.vcs_provider import VcsProvider
from ....types.repos.session import Session
from ....types.repos.session_status import SessionStatus
from ....types.repos.session_visibility import SessionVisibility
from ....types.repos.session_list_response import SessionListResponse
from ....types.repos.session_get_patch_response import SessionGetPatchResponse

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def status(self) -> StatusResource:
        return StatusResource(self._client)

    @cached_property
    def turns(self) -> TurnsResource:
        return TurnsResource(self._client)

    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/solver-api-python#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/solver-api-python#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        provider: VcsProvider,
        org: str,
        user_branch_name: str,
        description: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        visibility: SessionVisibility | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/alpha/repos/{provider}/{org}/{repo}/sessions",
            body=maybe_transform(
                {
                    "user_branch_name": user_branch_name,
                    "description": description,
                    "title": title,
                    "visibility": visibility,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def list(
        self,
        repo: str,
        *,
        provider: VcsProvider,
        org: str,
        only_user_owned: bool | NotGiven = NOT_GIVEN,
        page_offset: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        sort_attribute: Literal["created", "lastModified"] | NotGiven = NOT_GIVEN,
        sort_order: Literal["ascending", "descending"] | NotGiven = NOT_GIVEN,
        status_filter: List[SessionStatus] | NotGiven = NOT_GIVEN,
        title_filter: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/alpha/repos/{provider}/{org}/{repo}/sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "only_user_owned": only_user_owned,
                        "page_offset": page_offset,
                        "page_size": page_size,
                        "sort_attribute": sort_attribute,
                        "sort_order": sort_order,
                        "status_filter": status_filter,
                        "title_filter": title_filter,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            cast_to=SessionListResponse,
        )

    def get(
        self,
        session_id: str,
        *,
        provider: VcsProvider,
        org: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/alpha/repos/{provider}/{org}/{repo}/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def get_patch(
        self,
        session_id: str,
        *,
        provider: VcsProvider,
        org: str,
        repo: str,
        context_lines: int | NotGiven = NOT_GIVEN,
        interhunk_lines: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionGetPatchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/alpha/repos/{provider}/{org}/{repo}/sessions/{session_id}/patch",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "context_lines": context_lines,
                        "interhunk_lines": interhunk_lines,
                    },
                    session_get_patch_params.SessionGetPatchParams,
                ),
            ),
            cast_to=SessionGetPatchResponse,
        )

    def solve(
        self,
        session_id: str,
        *,
        provider: VcsProvider,
        org: str,
        repo: str,
        instruction: str,
        num_steps: int,
        invocation_options: Dict[str, Union[str, bool, float]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Turn:
        """
        Args:
          num_steps: The maximum number of steps to take when Solving

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/alpha/repos/{provider}/{org}/{repo}/sessions/{session_id}/solve",
            body=maybe_transform(
                {
                    "instruction": instruction,
                    "num_steps": num_steps,
                    "invocation_options": invocation_options,
                },
                session_solve_params.SessionSolveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Turn,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def status(self) -> AsyncStatusResource:
        return AsyncStatusResource(self._client)

    @cached_property
    def turns(self) -> AsyncTurnsResource:
        return AsyncTurnsResource(self._client)

    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/solver-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/solver-api-python#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        provider: VcsProvider,
        org: str,
        user_branch_name: str,
        description: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        visibility: SessionVisibility | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/alpha/repos/{provider}/{org}/{repo}/sessions",
            body=await async_maybe_transform(
                {
                    "user_branch_name": user_branch_name,
                    "description": description,
                    "title": title,
                    "visibility": visibility,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    async def list(
        self,
        repo: str,
        *,
        provider: VcsProvider,
        org: str,
        only_user_owned: bool | NotGiven = NOT_GIVEN,
        page_offset: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        sort_attribute: Literal["created", "lastModified"] | NotGiven = NOT_GIVEN,
        sort_order: Literal["ascending", "descending"] | NotGiven = NOT_GIVEN,
        status_filter: List[SessionStatus] | NotGiven = NOT_GIVEN,
        title_filter: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/alpha/repos/{provider}/{org}/{repo}/sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "only_user_owned": only_user_owned,
                        "page_offset": page_offset,
                        "page_size": page_size,
                        "sort_attribute": sort_attribute,
                        "sort_order": sort_order,
                        "status_filter": status_filter,
                        "title_filter": title_filter,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            cast_to=SessionListResponse,
        )

    async def get(
        self,
        session_id: str,
        *,
        provider: VcsProvider,
        org: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/alpha/repos/{provider}/{org}/{repo}/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    async def get_patch(
        self,
        session_id: str,
        *,
        provider: VcsProvider,
        org: str,
        repo: str,
        context_lines: int | NotGiven = NOT_GIVEN,
        interhunk_lines: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionGetPatchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/alpha/repos/{provider}/{org}/{repo}/sessions/{session_id}/patch",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "context_lines": context_lines,
                        "interhunk_lines": interhunk_lines,
                    },
                    session_get_patch_params.SessionGetPatchParams,
                ),
            ),
            cast_to=SessionGetPatchResponse,
        )

    async def solve(
        self,
        session_id: str,
        *,
        provider: VcsProvider,
        org: str,
        repo: str,
        instruction: str,
        num_steps: int,
        invocation_options: Dict[str, Union[str, bool, float]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Turn:
        """
        Args:
          num_steps: The maximum number of steps to take when Solving

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/alpha/repos/{provider}/{org}/{repo}/sessions/{session_id}/solve",
            body=await async_maybe_transform(
                {
                    "instruction": instruction,
                    "num_steps": num_steps,
                    "invocation_options": invocation_options,
                },
                session_solve_params.SessionSolveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Turn,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_raw_response_wrapper(
            sessions.create,
        )
        self.list = to_raw_response_wrapper(
            sessions.list,
        )
        self.get = to_raw_response_wrapper(
            sessions.get,
        )
        self.get_patch = to_raw_response_wrapper(
            sessions.get_patch,
        )
        self.solve = to_raw_response_wrapper(
            sessions.solve,
        )

    @cached_property
    def status(self) -> StatusResourceWithRawResponse:
        return StatusResourceWithRawResponse(self._sessions.status)

    @cached_property
    def turns(self) -> TurnsResourceWithRawResponse:
        return TurnsResourceWithRawResponse(self._sessions.turns)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._sessions.events)


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_raw_response_wrapper(
            sessions.create,
        )
        self.list = async_to_raw_response_wrapper(
            sessions.list,
        )
        self.get = async_to_raw_response_wrapper(
            sessions.get,
        )
        self.get_patch = async_to_raw_response_wrapper(
            sessions.get_patch,
        )
        self.solve = async_to_raw_response_wrapper(
            sessions.solve,
        )

    @cached_property
    def status(self) -> AsyncStatusResourceWithRawResponse:
        return AsyncStatusResourceWithRawResponse(self._sessions.status)

    @cached_property
    def turns(self) -> AsyncTurnsResourceWithRawResponse:
        return AsyncTurnsResourceWithRawResponse(self._sessions.turns)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._sessions.events)


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_streamed_response_wrapper(
            sessions.create,
        )
        self.list = to_streamed_response_wrapper(
            sessions.list,
        )
        self.get = to_streamed_response_wrapper(
            sessions.get,
        )
        self.get_patch = to_streamed_response_wrapper(
            sessions.get_patch,
        )
        self.solve = to_streamed_response_wrapper(
            sessions.solve,
        )

    @cached_property
    def status(self) -> StatusResourceWithStreamingResponse:
        return StatusResourceWithStreamingResponse(self._sessions.status)

    @cached_property
    def turns(self) -> TurnsResourceWithStreamingResponse:
        return TurnsResourceWithStreamingResponse(self._sessions.turns)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._sessions.events)


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_streamed_response_wrapper(
            sessions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            sessions.list,
        )
        self.get = async_to_streamed_response_wrapper(
            sessions.get,
        )
        self.get_patch = async_to_streamed_response_wrapper(
            sessions.get_patch,
        )
        self.solve = async_to_streamed_response_wrapper(
            sessions.solve,
        )

    @cached_property
    def status(self) -> AsyncStatusResourceWithStreamingResponse:
        return AsyncStatusResourceWithStreamingResponse(self._sessions.status)

    @cached_property
    def turns(self) -> AsyncTurnsResourceWithStreamingResponse:
        return AsyncTurnsResourceWithStreamingResponse(self._sessions.turns)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._sessions.events)
