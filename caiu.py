#!/usr/bin/env python

import pytz
from datetime import datetime


import os
import sys

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
    import datetime
    import pytz
except ImportError:
    os.system("pip install youtube-dl requests beautifulsoup4 fastapi uvicorn schedule selenium datetime pytz")

tz = pytz.timezone("America/Sao_Paulo")
timestamp = datetime.now(tz).strftime("%d%m_%H%M%S_%Y")


def main():
    os.system("touch ./BBMEXICOUSA.ts")
    os.system("sudo cat >./BBMEXICOUSA.ts <<EOL")

    streamlink_command_1 = "streamlink --force --hls-duration 00:00:15 --output "
    streamlink_command_1 += "\"GRAVADOS/$(date +%d%m)_$(date +%H%M%S)_CBSTELEMUNDO_-$(date +%Y).ts\" https://www.youtube.com/@TelemundoEntretenimiento/live best"
    os.system(streamlink_command_1)

    streamlink_command_2 = "streamlink --force --hls-duration 00:00:15 --output "
    streamlink_command_2 += "\"GRAVADOS/$(date +%d%m)_$(date +%H%M%S)_GLOBONEWS_-$(date +%Y).ts\" https://www.cbsnews.com/live/ best"
    os.system(streamlink_command_2)

    streamlink_command_3 = "streamlink --force --hls-duration 00:00:15 --output "
    streamlink_command_3 += "\"GRAVADOS/CNNPORTUGAL.ts\" https://tviplayer.iol.pt/direto/CNN best best"
    os.system(streamlink_command_3)

if __name__ == "__main__":
    main()
