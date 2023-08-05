import os
import openai
import re
from termcolor import colored
import subprocess
import time

from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")


def read_specifications():
    with open("specifications.txt", "r") as spec_file:
        specifications = spec_file.read()
    return specifications

def extract_files_to_generate(specifications):
    file_list_pattern = re.compile(r'-\s(.*\.(tsx|html))', re.MULTILINE)
    files_to_generate = file_list_pattern.findall(specifications)
    return [file[0] for file in files_to_generate]

def generate_code(filename, specifications):
    extension = filename.split('.')[-1]
    prompt = f"Create a {extension.upper()} file named {filename} for a web portfolio for Jaseunda, as described in the following specifications. Generate only pure code, without comments or additional information:\n\n"

    prompt += specifications

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return response['choices'][0]['message']['content'].strip()

def run_project():
    cmd = ["npm", "start"]
    process = subprocess.Popen(cmd, cwd=project_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    return process

def fix_code_errors():
    pass

def check_errors(process):
    error_pattern = re.compile(r'Error', re.IGNORECASE)

    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
            if error_pattern.search(output.strip()):
                process.terminate()
                return True
    return False
specifications = read_specifications()
files_to_generate = extract_files_to_generate(specifications)
project_dir = "temp"
if not os.path.exists(project_dir):
    os.mkdir(project_dir)
    print(colored("Creating project directory...", "green"))
subprocess.run(["npx", "create-react-app", project_dir, "--template", "typescript"])
subprocess.run(["npm", "install", "-D", "tailwindcss@latest", "postcss@latest", "autoprefixer@latest"], cwd=project_dir)
os.makedirs(os.path.join(project_dir, "src", "components"), exist_ok=True)
for filename in files_to_generate:
    print(colored(f"Generating code for {filename}...", "yellow"))
    code = generate_code(filename, specifications)
    with open(os.path.join(project_dir, "src", filename), "w") as file:
        file.write(code)
    print(colored(f"{filename} created successfully.", "green"))

print(colored("Web portfolio generation completed.", "green"))
while True:
    process = run_project()
    time.sleep(5)  # Wait for a few seconds for the project to run and check for errors

    errors_exist = check_errors(process)

    if errors_exist:
        fix_code_errors()
    else:
        break
