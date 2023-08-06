import os
import openai
import re
import json
from termcolor import colored
import subprocess
import time
import discord
from discord.ext import commands
import uuid
import aiohttp
import asyncio
from github import Github
from dotenv import load_dotenv
# from rich import print
# from rich.traceback import install

# install()

from out.output.output import socketio
from core.update.update_template.update import should_update_template
from core.update.update_template.template import update_template
from core.tools.delete.delete_dir import delete_directory
from core.auto.fix_code_error import fix_code_errors
from core.error.check_error import check_errors
from core.auto.npm_start import run_project
from core.github.push import push_project_to_github_repository

LAST_UPDATE_FILE = "last_update.txt"
TEMPLATE_DIR = "template"
TEMPLATE_ZIP_FILE = "template.zip"

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
FIGMA_KEY = os.getenv("FIGMA_TOKEN")

openai.api_key = os.getenv("OPENAI_API_KEY")

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

user_output_files = {}
  
@bot.event
async def on_ready():
    print(f"{bot.user} is connected to Discord!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if bot.user in message.mentions and "specifications.txt" in [attachment.filename for attachment in message.attachments]:
        await message.channel.send("Processing specifications...")
        specifications_attachment = None
        for attachment in message.attachments:
            if attachment.filename == "specifications.txt":
                specifications_attachment = attachment
                break

        if specifications_attachment:
            async with aiohttp.ClientSession() as session:
                async with session.get(specifications_attachment.url) as resp:
                    specifications = await resp.text()
            genfiles_dir = ".projects"
            os.makedirs(genfiles_dir, exist_ok=True)
            unique_dir = f"{genfiles_dir}/{message.author.name}_{uuid.uuid4().hex}"
            os.makedirs(unique_dir, exist_ok=True)
            with open(os.path.join(unique_dir, "specifications.txt"), "w") as f:
                f.write(specifications)

            await message.channel.send("Please provide the GitHub repo URL to upload the project:")
            try:
                repo_url_msg = await bot.wait_for('message', check=lambda msg: msg.author == message.author, timeout=60)
                github_repo_url = repo_url_msg.content.strip()
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

    
    def generate_code(filename, specifications, files_status):
        extension = filename.split('.')[-1]
        prompt = f"Generate only pure code, without comments or additional information, backticks, or anything not related to the code, for a {extension.upper()} file named {filename} for a web app that is mobile and desktop friendly, with visually appealing design using Tailwind CSS. Make it responsive, desktop and mobile friendly, and has good color combination. The file should follow these specifications:\n\n{specifications}\n\nFiles status:\n"

        for file, status in files_status.items():
            prompt += f"- {file}: {'Created' if status else 'Not Created'}\n"

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "CodeGenerator: True"},
                {"role": "system", "content": "AILanguageModel: False"},
                {"role": "system", "content": "GenerateCodeOnlyWithoutCommentOrBacktick: True"},
                {"role": "system", "content": "AllowCommentOnCode: True"},
                {"role": "system", "content": f"Files status: {json.dumps(files_status)}."},
                {"role": "user", "content": prompt}
            ],
        )

        message_content = response['choices'][0]['message']['content'].strip()
        code_only = re.sub(r'\[.+\]\n', '', message_content)  # Removes any message prefix with brackets

        return code_only

    os.makedirs(os.path.join(unique_dir, "project"), exist_ok=True)
    project_dir = os.path.join(unique_dir, "project")

    if should_update_template():
        update_template()

    if not os.path.exists(TEMPLATE_ZIP_FILE):
        update_template()
    with open(TEMPLATE_ZIP_FILE, "rb") as zip_file:
        process = subprocess.Popen(["tar", "-x", "--use-compress-program", "lz4", "-C", project_dir], stdin=subprocess.PIPE)
        process.communicate(zip_file.read())
    os.makedirs(project_dir, exist_ok=True)
    npm_process = subprocess.Popen(["npm", "install"], cwd=project_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    while True:
        output = npm_process.stdout.readline()
        if output == "" and npm_process.poll() is not None:
            break
        if output:
            socketio.emit("output", output)

    files_to_generate = extract_files_to_generate(specifications)

    created_files = []

    files_status = {filename: False for filename in files_to_generate}

    for filename in files_to_generate:
        socketio.emit("output", colored(f"Generating code for {filename}...", "yellow"))
        print(colored(f"Generating code for {filename}...", "yellow"))
        directory = os.path.join(project_dir, "src", os.path.dirname(filename))
        file_path = create_directory_and_file(directory, os.path.basename(filename))

        files_status[filename] = True

        code = generate_code(filename, specifications, files_status)
        with open(file_path, "w") as file:
            file.write(code)
        print(colored(f"{filename} created successfully.", "green"))

    print(colored("Web project generation completed.", "green"))

    push_project_to_github_repository(project_dir, github_repo_url)

    await ctx.send(f"Project successfully uploaded to {github_repo_url}")
    push_project_to_github_repository(project_dir, "https://github.com/haiagent/response")
    delete_directory(unique_dir)
    os.remove(f"{user_id}_output.html")
    
    while True:
        process = run_project(project_dir)
        time.sleep(5)

        errors_exist = check_errors(process)

        if errors_exist:
            fix_code_errors()
        else:
            break

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)