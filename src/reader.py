from pathlib import Path
from pypdf import PdfReader
from docx import Document


def read_txt(file_path: str):
    return Path(file_path).read_text(encoding="utf-8", errors="ignore")


def read_pdf(file_path: str):
    reader = PdfReader(file_path)
    pages = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        pages.append({
            "page": i + 1,
            "text": text
        })

    return pages


def read_docx(file_path: str):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])

    return [{
        "page": 1,
        "text": text
    }]


def read_file(file_path: str):
    suffix = Path(file_path).suffix.lower()

    if suffix == ".pdf":
        return read_pdf(file_path)

    if suffix == ".docx":
        return read_docx(file_path)

    if suffix in [".txt", ".md", ".log", ".py", ".java", ".yml", ".yaml", ".json"]:
        return [{
            "page": 1,
            "text": read_txt(file_path)
        }]

    raise ValueError(f"Unsupported file type: {suffix}")