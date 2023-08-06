#!/usr/bin/env python3
import os
import sys

def chat_interface():
    print("Welcome to the Python file runner setup!")
    file = input("Enter the path to the Python file you want to run: ")
    dev_mode = input("Do you want to run in development mode? (y/n): ").lower() == 'y'

    return file, dev_mode

def create_setup_file(file, dev_mode):
    with open("setup.py", "w") as f:
        f.write("#!/usr/bin/env python3\n")
        f.write("import subprocess\n\n")
        f.write("def main():\n")
        python_command = "python3" if dev_mode else "python"
        f.write(f"    subprocess.run(['{python_command}', '{file}'])\n\n")
        f.write("if __name__ == '__main__':\n")
        f.write("    main()\n")
    os.chmod("setup.py", 0o755)

def main():
    file, dev_mode = chat_interface()
    
    if not os.path.isfile(file):
        print(f"Error: '{file}' not found.")
        sys.exit(1)

    create_setup_file(file, dev_mode)
    print("Setup file 'setup.py' created successfully. Other users can now run the script using 'python3 setup.py'")

if __name__ == "__main__":
    main()
