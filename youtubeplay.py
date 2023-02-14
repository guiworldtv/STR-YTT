import streamlink
import subprocess
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# Configuring Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Instanciando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# URL da página desejada
url_twitch = "https://www.youtube.com/results?search_query=aula&sp=CAISBBABGAI%253D"

# Abrir a página desejada
driver.get(url_twitch)

# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(5)

# Scroll to the bottom of the page using ActionChains
while True:
    try:
        # Find the last video on the page
        last_video = driver.find_element_by_xpath("//a[@class='ScCoreLink-sc-16kq0mq-0 jKBAWW tw-link'][last()]")
        # Scroll to the last video
        actions = ActionChains(driver)
        actions.move_to_element(last_video).perform()
        time.sleep(1)
    except:
        break
        
        
# Get the page source again after scrolling to the bottom
html_content = driver.page_source

# Find the links and titles of the videos found
try:
    soup = BeautifulSoup(html_content, "html.parser")
    videos = soup.find_all("a", id="video-title", class_="yt-simple-endpoint style-scope ytd-video-renderer")
    links = ["https://www.youtube.com" + video.get("href") for video in videos]
    titles = [video.get("title") for video in videos]
    thumbnails = []
    for video in videos:
        thumbnail_tag = video.find("yt-image")
        if thumbnail_tag:
            thumbnail = thumbnail_tag.find("img")["src"]
        else:
            thumbnail = ""
        thumbnails.append(thumbnail)
except Exception as e:
    print(f"Erro: {e}")
finally:
    # Close the driver
    driver.quit()




# Instalando streamlink
subprocess.run(['pip', 'install', '--user', '--upgrade', 'streamlink'])

# Get the playlist and write to file
try:
    with open('./YOUTUBEPLAY.m3u', 'w') as f:
        f.write("#EXTM3U\n")  # Imprime #EXTM3U uma vez no início do arquivo
        for i, link in enumerate(links):
            # Get the stream information using streamlink
            streams = streamlink.streams(link)
            url = streams['best'].url
            # Write the stream information to the file
            title = titles[i]
            thumbnail = thumbnails[i]
            f.write(f"#EXTINF:-1 tvg-logo=\"{thumbnail}\" group-title=\"YOUTUBE\",{title}\n")
            f.write(f"{url}\n\n")
except Exception as e:
    print(f"Erro: {e}")
