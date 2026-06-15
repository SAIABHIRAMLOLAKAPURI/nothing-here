# Use Python base image
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    openjdk-17-jdk-headless \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Compile Java agents
RUN javac -d jarvis/agents/java jarvis/agents/java/*.java

# Train the model
RUN python3 jarvis/core/trainer.py

# Expose port
EXPOSE 5000

# Command to run the application
CMD ["python3", "jarvis/interface/server.py"]
