import requests
from bs4 import BeautifulSoup
import streamlink

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

m3u8_file = open("lista2str2.m3u", "w")

# Request the main page
url = "https://tviplayer.iol.pt/"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Find all program links
program_links = [f"https://tviplayer.iol.pt{item['href']}" for item in soup.find_all("a", href=lambda x: x and x.startswith("/programa"))]

# Visit each program page
for program_link in program_links:
    program_response = requests.get(program_link, headers=headers)
    program_soup = BeautifulSoup(program_response.content, "html.parser")
    
    # Find the first video link
    video_link = f"https://tviplayer.iol.pt{program_soup.find('a', class_='item')['href']}"
    
    # Get video details
    video_url = streamlink.streams(video_link)["best"].url if streamlink.streams(video_link) else None
    try:
        image_url = program_soup.find('a', class_='item')['style'].split("url(")[1].split(")")[0]
    except Exception as e:
        print(f"Error: {e}")
        image_url = "https://cdn.iol.pt/img/logostvi/branco/tviplayer.png"
    title = program_soup.find('span', class_='item-program-title').text
    
    # Write to the m3u8 file
    if video_url:
        m3u8_file.write(f"#EXTINF:-1 group-title=\"TVI PLAYER\" tvg-logo=\"{image_url}\",{title}\n{video_url}\n")
        m3u8_file.write("\n")

m3u8_file.close()
