import requests
from bs4 import BeautifulSoup

def scrape_images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = [img['src'] for img in soup.find_all('img', src=True) if 'menu' in img['src']]
    return images
