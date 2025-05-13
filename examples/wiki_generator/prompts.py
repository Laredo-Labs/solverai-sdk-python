from string import Template

DOCUMENTATION_PROMPT = """Your goal is to document this project, with a focus on a particular user query.
You MUST perform the following actions:

- Create a new directory named .wiki/ at the root of this repository.
- Inside the .wiki/ directory, create multiple Markdown (.md) files. These files should comprehensively document and answer the user's query.
- You must create a table of contents, and that file MUST be named README.md. This file should list and link to all other Markdown files you create in the .wiki/ directory.
- The content of all Markdown files should be detailed and well-structured. Use extensive Markdown formatting for clarity, including headings, lists, code blocks, and blockquotes where appropriate.
- Where beneficial for illustrating architectural changes, component interactions, or state transitions, include Mermaid diagrams within the Markdown files. These MUST be valid mermaid diagrams, within ```mermaid ... ``` blocks.
Remember, the primary output is the .wiki/ directory and its contents, created directly in the file system.
- Ensure that your documentation provides a clear understanding of how the codebase is evolving and the architectural consequences of these changes. The goal is to provide insights not into just how things work, but WHY they do.
- Include citations that link to the specific lines of code in the repository, of the form:
https://github.com/$organization/$repository/blob/main/path/to/file.md?plain=1#L70
(this is the actual organization and repository name you should use)
- As part of your investigation, you should spend at least 1/2 of your budget on exploration and study, to build the proper context on your documentation.
- Extensively use semantic search.

This is the user's query, which is your focus:
<user-query>
$query
</user-query>"""


def format_documentation_prompt(query: str, organization: str, repository: str) -> str:
    template = Template(DOCUMENTATION_PROMPT)
    return template.substitute(query=query, organization=organization, repository=repository)
