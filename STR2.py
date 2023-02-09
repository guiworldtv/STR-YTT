import streamlink
import moviepy.editor as mp
import time

# URL do stream
url = "https://hunq9fz8yk.zoeweb.tv/av85/av85.stream/chunklist_w123426081.m3u8"

# Tempo de captura de cada frame (em segundos)
capture_time = 5

# Número de frames a serem capturados
num_frames = 60

# Iniciar o stream
streams = streamlink.streams(url)
stream = streams["best"]

# Iniciar a captura de frames
frames = []
for i in range(num_frames):
    frame = stream.get_frames()
    frames.append(frame)
    time.sleep(capture_time)

# Criar o vídeo a partir dos frames capturados
clip = mp.ImageSequenceClip(frames, fps=1 / capture_time)
clip.write_videofile("timelapse.mp4")
