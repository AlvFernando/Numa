# Numa AI Assistant - Architecture Documentation

## Overview

**Numa** is a personal AI assistant designed to provide intelligent, context-aware assistance through natural language interaction. Built with modularity in mind, Numa leverages local LLM capabilities via Ollama to ensure privacy and offline functionality.

## Core Philosophy

- **Privacy First**: All processing happens locally using Ollama
- **Modular Design**: Easy to extend with new capabilities
- **User-Friendly**: Simple, intuitive interface
- **Extensible**: Built for future enhancements

## Current Architecture

### Core Components

```
numa/
├── main.py                 # Entry point and terminal interface
├── config/
│   └── settings.py        # Configuration management
├── modules/
│   └── llm_connector.py   # Ollama API integration
├── docs/
│   └── architecture.md    # This documentation
└── requirements.txt       # Python dependencies
```

### Module Descriptions

#### 1. **LLM Connector** (`modules/llm_connector.py`)
- **Purpose**: Handles communication with Ollama API
- **Key Functions**:
  - `ask_numa(prompt: str) -> str`: Main interface for LLM queries
  - `OllamaConnector`: Manages API connections and requests
- **Features**:
  - Configurable model selection
  - Error handling and retry logic
  - Connection timeout management

#### 2. **Configuration** (`config/settings.py`)
- **Purpose**: Centralized configuration management
- **Configurable Items**:
  - Ollama server URL
  - Default model selection
  - API endpoints
  - Request timeouts

#### 3. **Main Interface** (`main.py`)
- **Purpose**: Terminal-based user interface
- **Features**:
  - Interactive chat loop
  - Command handling (exit, help)
  - User-friendly prompts and responses
  - Error handling

## Planned Modules (Future Development)

### 1. **Chat Module** (`modules/chat.py`)
- **Purpose**: Enhanced conversation management
- **Features**:
  - Conversation history
- Context management
- Multi-turn dialogue support
- Conversation export/import

### 2. **News Digest Module** (`modules/news_digest.py`)
- **Purpose**: Automated news summarization and curation
- **Features**:
  - RSS feed integration
  - Topic-based filtering
  - Summary generation
  - Reading list management

### 3. **Note Memory Module** (`modules/note_memory.py`)
- **Purpose**: Persistent memory and knowledge management
- **Features**:
  - Note taking and organization
  - Semantic search
  - Knowledge graph integration
  - Memory retrieval and context

### 4. **Decision Helper Module** (`modules/decision_helper.py`)
- **Purpose**: Structured decision-making assistance
- **Features**:
  - Pros/cons analysis
  - Decision frameworks
  - Risk assessment
  - Action planning

### 5. **Telegram Interface** (`modules/telegram_bot.py`)
- **Purpose**: Mobile and remote access via Telegram
- **Features**:
  - Bot integration
  - Voice message support
  - Quick commands
  - Notification system

### 6. **Memory System** (`modules/memory.py`)
- **Purpose**: Long-term memory and learning
- **Features**:
  - User preference learning
  - Conversation memory
  - Personalization
  - Adaptive responses

## Technical Stack

### Backend
- **Language**: Python 3.8+
- **LLM Integration**: Ollama (local)
- **HTTP Client**: Requests library
- **Configuration**: Python settings module

### Dependencies
- `requests`: HTTP API communication
- `typing-extensions`: Enhanced type hints

## Development Roadmap

### Phase 1: Core Foundation ✅
- [x] Basic LLM integration
- [x] Terminal interface
- [x] Configuration system
- [x] Modular architecture

### Phase 2: Enhanced Features (Planned)
- [ ] Chat history and context
- [ ] Note-taking capabilities
- [ ] Basic memory system
- [ ] Improved error handling

### Phase 3: Advanced Features (Future)
- [ ] Telegram bot interface
- [ ] News digest functionality
- [ ] Decision helper tools
- [ ] Advanced memory and learning

### Phase 4: Integration & Polish (Future)
- [ ] Web interface
- [ ] Mobile app
- [ ] Plugin system
- [ ] Performance optimization

## Getting Started

1. **Prerequisites**:
   - Python 3.8+
   - Ollama installed and running
   - Mistral model pulled (`ollama pull mistral`)

2. **Installation**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Usage**:
   ```bash
   python main.py
   ```

## Contributing

The modular architecture makes it easy to add new features:

1. Create new modules in the `modules/` directory
2. Follow the established patterns in `llm_connector.py`
3. Update this documentation
4. Add tests for new functionality

## Security & Privacy

- All processing happens locally via Ollama
- No data is sent to external services
- Configuration can be customized for different environments
- Future modules will maintain the privacy-first approach 