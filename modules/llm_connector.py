"""
LLM Connector Module for Numa AI Assistant
Handles communication with Ollama running locally
"""

import json
import requests
from typing import Optional
import sys
import os

# Add the parent directory to the path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import (
    OLLAMA_BASE_URL,
    DEFAULT_MODEL,
    OLLAMA_GENERATE_ENDPOINT,
    REQUEST_TIMEOUT,
    MAX_RETRIES
)


class OllamaConnector:
    """Handles communication with Ollama API"""
    
    def __init__(self, model: str = DEFAULT_MODEL):
        self.model = model
        self.base_url = OLLAMA_BASE_URL
        self.generate_url = f"{self.base_url}{OLLAMA_GENERATE_ENDPOINT}"
    
    def _make_request(self, prompt: str) -> Optional[str]:
        """Make a request to Ollama API"""
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        
        headers = {
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(
                self.generate_url,
                json=payload,
                headers=headers,
                timeout=REQUEST_TIMEOUT
            )
            response.raise_for_status()
            
            result = response.json()
            return result.get("response", "")
            
        except requests.exceptions.Timeout:
            print(f"Request timed out after {REQUEST_TIMEOUT} seconds. The LLM might be processing a complex request.")
            return None
        except requests.exceptions.ConnectionError:
            print(f"Connection error: Could not connect to Ollama at {self.base_url}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to Ollama: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing response: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
    
    def ask(self, prompt: str) -> str:
        """Send a prompt to the LLM and return the response"""
        response = self._make_request(prompt)
        
        if response is None:
            return (
                "Sorry, I couldn't connect to the LLM. Please check:\n"
                "1. Ollama is running on your Windows machine\n"
                "2. The reverse proxy is active at http://172.20.160.1:11435\n"
                "3. The mistral model is pulled: 'ollama pull mistral'\n"
                "4. Your network connection is stable"
            )
        
        return response


# Global connector instance
_connector = None


def get_connector() -> OllamaConnector:
    """Get or create the global connector instance"""
    global _connector
    if _connector is None:
        _connector = OllamaConnector()
    return _connector


def ask_numa(prompt: str) -> str:
    """
    Main function to ask Numa a question
    
    Args:
        prompt (str): The question or prompt to send to the LLM
        
    Returns:
        str: The LLM's response or a helpful error message
    """
    connector = get_connector()
    return connector.ask(prompt) 