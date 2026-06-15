# JARVIS - AI Personal Assistant

JARVIS is a modular AI assistant that combines Python and Java for a powerful multi-agent experience.

## Features
- **Multi-Agent Architecture**: Specialized agents for AI creation, automation, research, trading, and freelancing.
- **Cross-Language Support**: Seamlessly executes Java agents from a Python core.
- **Web Interface**: Iron Man-inspired HUD for interaction.
- **Self-Modification**: Capability to read and update its own source code.

## Setup
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Compile Java agents:
   ```bash
   javac -d jarvis/agents/java jarvis/agents/java/*.java
   ```

## Running JARVIS
Start the backend server:
```bash
python jarvis/interface/server.py
```
Then open `jarvis/interface/index.html` in your browser.

## Testing
Run tests using pytest:
```bash
pytest
```
