"""
Configuration settings for Numa AI Assistant
"""

# Ollama Configuration
OLLAMA_HOST = "http://172.20.160.1:11435"
DEFAULT_MODEL = "mistral"

# API Endpoints
OLLAMA_GENERATE_ENDPOINT = "/api/generate"

# Request Configuration
REQUEST_TIMEOUT = 30  # seconds
MAX_RETRIES = 3 