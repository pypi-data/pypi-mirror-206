#!/usr/bin/env python3
import os
import sys

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
