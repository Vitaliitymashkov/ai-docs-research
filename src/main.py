import os
import sys
from pathlib import Path


project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))
# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.agent import FileSearchAgent


def get_user_input() -> str:
    """Get user input for the search query and directory."""
    print("\nWelcome to the File Search Assistant! 🌟")
    return input("Enter your search query: ").strip()

def display_search_results(query: str, results: str) -> None:
    """Display the search results to the user."""
    print(f"\nSearch Results for a query: {query}")
    print("="*48)
    print(results)
    print("="*48)

def main():
    agent = FileSearchAgent()

    while True:
        query = get_user_input()
        if not query:
            print("No query provided. Exiting the search assistant.")
            break
        
        directory = './files'
        
        if not os.path.exists(directory):
            print(f"The directory '{directory}' does not exist. Please try again.")
            continue
        
        results = agent.search(query, directory)
        display_search_results(query, results)

        if input("\nDo you want to perform another search? (yes/no): ").strip().lower() != 'yes':
            print("Thank you for using the File Search Assistant! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()  
# This script is the main entry point for the file search assistant application.
# It initializes the agent and handles user interactions.

