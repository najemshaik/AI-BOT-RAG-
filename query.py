import os
import warnings
import logging
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Suppress all warnings and logs
warnings.filterwarnings("ignore")
logging.getLogger("transformers").setLevel(logging.CRITICAL)
logging.getLogger("sentence_transformers").setLevel(logging.CRITICAL)
logging.getLogger("huggingface_hub").setLevel(logging.CRITICAL)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["TRANSFORMERS_VERBOSITY"] = "critical"

# Load environment variables
load_dotenv()

DB_PATH = "vector_db"

def query_documents(query_text, k=3, use_llm=True):
    """
    Query the vector database and get relevant documents
    
    Args:
        query_text: The user's query
        k: Number of relevant documents to retrieve
        use_llm: Whether to use OpenAI LLM for synthesis (requires API key)
    
    Returns:
        Response from the QA chain
    """
    try:
        # Load HuggingFace embeddings (FREE - no API key needed)
        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            show_progress=False
        )
        
        # Load the vector database
        db = Chroma(
            persist_directory=DB_PATH,
            embedding_function=embeddings
        )
        
        # Search for relevant documents
        docs = db.similarity_search(query_text, k=k)
        
        # Try to use LLM for synthesis if available
        if use_llm:
            api_key = os.getenv("OPENAI_API_KEY")
            if api_key:
                llm = ChatOpenAI(
                    model_name="gpt-3.5-turbo",
                    temperature=0.7,
                    api_key=api_key
                )
                
                prompt = PromptTemplate(
                    input_variables=["context", "question"],
                    template="""You are a helpful assistant. Answer the question based on the provided context. 
If the context doesn't contain the answer, say "I don't have enough information to answer this question."

Context:
{context}

Question: {question}

Answer:"""
                )
                
                context = "\n\n".join([doc.page_content for doc in docs])
                chain = prompt | llm
                result = chain.invoke({"context": context, "question": query_text})
                return result.content
        
        # Return concatenated documents if LLM not available
        context = "\n\n".join([f"[Document {i}]\n{doc.page_content}" for i, doc in enumerate(docs, 1)])
        return context
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Example usage
    user_query = "What is the climate?"
    print(f"Query: {user_query}\n")
    response = query_documents(user_query, use_llm=False)  # Set to True if you have OpenAI API key
    print(f"\n--- RESPONSE ---\n{response}")
