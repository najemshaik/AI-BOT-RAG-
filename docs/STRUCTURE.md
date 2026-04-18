# Project Structure

## Directory Layout

```
AI Bot/
├── README.md                    # Main documentation
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (not tracked)
├── .env.example                 # Environment template
├── .gitignore                   # Git ignore rules
│
├── ingest.py                    # Document ingestion script
├── query.py                     # Query engine backend
├── ask_bot.py                   # Interactive chatbot
│
├── data/                        # Your documents
│   ├── artificial_intelligence.txt
│   ├── data_science.txt
│   ├── machine_learning.txt
│   ├── python_guide.txt
│   └── web_development.txt
│
├── vector_db/                   # Vector database (auto-created)
│   └── [chroma db files]
│
├── docs/                        # Documentation
│   ├── QUICKSTART.md            # Quick start guide
│   ├── SETUP.md                 # Setup instructions
│   ├── STRUCTURE.md             # This file
│   └── API.md                   # API reference
│
└── venv/                        # Virtual environment (not tracked)
    └── [python packages]
```

## File Descriptions

### Core Scripts

| File | Purpose | When to Run |
|------|---------|-----------|
| `ingest.py` | Indexes documents into vector DB | Once after adding/updating documents |
| `query.py` | Backend query engine | Used by ask_bot.py |
| `ask_bot.py` | Interactive chatbot | Whenever you want to ask questions |

### Data Files

| File | Format | Size |
|------|--------|------|
| `artificial_intelligence.txt` | Text | ~5KB |
| `data_science.txt` | Text | ~2.7KB |
| `machine_learning.txt` | Text | ~4.5KB |
| `python_guide.txt` | Text | ~3.2KB |
| `web_development.txt` | Text | ~5.4KB |

### Configuration Files

| File | Purpose |
|------|---------|
| `.env` | Local environment variables (API keys) |
| `.env.example` | Template for .env |
| `.gitignore` | Files to ignore in Git |
| `requirements.txt` | Python package dependencies |

### Directories

| Directory | Contents |
|-----------|----------|
| `data/` | Your document files for AI to learn from |
| `vector_db/` | Generated vector embeddings (auto-created) |
| `docs/` | Documentation and guides |
| `venv/` | Python virtual environment |

## Workflow

```
1. Add documents to data/ folder
   ↓
2. Run ingest.py (creates vector_db/)
   ↓
3. Run ask_bot.py to ask questions
   ↓
4. Get answers from your documents
```

## To Add More Documents

1. **Add file to `data/` folder:**
   - Use `.txt` format recommended
   - Name it clearly (e.g., `python_advanced.txt`)

2. **Re-index documents:**
   ```bash
   python ingest.py
   ```

3. **Ask questions:**
   ```bash
   python ask_bot.py "Your new question"
   ```

## Cleanup

- **Remove old vector database:** 
  ```bash
  Remove-Item -Recurse -Force vector_db
  ```

- **Clear Python cache:** 
  ```bash
  Remove-Item -Recurse -Force __pycache__
  ```

- **Reinstall packages:** 
  ```bash
  pip install -r requirements.txt --upgrade
  ```

## Storage Usage

- **Vector DB:** ~50-200 MB (depends on documents)
- **Virtual Environment:** ~500 MB
- **Project Code:** ~50 KB
- **Documents:** Depends on your files

Total: ~600 MB - 1 GB

## Performance

- **First run:** 30-60 seconds (downloads ML models)
- **Subsequent runs:** 5-15 seconds
- **Query response:** 2-5 seconds per question
