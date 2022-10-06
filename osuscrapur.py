import requests
import bs4

html_text = requests.get('https://osu.ppy.sh/wiki/en/Tournaments/OWC/2020').html
soup = bs4.Soup(html_text)
mappool_div = soup.find('div', text='Mappools')
links = mappool.div.findAll('<a>')
