import os
import openai
import re
from termcolor import colored
import subprocess
import time
import discord
from discord.ext import commands
import uuid
import aiohttp
import asyncio
import urllib.parse
from github import Github
from dotenv import load_dotenv
import threading
import http.server
import socketserver
import socket
import shutil
import datetime
import zipfile
import pathspec
import webbrowser
import threading
from output import socketio
import secrets
from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, join_room
from flask import g
from threading import Thread
import requests
from interactions import Image
import eventlet

LAST_UPDATE_FILE = "last_update.txt"
TEMPLATE_DIR = "template"
TEMPLATE_ZIP_FILE = "template.zip"

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
FIGMA_KEY = os.getenv("FIGMA_TOKEN")

# Set up the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the bot
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is connected to Discord!")

def extract_figma_frames(figma_file_key, access_token):
    headers = {
        "FIGMA_TOKEN": access_token
    }
    base_url = "https://api.figma.com/v1/files/"

    response = requests.get(base_url + figma_file_key, headers=headers)
    file_data = response.json()
    frames = []

    for node_id, node in file_data['document']['nodes'].items():
        if node['document']['type'] == 'FRAME':
            frame_name = node['document']['name']
            image_url = f"https://api.figma.com/v1/images/{figma_file_key}?ids={node_id}&format=png"
            response = requests.get(image_url, headers=headers)
            img_data = response.content
            img = Image.open(io.BytesIO(img_data))
            frames.append((frame_name, img))

    return frames

def create_react_app_with_tailwind_typescript(project_dir):
    subprocess.run(["npx", "create-react-app", project_dir, "--template", "typescript"])
    subprocess.run(["npm", "install", "-D", "tailwindcss@latest", "postcss@latest", "autoprefixer@latest"], cwd=project_dir)

def copy_directory(src, dest):
    os.makedirs(dest, exist_ok=True)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            copy_directory(s, d)
        else:
            shutil.copy2(s, d)

def should_update_template():
    if not os.path.exists(LAST_UPDATE_FILE):
        return True

    with open(LAST_UPDATE_FILE, "r") as f:
        last_update_str = f.read().strip()
        last_update = datetime.datetime.strptime(last_update_str, "%Y-%m-%d")

    now = datetime.datetime.now()
    days_since_last_update = (now - last_update).days

    return days_since_last_update >= 7

def update_template():
    if os.path.exists(TEMPLATE_DIR):
        shutil.rmtree(TEMPLATE_DIR)

    create_react_app_with_tailwind_typescript(TEMPLATE_DIR)

    # Read the .gitignore file
    with open(os.path.join(TEMPLATE_DIR, ".gitignore"), "r") as gitignore_file:
        gitignore_content = gitignore_file.read()

    # Compile the pathspec
    gitignore_spec = pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, gitignore_content.splitlines())

    # Create a function to check if a file is ignored
    def is_ignored(file_path):
        return gitignore_spec.match_file(file_path)

    # Compress the project using liblz4-tool, skipping ignored files
    with open(TEMPLATE_ZIP_FILE, "wb") as zip_file:
        process = subprocess.Popen(["tar", "-c", "--use-compress-program", "lz4", "-C", TEMPLATE_DIR] + [file for file in os.listdir(TEMPLATE_DIR) if not is_ignored(file)], stdout=subprocess.PIPE)
        zip_file.write(process.communicate()[0])
        
def delete_directory(directory):
    shutil.rmtree(directory)

def push_project_to_github_repository(local_project_dir, github_repo_url):
    # Modify the GitHub repo URL to include the token
    parsed_url = urllib.parse.urlsplit(github_repo_url)
    modified_url = parsed_url._replace(netloc=f"{parsed_url.username}:{GITHUB_TOKEN}@{parsed_url.hostname}").geturl()

    os.chdir(local_project_dir)
    subprocess.run(["git", "init"])
    subprocess.run(["git", "remote", "add", "origin", modified_url])
    subprocess.run(["git", "config", "user.name", "haiagent"])
    subprocess.run(["git", "config", "user.email", "haiconvers@gmail.com"])
    subprocess.run(["git", "config", "init.defaultBranch", "main"])  # Set the default branch to 'main'
    subprocess.run(["git", "checkout", "-b", "main"])  # Create and switch to the 'main' branch
    subprocess.run(["git", "add", "."])

    commit_message = "Initial commit"
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "push", "-u", "origin", "main"])

def fix_code_errors():
    pass

def create_directory_and_file(directory, filename):
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, filename)
    with open(file_path, 'w') as file:
        pass

    return file_path

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

user_output_files = {}

def create_output_html_for_user(user_id):
        output_html_filename = f"{user_id}_output.html"
        shutil.copy("output.html", output_html_filename)
        return output_html_filename
    
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if bot.user in message.mentions and "specifications.txt" in [attachment.filename for attachment in message.attachments]:
        await message.channel.send("Processing specifications...")

        # Download the "specifications.txt" file
        specifications_attachment = None
        for attachment in message.attachments:
            if attachment.filename == "specifications.txt":
                specifications_attachment = attachment
                break

        if specifications_attachment:
            async with aiohttp.ClientSession() as session:
                async with session.get(specifications_attachment.url) as resp:
                    specifications = await resp.text()

            # Create a unique directory
            genfiles_dir = ".projects"
            os.makedirs(genfiles_dir, exist_ok=True)
            unique_dir = f"{genfiles_dir}/{message.author.name}_{uuid.uuid4().hex}"
            os.makedirs(unique_dir, exist_ok=True)

            # Save the specifications.txt file to the unique directory
            with open(os.path.join(unique_dir, "specifications.txt"), "w") as f:
                f.write(specifications)

            await message.channel.send("Please provide the GitHub repo URL to upload the project:")
            try:
                repo_url_msg = await bot.wait_for('message', check=lambda msg: msg.author == message.author, timeout=60)
                github_repo_url = repo_url_msg.content.strip()

                # Check if the bot has access to the repo
                github = Github(GITHUB_TOKEN)
                try:
                    repo = github.get_repo(github_repo_url.replace("https://github.com/", ""))
                except:
                    await message.channel.send("Unable to access the provided repository. Please invite the bot to the repository and try again.")
                    return

                await message.channel.send("Starting project generation and uploading process...")
                await process_specifications(message.channel, specifications, github_repo_url, unique_dir, message.author.id)
            except asyncio.TimeoutError:
                await message.channel.send("Request timed out. Please provide the GitHub repo URL within 60 seconds.")

    await bot.process_commands(message)

def read_specifications():
    with open("specifications.txt", "r") as spec_file:
        specifications = spec_file.read()
    return specifications

def run_project(unique_dir):
    cmd = ["npm", "start"]
    process = subprocess.Popen(cmd, cwd=unique_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    return process

def extract_files_to_generate(specifications):
    prompt = f"List the files that need to be generated for a web portfolio based on the following specifications:\n\n{specifications}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    files = response['choices'][0]['message']['content'].strip().split('\n')
    return [file.strip() for file in files]

async def process_specifications(ctx, specifications, github_repo_url, unique_dir, user_id):

    def extract_files_to_generate(specifications):
        file_list_pattern = re.compile(r'-\s(.*\.(tsx|html))', re.MULTILINE)
        files_to_generate = file_list_pattern.findall(specifications)
        return [file[0] for file in files_to_generate]

    def create_directory_and_file(path, filename):
        file_path = os.path.join(path, filename)
        if not os.path.isdir(path):
            os.makedirs(path)
        if not os.path.isfile(file_path):
            with open(file_path, "w") as file:
                file.write("")
        return file_path

    def generate_code(filename, specifications, created_files):
        extension = filename.split('.')[-1]
        prompt = f"Create a {extension.upper()} file named {filename} for a web app mobile and desktop friendly, like as described in the following specifications. Generate only pure code, without comments or additional information:\n\n"

        prompt += f"Files already created:\n"
        for created_file in created_files:
            prompt += f"- {created_file}\n"
        prompt += "\n"
        prompt += specifications

        directory = os.path.join(project_dir, "src", os.path.dirname(filename))
        file_path = os.path.join(directory, os.path.basename(filename))

        if not os.path.isdir(directory):
            os.makedirs(directory)

        if not os.path.isfile(file_path):
            with open(file_path, "w") as file:
                file.write("")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
        )

        message_content = response['choices'][0]['message']['content'].strip()
        code_only = re.sub(r'\[.+\]\n', '', message_content) # Removes any message prefix with brackets
        return code_only

    os.makedirs(os.path.join(unique_dir, "project"), exist_ok=True)
    project_dir = os.path.join(unique_dir, "project")

    if should_update_template():
        update_template()

    if not os.path.exists(TEMPLATE_ZIP_FILE):
        update_template()

    # Unzip the project using liblz4-tool
    with open(TEMPLATE_ZIP_FILE, "rb") as zip_file:
        process = subprocess.Popen(["tar", "-x", "--use-compress-program", "lz4", "-C", project_dir], stdin=subprocess.PIPE)
        process.communicate(zip_file.read())

    # Ensure the project directory is created before running npm install
    os.makedirs(project_dir, exist_ok=True)

    # Run npm install before generating the code
    npm_process = subprocess.Popen(["npm", "install"], cwd=project_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    # Capture the terminal output and send it to the live HTML page
    while True:
        output = npm_process.stdout.readline()
        if output == "" and npm_process.poll() is not None:
            break
        if output:
            socketio.emit("output", output)

    files_to_generate = extract_files_to_generate(specifications)

    created_files = []

    for filename in files_to_generate:
        socketio.emit("output", colored(f"Generating code for {filename}...", "yellow"))
        print(colored(f"Generating code for {filename}...", "yellow"))

        # Ensure the directory and file exist before generating the code
        directory = os.path.join(project_dir, "src", os.path.dirname(filename))
        file_path = create_directory_and_file(directory, os.path.basename(filename))

        created_files.append(filename)

        code = generate_code(filename, specifications, created_files)
        with open(file_path, "w") as file:
            file.write(code)
        print(colored(f"{filename} created successfully.", "green"))

    print(colored("Web project generation completed.", "green"))

    while True:
        process = run_project(project_dir)
        time.sleep(5)

        errors_exist = check_errors(process)

        if errors_exist:
            fix_code_errors()
        else:
            break

    push_project_to_github_repository(project_dir, github_repo_url)

    await ctx.send(f"Project successfully uploaded to {github_repo_url}")

    # Push the project to the haiagent/response repository
    push_project_to_github_repository(project_dir, "https://github.com/haiagent/response")

    # Delete the user's project directory to save space
    delete_directory(unique_dir)
    os.remove(f"{user_id}_output.html")

if __name__ == "__main__":
    # Start Discord bot
    bot.run(DISCORD_TOKEN)