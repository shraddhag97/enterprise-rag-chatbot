
# Enterprise RAG Chatbot 🤖

An enterprise-grade conversational chatbot built using **Retrieval Augmented Generation (RAG)**.  
The system provides **document-grounded, non-hallucinating answers** with session-based conversational memory.

---

## ✨ Key Features

- 🔍 **Retrieval Augmented Generation (RAG)**
  - Answers are generated strictly from provided documents
  - No hallucinated responses
- 🧠 **Session-based conversational memory**
  - Supports follow-up questions using `session_id`
- ⚡ **FastAPI backend**
  - Clean, modular, API-first design
- 💬 **Streamlit chat UI**
  - Real-time chat interface
  - Automatic session handling
- 🧱 **Vector search using FAISS**
  - Efficient similarity search over document embeddings
- 🔐 **Secure by design**
  - Environment variables for secrets
  - `.env` and `.venv` excluded from Git

---

## 🏗️ System Architecture

```

User
│
│  (chat input)
▼
Streamlit UI
│
│  POST /chat
▼
FastAPI Backend
│
├── Session Memory
│
├── RAG Pipeline
│     ├── Document Loader
│     ├── Embedding Generator (OpenAI)
│     ├── FAISS Vector Store
│     └── Context Retrieval
│
└── LLM Response Generator
│
▼
Grounded Answer

```

**Key principle:**  
> The LLM is never allowed to answer outside the retrieved document context.

---

## 📂 Project Structure

```

enterprise-rag-chatbot/
│
├── app/
│   ├── api.py                # FastAPI entry point
│   ├── config.py             # Environment & app config
│   ├── schemas/              # Request/response models
│   ├── chatbot/
│   │   └── memory.py         # Session-based memory
│   └── rag/
│       ├── loader.py         # Document loading
│       ├── embeddings.py     # Embedding generation
│       ├── vector_store.py   # FAISS vector store
│       └── rag_pipeline.py   # End-to-end RAG logic
│
├── data/
│   └── docs/
│       └── sample.txt        # Example knowledge source
│
├── ui/
│   └── chat_ui.py            # Streamlit chat interface
│
├── requirements.txt
├── README.md
└── .gitignore

````

---

## ⚙️ Tech Stack

- **Backend:** FastAPI
- **Frontend:** Streamlit
- **LLM:** OpenAI (pluggable: Azure / DeepSeek compatible)
- **Embeddings:** OpenAI Embeddings
- **Vector DB:** FAISS
- **Language:** Python 3.11

---

## ▶️ How to Run Locally

### 1️⃣ Create virtual environment
```bash
python3.11 -m venv .venv
source .venv/bin/activate
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

### 4️⃣ Start backend

```bash
uvicorn app.api:app
```

Backend runs at:

```
http://127.0.0.1:8000
```

### 5️⃣ Start Streamlit UI

```bash
streamlit run ui/chat_ui.py
```

UI runs at:

```
http://localhost:8501
```

---

## 🧪 Example Usage

1. Ask:

   > *What is Enterprise RAG Chatbot?*

2. Follow up:

   > *Is it trained on company data?*

The chatbot:

* Uses memory to understand context
* Answers **only** from documents
* Responds safely if information is missing

---

## 🧠 Design Highlights (Interview-Ready)

* RAG implemented **from scratch** (no LangChain dependency)
* Strict grounding enforcement (`"I don't know based on provided documents"`)
* Clean separation of UI, API, and AI logic
* Easily extensible to:

  * Azure OpenAI
  * S3 / Blob document sources
  * Redis-based memory
  * LangChain abstractions

---

## 🚀 Future Enhancements

* Document chunking & metadata filtering
* Conversation summarization memory
* Multi-document citation support
* Authentication & role-based access
* Deployment on AWS / Azure

---

## 📌 Disclaimer

This project is for educational and portfolio purposes.
No proprietary or confidential data is included.

````

