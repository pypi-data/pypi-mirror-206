import os
import imgkit
from urllib.parse import urlparse

def create_folder_structure(url):
    parsed_url = urlparse(url)
    website_folder = os.path.join("gen", "image", parsed_url.netloc)
    os.makedirs(website_folder, exist_ok=True)
    return website_folder

def screenshot_website(url, output_folder):
    options = {
        "quiet": "",
        "no-stop-slow-scripts": "",
        "javascript-delay": "2000",
        "encoding": "UTF-8",
        "width": "1280",
        "quality": "100",
    }

    output_filename = os.path.join(output_folder, "image.png")

    try:
        imgkit.from_url(url, output_filename, options=options)
        print(f"Long screenshot saved as {output_filename}")
    except Exception as e:
        print(f"Error taking screenshot: {e}")

if __name__ == "__main__":
    website_url = input("Enter the website URL: ")
    output_folder = create_folder_structure(website_url)
    screenshot_website(website_url, output_folder)
