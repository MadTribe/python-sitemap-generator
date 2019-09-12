from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import re


def get_image_info(url):
    image_info = list()

    html = urlopen(url)
    bs = BS(html, 'html.parser')
    image_elms = bs.find_all(
        'img', {'src': re.compile('.png|.jpg|.jpeg|.gif'), 'alt': re.compile('.*')})

    for image in image_elms:
        image_info.append({'src': image['src'], 'caption': image['alt']})

    return image_info


def get_subpage_url(url):
    html = urlopen(url)
    bs = BS(html, 'html.parser')
    link_elms = bs.find_all('a', {'href': re.compile(url)})
    return {link['href'] for link in link_elms}
