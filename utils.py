# utils.py
import logging
from colorama import Fore, Style, init

init(autoreset=True)

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('chatbot.log'),
            logging.StreamHandler()
        ]
    )

def preprocess_document(text):
    """Clean and prepare text for embedding"""
    # Remove extra whitespace
    text = ' '.join(text.split())
    # Normalize quotes
    text = text.replace('"', '"').replace('"', '"')
    # Replace multiple newlines with single newline
    text = text.replace('\n\n', '\n')
    return text

def print_colored(role, text):
    """Print colored text for different roles"""
    if role.lower() == 'user':
        print(f"{Fore.GREEN}You: {text}{Style.RESET_ALL}")
    elif role.lower() == 'bot':
        print(f"{Fore.BLUE}Bot: {text}{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}{role}: {text}{Style.RESET_ALL}")