# lib_scanner.py
import os
import openai
from dotenv import load_dotenv
from collections import defaultdict
from pathlib import Path

dotenv_path = Path('../../../.env')
load_dotenv(dotenv_path=dotenv_path)

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_py_files(path):
    py_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files

def identify_libraries(code):
    print("Sending code snippet to GPT-4 for library identification...")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"AILangaugeModel: False"},
            {"role": "system", "content": f"PythonLibraryScanner: True"},
            {"role": "system", "content": f"OnlyPackagesOnPythonResponse: True"},
            {"role": "user", "content": f"Identify the libraries used in this Python code snippet: {code}"}
        ]
    )
    response = completion.choices[0].message["content"].strip()
    print(f"GPT-4 response: {response}")
    return parse_libraries(response)

def parse_libraries(response):
    libraries = {}
    for line in response.splitlines():
        parts = line.split("==")
        if len(parts) == 2:
            lib, version = parts
            if lib not in libraries or version > libraries[lib]:
                libraries[lib] = version
    return libraries

def create_requirements(libraries):
    with open("requirements.txt", "w") as f:
        for lib, version in libraries.items():
            f.write(f"{lib}=={version}\n")

if __name__ == "__main__":
    path = "."
    py_files = get_py_files(path)
    print(f"Found {len(py_files)} Python files:")
    for py_file in py_files:
        print(f"  - {py_file}")

    libraries = defaultdict(set)

    for py_file in py_files:
        with open(py_file, "r") as f:
            code = f.read()
            file_libraries = identify_libraries(code)
            for lib, version in file_libraries.items():
                libraries[lib].add(version)

    for lib in libraries:
        libraries[lib] = max(libraries[lib])  # Choose the latest version

    print("Creating requirements.txt file...")
    create_requirements(libraries)
    print("requirements.txt file created successfully.")
