import faiss
import numpy as np


class FAISSStore:
    def __init__(self, embeddings: list[list[float]], documents: list[str]):
        self.embeddings = np.array(embeddings).astype("float32")
        self.documents = documents

        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(self.embeddings)

    def search(self, query_embedding: list[float], top_k: int = 3) -> list[str]:
        query = np.array([query_embedding]).astype("float32")
        _, indices = self.index.search(query, top_k)
        return [self.documents[i] for i in indices[0]]
