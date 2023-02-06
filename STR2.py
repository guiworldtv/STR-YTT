import requests
from bs4 import BeautifulSoup
import datetime
import streamlink

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

m3u8_file = open("lista2str2.m3u", "w")

url = "https://tviplayer.iol.pt/"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

video_link = soup.find("a", href="/direto/TVI")["href"]
video_link = f"https://tviplayer.iol.pt{video_link}"

video_url = streamlink.streams(video_link)["best"].url if streamlink.streams(video_link) else None

programs = soup.find_all("div", class_="programCover")
program_names = [program.find_parent("div", class_="program").find("div", class_="titlePrograma").text for program in programs]
program_images = [program["style"].split("url(")[1].split(")")[0] for program in programs]

for name, image in zip(program_names, program_images):
    m3u8_file.write(f"#EXTINF:-1 group-title=\"TVI PLAYER\" tvg-logo=\"{image}\",{name}\n{video_url}\n")
    m3u8_file.write("\n")

m3u8_file.close()
