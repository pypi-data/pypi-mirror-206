import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def download_file(url, save_path):
    response = requests.get(url)
    file_name = os.path.basename(urlparse(url).path)
    if not file_name:
        file_name = 'index.html'

    with open(os.path.join(save_path, file_name), 'wb') as file:
        file.write(response.content)

    return file_name


def save_webpage(url, save_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for img in soup.find_all('img'):
        img_url = urljoin(url, img['src'])
        img_path = download_file(img_url, save_path)
        img['src'] = img_path

    for link in soup.find_all('link', rel='stylesheet'):
        css_url = urljoin(url, link['href'])
        css_path = download_file(css_url, save_path)
        link['href'] = css_path

    for script in soup.find_all('script', src=True):
        js_url = urljoin(url, script['src'])
        js_path = download_file(js_url, save_path)
        script['src'] = js_path

    html_path = download_file(url, save_path)
    with open(os.path.join(save_path, html_path), 'w') as html_file:
        html_file.write(str(soup))

    print(f"Web page '{url}' saved to '{save_path}' for offline viewing.")


if __name__ == '__main__':
    url = 'https://example.com/'
    save_path = 'offline_page'

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    save_webpage(url, save_path)
