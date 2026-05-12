# File Search MCP

A Model Context Protocol (MCP) server that enables searching for and reading files on your local system.

## Features

- **File Search**: Search for files by name and folder path across multiple directories
  - Searches Documents, Downloads, Desktop, and OneDrive locations
  - Case-insensitive matching
  - Returns up to 50 matching results

- **File Reading**: Read content from multiple file formats
  - Plain text files (.txt, .log, .md, code files)
  - PDF files (.pdf)
  - Word documents (.docx)
  - Returns up to 5000 characters per file

## Setup

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository
```bash
git clone <repository-url>
cd File-search-mcp
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install mcp python-docx pypdf
```

## Usage

Run the MCP server:
```bash
python server.py
```

The server will start and expose two tools:

### search_files(query: str)
Search for files by filename or path.
- **Input**: Search query string
- **Output**: List of matching file paths (max 50 results)

### read_file(file_path: str)
Read content from a file.
- **Input**: Full file path
- **Output**: File content (first 5000 characters)
- **Supported formats**: .txt, .log, .md, code files, .pdf, .docx

## Configuration

Edit the `SEARCH_DIRECTORIES` list in `server.py` to customize which directories are searched:
```python
SEARCH_DIRECTORIES = [
    HOME / "OneDrive" / "Documents",
    HOME / "Downloads",
    HOME / "OneDrive" / "Desktop",
    HOME / "Documents",
    HOME / "Desktop"
]
```

## License

MIT
