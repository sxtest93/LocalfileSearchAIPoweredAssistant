# Local File Search AI-Powered Assistant

**An intelligent Model Context Protocol (MCP) server for seamless local file discovery and content retrieval**

A powerful MCP server that enables searching for and reading files on your local system. Perfect for AI-powered assistants that need access to local file search capabilities, document reading, and intelligent file discovery.

## Features

- **Semantic File Search**: Advanced search using vector embeddings for intelligent file discovery
  - Searches by content meaning, not just keywords
  - Powered by embeddings and ChromaDB
  
- **Multi-Format Support**: Handle various document types seamlessly
  - PDF files (.pdf)
  - Word documents (.docx)
  - Text files (.txt, .log, .md)
  - Code files with syntax awareness
  
- **Vector Embeddings**: Convert documents to semantic vectors for intelligent queries
  - Semantic similarity matching
  - Contextual search capabilities
  
- **ChromaDB Integration**: Persistent vector storage and retrieval
  - Fast similarity search
  - Efficient vector indexing
  - Metadata filtering
  
- **Document Q&A**: Ask questions about document content
  - Answer questions based on document context
  - Extract relevant information from files
  - Powered by AI-driven semantic search
  
- **MCP Tools**: Full Model Context Protocol implementation
  - search_files: Keyword and semantic file search
  - read_file: Extract content from documents
  - query_documents: Ask questions about documents
  
- **Secure Directory Access**: Controlled access to local files
  - Configurable search directories
  - Access restrictions and permissions
  - Safe file reading with error handling

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

The server will start and expose the following MCP tools:

### search_files(query: str)
Search for files using keyword matching and path lookup.
- **Input**: Search query string
- **Output**: List of matching file paths (max 50 results)
- **Example**: `search_files("report")` returns all files with "report" in name/path

### search_semantic(query: str)
Search files semantically using vector embeddings and ChromaDB.
- **Input**: Natural language search query
- **Output**: Ranked list of semantically relevant files
- **Example**: `search_semantic("financial performance documents")` finds related files by meaning

### read_file(file_path: str)
Read content from a file.
- **Input**: Full file path
- **Output**: File content (first 5000 characters)
- **Supported formats**: .txt, .log, .md, code files, .pdf, .docx
- **Example**: `read_file("C:/Users/Downloads/document.pdf")`

### query_document(file_path: str, question: str)
Ask questions about a specific document.
- **Input**: File path and question
- **Output**: Answer based on document content
- **Example**: `query_document("report.pdf", "What was Q4 revenue?")`

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
