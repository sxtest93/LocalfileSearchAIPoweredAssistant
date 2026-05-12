from pathlib import Path
from mcp.server.fastmcp import FastMCP

from reader import read_file
from indexer import chunk_text
from vector_store import add_chunk, search_chunks

# -----------------------------
# MCP Server Initialization
# -----------------------------
mcp = FastMCP("AI File Intelligence MCP")

# -----------------------------
# Allowed Directories
# -----------------------------
ALLOWED_DIRS = [
    Path.home() / "Documents",
    Path.home() / "Downloads",
    Path.home() / "Desktop"
]

# Block sensitive files
BLOCKED_FILES = [
    ".env",
    ".pem",
    ".key",
    "id_rsa",
    "credentials"
]


# -----------------------------
# Helper Functions
# -----------------------------
def is_allowed_path(file_path: str) -> bool:
    """
    Ensure file is inside allowed directories.
    """
    try:
        path = Path(file_path).resolve()

        allowed = any(
            str(path).startswith(str(allowed_dir.resolve()))
            for allowed_dir in ALLOWED_DIRS
        )

        blocked = any(
            blocked_name.lower() in path.name.lower()
            for blocked_name in BLOCKED_FILES
        )

        return allowed and not blocked

    except Exception:
        return False


def format_results(results):
    """
    Nicely format vector search results.
    """
    output = []

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    for doc, meta in zip(documents, metadatas):

        file_path = meta.get("file_path", "Unknown")
        page = meta.get("page", "N/A")
        chunk = meta.get("chunk", "N/A")

        output.append(
            f"""
========================================
FILE   : {file_path}
PAGE   : {page}
CHUNK  : {chunk}

CONTENT:
{doc[:1200]}
========================================
"""
        )

    return "\n".join(output)


# -----------------------------
# MCP Tools
# -----------------------------
@mcp.tool()
def health_check() -> str:
    """
    Check whether MCP server is running.
    """
    return "AI File Intelligence MCP is running successfully."


@mcp.tool()
def index_file(file_path: str) -> str:
    """
    Index a single file into the vector database.

    Supported:
    - PDF
    - DOCX
    - TXT
    - MD
    - LOG
    - JAVA
    - PY
    - YAML
    - JSON
    """

    if not is_allowed_path(file_path):
        return (
            "Access denied.\n"
            "File is outside allowed directories "
            "or is a blocked sensitive file."
        )

    try:
        pages = read_file(file_path)

        total_chunks = 0

        for page in pages:

            page_number = page["page"]
            text = page["text"]

            chunks = chunk_text(text)

            for idx, chunk in enumerate(chunks):

                chunk_id = (
                    f"{file_path}"
                    f"-page-{page_number}"
                    f"-chunk-{idx}"
                )

                metadata = {
                    "file_path": file_path,
                    "page": page_number,
                    "chunk": idx
                }

                add_chunk(
                    chunk_id=chunk_id,
                    text=chunk,
                    metadata=metadata
                )

                total_chunks += 1

        return (
            f"Successfully indexed file.\n"
            f"File: {file_path}\n"
            f"Total chunks indexed: {total_chunks}"
        )

    except Exception as e:
        return f"Error indexing file: {str(e)}"


@mcp.tool()
def semantic_search(query: str, top_k: int = 5) -> str:
    """
    Perform semantic vector search across indexed files.
    """

    try:
        results = search_chunks(query, top_k)

        documents = results.get("documents", [[]])[0]

        if not documents:
            return "No matching results found."

        return format_results(results)

    except Exception as e:
        return f"Semantic search failed: {str(e)}"


@mcp.tool()
def ask_documents(question: str) -> str:
    """
    Ask questions across indexed documents.
    Retrieves the most relevant chunks.
    """

    try:
        results = search_chunks(question, top_k=5)

        documents = results.get("documents", [[]])[0]

        if not documents:
            return "No relevant information found."

        response = [
            "Relevant evidence retrieved from indexed documents:\n"
        ]

        formatted = format_results(results)

        response.append(formatted)

        return "\n".join(response)

    except Exception as e:
        return f"Document Q&A failed: {str(e)}"


@mcp.tool()
def list_allowed_directories() -> str:
    """
    Show directories allowed for indexing/searching.
    """

    return "\n".join(
        [str(directory) for directory in ALLOWED_DIRS]
    )


# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    mcp.run()