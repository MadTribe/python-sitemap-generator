from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://mycertify.com/')
bs = BeautifulSoup(html, 'html.parser')

""" images = bs.find_all('img', {'src': re.compile('.jpg|.png')})

image_urls = { image['src'] for image in images }

print(image_urls) """

""" background_images = bs.find_all('div', {'style': re.compile(
    '(background.+(.jpg|.png))|(background-image.+(\.jpg|\.png))')})

for image_elm in background_images:
    print(image_elm['style']) """
