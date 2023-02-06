import requests
from bs4 import BeautifulSoup

url = 'https://tviplayer.iol.pt/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

links = []
names = []
images = []

for link in soup.find_all('a', href=True):
    if '/direto/TVI' in link['href']:
        links.append('https://tviplayer.iol.pt' + link['href'])

for name in soup.find_all('div', class_='titlePrograma'):
    names.append(name.text)

for image in soup.find_all('div', class_='programCover'):
    images.append(image['style'].split("'")[1])

for i in range(len(links)):
    stream_url = streamlink.streams("https://tviplayer.iol.pt" + links[i])['best'].url
    print("Nome: " + names[i] + ", URL: " + stream_url + ", Thumbnail: " + images[i])
