import subprocess
import urllib.parse
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('../../../.env')
load_dotenv(dotenv_path=dotenv_path)

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def push_project_to_github_repository(local_project_dir, github_repo_url):
    parsed_url = urllib.parse.urlsplit(github_repo_url)
    modified_url = parsed_url._replace(netloc=f"{parsed_url.username}:{GITHUB_TOKEN}@{parsed_url.hostname}").geturl()

    os.chdir(local_project_dir)
    subprocess.run(["git", "init"])
    subprocess.run(["git", "remote", "add", "origin", modified_url])
    subprocess.run(["git", "config", "user.name", "haiagent"])
    subprocess.run(["git", "config", "user.email", "haiconvers@gmail.com"])
    subprocess.run(["git", "config", "init.defaultBranch", "main"]) 
    subprocess.run(["git", "checkout", "-b", "main"]) 
    subprocess.run(["git", "add", "."])

    commit_message = "Initial commit"
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "push", "-u", "origin", "main"])
