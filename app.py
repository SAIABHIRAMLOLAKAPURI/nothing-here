import os
import sys
import subprocess

def check_dependencies():
    required = ["flask", "flask_cors", "psutil", "bs4", "requests", "pandas", "sklearn", "joblib"]
    missing = []
    for lib in required:
        try:
            __import__(lib)
        except ImportError:
            missing.append(lib)

    if missing:
        print(f"Error: Missing dependencies: {', '.join(missing)}")
        print(f"Please run: {sys.executable} -m pip install -r requirements.txt")
        sys.exit(1)

def launch():
    check_dependencies()
    print("Launching JARVIS App...")
    # Ensure model is trained
    if not os.path.exists("jarvis/data/intent_model.pkl"):
        print("Training intent model...")
        subprocess.run([sys.executable, "jarvis/core/trainer.py"])

    # Compile Java
    print("Compiling Java agents...")
    java_files = [
        os.path.join("jarvis", "agents", "java", "FreelancingAgent.java"),
        os.path.join("jarvis", "agents", "java", "TradingAgent.java")
    ]
    output_dir = os.path.join("jarvis", "agents", "java")
    subprocess.run(["javac", "-d", output_dir] + java_files)

    # Run server
    print("Starting backend server...")
    env = os.environ.copy()
    env["PYTHONPATH"] = os.getcwd()
    subprocess.run([sys.executable, "jarvis/interface/server.py"], env=env)

if __name__ == "__main__":
    launch()
