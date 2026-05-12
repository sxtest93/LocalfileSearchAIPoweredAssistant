import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="./data/chroma_db")
collection = client.get_or_create_collection("file_chunks")

model = SentenceTransformer("all-MiniLM-L6-v2")


def add_chunk(chunk_id, text, metadata):
    embedding = model.encode(text).tolist()

    collection.add(
        ids=[chunk_id],
        embeddings=[embedding],
        documents=[text],
        metadatas=[metadata]
    )


def search_chunks(query: str, top_k: int = 5):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results