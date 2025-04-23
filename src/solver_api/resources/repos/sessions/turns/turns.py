# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from .....types import VcsProvider
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.repos.turn import Turn
from .....types.vcs_provider import VcsProvider
from .....types.repos.sessions.turn_list_response import TurnListResponse
from .....types.repos.sessions.turn_patch_response import TurnPatchResponse

__all__ = ["TurnsResource", "AsyncTurnsResource"]


class TurnsResource(SyncAPIResource):
    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TurnsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Laredo-Labs/solverai-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TurnsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TurnsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Laredo-Labs/solverai-sdk-python#with_streaming_response
        """
        return TurnsResourceWithStreamingResponse(self)

    def list(
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
    ) -> TurnListResponse:
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
            f"/repos/{provider}/{org}/{repo}/sessions/{session_id}/turns",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TurnListResponse,
        )

    def cancel(
        self,
        turn_id: str,
        *,
        provider: VcsProvider,
        org: str,
        repo: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Turn:
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
        if not turn_id:
            raise ValueError(f"Expected a non-empty value for `turn_id` but received {turn_id!r}")
        return self._post(
            f"/repos/{provider}/{org}/{repo}/sessions/{session_id}/turns/{turn_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Turn,
        )

    def get(
        self,
        turn_id: str,
        *,
        provider: VcsProvider,
        org: str,
        repo: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Turn:
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
        if not turn_id:
            raise ValueError(f"Expected a non-empty value for `turn_id` but received {turn_id!r}")
        return self._get(
            f"/repos/{provider}/{org}/{repo}/sessions/{session_id}/turns/{turn_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Turn,
        )

    def patch(
        self,
        turn_id: str,
        *,
        provider: VcsProvider,
        org: str,
        repo: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TurnPatchResponse:
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
        if not turn_id:
            raise ValueError(f"Expected a non-empty value for `turn_id` but received {turn_id!r}")
        return self._get(
            f"/repos/{provider}/{org}/{repo}/sessions/{session_id}/turns/{turn_id}/patch",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TurnPatchResponse,
        )


class AsyncTurnsResource(AsyncAPIResource):
    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTurnsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Laredo-Labs/solverai-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTurnsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTurnsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Laredo-Labs/solverai-sdk-python#with_streaming_response
        """
        return AsyncTurnsResourceWithStreamingResponse(self)

    async def list(
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
    ) -> TurnListResponse:
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
            f"/repos/{provider}/{org}/{repo}/sessions/{session_id}/turns",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TurnListResponse,
        )

    async def cancel(
        self,
        turn_id: str,
        *,
        provider: VcsProvider,
        org: str,
        repo: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Turn:
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
        if not turn_id:
            raise ValueError(f"Expected a non-empty value for `turn_id` but received {turn_id!r}")
        return await self._post(
            f"/repos/{provider}/{org}/{repo}/sessions/{session_id}/turns/{turn_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Turn,
        )

    async def get(
        self,
        turn_id: str,
        *,
        provider: VcsProvider,
        org: str,
        repo: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Turn:
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
        if not turn_id:
            raise ValueError(f"Expected a non-empty value for `turn_id` but received {turn_id!r}")
        return await self._get(
            f"/repos/{provider}/{org}/{repo}/sessions/{session_id}/turns/{turn_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Turn,
        )

    async def patch(
        self,
        turn_id: str,
        *,
        provider: VcsProvider,
        org: str,
        repo: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TurnPatchResponse:
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
        if not turn_id:
            raise ValueError(f"Expected a non-empty value for `turn_id` but received {turn_id!r}")
        return await self._get(
            f"/repos/{provider}/{org}/{repo}/sessions/{session_id}/turns/{turn_id}/patch",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TurnPatchResponse,
        )


class TurnsResourceWithRawResponse:
    def __init__(self, turns: TurnsResource) -> None:
        self._turns = turns

        self.list = to_raw_response_wrapper(
            turns.list,
        )
        self.cancel = to_raw_response_wrapper(
            turns.cancel,
        )
        self.get = to_raw_response_wrapper(
            turns.get,
        )
        self.patch = to_raw_response_wrapper(
            turns.patch,
        )

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._turns.events)


class AsyncTurnsResourceWithRawResponse:
    def __init__(self, turns: AsyncTurnsResource) -> None:
        self._turns = turns

        self.list = async_to_raw_response_wrapper(
            turns.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            turns.cancel,
        )
        self.get = async_to_raw_response_wrapper(
            turns.get,
        )
        self.patch = async_to_raw_response_wrapper(
            turns.patch,
        )

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._turns.events)


class TurnsResourceWithStreamingResponse:
    def __init__(self, turns: TurnsResource) -> None:
        self._turns = turns

        self.list = to_streamed_response_wrapper(
            turns.list,
        )
        self.cancel = to_streamed_response_wrapper(
            turns.cancel,
        )
        self.get = to_streamed_response_wrapper(
            turns.get,
        )
        self.patch = to_streamed_response_wrapper(
            turns.patch,
        )

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._turns.events)


class AsyncTurnsResourceWithStreamingResponse:
    def __init__(self, turns: AsyncTurnsResource) -> None:
        self._turns = turns

        self.list = async_to_streamed_response_wrapper(
            turns.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            turns.cancel,
        )
        self.get = async_to_streamed_response_wrapper(
            turns.get,
        )
        self.patch = async_to_streamed_response_wrapper(
            turns.patch,
        )

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._turns.events)
