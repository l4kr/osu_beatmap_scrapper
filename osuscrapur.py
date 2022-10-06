import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://osu.ppy.sh/wiki/en/Tournaments/OWC/2020').text
soup = BeautifulSoup(html_text, "lxml")
mappool_div = soup.find('div', text='Mappools')
links = mappool_div.findAll('<a>')
print(links)