import os
import discord
import openai
import json
from dotenv import load_dotenv

# Load the Discord tokens
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MARKETING_DISCORD_TOKEN = os.getenv("MARKETING_DISCORD_TOKEN")

# Set up the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the JSON file
with open('./config/marketing.json', 'r') as f:
    config_data = json.load(f)

marketing = discord.Client(intents=discord.Intents.default())

@marketing.event
async def on_ready():
    print(f'{marketing.user} has connected to Discord!')

@marketing.event
async def on_message(message):
    if message.author == marketing.user:
        return

    if not message.guild:
        return

    # Check if message has an attachment
    if message.attachments:
        attachment = message.attachments[0]
        user_message = await attachment.read()
    else:
        user_message = message.content

    # Only reply when mentioned or replied to
    if marketing.user in message.mentions or message.reference:
        if user_message:
            system_message = ""
            for section, data in config_data.items():
                for key, value in data.items():
                    if isinstance(value, list):
                        value = ', '.join(value)
                    system_message += f"{key}: {value}\n"

            response = openai.ChatCompletion.create(
                model=config_data["Settings"]["Model"],
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ],
            )

            reply = response['choices'][0]['message']['content'].strip()

            # Add mention to the reply
            reply = f"{message.author.mention}, {reply}"

            # Reply to the user with typing animation
            async with message.channel.typing():
                await message.channel.send(reply)


marketing.run(MARKETING_DISCORD_TOKEN)
