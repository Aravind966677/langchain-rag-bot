# main.py
from chatbot import RAGChatbot
from utils import print_colored
from colorama import Fore, Style

def main():
    # Set up the chatbot
    try:
        chatbot = RAGChatbot(docs_dir="./knowledge_base")
        print_colored("System", "Chatbot initialized. Type 'quit' to exit.")
        
        # Interactive chat loop
        while True:
            # Get user input
            user_input = input(f"{Fore.GREEN}You: {Style.RESET_ALL}")
            
            # Check for exit command
            if user_input.lower() == 'quit':
                print_colored("System", "Goodbye!")
                break
            
            # Get and print response
            response = chatbot.chat(user_input)
            print_colored("Bot", response)
            
    except Exception as e:
        print_colored("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()