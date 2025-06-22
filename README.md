# 🤖 Numa - Personal AI Assistant

A privacy-focused, modular AI assistant that runs locally using Ollama. Numa provides intelligent assistance through natural language interaction while keeping all your data private and secure.

## ✨ Features

- **🔒 Privacy First**: All processing happens locally via Ollama
- **🧩 Modular Design**: Easy to extend with new capabilities
- **💬 Natural Interaction**: Simple terminal-based chat interface
- **⚙️ Configurable**: Easy to customize models and settings
- **🚀 Future-Ready**: Built for advanced features like memory, news digest, and more

## 🏗️ Architecture

Numa is built with a clean, modular architecture:

```
numa/
├── main.py                 # Entry point and terminal interface
├── config/
│   └── settings.py        # Configuration management
├── modules/
│   └── llm_connector.py   # Ollama API integration
├── docs/
│   └── architecture.md    # Detailed architecture documentation
└── requirements.txt       # Python dependencies
```

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+** installed on your system
2. **Ollama** installed and running locally
3. **Mistral model** pulled in Ollama

### Installation

1. **Clone or download** this repository
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Ensure Ollama is running**:
   ```bash
   ollama serve
   ```
4. **Pull the Mistral model** (if not already done):
   ```bash
   ollama pull mistral
   ```

### Usage

Run Numa with:
```bash
python main.py
```

Then start chatting! Type your questions and Numa will respond using the local LLM.

## 💬 Example Interactions

```
🤖 You: What's the weather like today?
🤔 Numa is thinking...
🤖 Numa: I don't have access to real-time weather data, but I can help you find weather information! You can check weather apps, websites like weather.com, or ask your device's weather app for current conditions in your area.

🤖 You: Help me plan my day
🤔 Numa is thinking...
🤖 Numa: I'd be happy to help you plan your day! To give you the best suggestions, could you tell me:
- What time you're starting your day
- Any specific tasks or goals you have
- Whether you prefer a structured schedule or flexible planning
- Any time constraints or appointments

This will help me create a personalized daily plan for you!
```

## ⚙️ Configuration

Edit `config/settings.py` to customize:

- **Model**: Change the default LLM model
- **Server URL**: Modify Ollama server address
- **Timeouts**: Adjust request timeouts
- **Retry settings**: Configure retry behavior

```python
# Example configuration
OLLAMA_BASE_URL = "http://localhost:11434"
DEFAULT_MODEL = "mistral"  # or "llama2", "codellama", etc.
REQUEST_TIMEOUT = 30
```

## 🔧 Available Commands

- **Type your question**: Ask anything and get AI-powered responses
- **`help`**: Show available commands and tips
- **`exit`**, **`quit`**, **`bye`**: Close Numa

## 🛠️ Development

### Project Structure

- **`main.py`**: Terminal interface and main application loop
- **`modules/llm_connector.py`**: Ollama API integration with error handling
- **`config/settings.py`**: Centralized configuration management
- **`docs/architecture.md`**: Detailed technical documentation

### Adding New Features

The modular design makes it easy to extend Numa:

1. Create new modules in the `modules/` directory
2. Follow the established patterns in `llm_connector.py`
3. Update configuration in `config/settings.py` if needed
4. Document new features in `docs/architecture.md`

## 🔮 Future Features

Numa is designed for expansion. Planned modules include:

- **📝 Chat History**: Conversation memory and context
- **📰 News Digest**: Automated news summarization
- **🧠 Note Memory**: Knowledge management and retrieval
- **🤔 Decision Helper**: Structured decision-making assistance
- **📱 Telegram Bot**: Mobile interface via Telegram
- **💾 Memory System**: Long-term learning and personalization

## 🛡️ Privacy & Security

- **Local Processing**: All AI processing happens on your machine
- **No Data Collection**: No information is sent to external services
- **Configurable**: Full control over models and settings
- **Open Source**: Transparent codebase for security review

## 🤝 Contributing

Contributions are welcome! Please:

1. Follow the existing code style and patterns
2. Add tests for new functionality
3. Update documentation for new features
4. Ensure all code runs locally with Ollama

## 📄 License

This project is open source. See the repository for license details.

## 🆘 Troubleshooting

### Common Issues

**"Error connecting to Ollama"**
- Ensure Ollama is running: `ollama serve`
- Check if the model is pulled: `ollama list`
- Verify the server URL in `config/settings.py`

**"Model not found"**
- Pull the required model: `ollama pull mistral`
- Check available models: `ollama list`

**Import errors**
- Install dependencies: `pip install -r requirements.txt`
- Ensure you're in the correct directory

### Getting Help

- Check the [architecture documentation](docs/architecture.md) for technical details
- Ensure Ollama is properly installed and running
- Verify your Python environment and dependencies

---

**Happy chatting with Numa! 🤖✨** 