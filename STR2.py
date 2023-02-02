import requests
from bs4 import BeautifulSoup
import datetime
import streamlink

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

m3u8_file = open("lista2str2.m3u", "w")

for i in range(1, 3):
    url = f"https://tviplayer.iol.pt/videos/ultimos/{i}/canal:"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    video_titles = [item.text for item in soup.find_all("span", class_="item-title")]
    video_links = [f"https://tviplayer.iol.pt{item['href']}" for item in soup.find_all("a", class_="item")]
    Data = [item.text for item in soup.find_all("span", class_="item-date")]
    image_url = item["style"].split("url(")[1].split(")")[0]


    for title, link in zip(video_titles, video_links):
        now = datetime.datetime.now()
        timestamp = now.strftime("%m%d%H%M%S")
        video_url = streamlink.streams(link)["best"].url
        m3u8_file.write(f"#EXTINF:-1 group-title = \"{image_url}\", {title}\n{video_url}\n")




m3u8_file.close()
