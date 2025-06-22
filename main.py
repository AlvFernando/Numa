#!/usr/bin/env python3
"""
Numa AI Assistant - Main Entry Point
A personal AI assistant powered by Ollama
"""

import sys
import os

# Add the current directory to the path to import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.llm_connector import ask_numa


def print_banner():
    """Print the Numa banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║                    🤖 NUMA AI ASSISTANT 🤖                   ║
    ║                                                              ║
    ║              Your Personal AI Assistant                      ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_help():
    """Print help information"""
    help_text = """
    💡 Available Commands:
    • Type your question or request and press Enter
    • Type 'exit' or 'quit' to close Numa
    • Type 'help' to show this message
    
    🚀 Getting Started:
    • Ask me anything: "What's the weather like?"
    • Get help with tasks: "Help me plan my day"
    • Ask for explanations: "Explain quantum computing"
    
    ⚠️  Make sure Ollama is running with the mistral model loaded!
    """
    print(help_text)


def main():
    """Main application loop"""
    print_banner()
    print_help()
    
    print("\n" + "="*60)
    print("Numa is ready! Start chatting...")
    print("="*60 + "\n")
    
    while True:
        try:
            # Get user input
            user_input = input("🤖 You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\n👋 Goodbye! Thanks for using Numa!")
                break
            
            # Check for help command
            if user_input.lower() == 'help':
                print_help()
                continue
            
            # Skip empty input
            if not user_input:
                continue
            
            # Get response from Numa
            print("🤔 Numa is thinking...")
            response = ask_numa(user_input)
            
            # Print response
            print(f"\n🤖 Numa: {response}\n")
            print("-" * 60)
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Thanks for using Numa!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            print("Please try again or type 'exit' to quit.\n")


if __name__ == "__main__":
    main()
