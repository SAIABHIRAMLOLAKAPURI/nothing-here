import os
import sys
import subprocess
import threading
import time
import webview

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

def run_backend():
    print("Starting backend server...")
    env = os.environ.copy()
    env["PYTHONPATH"] = os.getcwd()
    # Using python -m tejodaya.interface.server or similar if needed,
    # but here we just call the script.
    server_path = os.path.join("tejodaya", "interface", "server.py")
    subprocess.run([sys.executable, server_path], env=env)

def launch():
    check_dependencies()
    print("Launching Tejodaya App...")

    # Setup
    if not os.path.exists("tejodaya/data/intent_model.pkl"):
        subprocess.run([sys.executable, "tejodaya/core/trainer.py"])

    java_files = [
        os.path.join("tejodaya", "agents", "java", "FreelancingAgent.java"),
        os.path.join("tejodaya", "agents", "java", "TradingAgent.java")
    ]
    subprocess.run(["javac", "-d", os.path.join("tejodaya", "agents", "java")] + java_files)

    # Start Backend in thread
    t = threading.Thread(target=run_backend, daemon=True)
    t.start()

    # Give server time to start
    time.sleep(2)

    # Launch Native Window
    print("Opening Tejodaya HUD...")
    webview.create_window('Tejodaya HUD', 'http://localhost:5000', width=1200, height=800)
    webview.start()

if __name__ == "__main__":
    launch()
