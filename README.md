# 🏛️ GovDocs RAG Assistant

> **Domain-Specific Retrieval-Augmented Generation (RAG) System for Government Building Regulations & Development Control Standards**

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Qdrant](https://img.shields.io/badge/Qdrant-VectorDB-red.svg)](https://qdrant.tech/)
[![LangChain](https://img.shields.io/badge/LangChain-Enabled-1C3C3C.svg)](https://www.langchain.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 📌 Executive Summary

**GovDocs RAG Assistant** is an enterprise-grade, end-to-end Retrieval-Augmented Generation (RAG) pipeline designed to index, query, and synthesize complex government regulations and building codes (e.g., UDCPR 2020/2025, PMRDA DCPR 2018, PMC DCPR 2015). 

Legal and statutory document retrieval often suffers from accuracy issues due to outdated regulations, dense legal phrasing, and high risk of LLM hallucinations. This project tackles these challenges by integrating **metadata-aware vector search**, **dense embeddings**, **strict status-filtering**, and **hallucination guardrails** to deliver grounded, source-attributed answers with exact document and page references.

---

## 🚀 Key Features

- 📑 **Metadata-Driven Context Retrieval**: Extracted chunks are enriched with document titles, authority metadata, revision versions, and status tags (`current` vs. `historical`) to prevent outdated statutory laws from being retrieved.
- ⚡ **High-Performance Dense Vector Search**: Leverages HuggingFace's `BAAI/bge-small-en-v1.5` embeddings (384 dimensions) paired with a persistent **Qdrant Vector Database** using cosine distance metrics.
- 🛡️ **Hallucination-Resistant Synthesis**: Utilizes `openai/gpt-oss-120b` via Hugging Face Inference Client with strict zero-hallucination prompts and fallback responses (`"I could not find a reliable answer in the provided documents."`).
- 🔗 **Full Transparency & Citation**: Every generated response includes detailed source attribution listing document titles, page numbers, status, and retrieved context chunks.
- ⚡ **Production-Ready FastAPI Backend**: Asynchronous REST API endpoints with request validation (Pydantic models) and CORS support.
- 💻 **Interactive Web Interface**: Clean, responsive frontend built with modern UI standards for instant query execution and source review.

---

## 🏗️ Architecture & Pipeline Flow

```
+------------------+     +--------------------+     +-------------------+
|  Government PDFs | --> | Ingestion Pipeline | --> | Document Cleaning |
| (UDCPR, DCPR...) |     | (PyPDF Loader)     |     | & Normalization   |
+------------------+     +--------------------+     +-------------------+
                                                              |
                                                              v
+------------------+     +--------------------+     +-------------------+
|  Qdrant Vector   | <-- | BGE Embeddings     | <-- | Recursive Chunking|
|  Database        |     | (384-dim Dense)    |     | (1000 size / 200) |
+------------------+     +--------------------+     +-------------------+
        |
        v
+------------------+     +--------------------+     +-------------------+
| Metadata Filter  | --> | LLM Prompt Engine  | --> | FastAPI Endpoint  |
| (status=current) |     | (GPT-OSS-120B)     |     | & Web Interface   |
+------------------+     +--------------------+     +-------------------+
```

---

## 🛠️ Tech Stack

| Layer | Component / Technology |
| :--- | :--- |
| **LLM Engine** | `openai/gpt-oss-120b` via Hugging Face Inference API |
| **Embedding Model** | `BAAI/bge-small-en-v1.5` (Sentence-Transformers) |
| **Vector Store** | Qdrant (Persistent Local Engine) |
| **Orchestration** | LangChain Core, LangChain Community, LangChain Text Splitters |
| **Backend API** | FastAPI, Uvicorn, Pydantic |
| **Document Parsing** | PyPDF |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Testing** | Pytest, Custom Pipeline Scripts |

---

## 📁 Repository Structure

```
govdocs-rag-assistant/
├── data/
│   └── raw/               # Raw government regulatory PDF documents
├── qdrant_db/             # Local persistent Qdrant vector database storage
├── scripts/               # Test suites and operational scripts
│   ├── check_qdrant.py
│   ├── ingest_to_qdrant.py
│   ├── test_chunker.py
│   ├── test_embeddings.py
│   ├── test_llm.py
│   └── test_rag.py
├── src/
│   ├── api/               # FastAPI routes and server definitions
│   │   └── main.py
│   ├── embeddings/        # Embedding model initializers
│   │   └── embeddings.py
│   ├── frontend/          # Web dashboard (HTML/CSS/JS)
│   │   ├── index.html
│   │   ├── script.js
│   │   └── style.css
│   ├── ingestion/         # PDF extraction, cleaning, chunking & metadata pipeline
│   │   ├── chunker.py
│   │   ├── cleaner.py
│   │   ├── metadata.py
│   │   ├── pdf_loader.py
│   │   └── pipeline.py
│   ├── LLM/               # LLM inference client wrappers
│   │   └── llm.py
│   ├── RAG/               # Core retrieval, context assembly & prompt chain
│   │   └── rag_pipeline.py
│   ├── vector_store/      # Qdrant client connection & index manager
│   │   └── qdrant_store.py
│   └── config.py          # Centralized project configuration & environment paths
├── .env.example           # Environment template file
├── .gitignore             # Standard ignore configuration
├── requirements.txt       # Python dependency specifications
└── README.md              # Project documentation
```

---

## 🚦 Quickstart Guide

### 1. Prerequisites

- Python `3.10+` installed.
- Hugging Face API Token (with access to Inference API).

### 2. Installation & Setup

Clone the repository and set up a virtual environment:

```bash
# Clone the repository
git clone https://github.com/sinu-ops/govdocs-rag-assistant.git
cd govdocs-rag-assistant

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# macOS / Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Add your Hugging Face API Token to `.env`:

```env
HF_TOKEN=your_huggingface_token_here
```

---

## ⚙️ Running Ingestion & API

### 1. Ingest Regulatory Documents

Place your PDF regulatory files into `data/raw/` and execute the ingestion script to process, chunk, embed, and store vector representations in Qdrant:

```bash
python -m scripts.ingest_to_qdrant
```

### 2. Launch FastAPI Server & Frontend

Start the server using Uvicorn:

```bash
uvicorn src.api.main:app --reload --port 8000
```

Open your browser and navigate to:
- **Interactive Web Interface**: `http://localhost:8000/`
- **Swagger API Docs**: `http://localhost:8000/docs`

---

## 🔌 API Endpoint Documentation

### Request: `POST /ask`

```json
{
  "question": "What is the maximum allowed FSI for residential zones under UDCPR?"
}
```

### Response Schema

```json
{
  "question": "What is the maximum allowed FSI for residential zones under UDCPR?",
  "answer": "According to UDCPR Regulation 6.1, the basic allowed FSI for residential zones is 1.10 for road widths up to 9.0 meters...",
  "sources": [
    {
      "source": "source_1",
      "document_title": "Unified Development Control and Promotion Regulations",
      "page": "84",
      "version": "UDCPR 2020 Updated 2025",
      "status": "current",
      "content": "Excerpt of retrieved regulation text..."
    }
  ]
}
```

---

## 🧪 Testing & Verification

Run individual module test scripts located in the `scripts/` folder:

```bash
# Verify HuggingFace token and LLM access
python -m scripts.test_llm

# Test Qdrant vector database persistence
python -m scripts.test_qdrant

# Test full RAG retrieval & generation end-to-end
python -m scripts.test_rag
```

---

## 💡 AI Engineering Highlights & Design Decisions

- **Why Metadata Filtering over Plain RAG?** Government regulations evolve continuously. Searching across all historical documents leads to illegal or outdated compliance advice. By annotating chunks with metadata and enforcing `status == "current"` filtering in Qdrant, we ensure queries resolve against active legislation.
- **Why BAAI/bge-small-en-v1.5?** Offers top-tier MTEB retrieval leaderboard performance for dense vector embeddings while maintaining lightweight CPU/GPU memory overhead.
- **Temperature & Prompt Calibration**: Standard LLMs hallucinate precise numerical constants (FSI, setback distances). Setting `temperature=0.1` and applying strict system boundaries ensures responses are strictly derived from context.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.

---

## 👤 Author

- **GitHub**: [@sinu-ops](https://github.com/sinu-ops)
- **Role Target**: AI Engineer / RAG Specialist / LLM Applications Developer
