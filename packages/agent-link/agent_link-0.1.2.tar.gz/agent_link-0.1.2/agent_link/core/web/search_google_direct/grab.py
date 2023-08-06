import os
import re
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import openai
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('../../../.env')
load_dotenv(dotenv_path=dotenv_path)

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

def fetch_content_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    text = soup.get_text()
    tokens = text.split()[:1000] 
    content = ' '.join(tokens)

    return content

def google_search(query):
    results = []
    for j in search(query, num_results=3):
        results.append(j)
    return results

def extract_url_from_prompt(prompt):
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = url_pattern.findall(prompt)
    return urls[0] if urls else None

def test():
    grab_internet(user_prompt="what is https://scodestudio.com and who made it.", model="gpt-4")

def grab_internet(user_prompt, model):
    url = extract_url_from_prompt(user_prompt)

    if url:
        content = fetch_content_from_url(url)
    else:
        content = ""

    messages = [
        {"role": "system", "content": "InternetAccess: True"},
        {"role": "system", "content": "AILanguageModel: False"},
        {"role": "system", "content": "AIAgentModel: True"},
        {"role": "system", "content": "CapabilityToRememberChat: True"},
        {"role": "system", "content": "Developer: John Dave Natividad (JASEUNDA)"},
        {"role": "system", "content": content},
        {"role": "user", "content": user_prompt}
    ]

    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    # callback(completion.choices[0].message)
    print(completion.choices[0].message)

# TESTER
# if __name__ == "__main__":
#     test()
