from collections import defaultdict
from core.lib.lib_scanner.scan import get_py_files, identify_libraries, create_requirements

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
