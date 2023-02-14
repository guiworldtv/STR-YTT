import streamlink
import subprocess
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options




# URL da página desejada
url_twitch = "https://www.twitch.tv/search?term=big%20brother"

 # Configuring Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Instanciando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# Abrir a página desejada
driver.get(url_twitch)

# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(5)

# Obter o conteúdo da página
html_content = driver.page_source

# Encontrar o link do primeiro canal encontrado
soup = BeautifulSoup(html_content, "html.parser")
link = "https://www.twitch.tv" + soup.find("a", class_="ScCoreLink-sc-16kq0mq-0 eYjhIv tw-link").get("href")

# Fechar o driver
driver.quit()

print(link)

# Instalando streamlink
subprocess.run(['pip', 'install', '--user', '--upgrade', 'streamlink'])

    
try:
    # Get LISTA4.m3u8
    with open('./BBVIPALBANIA.m3u8', 'w') as f:
        streams = streamlink.streams(link)
        url = streams['best'].url
        f.write("#EXTM3U\n")
        f.write("#EXT-X-VERSION:3\n")
        f.write("#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000\n")
        f.write(f"{url}\n")
except Exception as e:
    print(f"Erro ao criar o arquivo .m3u8: {e}")
    
    
