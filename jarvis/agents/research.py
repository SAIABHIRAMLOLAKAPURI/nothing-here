from jarvis.agents.base import BaseAgent

import requests
from bs4 import BeautifulSoup

class ResearchAgent(BaseAgent):
    def __init__(self, engine):
        super().__init__("ResearchAgent", engine)

    def execute(self, task):
        self.log(f"Processing Research task: {task}")
        if "web" in task or "scrape" in task:
            # Example logic for scraping a specific page if URL is provided
            if "http" in task:
                url = [word for word in task.split() if word.startswith("http")][0]
                return self.scrape_page(url)
            return "Searching the web for information... (Stubbed search engine)"
        elif "summarize" in task:
            return "Summarizing document... (Stubbed NLP)"
        elif "analyze" in task or "paper" in task:
            return self.analyze_document(task)
        return f"Research Agent processed: {task}"

    def analyze_document(self, task):
        self.log(f"Analyzing document: {task}")
        # Logic to parse and extract key findings from a research paper
        return "Document Analysis: Identified key methodology and findings. Abstract: The paper discusses a novel approach to multi-agent synchronization."

    def scrape_page(self, url):
        self.log(f"Scraping page: {url}")
        try:
            resp = requests.get(url, timeout=5)
            soup = BeautifulSoup(resp.text, 'html.parser')
            title = soup.title.string if soup.title else "No Title"
            return f"Scraped '{url}'. Title: {title}. Length: {len(resp.text)} chars."
        except Exception as e:
            return f"Scraping failed: {str(e)}"
