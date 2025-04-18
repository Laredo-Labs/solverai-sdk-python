# Repos

Types:

```python
from solver_api.types import VcsProvider, RepoRetrieveResponse
```

Methods:

- <code title="get /repos/{provider}">client.repos.<a href="./src/solver_api/resources/repos/repos.py">retrieve</a>(provider) -> <a href="./src/solver_api/types/repo_retrieve_response.py">RepoRetrieveResponse</a></code>

## Sessions

Types:

```python
from solver_api.types.repos import (
    Session,
    SessionStatus,
    SessionVisibility,
    Turn,
    SessionListResponse,
    SessionPatchResponse,
)
```

Methods:

- <code title="post /repos/{provider}/{org}/{repo}/sessions">client.repos.sessions.<a href="./src/solver_api/resources/repos/sessions/sessions.py">create</a>(repo, \*, provider, org, \*\*<a href="src/solver_api/types/repos/session_create_params.py">params</a>) -> <a href="./src/solver_api/types/repos/session.py">Session</a></code>
- <code title="get /repos/{provider}/{org}/{repo}/sessions/{sessionId}">client.repos.sessions.<a href="./src/solver_api/resources/repos/sessions/sessions.py">retrieve</a>(session_id, \*, provider, org, repo) -> <a href="./src/solver_api/types/repos/session.py">Session</a></code>
- <code title="get /repos/{provider}/{org}/{repo}/sessions">client.repos.sessions.<a href="./src/solver_api/resources/repos/sessions/sessions.py">list</a>(repo, \*, provider, org, \*\*<a href="src/solver_api/types/repos/session_list_params.py">params</a>) -> <a href="./src/solver_api/types/repos/session_list_response.py">SessionListResponse</a></code>
- <code title="get /repos/{provider}/{org}/{repo}/sessions/{sessionId}/patch">client.repos.sessions.<a href="./src/solver_api/resources/repos/sessions/sessions.py">patch</a>(session_id, \*, provider, org, repo, \*\*<a href="src/solver_api/types/repos/session_patch_params.py">params</a>) -> <a href="./src/solver_api/types/repos/session_patch_response.py">SessionPatchResponse</a></code>
- <code title="post /repos/{provider}/{org}/{repo}/sessions/{sessionId}/solve">client.repos.sessions.<a href="./src/solver_api/resources/repos/sessions/sessions.py">solve</a>(session_id, \*, provider, org, repo, \*\*<a href="src/solver_api/types/repos/session_solve_params.py">params</a>) -> <a href="./src/solver_api/types/repos/turn.py">Turn</a></code>

### Status

Types:

```python
from solver_api.types.repos.sessions import StatusStreamResponse
```

Methods:

- <code title="get /repos/{provider}/{org}/{repo}/sessions/status/stream">client.repos.sessions.status.<a href="./src/solver_api/resources/repos/sessions/status.py">stream</a>(repo, \*, provider, org, \*\*<a href="src/solver_api/types/repos/sessions/status_stream_params.py">params</a>) -> <a href="./src/solver_api/types/repos/sessions/status_stream_response.py">StatusStreamResponse</a></code>

### Turns

Types:

```python
from solver_api.types.repos.sessions import TurnListResponse, TurnPatchResponse
```

Methods:

- <code title="get /repos/{provider}/{org}/{repo}/sessions/{sessionId}/turns/{turnId}">client.repos.sessions.turns.<a href="./src/solver_api/resources/repos/sessions/turns/turns.py">retrieve</a>(turn_id, \*, provider, org, repo, session_id) -> <a href="./src/solver_api/types/repos/turn.py">Turn</a></code>
- <code title="get /repos/{provider}/{org}/{repo}/sessions/{sessionId}/turns">client.repos.sessions.turns.<a href="./src/solver_api/resources/repos/sessions/turns/turns.py">list</a>(session_id, \*, provider, org, repo) -> <a href="./src/solver_api/types/repos/sessions/turn_list_response.py">TurnListResponse</a></code>
- <code title="post /repos/{provider}/{org}/{repo}/sessions/{sessionId}/turns/{turnId}/cancel">client.repos.sessions.turns.<a href="./src/solver_api/resources/repos/sessions/turns/turns.py">cancel</a>(turn_id, \*, provider, org, repo, session_id) -> <a href="./src/solver_api/types/repos/turn.py">Turn</a></code>
- <code title="get /repos/{provider}/{org}/{repo}/sessions/{sessionId}/turns/{turnId}/patch">client.repos.sessions.turns.<a href="./src/solver_api/resources/repos/sessions/turns/turns.py">patch</a>(turn_id, \*, provider, org, repo, session_id) -> <a href="./src/solver_api/types/repos/sessions/turn_patch_response.py">TurnPatchResponse</a></code>

#### Events

Methods:

- <code title="get /repos/{provider}/{org}/{repo}/sessions/{sessionId}/turns/{turnId}/events/stream">client.repos.sessions.turns.events.<a href="./src/solver_api/resources/repos/sessions/turns/events.py">stream</a>(turn_id, \*, provider, org, repo, session_id) -> <a href="./src/solver_api/types/repos/sessions/trace_event.py">TraceEvent</a></code>

### Events

Types:

```python
from solver_api.types.repos.sessions import TraceEvent, EventPatchResponse
```

Methods:

- <code title="get /repos/{provider}/{org}/{repo}/sessions/{sessionId}/events/{eventId}">client.repos.sessions.events.<a href="./src/solver_api/resources/repos/sessions/events.py">retrieve</a>(event_id, \*, provider, org, repo, session_id) -> <a href="./src/solver_api/types/repos/sessions/trace_event.py">TraceEvent</a></code>
- <code title="get /repos/{provider}/{org}/{repo}/sessions/{sessionId}/events/{eventId}/patch">client.repos.sessions.events.<a href="./src/solver_api/resources/repos/sessions/events.py">patch</a>(event_id, \*, provider, org, repo, session_id, \*\*<a href="src/solver_api/types/repos/sessions/event_patch_params.py">params</a>) -> <a href="./src/solver_api/types/repos/sessions/event_patch_response.py">EventPatchResponse</a></code>
- <code title="get /repos/{provider}/{org}/{repo}/sessions/{sessionId}/events/stream">client.repos.sessions.events.<a href="./src/solver_api/resources/repos/sessions/events.py">stream</a>(session_id, \*, provider, org, repo) -> <a href="./src/solver_api/types/repos/sessions/trace_event.py">TraceEvent</a></code>
