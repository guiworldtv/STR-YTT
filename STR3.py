import requests
from bs4 import BeautifulSoup
import datetime
import streamlink

import streamlink.compat
streamlink.compat.monkeypatch()
streamlink.set_option("hls-segment-threads", 1)
streamlink.set_option("http-ssl-verify", False)
streamlink.set_option("http-no-ssl-verify", True)
streamlink.set_option("http-headers", headers)
streamlink.set_option("hls-live-edge", 9999999)
streamlink.set_option("hls-timeout", 9999999)
streamlink.set_option("hls-start-offset", 9999999)
streamlink.set_option("http-user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
streamlink.set_loglevel("error")
streamlink.set_logoutput(None)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

m3u8_file = open("lista3str3.m3u", "w")

url = "https://www.youtube.com/results?search_query=aula&sp=CAISBBABGAI%253D"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

video_titles = [item.text for item in soup.find_all("yt-formatted-string", class_="style-scope ytd-video-renderer")]
video_images = [item["src"] for item in soup.find_all("img", class_="yt-core-image")]
video_links = [f"https://www.youtube.com{item['href']}" for item in soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-video-renderer")]


for title, link in zip(video_titles, video_links):
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d%H%M%S")
    video_url = streamlink.streams(link)["best"].url if streamlink.streams(link) else None
if video_url:
    image_url = f"https://i.ytimg.com/vi/{link.split('watch?v=')[1]}/hqdefault.jpg"
    m3u8_file.write(f"#EXTINF:-1 tvg-group=\"YOUTOBA\" tvg-logo=\"{image_url}\",{title}\n{video_url}\n")
    m3u8_file.write("\n")
else:
    print(f"Não foi possível acessar o vídeo: {title}")

    

m3u8_file.close()
