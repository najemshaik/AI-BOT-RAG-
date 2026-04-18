# Setup Guide

## System Requirements
- Windows 10+
- Python 3.10 or higher
- 2 GB Free RAM
- 500 MB Free Disk Space

## Step-by-Step Setup

### Step 1: Download Project
Already done! Your project is at:
```
C:\Users\NAZIM\OneDrive\Desktop\AI Bot
```

### Step 2: Activate Virtual Environment
```powershell
cd 'C:\Users\NAZIM\OneDrive\Desktop\AI Bot'
.\venv\Scripts\Activate.ps1
```

You should see `(venv)` at the start of your terminal.

### Step 3: Verify Installation
```bash
pip list
```

Should show: langchain, langchain-community, chromadb, sentence-transformers, etc.

### Step 4: First Run - Index Documents
```bash
python ingest.py
```

Expected output:
```
Step 1: Loading documents from data folder...
[OK] Loaded: ...
Step 5: SUCCESS - Vector database created!
```

### Step 5: Test the Bot
```bash
python ask_bot.py "What is Python?"
```

## Troubleshooting

### Issue: Module not found
**Solution:** Reinstall requirements
```bash
pip install -r requirements.txt
```

### Issue: Vector database error
**Solution:** Rebuild the database
```bash
Remove-Item -Recurse -Force .\vector_db
python ingest.py
```

### Issue: "No such file or directory"
**Solution:** Make sure you're in the correct folder
```bash
cd 'C:\Users\NAZIM\OneDrive\Desktop\AI Bot'
```

## Configuration

### Add More Documents
1. Place documents in `data/` folder (.txt files)
2. Run: `python ingest.py`
3. Your AI Bot will automatically learn from new documents

### Supported File Formats
- `.txt` - Text files
- `.pdf` - PDF files (if properly formatted)
- `.docx` - Word documents

### Using OpenAI (Optional)
To use GPT-3.5 for better responses:
1. Add your OpenAI API key to `.env`
2. Modify query.py to set `use_llm=True`
