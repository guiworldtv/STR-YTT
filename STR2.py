import requests
from bs4 import BeautifulSoup
import datetime
import streamlink
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

m3u8_file = open("lista2str2.m3u", "w")

url = "https://tviplayer.iol.pt/"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

video_links = [f"https://tviplayer.iol.pt{item['href']}" for item in soup.find_all("a", class_="direto")]
video_titles = [item.text for item in soup.find_all("div", class_="titlePrograma")]
image_urls = [item["style"].split("url(")[1].split(")")[0] for item in soup.find_all("div", class_="programCover")]

for link, title, image_url in zip(video_links, video_titles, image_urls):
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d%H%M%S")
    video_url = streamlink.streams(link)["best"].url if streamlink.streams(link) else None
    if video_url:
        m3u8_file.write(f"#EXTINF:-1 group-title=\"TVI PLAYER\" tvg-logo=\"{image_url}\",{title}\n{video_url}\n")
        m3u8_file.write("\n")

time.sleep(12)

m3u8_file.close()
