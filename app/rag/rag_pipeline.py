from app.rag.loader import load_documents
from app.rag.embeddings import embed_texts
from app.rag.vector_store import FAISSStore
from app.chatbot.llm import generate_response


class RAGPipeline:
    def __init__(self):
        # Load documents
        docs = load_documents("data/docs")

        # Create embeddings for documents
        embeddings = embed_texts(docs)

        # Create FAISS vector store
        self.store = FAISSStore(embeddings, docs)

    def answer(self, question: str, history: list[str]) -> str:
        query_embedding = embed_texts([question])[0]
        context_docs = self.store.search(query_embedding)

        context = "\n".join(context_docs)
        conversation = "\n".join(history)

        prompt = f"""
You are an enterprise assistant.

Conversation so far:
{conversation}

You MUST answer the question using ONLY the information present in the context.
If the answer is not present in the context, reply exactly with:
"I don't know based on the provided documents."

Context:
{context}

Question:
{question}
"""

        return generate_response(prompt)
