# 🤖 RAG Chatbot — Intelligent PDF Analysis

**RAG Chatbot** è una web application per l’analisi intelligente di documenti PDF basata su architettura **Retrieval-Augmented Generation (RAG)**.  
Consente di caricare un PDF e interrogare il contenuto tramite un’interfaccia chat moderna, accessibile e responsive.

> Progetto focalizzato su **AI applicata**, **LLM orchestration**, **UX accessibile (WCAG 2.1)** e **best practice software engineering**.

---

## ✨ Features principali

- 📄 **Upload PDF** (max 20MB)
- 🔍 **Indicizzazione semantica** con embedding vettoriali
- 🤖 **Chat intelligente** basata su LLM (Ollama o OpenAI)
- ⚡ **Risposte contestuali** tramite RetrievalQA
- 🎨 **UI moderna e accessibile** (WCAG 2.1 AAA-oriented)
- 🌙 **Dark / Light mode automatico**
- 🧠 **Caching dei documenti** per performance migliori
- 🧹 **Pulizia automatica dell’output LLM** (no reasoning leaks)

---

## 🧠 Architettura

PDF
└─► Loader (PyPDF)
└─► Text Splitter
└─► Embedding Model
└─► Vector Store (Chroma)
└─► Retriever
└─► LLM
└─► Chat UI (Gradio)

### Pattern utilizzati
- **RAG (Retrieval-Augmented Generation)**
- **Separation of Concerns**
- **Streaming response**
- **LLM-agnostic backend**
- **Design tokens + deterministic CSS**

---

## 🛠️ Tech Stack

### Frontend
- **Gradio 4.x**
- CSS custom (design tokens)
- WCAG 2.1 compliant UI
- Keyboard & focus accessibility

### Backend
- **Python 3.10+**
- **LangChain**
- **ChromaDB**
- **PyPDF**
- **Ollama** (default) / **OpenAI** (optional)

### Modelli supportati
- `qwen3:1.7b` (LLM, locale)
- `nomic-embed-text` (embedding)
- `gpt-4o-mini` (opzionale via OpenAI)

---

## 📂 Struttura del progetto

├── app.py # UI + event handling
├── backend.py # RAG backend logic
├── config.py # Configurazioni centralizzate
├── theme.py # Tema UI (WCAG + product-grade)
├── requirements.txt # Dipendenze
└── README.md

---

## ⚙️ Configurazione

### 1️⃣ Clona il repository

```bash
git clone https://github.com/tuo-username/rag-chatbot.git
cd rag-chatbot

2️⃣ Crea un virtual environment

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Installa le dipendenze

pip install -r requirements.txt

4️⃣ Avvia Ollama (se usi backend locale)

ollama run qwen3:1.7b

5️⃣ Avvia l’app

python app.py
Apri 👉 http://localhost:7860

🔄 Backend: Ollama vs OpenAI

Nel file config.py puoi scegliere il backend:

BACKEND_TYPE = "ollama"   # oppure "openai"
```

Per OpenAI:

export OPENAI_API_KEY="your_api_key"

🎨 UI & Accessibilità

🎯 WCAG 2.1 AAA-oriented

Contrast-safe colors

Focus ring visibile

Dark mode senza “flip” di colori

Chat bubble proporzionate (product-grade)

L’interfaccia è ispirata a prodotti SaaS moderni (ChatGPT-like)
senza copiare brand o CSS proprietari

🚀 Performance & Scalabilità

Chunking configurabile

Caching per documento

Limite massimo chunk per PDF

Retriever k configurabile

Architettura pronta per:

streaming avanzato

memoria conversazionale

multi-document RAG

🔐 Sicurezza & Privacy

Nessun dato persistente lato server

Vector store in memoria

Nessun upload remoto obbligatorio

OpenAI usato solo se esplicitamente configurato

🧪 Stato del progetto

✅ Stable
🧩 Estendibile


👤 Autore

Alessandro Benin
Aspiring AI Specialist / Backend Developer


📜 Licenza MIT
