import os
import subprocess
import sys

def run_command(command):
    """
    Executa um comando e retorna a saída e o erro.
    """
    try:
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        output, error = process.communicate()
        return output.decode().strip(), error.decode().strip()
    except Exception as e:
        print("Erro ao executar comando:", e)
        sys.exit(1)

def install_dependency(dependency_name, dependency_url, binary_path):
    """
    Instala uma dependência a partir de uma URL e define permissões de execução.
    """
    try:
        os.system(f"wget {dependency_url} -O {binary_path}")
        os.system(f"chmod a+rx {binary_path}")
    except Exception as e:
        print(f"Erro ao instalar {dependency_name}:", e)
        sys.exit(1)

def install_yt_dlp():
    """
    Instala o yt-dlp.
    """
    install_dependency("yt-dlp", "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp", "/usr/local/bin/yt-dlp")

def install_youtube_dl():
    """
    Instala o youtube-dl.
    """
    install_dependency("youtube-dl", "https://yt-dl.org/downloads/latest/youtube-dl", "/usr/local/bin/youtube-dl")
    try:
        os.system("youtube-dl -U")
    except Exception as e:
        print("Erro ao atualizar youtube-dl:", e)
        sys.exit(1)

def install_streamlink():
    """
    Instala o Streamlink usando o pip.
    """
    try:
        os.system("pip install --user --upgrade streamlink")
    except Exception as e:
        print("Erro ao instalar streamlink:", e)
        sys.exit(1)

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
        f.write("$(streamlink --url --default-stream  --stream-url https://www.nbcnews.com/now?icid=now_hp_header best)\n")

def main():
    run_command()
    install_dependency()
    install_yt_dlp()
    install_youtube_dl()
    install_streamlink()
    get_lista4_m3u8()
    
if __name__ == '__main__':
    main()
