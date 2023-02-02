import requests
from bs4 import BeautifulSoup
import datetime
import streamlink

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

m3u8_file = open("lista3str3.m3u", "w")

url = "https://www.rtve.es/play/la-1/"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

video_links = [item['href'] for item in soup.find_all("a", class_="goto_media")]
video_titles = [item['title'] for item in soup.find_all("a", class_="goto_media")]


for title, link in zip(video_titles, video_links):
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d%H%M%S")
    video_url = streamlink.streams(link)["best"].url if streamlink.streams(link) else None
    item = soup.find("a", class_="goto_media", href=link)
    try:
        image_url = item["style"].split("url(")[1].split(")")[0]
    except Exception as e:
        print(f"Error: {e}")
        image_url = "https://cdn.rtve.es/resources/png/2/0/1607938114762.png"
    if video_url:
        m3u8_file.write(f"#EXTINF:-1 tvg-group=\"RTVE La 1\" tvg-logo=\"{image_url}\",{title}\n{video_url}\n")
        m3u8_file.write("\n")

m3u8_file.close()
