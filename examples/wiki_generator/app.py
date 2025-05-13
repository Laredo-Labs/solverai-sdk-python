import os
import uuid
import shutil
import subprocess
from typing import List, Tuple, Union, Literal

from flask import (
    Flask,
    Response as FlaskResponse,
    request,
    url_for,
    redirect,
    render_template,
    send_from_directory,
)
from prompts import format_documentation_prompt
from werkzeug.wrappers import Response as WerkzeugResponse

from solverai import Solver, APIStatusError
from solverai.types.repos.session import Session

app = Flask(__name__)

DocId = str
DocPath = str
ViewResponse = Union[str, FlaskResponse, WerkzeugResponse]


DOCS_DIR = os.path.join(app.root_path, "generated_solver_docs")
NUM_STEPS: Literal[8, 16, 24, 32, 40] = 8

os.makedirs(DOCS_DIR, exist_ok=True)


def generate_docs_directory() -> Tuple[DocId, DocPath]:
    unique_id = str(uuid.uuid4())
    docs_path = os.path.join(DOCS_DIR, unique_id)
    os.makedirs(docs_path, exist_ok=True)
    return unique_id, docs_path


def _cleanup_session_config(doc_id: str) -> None:
    app.logger.debug(f"Cleaning up session config for doc_id: {doc_id}")
    for key_suffix in ["solver_session", "org", "repo", "docs_path"]:
        app.config.pop(f"{key_suffix}_{doc_id}", None)  # type: ignore


def _apply_patch_to_docs(docs_path: str, patch_content: str) -> None:
    app.logger.info(f"Attempting to apply patch to {docs_path}")
    process = subprocess.run(
        ["patch", "-p1", "-d", docs_path],
        input=patch_content,
        text=True,
        capture_output=True,
        check=True,
    )
    app.logger.info(f"Patch applied successfully to {docs_path}. Stdout: {process.stdout}")
    if process.stderr:
        app.logger.warning(f"Patch application to {docs_path} produced stderr: {process.stderr}")


def _process_wiki_directory(docs_path: str) -> None:
    source_dot_wiki_dir = os.path.join(docs_path, ".wiki")
    if not (os.path.exists(source_dot_wiki_dir) and os.path.isdir(source_dot_wiki_dir)):
        return

    app.logger.info(f"Flattening .wiki directory: {source_dot_wiki_dir} into {docs_path}")
    try:
        for item_name in os.listdir(source_dot_wiki_dir):
            source_item_path = os.path.join(source_dot_wiki_dir, item_name)
            dest_item_path = os.path.join(docs_path, item_name)

            if os.path.isdir(source_item_path):
                shutil.copytree(source_item_path, dest_item_path, dirs_exist_ok=True)
                shutil.rmtree(source_item_path)
            else:
                shutil.move(source_item_path, dest_item_path)

        if not os.listdir(source_dot_wiki_dir):
            os.rmdir(source_dot_wiki_dir)
            app.logger.info(f"Removed empty directory: {source_dot_wiki_dir}")
    except OSError as e:
        app.logger.error(f"Failed to process {source_dot_wiki_dir}: {str(e)}")


def _rename_if_exists(source: str, dest: str) -> None:
    if os.path.exists(source):
        try:
            os.rename(source, dest)
            app.logger.info(f"Renamed {source} to {dest}")
        except OSError as e:
            app.logger.error(f"Failed to rename {source} to {dest}: {str(e)}")


@app.route("/", methods=["GET"])
def index() -> ViewResponse:
    repositories = get_available_repositories()
    return render_template("index.html", repositories=repositories)


def get_available_repositories() -> List[str]:
    try:
        solver = Solver(api_key=os.environ["SOLVER_API_KEY"])
        repos = solver.repos.list(provider="github")
        return [f"{repo.org}/{repo.repo}" for repo in repos]
    except (APIStatusError, KeyError) as e:
        app.logger.error(f"Failed to list repositories: {str(e)}")
        return []


@app.route("/search", methods=["POST"])
def search() -> ViewResponse:
    query = request.form.get("query", "")
    repository = request.form.get("repository", "")

    if not query or not repository:
        return redirect(url_for("index"))

    try:
        doc_id, docs_path = generate_docs_directory()
        solver = Solver(api_key=os.environ["SOLVER_API_KEY"])
        org, repo = repository.split("/")

        turn = solver.repos.sessions.create_and_solve(
            provider="github",
            org=org,
            repo=repo,
            user_branch_name="main",
            instruction=format_documentation_prompt(query, org, repo),
            num_steps=NUM_STEPS,
        )

        app.config[f"solver_session_{doc_id}"] = turn.session_id
        app.config[f"org_{doc_id}"] = org
        app.config[f"repo_{doc_id}"] = repo
        app.config[f"docs_path_{doc_id}"] = docs_path

        static_folder = str(app.static_folder) if app.static_folder else ""
        sidebar_template = os.path.join(static_folder, "doc_template", "_sidebar.md")
        if os.path.exists(sidebar_template):
            shutil.copy2(sidebar_template, os.path.join(docs_path, "_sidebar.md"))

        return redirect(url_for("progress", query=query, doc_id=doc_id, repository=repository))

    except APIStatusError as e:
        app.logger.error(f"Failed to access repository: {str(e)}")
        return render_template(
            "index.html",
            error="Failed to access repository. Please check permissions and try again.",
            repositories=get_available_repositories(),
        )


@app.route("/progress", methods=["GET"])
def progress() -> ViewResponse:
    query = request.args.get("query", "")
    doc_id = request.args.get("doc_id", "")
    repository = request.args.get("repository", "")

    if not query or not doc_id or not repository:
        return redirect(url_for("index"))

    session_id = app.config.get(f"solver_session_{doc_id}")  # type: ignore
    docs_path = app.config.get(f"docs_path_{doc_id}")  # type: ignore
    org = app.config.get(f"org_{doc_id}")  # type: ignore
    repo = app.config.get(f"repo_{doc_id}")  # type: ignore

    if not all([session_id, docs_path, org, repo]):  # type: ignore
        app.logger.warning("Progress page accessed with incomplete session data for doc_id: %s", doc_id)
        return redirect(url_for("index", error="Session data incomplete. Please start over."))

    assert isinstance(session_id, str)
    assert isinstance(docs_path, str)
    assert isinstance(org, str)
    assert isinstance(repo, str)

    try:
        solver = Solver(api_key=os.environ["SOLVER_API_KEY"])
        session_details: Session = solver.repos.sessions.get(
            provider="github", org=org, repo=repo, session_id=session_id
        )

        status = str(session_details.status).upper()
        app.logger.info(f"Session {session_id} for doc_id {doc_id}: status '{status}'")

        if status not in ("READY"):
            return render_template(
                "progress.html",
                query=query,
                doc_id=doc_id,
                repository=repository,
                status_message=f"Current status: {status}",
            )

        patch_response = solver.repos.sessions.get_patch(provider="github", org=org, repo=repo, session_id=session_id)

        if not patch_response.patch_set:
            _cleanup_session_config(doc_id)
            return render_template(
                "index.html",
                error="Documentation generation completed, but no content was produced. Please try again.",
                repositories=get_available_repositories(),
            )

        _apply_patch_to_docs(docs_path, patch_response.patch_set)
        _process_wiki_directory(docs_path)

        _rename_if_exists(
            os.path.join(docs_path, "index.md"),
            os.path.join(docs_path, "README.md"),
        )
        _rename_if_exists(
            os.path.join(docs_path, "_toc.md"),
            os.path.join(docs_path, "_sidebar.md"),
        )

        docsify_template_path = os.path.join(app.root_path, "templates", "docsify.html")
        target_index_html_path = os.path.join(docs_path, "index.html")
        shutil.copy2(docsify_template_path, target_index_html_path)

        _cleanup_session_config(doc_id)
        return redirect(url_for("view_docs", doc_id=doc_id))

    except APIStatusError as e:
        error_msg = str(e)
        app.logger.error(f"Error processing documentation for session {session_id} (doc_id {doc_id}): {str(e)}")
        _cleanup_session_config(doc_id)
        return render_template(
            "index.html",
            error=error_msg,
            repositories=get_available_repositories(),
        )


@app.route("/docs/<doc_id>", methods=["GET"])
def view_docs(doc_id: str) -> ViewResponse:
    docs_path = os.path.join(DOCS_DIR, doc_id)
    index_html_path = os.path.join(docs_path, "index.html")

    if not os.path.exists(index_html_path):
        app.logger.warning(f"Attempted to access docs for {doc_id}, but index.html not found at {index_html_path}")
        return redirect(url_for("index", error="Documentation files not found or setup is incomplete."))

    return send_from_directory(docs_path, "index.html")


@app.route("/docs/<doc_id>/<path:filename>")
def serve_docs(doc_id: str, filename: str) -> ViewResponse:
    docs_path = os.path.join(DOCS_DIR, doc_id)
    return send_from_directory(docs_path, filename)


if __name__ == "__main__":
    if not os.environ.get("SOLVER_API_KEY"):
        app.logger.error("SOLVER_API_KEY is not set")
        exit(1)
    app.run(debug=True)
