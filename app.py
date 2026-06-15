import os
import sys
import subprocess

def launch():
    print("Launching JARVIS App...")
    # Ensure model is trained
    if not os.path.exists("jarvis/data/intent_model.pkl"):
        print("Training intent model...")
        subprocess.run([sys.executable, "jarvis/core/trainer.py"])

    # Compile Java
    print("Compiling Java agents...")
    subprocess.run(["javac", "-d", "jarvis/agents/java", "jarvis/agents/java/FreelancingAgent.java", "jarvis/agents/java/TradingAgent.java"])

    # Run server
    print("Starting backend server...")
    env = os.environ.copy()
    env["PYTHONPATH"] = os.getcwd()
    subprocess.run([sys.executable, "jarvis/interface/server.py"], env=env)

if __name__ == "__main__":
    launch()
