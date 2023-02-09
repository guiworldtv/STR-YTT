import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

m3u8_file = open("youtube_videos.m3u", "w")

url = "https://www.youtube.com/results?search_query=aula&sp=CAISBBABGAI%253D"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

video_links = [f"https://www.youtube.com{item['href']}" for item in soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-video-renderer", limit=6)]
video_titles = [item["aria-label"] for item in soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-video-renderer", limit=6)]
video_images = [f"https://i.ytimg.com/vi/{link.split('=')[1]}/hq720.jpg" for link in video_links]

for title, link, image in zip(video_titles, video_links, video_images):
    m3u8_file.write(f"#EXTINF:-1 group-title=\"YouTube Videos\",{title}\n{link}\n")
    m3u8_file.write(f"tvg-logo={image}\n")
    m3u8_file.write("\n")

m3u8_file.close()
