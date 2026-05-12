# Local File Search AI-Powered Assistant

**An intelligent Model Context Protocol (MCP) server for seamless local file discovery and content retrieval**

A powerful MCP server that enables searching for and reading files on your local system. Perfect for AI-powered assistants (Claude, VSCode) that need access to local file search capabilities, document reading, and intelligent semantic search powered by vector embeddings.

## Features

- **🔍 Dual Search Methods**
  - Keyword-based file search by name and path
  - Semantic search using AI embeddings and ChromaDB
  
- **📄 Multi-Format Support**
  - PDF files (.pdf)
  - Word documents (.docx)
  - Text files (.txt, .md, .log)
  - Code files (.py, .java, .yml, .yaml, .json)
  
- **🧠 Vector Intelligence**
  - Semantic embeddings using sentence-transformers (all-MiniLM-L6-v2)
  - ChromaDB for persistent vector storage
  - Text chunking with configurable overlap
  
- **💬 Document Q&A**
  - Ask questions across indexed documents
  - Retrieve relevant evidence from documents
  - Context-aware responses
  
- **🔒 Secure Access Control**
  - Whitelisted directory access
  - Blocked sensitive file detection (.env, .pem, .key, credentials)
  - Path validation and access restrictions
  
- **🔧 MCP Integration**
  - Full Model Context Protocol implementation
  - Compatible with Claude, VSCode, and other MCP clients
  - 9 powerful tools for file operations

## Architecture

```
Claude/Desktop/VSCode
        ↓
      MCP
        ↓
   server.py (MCP Server)
        ↓
    ├── reader.py (File Reading)
    ├── indexer.py (Text Chunking)
    └── vector_store.py (ChromaDB)
        ↓
   Embeddings (sentence-transformers)
        ↓
   ChromaDB (Vector Storage)
        ↓
PDF/DOCX/TXT/Code Files
```

### Core Components

| Component | Purpose |
|-----------|---------|
| **server.py** | MCP server with 9 tools for file operations |
| **reader.py** | Multi-format file readers (PDF, DOCX, TXT, etc.) |
| **vector_store.py** | ChromaDB integration for semantic search |
| **indexer.py** | Text chunking with configurable overlap (800 chars, 100 overlap) |
| **config.py** | Configuration for allowed directories, blocked files, search settings |

## Project Structure

```
File-search-mcp/
├── src/
│   ├── __init__.py
│   ├── server.py           # Main MCP server with 9 tools
│   ├── reader.py           # Multi-format file readers
│   ├── vector_store.py     # ChromaDB semantic search
│   ├── indexer.py          # Text chunking logic
│   └── config.py           # Configuration settings
├── tests/
│   ├── __init__.py
│   └── test_server.py      # Unit tests
├── data/
│   └── chroma_db/          # Vector database (auto-created)
├── requirements.txt        # Python dependencies
├── pyproject.toml          # Project configuration
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

### Start the MCP Server
```bash
python -m src.server
```

The server will initialize and be ready for MCP connections.

## Available MCP Tools

### 🏥 Health & Configuration
#### `health_check() → str`
Check if MCP server is running and operational.
```
Example output: "AI File Intelligence MCP is running successfully."
```

#### `list_allowed_directories() → str`
Show all directories allowed for indexing and searching.
```
Example output:
C:\Users\YourName\Documents
C:\Users\YourName\Downloads
C:\Users\YourName\Desktop
```

### 📂 File System Navigation
#### `find_files(file_name: str) → str`
Search for files by name across allowed directories.
```
Example: find_files("report")
Output: List of files matching "report"
```

#### `find_folder(folder_name: str) → str`
Search for folders by name across allowed directories.
```
Example: find_folder("Projects")
Output: List of folders matching "Projects"
```

#### `list_files(folder_path: str) → str`
List all files and folders inside a directory.
```
Example: list_files("C:\\Users\\YourName\\Documents")
Output:
DIR: C:\Users\YourName\Documents\Projects
FILE: C:\Users\YourName\Documents\report.pdf
```

### 📖 File Reading
#### `read_file_content(file_path: str) → str`
Read content from supported file formats.
- **Supported**: PDF, DOCX, TXT, MD, LOG, PY, JAVA, YAML, JSON
- **Output**: First 3000 characters per page
```
Example: read_file_content("C:\\Users\\YourName\\Downloads\\document.pdf")
Output: File content with page numbers
```

### 🧠 Semantic Search & RAG
#### `index_file(file_path: str) → str`
Index a file into the vector database for semantic search.
- Creates text chunks (800 chars with 100 char overlap)
- Generates embeddings using sentence-transformers
- Stores in ChromaDB for fast retrieval
```
Example: index_file("C:\\Users\\YourName\\Documents\\report.pdf")
Output: "Successfully indexed file. Total chunks indexed: 45"
```

#### `semantic_search(query: str, top_k: int = 5) → str`
Search indexed files semantically using vector embeddings.
```
Example: semantic_search("financial performance", top_k=5)
Output: Top 5 most relevant chunks with file paths and content
```

#### `ask_documents(question: str) → str`
Ask questions about indexed documents and get relevant answers.
```
Example: ask_documents("What was the Q4 revenue?")
Output: Relevant document chunks that answer the question
```

## Configuration

Edit `src/config.py` to customize:

```python
# Allowed directories for indexing/searching
ALLOWED_DIRS = [
    Path.home() / "Documents",
    Path.home() / "Downloads",
    Path.home() / "Desktop"
]

# Sensitive files to block
BLOCKED_FILES = [".env", ".pem", ".key", "id_rsa", "credentials"]

# Semantic search results (default top 5)
DEFAULT_TOP_K = 5

# Max characters in search results (1200)
MAX_RESULT_CHARS = 1200
```

## Workflow Example

### 1. Find a File
```bash
find_files("quarterly_report")
```

### 2. Index It
```bash
index_file("C:\\Users\\YourName\\Documents\\quarterly_report.pdf")
```

### 3. Search Semantically
```bash
semantic_search("revenue and profit margins")
```

### 4. Ask Questions
```bash
ask_documents("What were the main challenges mentioned?")
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

### Customize Text Chunking
Edit `src/indexer.py`:
```python
def chunk_text(text: str, chunk_size: int = 800, overlap: int = 100):
```
- `chunk_size`: Larger = fewer chunks, less granular search
- `overlap`: Prevents context loss between chunks

## Dependencies

| Package | Purpose |
|---------|---------|
| mcp | Model Context Protocol framework |
| chromadb | Vector database for semantic search |
| sentence-transformers | AI embeddings model (all-MiniLM-L6-v2) |
| python-docx | DOCX file reading |
| pypdf | PDF file reading |
| numpy | Numerical computing |

## Security

- ✅ Directory whitelisting prevents unauthorized access
- ✅ Sensitive file detection blocks .env, credentials, keys
- ✅ Path validation ensures files are in allowed directories
- ✅ Error handling prevents information leakage
- ✅ Safe file reading with UTF-8 error handling

## Troubleshooting

### "Access denied" error
- File is outside allowed directories (check `config.py`)
- File name contains blocked keywords (.env, credentials, etc.)

### No semantic search results
- Make sure to `index_file()` first before searching
- Check if files were successfully indexed

### Slow semantic search
- Reduce `top_k` value for faster results
- Consider indexing fewer files initially

## License

MIT

## Contributing

Contributions welcome! Please ensure tests pass and follow the existing code style.
