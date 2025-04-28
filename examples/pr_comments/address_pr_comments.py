import os
import re
import json
import argparse
import subprocess
from typing import Any, Dict, Tuple
from urllib.parse import urlparse

from solverai import Solver


def parse_github_pr_url(url: str) -> Tuple[str, str, int]:
    parsed = urlparse(url)
    if parsed.netloc != "github.com":
        raise ValueError("Invalid URL: Not a github.com URL.")
    match = re.match(r"/([^/]+)/([^/]+)/pull/(\d+)", parsed.path)
    if not match:
        raise ValueError(
            "Invalid URL: Path does not match expected GitHub PR format (/owner/repo/pull/number)."
        )
    owner, repo, pr_number = match.groups()
    return owner, repo, int(pr_number)


def get_pr_details(owner: str, repo_name: str, pr_number: int) -> Dict[str, Any]:
    graphql_query = f"""
    query {{ 
      repository(owner: "{owner}", name: "{repo_name}") {{ 
        pullRequest(number: {pr_number}) {{ 
          title
          body
          author {{
            login
          }}
          headRefName
          reviewThreads(first: 100) {{ 
            nodes {{ 
              isResolved
              comments(first: 100) {{ 
                nodes {{
                  id
                  path
                  body
                  author {{
                    login
                  }}
                  diffHunk
                }}
              }}
            }}
          }}
        }}
      }}
    }}
    """
    api_result = json.loads(
        subprocess.run(
            ["gh", "api", "graphql", "-f", f"query={graphql_query}"],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        ).stdout
    )

    pr = api_result["data"]["repository"]["pullRequest"]
    return {
        "title": pr["title"],
        "body": pr["body"],
        "author_login": pr["author"]["login"],
        "branch": pr["headRefName"],
        "threads": pr["reviewThreads"]["nodes"],
    }


def format_request(pr_data: Dict[str, Any]) -> str:
    request = (
        f"Pull request title: {pr_data['title']}\n"
        f"Pull request author: {pr_data['author_login']}\n\n"
        f"Pull request body:\n{pr_data['body']}\n\n"
        "---\n"
        "Please address the following comments on this pull request:\n"
    )

    processed_thread_count = 0
    for thread in pr_data["threads"]:
        if thread["isResolved"] or not thread["comments"]["nodes"]:
            continue

        processed_thread_count += 1
        first_comment = thread["comments"]["nodes"][0]
        path = first_comment["path"]
        diff_hunk = first_comment["diffHunk"]

        request += (
            f"\nThread {processed_thread_count} on file: {path}\n"
            f"\n```diff\n{diff_hunk}\n```\n"
            f"Comments:\n"
        )
        for comment in thread["comments"]["nodes"]:
            body = comment["body"]
            commenter = comment["author"]["login"]
            request += f"- @{commenter}: {body}\n"
        request += "---\n"

    if processed_thread_count == 0:
        request += "\n(No specific unresolved review threads found - address the main PR description.)\n"

    return request


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Minimal SolverAI SDK example using a GitHub PR."
    )
    parser.add_argument("pr_url", help="URL of the GitHub Pull Request.")
    return parser.parse_args()


def main(pr_url: str) -> None:
    owner, repo_name, pr_number = parse_github_pr_url(pr_url)
    pr_data = get_pr_details(owner, repo_name, pr_number)
    client = Solver(api_key=os.environ["SOLVER_API_KEY"])

    session = client.repos.sessions.create(
        provider="github",
        org=owner,
        repo=repo_name,
        user_branch_name=pr_data["branch"],
    )
    client.repos.sessions.solve(
        session_id=session.id,
        provider="github",
        org=owner,
        repo=repo_name,
        instruction=format_request(pr_data),
        num_steps=24
    )
    print(session.solver_url)


if __name__ == "__main__":
    main(**vars(parse_args()))
