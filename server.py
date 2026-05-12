import os
from pathlib import Path

from docx import Document
from pypdf import PdfReader

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Laptop File Finder")

HOME = Path.home()

SEARCH_DIRECTORIES = [
    HOME / "OneDrive" / "Documents",
    HOME / "Downloads",
    HOME / "OneDrive" / "Desktop",
    HOME / "Documents",
    HOME / "Desktop"
]


@mcp.tool()
def search_files(query: str) -> str:
    """
    Search files by filename and full folder path.
    """

    matches = []
    query_lower = query.lower()

    for directory in SEARCH_DIRECTORIES:

        if not directory.exists():
            continue

        for root, dirs, files in os.walk(str(directory)):

            for file in files:

                full_path = os.path.join(root, file)

                if (
                    query_lower in file.lower()
                    or query_lower in full_path.lower()
                ):
                    matches.append(full_path)

    if not matches:
        return "No matching files found."

    return "\n".join(matches[:50])


@mcp.tool()
def read_file(file_path: str) -> str:
    """
    Read txt, log, markdown, code, docx, and pdf files.
    """

    try:

        path = Path(file_path)

        if not path.exists():
            return "File does not exist."

        # DOCX SUPPORT
        if path.suffix.lower() == ".docx":

            doc = Document(str(path))

            text = [para.text for para in doc.paragraphs]

            return "\n".join(text)[:5000]

        # PDF SUPPORT
        elif path.suffix.lower() == ".pdf":

            reader = PdfReader(str(path))

            text = []

            for page in reader.pages:

                extracted = page.extract_text()

                if extracted:
                    text.append(extracted)

            return "\n".join(text)[:5000]

        # TXT / CODE / LOGS
        else:

            with open(
                path,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as file:

                content = file.read()

            return content[:5000]

    except Exception as e:
        return f"Error reading file: {str(e)}"


if __name__ == "__main__":
    mcp.run()