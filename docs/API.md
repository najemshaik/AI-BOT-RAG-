# API Reference

## query_documents()

Main function for querying the vector database.

### Syntax
```python
from query import query_documents

response = query_documents(query_text, k=3, use_llm=False)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query_text` | str | Required | Your question |
| `k` | int | 3 | Number of documents to retrieve |
| `use_llm` | bool | False | Use OpenAI LLM for synthesis |

### Returns

`str` - The answer or relevant document excerpts

### Example 1: Simple Query
```python
from query import query_documents

answer = query_documents("What is Python?")
print(answer)
```

### Example 2: Get More Documents
```python
# Retrieve 5 most relevant documents instead of 3
answer = query_documents("What is machine learning?", k=5)
print(answer)
```

### Example 3: With OpenAI LLM
```python
# Requires OPENAI_API_KEY in .env
answer = query_documents("Explain neural networks", use_llm=True)
print(answer)
```

## ask_bot.py Commands

### Command Line Usage
```bash
# Single question
python ask_bot.py "Your question here"

# Interactive mode
python ask_bot.py
```

### Examples
```bash
# Ask one question
python ask_bot.py "What is artificial intelligence?"

# Start interactive session
python ask_bot.py

# Then type questions:
# > What is Python?
# > How does machine learning work?
# > quit
```

## ingest.py

Indexes documents from the `data/` folder into Chroma vector database.

### Usage
```bash
python ingest.py
```

### Process
1. Loads all `.txt`, `.pdf`, `.docx` files from `data/`
2. Splits documents into 500-character chunks
3. Generates embeddings using HuggingFace
4. Stores in `vector_db/` directory

### Output
```
Step 1: Loading documents from data folder...
Step 2: Splitting documents into chunks...
Step 3: Creating embeddings...
Step 4: Creating Chroma vector database...
Step 5: SUCCESS - Vector database created!
Documents indexed successfully!
```

## Configuration

### Environment Variables (.env)

```env
# Optional: OpenAI API key for GPT synthesis
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx

# Optional: HuggingFace token for higher rate limits
HF_TOKEN=hf_xxxxxxxxxxxxx
```

### Tuning Parameters

Edit in `ingest.py`:
```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,        # Characters per chunk
    chunk_overlap=50       # Character overlap between chunks
)
```

Edit in `query.py`:
```python
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"  # Embedding model
)
```

## Performance Tips

### Faster Ingestion
- Keep documents smaller (< 1 MB each)
- Use `.txt` format instead of `.pdf`

### Better Answers
- Add more relevant documents
- Increase `k` parameter to retrieve more docs
- Use `use_llm=True` for synthesis (requires OpenAI)

### Reduce Memory Usage
- Decrease `chunk_size` in ingest.py
- Clear `vector_db/` and rebuild periodically

## Error Handling

### Common Errors

**Error: "Vector database not found"**
```bash
# Solution: Run ingestion first
python ingest.py
```

**Error: "No documents loaded"**
```bash
# Solution: Ensure data/ folder has .txt files
# Check: ls data/
```

**Error: "Module not found"**
```bash
# Solution: Install requirements
pip install -r requirements.txt
```

**Error: "Memory error"**
```bash
# Solution: Process smaller batches
# Or increase chunk_overlap in ingest.py
```

## Advanced Usage

### Custom Query Script
```python
from query import query_documents

questions = [
    "What is Python?",
    "Explain machine learning",
    "What are neural networks?"
]

for q in questions:
    print(f"Q: {q}")
    answer = query_documents(q, k=5)
    print(f"A: {answer}\n")
```

### Batch Processing
```python
import csv
from query import query_documents

# Read questions from CSV
with open('questions.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        question = row[0]
        answer = query_documents(question)
        print(f"{question} => {answer[:100]}...")
```

## Version Information

- Python: 3.10+
- LangChain: 1.2.15+
- Chroma: 1.5.8+
- HuggingFace: Latest

## Support

For issues or questions, refer to:
- QUICKSTART.md - Getting started
- SETUP.md - Installation help
- STRUCTURE.md - Project layout
