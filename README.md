# RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built using LangChain and HuggingFace models. This chatbot can understand and answer questions based on your custom knowledge base.

## Features

- Custom knowledge base integration
- Retrieval-augmented responses
- Conversation memory
- Colored console interface
- Logging system
- Error handling

## Prerequisites

- Python 3.8 or higher
- HuggingFace account and API token
- At least 8GB RAM recommended

## Project Structure

```
project/
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
├── config.py              # Configuration settings
├── utils.py               # Utility functions
├── chatbot.py             # Main chatbot class
├── main.py                # Entry point
├── test_chatbot.py        # Tests
└── knowledge_base/        # Your documents
    ├── company_info.txt
    ├── product_faq.txt
    └── technical_docs.txt
```

## Installation

1. Clone the repository:
```bash
git clone [your-repo-url]
cd [your-repo-name]
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up HuggingFace token:
   - Go to https://huggingface.co/settings/tokens
   - Create a new token with Inference API permission
   - Create `.env` file and add:
```
HUGGINGFACEHUB_API_TOKEN=hf_your_token_here
```

## Knowledge Base Setup

1. Create a `knowledge_base` directory
2. Add your .txt files with content
3. Format requirements:
   - UTF-8 encoding
   - Plain text (.txt) files
   - Clear, well-structured content

Example document structure:
```text
Title: [Document Title]

[Main content goes here...]

Key Points:
1. [Point 1]
2. [Point 2]

Additional Information:
- [Detail 1]
- [Detail 2]
```

## Usage

1. Start the chatbot:
```bash
python main.py
```

2. Interact with the chatbot:
   - Type your questions
   - Type 'quit' to exit
   - Wait for the bot's responses

Example queries:
```
You: What is TechCorp Solutions?
Bot: [Response based on knowledge base]

You: Tell me about the AI Analytics Suite
Bot: [Response about the product]
```

## Configuration

Modify `config.py` to adjust:
- Embedding model
- Language model
- Chunk size
- Temperature
- Maximum response length

```python
MODEL_CONFIG = {
    "embedding_model": "sentence-transformers/all-mpnet-base-v2",
    "llm_model": "google/flan-t5-base",
    "chunk_size": 1000,
    "chunk_overlap": 200,
    "temperature": 0.5,
    "max_length": 512
}
```

## Adding New Documents

1. Add .txt files to the knowledge_base directory
2. Files are automatically loaded on startup
3. Format: UTF-8 encoded text files

## Testing

Run the test suite:
```bash
python -m unittest test_chatbot.py
```

## Logging

- Logs are written to `chatbot.log`
- Includes INFO and ERROR level messages
- Timestamps and component information

## Troubleshooting

1. Token Error:
   - Verify token starts with "hf_"
   - Check .env file format
   - Ensure token has Inference API permission

2. Memory Issues:
   - Reduce chunk size in config.py
   - Process smaller documents
   - Use lighter embedding model

3. Dependencies:
   - Update requirements: `pip install -r requirements.txt`
   - Check Python version compatibility
   - Verify virtual environment activation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License

[Your chosen license]

## Acknowledgments

- LangChain for the framework
- HuggingFace for models and API
- FAISS for vector storage