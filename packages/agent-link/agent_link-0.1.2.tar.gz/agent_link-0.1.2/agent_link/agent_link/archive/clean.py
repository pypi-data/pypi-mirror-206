import argparse
import re

def remove_comments(filename):
    # open the file
    with open(filename, "r") as f:
        # read the contents of the file
        contents = f.read()
        
        # remove single-line comments
        contents = re.sub(r'(?m)^\s*#.*\n?', '', contents)
        
        # remove multi-line comments
        contents = re.sub(r'\n\s*""".*?"""', '', contents, flags=re.DOTALL)
        
    # write the modified contents back to the file
    with open(filename, "w") as f:
        f.write(contents)

if __name__ == "__main__":
    # create a command line argument parser
    parser = argparse.ArgumentParser(description="Remove comments from a Python file")
    
    # add a positional argument for the filename
    parser.add_argument("filename", type=str, help="the name of the file to remove comments from")
    
    # parse the command line arguments
    args = parser.parse_args()
    
    # remove comments from the specified file
    remove_comments(args.filename)
    
    print(f"Comments removed from {args.filename}")
