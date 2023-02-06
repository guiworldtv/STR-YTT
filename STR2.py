import os
import subprocess
import sys
import logging

logger = logging.getLogger(__name__)

def run_command(command):
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    output, error = process.communicate()
    if process.returncode != 0:
        logger.error(f"Error running command: {command}. Error: {error}")
        return None, None
    return output.decode().strip(), error.decode().strip()

def install_dependencies():
    dependencies = ["yt-dlp", "youtube-dl", "streamlink"]
    for dependency in dependencies:
        if not run_command(f"which {dependency}")[0]:
            install_command = f"pip install {dependency}"
            os.system(install_command)

def write_m3u_header(f):
    f.write("#EXTM3U\n")
    f.write("#EXT-X-VERSION:3\n")

def write_m3u_entry(f, tvg_id, tvg_logo, title, stream_url):
    f.write("#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000\n")
    f.write(f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-logo="{tvg_logo}",{title}\n')
    f.write(stream_url + "\n")

def get_lista4_m3u8():
    youtube_url = "https://www.youtube.com/watch?v=EeQnkxY9QFs"
    dailymotion_url = "https://www.dailymotion.com/video/x82pp99"
    telemundo_url = "https://www.youtube.com/@TelemundoEntretenimiento/live"
    nbcnews_url = "https://www.nbcnews.com/now?icid=now_hp_header"
    file_path = "./BLINK182.m3u"

    if os.path.exists(file_path):
        logger.error(f"File already exists: {file_path}")
        return
    
    install_dependencies()
    
    try:
        with open(file_path, "w") as f:
            write_m3u_header(f)
            youtube_title = run_command(f"yt-dlp --get-title {youtube_url}")[0]
            if not youtube_title:
                raise Exception(f"Failed to get title for url: {youtube_url}")
            youtube_thumbnail = run_command(f"yt-dlp --get-thumbnail {youtube_url}")[0]
            if not youtube_thumbnail:
                raise Exception(f"Failed to get thumbnail for url: {youtube_url}
