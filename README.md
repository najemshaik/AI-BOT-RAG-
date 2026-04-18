# 🤖 AI Bot - RAG Chatbot with Free Embeddings

A **FREE**, open-source Retrieval-Augmented Generation (RAG) chatbot that learns from your documents. No API keys required! 

Uses HuggingFace embeddings for semantic search and ChromaDB for vector storage. Built with Python and LangChain.

## ✨ Features

- **100% FREE** - Uses HuggingFace embeddings (no OpenAI costs!)
- **Document Ingestion** - Support for TXT, PDF, and DOCX files
- **Semantic Search** - Finds relevant documents using similarity
- **Interactive Q&A** - Ask questions about your documents
- **Clean Output** - No verbose logs or debug messages
- **Easy Setup** - Just run 2 commands and you're done

## 🚀 Quick Start

### 1. Clone & Setup

```bash
git clone https://github.com/YOUR_USERNAME/AI-Bot.git
cd AI-Bot

# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
# or: source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### 2. Add Documents

Place your documents in the `data/` folder:
- `.txt` files
- `.pdf` files  
- `.docx` files

Example: `data/my_document.txt`

### 3. Index Documents

```bash
python ingest.py
```

This creates a vector database from your documents. Run this once, then you're ready to ask questions!

### 4. Ask Questions

**Single question:**
```bash
python ask_bot.py "What is artificial intelligence?"
```

**Interactive mode:**
```bash
python ask_bot.py
```

Then keep asking questions until you type `quit`

## 📁 Project Structure

```
AI-Bot/
├── ingest.py              # Document indexing script
├── query.py               # Query engine
├── ask_bot.py             # Interactive chatbot interface
├── requirements.txt       # Dependencies
├── README.md              # This file
├── .env.example           # Environment template
├── .gitignore             # Git ignore rules
│
├── data/                  # Your documents
│   ├── document1.txt
│   ├── document2.pdf
│   └── document3.docx
│
├── vector_db/             # Auto-generated embeddings database
│   └── [chroma files]
│
└── docs/                  # Documentation
    ├── QUICKSTART.md      # 30-second getting started
    ├── SETUP.md           # Detailed setup guide
    ├── STRUCTURE.md       # Architecture details
    └── API.md             # Advanced usage
```

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Framework** | LangChain | Orchestrate LLM workflows |
| **Embeddings** | HuggingFace (all-MiniLM-L6-v2) | Generate vector embeddings |
| **Vector DB** | ChromaDB | Store & search embeddings |
| **Document Processing** | pypdf, docx2txt | Load documents |
| **Runtime** | Python 3.13+ | Execution environment |

## 📖 Usage Examples

### Python Script
```python
from query import query_documents

# Get answer from documents
answer = query_documents("What is machine learning?", k=3, use_llm=False)
print(answer)
```

### Command Line
```bash
# Single query
python ask_bot.py "Tell me about Python"

# Interactive session
python ask_bot.py
```

## ⚙️ Configuration

Edit these parameters in `ingest.py` and `query.py`:

- **Chunk Size**: How large each document piece is (default: 500 chars)
- **Chunk Overlap**: Overlap between chunks for context (default: 50 chars)
- **Retrieval K**: How many documents to search (default: 3)

## 📝 Adding More Documents

1. Add files to `data/` folder
2. Run: `python ingest.py` (rebuilds the database)
3. Ask questions: `python ask_bot.py`

## 🆓 Why This Project is Free

- ✅ HuggingFace embeddings - **FREE**
- ✅ ChromaDB vector storage - **FREE**
- ✅ No API calls to OpenAI - **NO COSTS**
- ✅ Runs locally on your machine - **PRIVATE**

## 🔧 Troubleshooting

**"Module not found" error:**
```bash
pip install -r requirements.txt --upgrade
```

**Slow first run:**
The first run downloads the embedding model (~300MB). Subsequent runs are fast!

**Want LLM synthesis?** (Optional)
To synthesize answers with OpenAI GPT:
1. Add `OPENAI_API_KEY=your_key` to `.env`
2. Change `use_llm=False` to `use_llm=True` in `ask_bot.py`

## 📚 Documentation

- **[QUICKSTART.md](docs/QUICKSTART.md)** - Get running in 30 seconds
- **[SETUP.md](docs/SETUP.md)** - Detailed installation guide
- **[STRUCTURE.md](docs/STRUCTURE.md)** - Architecture overview
- **[API.md](docs/API.md)** - Function reference

## 📄 License

MIT License - Feel free to use and modify!

## 🤝 Contributing

Contributions welcome! Feel free to:
- Add new features
- Improve documentation
- Report issues
- Suggest enhancements

## ⭐ If you found this helpful, please star the repo!

## Usage Example

```python
from query import query_documents

# Ask a question
response = query_documents("What are the main topics?", k=5)
print(response)
```

## Troubleshooting

- **API Key Error**: Ensure `OPENAI_API_KEY` is set in `.env`
- **No Vector DB**: Run `python ingest.py` first to create the database
- **Module Not Found**: Install dependencies with `pip install -r requirements.txt`
