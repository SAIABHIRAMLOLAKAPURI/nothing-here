import json
import os

class JarvisMemory:
    def __init__(self, storage_path="jarvis/data/memory/"):
        self.storage_path = storage_path
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)

        self.short_term = []
        self.long_term_file = os.path.join(self.storage_path, "long_term.json")
        self.long_term = self._load_long_term()

    def _load_long_term(self):
        if os.path.exists(self.long_term_file):
            with open(self.long_term_file, 'r') as f:
                return json.load(f)
        return {"projects": {}, "preferences": {}, "knowledge": {}}

    def save_long_term(self):
        with open(self.long_term_file, 'w') as f:
            json.dump(self.long_term, f, indent=4)

    def add_to_short_term(self, interaction):
        self.short_term.append(interaction)
        # Keep last 10 interactions for context
        if len(self.short_term) > 10:
            self.short_term.pop(0)

    def store_knowledge(self, key, value):
        self.long_term["knowledge"][key] = value
        self.save_long_term()

    def get_knowledge(self, key):
        return self.long_term["knowledge"].get(key)

    def store_project_data(self, project_name, data):
        self.long_term["projects"][project_name] = data
        self.save_long_term()

    def get_project_data(self, project_name):
        return self.long_term["projects"].get(project_name)

    def set_preference(self, key, value):
        self.long_term["preferences"][key] = value
        self.save_long_term()

    def get_preference(self, key):
        return self.long_term["preferences"].get(key)
