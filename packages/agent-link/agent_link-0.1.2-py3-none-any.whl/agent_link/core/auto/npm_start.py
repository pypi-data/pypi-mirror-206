import subprocess

def run_project(unique_dir):
    cmd = ["npm", "start"]
    process = subprocess.Popen(cmd, cwd=unique_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    return process