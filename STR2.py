import os
import subprocess

def run_command(command):
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    output, error = process.communicate()
    return output.decode().strip(), error.decode().strip()

def install_yt_dlp():
    os.system("sudo wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp")
    os.system("sudo chmod a+rx /usr/local/bin/yt-dlp")

def install_youtube_dl():
    os.system("sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl")
    os.system("sudo chmod a+rx /usr/local/bin/youtube-dl")
    os.system("youtube-dl -U")

def install_streamlink():
    os.system("pip install --user --upgrade streamlink")

def get_lista4_m3u8():
    with open("./BLINK182.m3u", "w") as f:
        f.write("#EXTM3U\n")
        f.write("#EXT-X-VERSION:3\n")
        f.write("#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000\n")
        f.write('#EXTINF:-1 tvg-id="$(yt-dlp --get-title https://www.youtube.com/watch?v=EeQnkxY9QFs)" group-title="Reality Show\'S Live" group-title="CNN\'s" tvg-logo="$(yt-dlp --get-thumbnail https://www.youtube.com/watch?v=EeQnkxY9QFs)", YOUTUBEAOVIVO - $(yt-dlp --get-title https://www.youtube.com/watch?v=EeQnkxY9QFs)\n')
        f.write("$(streamlink --url --default-stream  --stream-url  https://www.youtube.com/@TelemundoEntretenimiento/live best)\n")
        f.write("#EXTM3U\n")
        f.write("#EXT-X-VERSION:3\n")
        f.write("#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000\n")
        f.write('#EXTINF:-1 tvg-id="$(youtube-dl --get-id https://www.dailymotion.com/video/x82pp99)" tvg-logo="$(youtube-dl --get-thumbnail https://www.dailymotion.com/video/x82pp99)",$(youtube-dl -e -C https://www.dailymotion.com/video/x82pp99) TV BRASIL\n')
        f.write("$(streamlink --url --default-stream  --stream-url  https://www.dailymotion.com/video/x82pp99 best)\n")

def main():
    install_yt_dlp()
    install_youtube_dl()
    install_streamlink()


if __name__ == '__main__':
    main()

