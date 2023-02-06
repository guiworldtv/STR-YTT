import requests
from bs4 import BeautifulSoup

url = 'https://tviplayer.iol.pt/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

links = []
names = []
images = []

for link in soup.find_all('a', href=True):
    if link['href'].startswith('/direto/'):
        video_url = 'https://tviplayer.iol.pt' + link['href']
        title = link.find_next('div', class_='titlePrograma').text
        image_url = link.find_next('div', class_='programCover')['style'].split("url(")[1].split(")")[0]
        entry = "#EXTINF:-1 group-title=\"TVI PLAYER\" tvg-logo=\"{}\",{}\n{}".format(image_url, title, video_url)
        with open('tvi_player.m3u', 'a') as file:
            file.write(entry)

for name in soup.find_all('div', class_='titlePrograma'):
    names.append(name.text)

for image in soup.find_all('div', class_='programCover'):
    images.append(image['style'].split("'")[1])

for i in range(len(links)):
    stream_url = streamlink.streams("https://tviplayer.iol.pt" + links[i])['best'].url
    print("Nome: " + names[i] + ", URL: " + stream_url + ", Thumbnail: " + images[i])
