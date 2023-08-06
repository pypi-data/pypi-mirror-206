import os
import discord
import openai
import aiohttp
from dotenv import load_dotenv

# Load the Discord tokens
load_dotenv()
PROMPT_MASTER_DISCORD_TOKEN = os.getenv("PROMPT_MASTER_DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set up the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

prompt_master = discord.Client(intents=discord.Intents.default())

async def improve_specifications(specifications):
    prompt = f"Improve the following project specifications to make them more clear and detailed:\n\n{specifications}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return response['choices'][0]['message']['content'].strip()

@prompt_master.event
async def on_ready():
    print(f'{prompt_master.user} has connected to Discord!')

@prompt_master.event
async def on_message(message):
    if message.author == prompt_master.user:
        return

    if not message.guild:
        return

    # Check if the message has an attachment named "specifications.txt"
    for attachment in message.attachments:
        if attachment.filename == "specifications.txt":
            # Download the attachment
            async with aiohttp.ClientSession() as session:
                async with session.get(attachment.url) as response:
                    if response.status != 200:
                        await message.channel.send('Failed to download attachment.')
                    else:
                        specifications = await response.text()

            # Show typing animation while generating the response
            async with message.channel.typing():
                # Improve the specifications using GPT-3
                improved_specifications = await improve_specifications(specifications)

            # Save the improved specifications to a file
            improved_specifications_file = "specifications.txt"
            with open(improved_specifications_file, "w") as file:
                file.write(improved_specifications)

            # Send the improved specifications back to the user who sent the original specifications in the same channel
            mention = message.author.mention
            await message.channel.send(f"{mention} Here is the improved specifications.txt file:", file=discord.File(improved_specifications_file))

            # Remove the improved specifications file after sending
            os.remove(improved_specifications_file)

prompt_master.run(PROMPT_MASTER_DISCORD_TOKEN)
