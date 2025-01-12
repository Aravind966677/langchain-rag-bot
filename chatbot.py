import os
from typing import List, Dict, Any
import logging
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import HuggingFaceHub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from config import MODEL_CONFIG
from utils import setup_logging, preprocess_document, print_colored

class RAGChatbot:
    def __init__(self, docs_dir: str, config: Dict[str, Any] = None):
        # Load environment variables
        load_dotenv()
        
        # Ensure HuggingFace token is set
        if not os.getenv("HUGGINGFACEHUB_API_TOKEN"):
            raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in environment variables")
            
        # Setup logging
        setup_logging()
        self.logger = logging.getLogger(__name__)
        
        # Load configuration
        self.config = config or MODEL_CONFIG
        
        # Initialize components
        self._initialize_components(docs_dir)
        
        self.logger.info("Chatbot initialized successfully")

    def _initialize_components(self, docs_dir: str):
        """Initialize all components of the chatbot"""
        try:
            # Initialize embeddings
            self.embeddings = HuggingFaceEmbeddings(
                model_name=self.config["embedding_model"]
            )
            
            # Load and process documents
            self.docs = self._load_documents(docs_dir)
            
            # Create vector store
            self.vectorstore = FAISS.from_documents(self.docs, self.embeddings)
            
            # Initialize language model with explicit token
            self.llm = HuggingFaceHub(
                repo_id=self.config["llm_model"],
                huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
                model_kwargs={
                    "temperature": self.config["temperature"],
                    "max_length": self.config["max_length"]
                }
            )
            
            # Setup conversation memory
            self.memory = ConversationBufferMemory(
                memory_key="chat_history",
                return_messages=True
            )
            
            # Create RAG chain
            self.qa_chain = ConversationalRetrievalChain.from_llm(
                llm=self.llm,
                retriever=self.vectorstore.as_retriever(),
                memory=self.memory
            )
            
        except Exception as e:
            self.logger.error(f"Error initializing components: {str(e)}")
            raise

    def _load_documents(self, docs_dir: str) -> List:
        """Load and process documents from the specified directory"""
        try:
            # Load documents
            loader = DirectoryLoader(
                docs_dir,
                glob="**/*.txt",
                loader_cls=TextLoader
            )
            documents = loader.load()
            
            # Preprocess documents
            processed_docs = []
            for doc in documents:
                doc.page_content = preprocess_document(doc.page_content)
                processed_docs.append(doc)
            
            # Split documents
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.config["chunk_size"],
                chunk_overlap=self.config["chunk_overlap"]
            )
            
            return text_splitter.split_documents(processed_docs)
            
        except Exception as e:
            self.logger.error(f"Error loading documents: {str(e)}")
            raise

    def chat(self, query: str) -> str:
        """Process a user query and return a response"""
        try:
            response = self.qa_chain({"question": query})
            return response['answer']
        except Exception as e:
            error_msg = f"Error processing query: {str(e)}"
            self.logger.error(error_msg)
            return error_msg