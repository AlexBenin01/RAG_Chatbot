import os

# Configurazioni Backend
BACKEND_TYPE = "ollama"  # "openai" o "ollama"
OLLAMA_BASE_URL = "http://localhost:11434"

# Modelli
LLM_MODEL_OLLAMA = "qwen3:1.7b"
EMBEDDING_MODEL_OLLAMA = "nomic-embed-text"
LLM_MODEL_OPENAI = "gpt-4o-mini"
EMBEDDING_MODEL_OPENAI = "text-embedding-3-small"

# Parametri RAG
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100
RETRIEVER_K = 3

# App UI
APP_TITLE = "RAG Chatbot"
APP_SUBTITLE = f"Powered by {BACKEND_TYPE.upper()} • Analisi intelligente di documenti PDF"
