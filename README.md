# File Search MCP

A Model Context Protocol (MCP) server that enables searching for and reading files on your local system. Perfect for AI-powered assistants that need access to local file search capabilities.

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

## Project Structure

```
File-search-mcp/
├── src/
│   ├── __init__.py
│   └── server.py           # Main MCP server implementation
├── tests/
│   ├── __init__.py
│   └── test_server.py      # Unit tests
├── requirements.txt        # Python dependencies
├── pyproject.toml         # Project configuration
├── .gitignore
└── README.md
```

## Setup

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

1. Clone the repository
```bash
git clone https://github.com/sxtest93/LocalfileSearchAIPoweredAssistant.git
cd LocalfileSearchAIPoweredAssistant
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

Run the MCP server:
```bash
python -m src.server
```

The server will start and expose two tools:

### search_files(query: str)
Search for files by filename or path.
- **Input**: Search query string
- **Output**: List of matching file paths (max 50 results)
- **Example**: `search_files("report")` returns all files with "report" in name/path

### read_file(file_path: str)
Read content from a file.
- **Input**: Full file path
- **Output**: File content (first 5000 characters)
- **Supported formats**: .txt, .log, .md, code files, .pdf, .docx
- **Example**: `read_file("C:/Users/Downloads/document.pdf")`

## Configuration

Edit the `SEARCH_DIRECTORIES` list in `src/server.py` to customize which directories are searched:
```python
SEARCH_DIRECTORIES = [
    HOME / "OneDrive" / "Documents",
    HOME / "Downloads",
    HOME / "OneDrive" / "Desktop",
    HOME / "Documents",
    HOME / "Desktop"
]
```

## Development

### Running Tests
```bash
pytest tests/
```

### Installing in Development Mode
```bash
pip install -e .
```

## License

MIT
