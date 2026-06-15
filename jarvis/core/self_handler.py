import os

class SelfHandler:
    def __init__(self, base_dir="."):
        self.base_dir = base_dir

    def read_source(self, relative_path):
        full_path = os.path.join(self.base_dir, relative_path)
        if os.path.exists(full_path):
            with open(full_path, 'r') as f:
                return f.read()
        return None

    def update_source(self, relative_path, new_content):
        full_path = os.path.join(self.base_dir, relative_path)
        # In a real JARVIS, we'd have safety checks, backups, and possibly a git commit
        with open(full_path, 'w') as f:
            f.write(new_content)
        return f"Updated {relative_path} successfully."

    def list_source_files(self):
        source_files = []
        for root, dirs, files in os.walk(self.base_dir):
            for file in files:
                if file.endswith(('.py', '.java', '.html', '.css', '.js')):
                    source_files.append(os.path.relpath(os.path.join(root, file), self.base_dir))
        return source_files
