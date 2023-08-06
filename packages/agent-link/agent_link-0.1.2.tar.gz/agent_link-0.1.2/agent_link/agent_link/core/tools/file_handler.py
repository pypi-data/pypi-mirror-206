import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class EnvFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        self.check_and_add_to_gitignore(event.src_path)

    def check_and_add_to_gitignore(self, file_path):
        gitignore_path = '.gitignore'
        file_path = os.path.relpath(file_path)

        if not os.path.isfile(gitignore_path):
            open(gitignore_path, 'w').close()

        with open(gitignore_path, 'r') as gitignore_file:
            gitignore_lines = gitignore_file.readlines()

        if f"{file_path}\n" not in gitignore_lines:
            with open(gitignore_path, 'a') as gitignore_file:
                gitignore_file.write(f"{file_path}\n")
            print(f"Added {file_path} to .gitignore")

    def check_existing_files(self, start_path="."):
        for root, _, files in os.walk(start_path):
            for file in files:
                if file.endswith(".env") or os.path.basename(file) in ["node_modules", "dist", "__pycache__"]:
                    self.check_and_add_to_gitignore(os.path.join(root, file))
