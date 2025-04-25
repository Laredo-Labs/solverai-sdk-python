# Repos

Types:

```python
from solverai.types import VcsProvider, RepoListResponse
```

Methods:

- <code title="get /alpha/repos/{provider}">client.repos.<a href="./src/solverai/resources/repos/repos.py">list</a>(provider) -> <a href="./src/solverai/types/repo_list_response.py">RepoListResponse</a></code>

## Sessions

Types:

```python
from solverai.types.repos import (
    Session,
    SessionStatus,
    SessionVisibility,
    Turn,
    SessionListResponse,
    SessionGetPatchResponse,
)
```

Methods:

- <code title="post /alpha/repos/{provider}/{org}/{repo}/sessions">client.repos.sessions.<a href="./src/solverai/resources/repos/sessions/sessions.py">create</a>(repo, \*, provider, org, \*\*<a href="src/solverai/types/repos/session_create_params.py">params</a>) -> <a href="./src/solverai/types/repos/session.py">Session</a></code>
- <code title="get /alpha/repos/{provider}/{org}/{repo}/sessions">client.repos.sessions.<a href="./src/solverai/resources/repos/sessions/sessions.py">list</a>(repo, \*, provider, org, \*\*<a href="src/solverai/types/repos/session_list_params.py">params</a>) -> <a href="./src/solverai/types/repos/session_list_response.py">SessionListResponse</a></code>
- <code title="get /alpha/repos/{provider}/{org}/{repo}/sessions/{sessionId}">client.repos.sessions.<a href="./src/solverai/resources/repos/sessions/sessions.py">get</a>(session_id, \*, provider, org, repo) -> <a href="./src/solverai/types/repos/session.py">Session</a></code>
- <code title="get /alpha/repos/{provider}/{org}/{repo}/sessions/{sessionId}/patch">client.repos.sessions.<a href="./src/solverai/resources/repos/sessions/sessions.py">get_patch</a>(session_id, \*, provider, org, repo, \*\*<a href="src/solverai/types/repos/session_get_patch_params.py">params</a>) -> <a href="./src/solverai/types/repos/session_get_patch_response.py">SessionGetPatchResponse</a></code>
- <code title="post /alpha/repos/{provider}/{org}/{repo}/sessions/{sessionId}/solve">client.repos.sessions.<a href="./src/solverai/resources/repos/sessions/sessions.py">solve</a>(session_id, \*, provider, org, repo, \*\*<a href="src/solverai/types/repos/session_solve_params.py">params</a>) -> <a href="./src/solverai/types/repos/turn.py">Turn</a></code>

### Status

Types:

```python
from solverai.types.repos.sessions import StatusStreamResponse
```

Methods:

- <code title="get /alpha/repos/{provider}/{org}/{repo}/sessions/status/stream">client.repos.sessions.status.<a href="./src/solverai/resources/repos/sessions/status.py">stream</a>(repo, \*, provider, org, \*\*<a href="src/solverai/types/repos/sessions/status_stream_params.py">params</a>) -> <a href="./src/solverai/types/repos/sessions/status_stream_response.py">StatusStreamResponse</a></code>

### Turns

Types:

```python
from solverai.types.repos.sessions import TurnListResponse, TurnGetPatchResponse
```

Methods:

- <code title="get /alpha/repos/{provider}/{org}/{repo}/sessions/{sessionId}/turns">client.repos.sessions.turns.<a href="./src/solverai/resources/repos/sessions/turns.py">list</a>(session_id, \*, provider, org, repo) -> <a href="./src/solverai/types/repos/sessions/turn_list_response.py">TurnListResponse</a></code>
- <code title="post /alpha/repos/{provider}/{org}/{repo}/sessions/{sessionId}/turns/{turnId}/cancel">client.repos.sessions.turns.<a href="./src/solverai/resources/repos/sessions/turns.py">cancel</a>(turn_id, \*, provider, org, repo, session_id) -> <a href="./src/solverai/types/repos/turn.py">Turn</a></code>
- <code title="get /alpha/repos/{provider}/{org}/{repo}/sessions/{sessionId}/turns/{turnId}">client.repos.sessions.turns.<a href="./src/solverai/resources/repos/sessions/turns.py">get</a>(turn_id, \*, provider, org, repo, session_id) -> <a href="./src/solverai/types/repos/turn.py">Turn</a></code>
- <code title="get /alpha/repos/{provider}/{org}/{repo}/sessions/{sessionId}/turns/{turnId}/patch">client.repos.sessions.turns.<a href="./src/solverai/resources/repos/sessions/turns.py">get_patch</a>(turn_id, \*, provider, org, repo, session_id) -> <a href="./src/solverai/types/repos/sessions/turn_get_patch_response.py">TurnGetPatchResponse</a></code>

### Events

Types:

```python
from solverai.types.repos.sessions import TraceEvent, EventGetPatchResponse
```

Methods:

- <code title="get /alpha/repos/{provider}/{org}/{repo}/sessions/{sessionId}/events/{eventId}">client.repos.sessions.events.<a href="./src/solverai/resources/repos/sessions/events.py">get</a>(event_id, \*, provider, org, repo, session_id) -> <a href="./src/solverai/types/repos/sessions/trace_event.py">TraceEvent</a></code>
- <code title="get /alpha/repos/{provider}/{org}/{repo}/sessions/{sessionId}/events/{eventId}/patch">client.repos.sessions.events.<a href="./src/solverai/resources/repos/sessions/events.py">get_patch</a>(event_id, \*, provider, org, repo, session_id, \*\*<a href="src/solverai/types/repos/sessions/event_get_patch_params.py">params</a>) -> <a href="./src/solverai/types/repos/sessions/event_get_patch_response.py">EventGetPatchResponse</a></code>
