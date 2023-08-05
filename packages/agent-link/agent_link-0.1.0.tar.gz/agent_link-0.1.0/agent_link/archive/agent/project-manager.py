import os
import discord
import openai
from dotenv import load_dotenv
import asyncio
import random

# Load the Discord tokens
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PROJECT_MANAGER_DISCORD_TOKEN = os.getenv("PROJECT_MANAGER_DISCORD_TOKEN")


# Set up the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
        
client = discord.Client(intents=discord.Intents.default())
project_manager = discord.Client(intents=discord.Intents.default())

@project_manager.event
async def on_ready():
    print(f'{project_manager.user} has connected to Discord!')

async def send_specifications_to_role(message, role_id, channel_id, specifications, custom_message):
    channel = project_manager.get_channel(channel_id)
    async with channel.typing():
        await channel.send(f"{custom_message}", file=discord.File(specifications))

async def send_file_to_prompt_master(channel_id, filepath):
    channel = project_manager.get_channel(channel_id)
    async with channel.typing():
        message = await channel.send("Processing specifications.txt for improvements", file=discord.File(filepath))
        return message

async def send_gpt3_reply(message, user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_message}
        ],
    )

    reply = response['choices'][0]['message']['content'].strip()
    reply = f"{message.author.mention}, {reply}"

    # Add a typing animation before sending the message
    async with message.channel.typing():
        await asyncio.sleep(random.uniform(1, 3))  # Simulate typing time
        await message.channel.send(reply)

async def send_file_to_prompt_master(channel_id, filepath, mention_text):
    channel = project_manager.get_channel(channel_id)
    async with channel.typing():
        message = await channel.send(mention_text, file=discord.File(filepath))
        return message

@project_manager.event
async def on_message(message):
    if message.author == project_manager.user:
        return

    if not message.guild:
        return

    developer_role = discord.utils.get(message.guild.roles, name="Developer")
    marketing_role = discord.utils.get(message.guild.roles, name="Marketing")
    prompt_master_role = discord.utils.get(message.guild.roles, name="PromptMaster")

    ROLE_THAT_SENDS_SPECIFICATIONS_ID = 1097958952244871268
    PROMPT_MASTER_ROLE_ID = 1097952936258179213
    PROMPT_MASTER_CHANNEL_ID = 1097950934744711198
    DEVELOPER_CHANNEL_ID = 1097949285926055956
    MARKETING_CHANNEL_ID = 1097949442386182206
    ROLE_TO_NOTIFY_ID = 746615709122953259
    DEVELOPER_ROLE_ID = 1097785643679105136
    MARKETING_ROLE_ID = 1097958039551738016
    
    # Reply to normal messages like a human using GPT-3
    if not any(role.id in [DEVELOPER_ROLE_ID, MARKETING_ROLE_ID] for role in message.author.roles) and message.content and random.random() < 0.1:
        await send_gpt3_reply(message, message.content)

    if any(role.id == ROLE_THAT_SENDS_SPECIFICATIONS_ID for role in message.author.roles) and message.attachments:
        attachment = message.attachments[0]
        if attachment.filename == 'specifications.txt':
            await message.channel.send("Thank you! Got it, will inform the team and start the project soon.")
            await attachment.save("specifications.txt")

            prompt_master_mention = f"<@{PROMPT_MASTER_ROLE_ID}>, please review and improve the specifications."
            sent_message = await send_file_to_prompt_master(PROMPT_MASTER_CHANNEL_ID, "specifications.txt", prompt_master_mention)


    if message.channel.id == PROMPT_MASTER_CHANNEL_ID and message.attachments:
        attachment = message.attachments[0]
        if attachment.filename.endswith('.txt'):
            await attachment.save("improved_specifications.txt")
            specifications_file_developer = f"specifications.txt"
            specifications_file_marketing = f"specifications.txt"
            with open("improved_specifications.txt", "r") as f:
                improved_specifications = f.read()

            with open(specifications_file_developer, "w") as file:
                file.write("Developer-specific content\n\n" + improved_specifications)
            with open(specifications_file_marketing, "w") as file:
                file.write("Marketing-specific content\n\n" + improved_specifications)

            await send_specifications_to_role(message, DEVELOPER_ROLE_ID, DEVELOPER_CHANNEL_ID, specifications_file_developer, "<@1097785643679105136>. Here are the improved specifications for the Developer team.")
            await send_specifications_to_role(message, MARKETING_ROLE_ID, MARKETING_CHANNEL_ID, specifications_file_marketing, "Here are the improved specifications for the Marketing team <@1097958039551738016>.")

            os.remove(specifications_file_developer)
            os.remove(specifications_file_marketing)
            os.remove("improved_specifications.txt")

    if any(role.id in [DEVELOPER_ROLE_ID, MARKETING_ROLE_ID] for role in message.author.roles):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message.content}
            ],
        )

        reply = response['choices'][0]['message']['content'].strip()

        if "github link" in message.content.lower():
            reply = f"<@{ROLE_TO_NOTIFY_ID}>, please provide the GitHub link for the project."

        reply = f"{message.author.mention}, {reply}"
        await message.channel.send(reply)
        
    developer_role_id = 1097786258576658446
    marketing_role_id = 1097958182955008062
    prompt_master_role_id = 1097953183260737778

    developer_role = discord.utils.get(message.guild.roles, id=developer_role_id)
    marketing_role = discord.utils.get(message.guild.roles, id=marketing_role_id)
    prompt_master_role = discord.utils.get(message.guild.roles, id=prompt_master_role_id)

    if developer_role is None:
        print("Error: Developer role not found in the server")
    if marketing_role is None:
        print("Error: Marketing role not found in the server")
    if prompt_master_role is None:
        print("Error: PromptMaster role not found in the server")

    elif project_manager.user in message.mentions or (message.reference and message.reference.resolved.author.id == project_manager.user.id):
        user_message = message.content
        if user_message:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": user_message}
                ],
            )

            reply = response['choices'][0]['message']['content'].strip()

            if "dev" in user_message.lower() and "create" in user_message.lower() and "simple one page website" in user_message.lower():
                reply = f"<@{developer_role_id}>, please create a simple one-page website as requested by {message.author.mention}."
            else:
                mention_user_ids = []
                if developer_role in message.role_mentions:
                    mention_user_ids.append(str(developer_role_id))
                if marketing_role in message.role_mentions:
                    mention_user_ids.append(str(marketing_role_id))
                if prompt_master_role in message.role_mentions:
                    mention_user_ids.append(str(prompt_master_role_id))

                if mention_user_ids:
                    reply += " " + " ".join(f"<@{user_id}>" for user_id in mention_user_ids) + ", please take note."

            reply = f"{message.author.mention}, {reply}"
            await message.channel.send(reply)

project_manager.run(PROJECT_MANAGER_DISCORD_TOKEN)