import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://osu.ppy.sh/wiki/en/Tournaments/OWC/2020').text
soup = BeautifulSoup(html_text, "lxml")
links = soup.findAll('a')
print(links)