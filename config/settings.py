"""
Configuration settings for Numa AI Assistant
"""

# Ollama Configuration
OLLAMA_BASE_URL = "http://172.20.160.1:11435"
DEFAULT_MODEL = "mistral"

# API Endpoints
OLLAMA_GENERATE_ENDPOINT = "/api/generate"

# Request Configuration
REQUEST_TIMEOUT = 60  # seconds - increased for WSL setup and longer LLM responses
MAX_RETRIES = 3 