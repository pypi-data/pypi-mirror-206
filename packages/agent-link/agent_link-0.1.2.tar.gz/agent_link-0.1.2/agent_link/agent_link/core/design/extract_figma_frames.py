import requests
from interactions import Image


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