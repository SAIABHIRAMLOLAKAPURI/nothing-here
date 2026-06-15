# JARVIS - AI Personal Assistant

JARVIS is a modular AI assistant that combines Python and Java for a powerful multi-agent experience.

## Features
- **Multi-Agent Architecture**: Specialized agents for AI creation, automation, research, trading, and freelancing.
- **Cross-Language Support**: Seamlessly executes Java agents from a Python core.
- **Web Interface**: Iron Man-inspired HUD for interaction.
- **Self-Modification**: Capability to read and update its own source code.

## Setup & Installation

### Option 1: Standard Installation
1. **Clone the repository** (if applicable) and navigate to the root directory.
2. **Install Python dependencies**:
   - **Windows**:
     ```powershell
     python -m pip install -r requirements.txt
     ```
   - **Linux/macOS**:
     ```bash
     python3 -m pip install -r requirements.txt
     ```
3. **Install Java JDK** (version 17 or higher):
   - Ensure `javac` is in your PATH.

### Option 2: Docker (Recommended)
1. **Build and run using Docker Compose**:
   ```bash
   docker-compose up --build
   ```

## Running JARVIS

### Using the Application Wrapper (Simplest)
The `app.py` script automatically trains the intent model, compiles Java agents, and starts the backend.
- **Windows**: `python app.py`
- **Linux/macOS**: `python3 app.py`

### Option 3: Building a Standalone Executable (.exe)
You can create a standalone executable for easier distribution:
1. **Install requirements**: `pip install -r requirements.txt`
2. **Run the build script**:
   ```bash
   python build_exe.py
   ```
3. The executable will be generated in the `dist/` directory.

### Manual Launch
If you prefer manual steps:
1. **Train the AI Model**:
   ```bash
   python jarvis/core/trainer.py
   ```
2. **Compile Java Agents**:
   ```bash
   javac -d jarvis/agents/java jarvis/agents/java/*.java
   ```
3. **Start the Backend**:
   ```bash
   PYTHONPATH=. python jarvis/interface/server.py
   ```

## Accessing the Interface
Once the server is running (at `http://localhost:5000`):
- Open `jarvis/interface/index.html` directly in your web browser.
- Or navigate to `http://localhost:5000` if the server is serving static files.

### Security Note
The application uses a static API token for communication between the frontend and backend.
- **Default Token**: `jarvis_secure_token_2026`
- This is configured in `jarvis/interface/server.py` and `jarvis/interface/index.html`.

### Troubleshooting (Windows)
If you get `ModuleNotFoundError` after installing requirements:
1. Ensure you are using the same Python executable for both installation and running.
2. Use `python -m pip install` instead of just `pip install`.
3. Try running with `python app.py`.

## Testing
Run tests using pytest:
```bash
pytest
```
