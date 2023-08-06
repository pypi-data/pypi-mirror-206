import os
import re
import requests
from dotenv import load_dotenv
import openai
import json
import shutil
import urllib.parse

load_dotenv()
figma_api_key = os.getenv('FIGMA_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def extract_figma_file_id(figma_url):
    file_id = None
    if 'figma.com/file/' in figma_url:
        file_id = figma_url.split('/file/')[1].split('/')[0]
    return file_id

def extract_figma_node_id(figma_url):
    node_id = None
    if 'node-id=' in figma_url:
        node_id = figma_url.split('node-id=')[1].split('&')[0]
        node_id = urllib.parse.unquote(node_id)
    return node_id


def get_all_frames(node):
    frames = []
    if node['type'] == 'FRAME':
        frames.append(node)
    elif 'children' in node:
        for child in node['children']:
            frames.extend(get_all_frames(child))
    return frames

def get_document_root(figma_file_id):
    headers = {
        'X-Figma-Token': figma_api_key
    }
    response = requests.get(f'https://api.figma.com/v1/files/{figma_file_id}', headers=headers)
    if response.status_code != 200:
        print(f'Error: {response.status_code}')
        return
    data = response.json()
    return data['document']

def generate_code_snippets(api_key, design_info):
    openai.api_key = api_key
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a code generator."},
            {"role": "user", "content": f"Generate HTML, CSS, and JS code snippets for this design: {design_info}"}
        ]
    )

    code_str = completion['choices'][0]['message']['content'].strip()
    code_parts = code_str.split('```')
    code_dict = {}
    for part in code_parts:
        if 'html' in part.lower():
            code_dict['html'] = part.split('\n', 1)[1]
        elif 'css' in part.lower():
            code_dict['css'] = part.split('\n', 1)[1]
        elif 'javascript' in part.lower():
            code_dict['js'] = part.split('\n', 1)[1]
    return code_dict

def save_files(folder, frame_name, code_dict):
    os.makedirs(folder, exist_ok=True)
    for key, value in code_dict.items():
        with open(os.path.join(folder, f'{frame_name}.{key}'), 'w') as f:
            f.write(value)

def export_images(figma_file_id, figma_node_id, frame_name, folder):
    headers = {
        'X-Figma-Token': figma_api_key
    }
    response = requests.get(f'https://api.figma.com/v1/images/{figma_file_id}?ids={figma_node_id}&format=png', headers=headers)
    if response.status_code != 200:
        print(f'Error exporting images: {response.status_code}')
        return
    data = response.json()
    image_url = data['images'][figma_node_id]
    if image_url:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        with open(os.path.join(folder, f'{frame_name}.png'), 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)

if __name__ == '__main__':
    print("Welcome to the Figma design parser!")
    figma_url = input("Enter your Figma file URL: ")

    figma_file_id = extract_figma_file_id(figma_url)
    selected_frame_id = extract_figma_node_id(figma_url)

    if figma_file_id and selected_frame_id:
        root_node = get_document_root(figma_file_id)
        if root_node:
            frames = get_all_frames(root_node)
            selected_frame = None
            for frame in frames:
                if frame['id'] == selected_frame_id:
                    selected_frame = frame
                    break
            if selected_frame:
                design_info = f"Frame name: {selected_frame['name']}\nFrame ID: {selected_frame['id']}"
                print(design_info)

                gen_folder = 'generated'
                code_snippets = generate_code_snippets(OPENAI_API_KEY, design_info)
                save_files(gen_folder, selected_frame['name'], code_snippets)
                export_images(figma_file_id, selected_frame_id, selected_frame['name'], gen_folder)
            else:
                print("Selected frame not found in the Figma file")
        else:
            print("Error fetching Figma document root")
    else:
        print("Invalid Figma file URL")
