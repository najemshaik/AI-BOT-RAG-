import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

print("Step 1: Loading documents from data folder...")
DATA_PATH = "data"
DB_PATH = "vector_db"

documents = []
for file in os.listdir(DATA_PATH):
    path = os.path.join(DATA_PATH, file)
    try:
        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)
        elif file.endswith(".txt"):
            loader = TextLoader(path)
        elif file.endswith(".docx"):
            loader = Docx2txtLoader(path)
        else:
            continue
        documents.extend(loader.load())
        print(f"  [OK] Loaded: {file}")
    except Exception as e:
        print(f"  [SKIP] {file}: {str(e)}")

print(f"\nStep 2: Splitting documents into chunks...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(documents)
print(f"  Created {len(chunks)} chunks from {len(documents)} documents")

print(f"\nStep 3: Creating embeddings (using HuggingFace - FREE)...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
print(f"  Embeddings model loaded successfully")

print(f"\nStep 4: Creating Chroma vector database...")
db = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory=DB_PATH
)
db.persist()

print(f"\nStep 5: SUCCESS - Vector database created!")
print(f"  Location: {os.path.abspath(DB_PATH)}")
print(f"  Total documents: {len(documents)}")
print(f"  Total chunks: {len(chunks)}")
print(f"\nDocuments indexed successfully!")