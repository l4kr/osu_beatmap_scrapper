import requests
import webbrowser
from bs4 import BeautifulSoup

owc2020 = 'https://osu.ppy.sh/wiki/en/Tournaments/OWC/2020'
html_text = requests.get(owc2020).text
soup = BeautifulSoup(html_text, "lxml")
links = soup.findAll('a')
for link in links:
    print(link['href'])

