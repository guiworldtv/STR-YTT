import os
import sys
import pytz
import datetime
try:
    import streamlink
except ImportError:
    os.system("pip install --user --upgrade streamlink")

try:
    import youtube_dl
    import requests
    import beautifulsoup4
    import fastapi
    import uvicorn
    import schedule
    import selenium

except ImportError:
    os.system("pip install youtube-dl requests beautifulsoup4 fastapi uvicorn schedule selenium datetime")


def main():
    os.system("touch ./BBMEXICOUSA.ts")
    os.system("sudo cat >./BBMEXICOUSA.ts <<EOL")

    # Obtenha a hora atual no fuso horário de São Paulo
    tz = pytz.timezone("America/Sao_Paulo")
    hora_atual = datetime.datetime.now(tz).strftime("%d%m_%H%M%S")

    streamlink_command_1 = "streamlink --force --hls-duration 00:04:00 --output "
    streamlink_command_1 += f"\"GRAVADOS/{hora_atual}_CBSTELEMUNDO_.ts\" https://www.youtube.com/@TelemundoEntretenimiento/live best"
    os.system(streamlink_command_1)

    streamlink_command_2 = "streamlink --force --hls-duration 00:07:00 --output "
    streamlink_command_2 += f"\"GRAVADOS/{hora_atual}_CBSNEWS_.ts\" https://www.cbsnews.com/live/ best"
    os.system(streamlink_command_2)

    streamlink_command_3 = "streamlink --force --hls-duration 00:07:00 --output "
    streamlink_command_3 += f"\"GRAVADOS/{hora_atual}_CNNPORTUGAL.ts\" https://tviplayer.iol.pt/direto/CNN best"
    os.system(streamlink_command_3)

if __name__ == "__main__":
    main()
