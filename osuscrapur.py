from http.cookiejar import CookieJar
import requests
import browser_cookie3
from bs4 import BeautifulSoup

owc2020 = 'https://osu.ppy.sh/wiki/en/Tournaments/OWC/2020'
#CookieJar - browser_cookie3.firefox()
#r = requests.get(owc2020, cookies=Cookiejar)
html_text = requests.get(owc2020).text
soup = BeautifulSoup(html_text, "lxml")
links = soup.findAll('a')
for link in links:
    link = link['href']
    if "beatmapsets/" in link:
        print(link)