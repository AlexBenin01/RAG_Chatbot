import os
import re
import time
import logging
import traceback
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
import config

# Configura logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class RAGBackend:
    def __init__(self):
        self.vector_store_cache = {}
        self.current_pdf_name = None

    def clean_llm_output(self, text):
        """Pulisce tag di pensiero dall'output"""
        if not text: return text
        patterns = [
            r'<think>.*?</think>',
            r'<reasoning>.*?</reasoning>',
            r'\[THINKING\].*?\[/THINKING\]',
            r'\*\*Thinking:?\*\*.*?(?=\n\n|\Z)'
        ]
        for pattern in patterns:
            text = re.sub(pattern, '', text, flags=re.DOTALL | re.IGNORECASE)
        return text.strip()

    def get_llm(self):
        try:
            if config.BACKEND_TYPE == "openai":
                api_key = os.getenv("OPENAI_API_KEY")
                if not api_key: raise ValueError("OPENAI_API_KEY mancante")
                return ChatOpenAI(model=config.LLM_MODEL_OPENAI, temperature=0.5, openai_api_key=api_key)
            else:
                return Ollama(model=config.LLM_MODEL_OLLAMA, base_url=config.OLLAMA_BASE_URL, temperature=0.5)
        except Exception as e:
            logger.error(f"Err LLM: {e}")
            raise

    def get_embedding_model(self):
        try:
            if config.BACKEND_TYPE == "openai":
                return OpenAIEmbeddings(model=config.EMBEDDING_MODEL_OPENAI, openai_api_key=os.getenv("OPENAI_API_KEY"))
            else:
                return OllamaEmbeddings(model=config.EMBEDDING_MODEL_OLLAMA, base_url=config.OLLAMA_BASE_URL)
        except Exception as e:
            logger.error(f"Err Embedding: {e}")
            raise

    def process_document(self, file_path):
        """Carica, splitta e indicizza il PDF"""
        logger.info(f"Processing: {file_path}")
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHUNK_SIZE, 
            chunk_overlap=config.CHUNK_OVERLAP
        )
        chunks = splitter.split_documents(docs)
        
        # Limit chunks per performance
        if len(chunks) > 150: chunks = chunks[:150]
        
        embedding_model = self.get_embedding_model()
        return Chroma.from_documents(chunks, embedding_model, persist_directory=None)

    def get_retriever(self, file_path):
        filename = os.path.basename(file_path)
        if filename in self.vector_store_cache:
            return self.vector_store_cache[filename]
        
        vectordb = self.process_document(file_path)
        retriever = vectordb.as_retriever(search_kwargs={"k": config.RETRIEVER_K})
        self.vector_store_cache[filename] = retriever
        return retriever

    def query(self, file, query_text):
        if not file: yield "⚠️ Carica prima un PDF"; return
        if not query_text.strip(): yield "⚠️ Scrivi una domanda"; return

        try:
            start_time = time.time()
            pdf_name = os.path.basename(file)
            
            # Feedback iniziale
            if pdf_name != self.current_pdf_name:
                yield f"🔄 Analisi documento: `{pdf_name}`..."
                self.current_pdf_name = pdf_name
            
            retriever = self.get_retriever(file)
            llm = self.get_llm()
            
            qa_chain = RetrievalQA.from_chain_type(
                llm=llm, chain_type="stuff", retriever=retriever
            )
            
            response = qa_chain.invoke(query_text)
            clean_res = self.clean_llm_output(response['result'])
            elapsed = time.time() - start_time
            
            yield f"{clean_res}\n\n---\n*⏱️ {elapsed:.1f}s | 📄 {pdf_name}*"

        except Exception as e:
            logger.error(traceback.format_exc())
            yield f"❌ Errore: {str(e)}"
