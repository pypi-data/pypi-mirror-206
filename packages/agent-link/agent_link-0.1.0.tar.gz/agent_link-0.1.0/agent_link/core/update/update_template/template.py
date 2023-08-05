import os 
import shutil
import pathspec
import subprocess
from core.gen.react_tailwind_typescript.create import create_react_app_with_tailwind_typescript

TEMPLATE_DIR = "../../../template"
TEMPLATE_ZIP_FILE = "../../../template.zip"

def update_template():
    if os.path.exists(TEMPLATE_DIR):
        shutil.rmtree(TEMPLATE_DIR)

    create_react_app_with_tailwind_typescript(TEMPLATE_DIR)
    with open(os.path.join(TEMPLATE_DIR, ".gitignore"), "r") as gitignore_file:
        gitignore_content = gitignore_file.read()
    gitignore_spec = pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, gitignore_content.splitlines())
    def is_ignored(file_path):
        return gitignore_spec.match_file(file_path)
    with open(TEMPLATE_ZIP_FILE, "wb") as zip_file:
        process = subprocess.Popen(["tar", "-c", "--use-compress-program", "lz4", "-C", TEMPLATE_DIR] + [file for file in os.listdir(TEMPLATE_DIR) if not is_ignored(file)], stdout=subprocess.PIPE)
        zip_file.write(process.communicate()[0])