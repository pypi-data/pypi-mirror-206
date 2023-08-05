import argparse
import re

def remove_comments(filename):
    with open(filename, "r") as f:

        contents = f.read()
        
        contents = re.sub(r'(?m)^\s*#.*\n?', '', contents)

        contents = re.sub(r'\n\s*""".*?"""', '', contents, flags=re.DOTALL)
        
    with open(filename, "w") as f:
        f.write(contents)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove comments from a Python file")
    
    parser.add_argument("filename", type=str, help="the name of the file to remove comments from")
    
    args = parser.parse_args()
    
    remove_comments(args.filename)
    
    print(f"Comments removed from {args.filename}")
