# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import VcsProvider
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .sessions.sessions import (
    SessionsResource,
    AsyncSessionsResource,
    SessionsResourceWithRawResponse,
    AsyncSessionsResourceWithRawResponse,
    SessionsResourceWithStreamingResponse,
    AsyncSessionsResourceWithStreamingResponse,
)
from ...types.vcs_provider import VcsProvider
from ...types.repo_retrieve_response import RepoRetrieveResponse

__all__ = ["ReposResource", "AsyncReposResource"]


class ReposResource(SyncAPIResource):
    @cached_property
    def sessions(self) -> SessionsResource:
        return SessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReposResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/solver-api-python#accessing-raw-response-data-eg-headers
        """
        return ReposResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReposResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/solver-api-python#with_streaming_response
        """
        return ReposResourceWithStreamingResponse(self)

    def retrieve(
        self,
        provider: VcsProvider,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return self._get(
            f"/repos/{provider}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepoRetrieveResponse,
        )


class AsyncReposResource(AsyncAPIResource):
    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        return AsyncSessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReposResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/solver-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReposResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReposResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/solver-api-python#with_streaming_response
        """
        return AsyncReposResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        provider: VcsProvider,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return await self._get(
            f"/repos/{provider}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepoRetrieveResponse,
        )


class ReposResourceWithRawResponse:
    def __init__(self, repos: ReposResource) -> None:
        self._repos = repos

        self.retrieve = to_raw_response_wrapper(
            repos.retrieve,
        )

    @cached_property
    def sessions(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self._repos.sessions)


class AsyncReposResourceWithRawResponse:
    def __init__(self, repos: AsyncReposResource) -> None:
        self._repos = repos

        self.retrieve = async_to_raw_response_wrapper(
            repos.retrieve,
        )

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self._repos.sessions)


class ReposResourceWithStreamingResponse:
    def __init__(self, repos: ReposResource) -> None:
        self._repos = repos

        self.retrieve = to_streamed_response_wrapper(
            repos.retrieve,
        )

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self._repos.sessions)


class AsyncReposResourceWithStreamingResponse:
    def __init__(self, repos: AsyncReposResource) -> None:
        self._repos = repos

        self.retrieve = async_to_streamed_response_wrapper(
            repos.retrieve,
        )

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self._repos.sessions)
