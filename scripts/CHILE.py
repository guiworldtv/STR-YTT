#! /usr/bin/python3

from __future__ import unicode_literals
import youtube_dl
import requests
import shutil
from urllib.request import urlopen
from bs4 import BeautifulSoup
channel_no = 0
m3u = None
def get_live_info(channel_id):
    try:
        webpage = urlopen(f"{channel_id}").read()
        soup = BeautifulSoup(webpage, 'html.parser')
        urlMeta = soup.find("meta", property="og:url")
        if urlMeta is None:
            return None
        url = urlMeta.get("content")
        if(url is None or url.find("/watch?v=") == -1):
            return None
        titleMeta = soup.find("meta", property="og:title")
        imageMeta = soup.find("meta", property="og:image")
        descriptionMeta = soup.find("meta", property="og:description")
        return {
            "url": url,
            "title": titleMeta.get("content"),
            "image": imageMeta.get("content"),
            "description": descriptionMeta.get("content")
        }

    except Exception as e:
                return None



banner = r'''
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=5400000
'''

banner2 = r'''
###########################################################################
#                                                                         #

    
          
            
    

          
          
            
    

          
    
    @@ -168,83 +130,60 @@ def get_live_info(channel_id):
  
#                                  >> https://github.com/guiworldtv       #
###########################################################################
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1,052 24 HORAS
http://45.181.121.57:8111/play/052
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1,054 CNN Chile
http://45.181.121.57:8111/play/054
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1,062 La Red HD
http://45.181.121.57:8111/play/062
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1,064 TVN HD
http://45.181.121.57:8111/play/064
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1,065 Mega
http://45.181.121.57:8111/play/065
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1,065 Mega SD
https://unlimited1-cl-isp.dps.live/mega/mega.smil/playlist.m3u8
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1,066 CHV HD
http://45.181.121.57:8111/play/066
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1,067 Canal 13
http://45.181.121.57:8111/play/067
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1,CHVNOTICIAS_PLUTOTV
https://siloh-latam-aka.plutotv.net/lilo/production/Chilevision/master.m3u8
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1  group-title="CHILE" tvg-logo="https://i.postimg.cc/VvRHKwjz/Logo-C24-H.png",CANAL 24 HORAS
https://marine2.miplay.cl/24horas/index.m3u8
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1  group-title="CHILE" tvg-logo="https://fotos.subefotos.com/ae8059a01777a066979869891e176077o.png",T13
https://unlimited2-cl-isp.dps.live/t13/t13.smil/playlist.m3u8
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1  group-title="CHILE" tvg-logo="https://i.postimg.cc/nxSxgp1k/Logo-MEGANOTICIAS.png",MEGANOTICIAS
https://mdstrm.com/live-stream-playlist-v/561430ae330428c223687e1e.m3u8
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1  group-title="CHILE" tvg-logo="https://i.postimg.cc/VvRHKwjz/Logo-C24-H.png",24 PLAY
http://mdstrm.com/live-stream-playlist-v/57d1a22064f5d85712b20dab.m3u8
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1  group-title="CHILE" tvg-logo="https://im2.ezgif.com/tmp/ezgif-2-cbd343be23.png",CHV NOTICIAS
https://siloh.pluto.tv/lilo/production/Chilevision/master_1.m3u8
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1  group-title="CHILE" tvg-logo="N/A",CNN INTERNACIONAL
https://cnn-cnninternational-1-gb.samsung.wurl.com/manifest/playlist.m3u8
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1  group-title="CHILE" tvg-logo="N/A",tv saúde - chile
https://srv3.zcast.com.br/mastermedia/mastermedia/playlist.m3u8
#EXTINF:-1 tvg-name="Camara de Diputados" tvg-logo="https://i2.paste.pics/8ac54ede0184c4fd9e872231a6d673b3.png" group-title="CHILE",Camara de Diputados
https://tls-cl.cdnz.cl/camara/live/playlist.m3u8
#EXTINF:-1 tvg-name="TV Senado" tvg-logo="https://i2.paste.pics/ee6b562807f06f0139f28cd160a82a8f.png" group-title="CHILE",TV Senado
https://janus-tv-ply.senado.cl/playlist/playlist.m3u8
#EXTINF:-1 tvg-name="Cultura Online" tvg-logo="https://i2.paste.pics/a64816b3950330d38cae04c477929f3f.png" group-title="CHILE",Cultura Online
https://v1.tustreaming.cl:19360/culturaonline/culturaonline.m3u8
#EXTINF:-1 tvg-name="TV+" tvg-logo="https://lh3.googleusercontent.com/-OyqOBTEx-1E/XyA3AZwIgTI/AAAAAAAA3jQ/aDMZaLOx3mQuXBqjDKAF0X7dxExKFzawACK8BGAsYHg/s0/2020-07-28.png" group-title="CHILE",TV+
https://mdstrm.com/live-stream-playlist/5c0e8b19e4c87f3f2d3e6a59.m3u8
#EXTINF:-1 tvg-name="TVN" tvg-logo="https://lh3.googleusercontent.com/-ETprzEeH-JY/XbCxYXbNQUI/AAAAAAAArkw/zQxemFrwNjAbMoyByyr_sesnZ8QKgap-QCK8BGAsYHg/s0/2019-10-23.png" group-title="CHILE",TVN
https://marine2.miplay.cl/tvn/playlist.m3u8
#EXTINF:-1 tvg-name="TVN - 24h" tvg-logo="https://lh3.googleusercontent.com/-ETprzEeH-JY/XbCxYXbNQUI/AAAAAAAArkw/zQxemFrwNjAbMoyByyr_sesnZ8QKgap-QCK8BGAsYHg/s0/2019-10-23.png" group-title="CHILE",TVN - 24h
http://mdstrm.com/live-stream-playlist-v/5346f5f2c1e6f5810b5b9df0.m3u8
#EXTINF:-1 tvg-name="TVN - Reuters" tvg-logo="https://lh3.googleusercontent.com/-ETprzEeH-JY/XbCxYXbNQUI/AAAAAAAArkw/zQxemFrwNjAbMoyByyr_sesnZ8QKgap-QCK8BGAsYHg/s0/2019-10-23.png" group-title="CHILE",TVN - Reuters
https://mdstrm.com/live-stream-playlist/5346f657c1e6f5810b5b9df3.m3u8
#EXTINF:-1 tvg-name="Mega" tvg-logo="https://lh3.googleusercontent.com/-xqKe__ypgDY/XnzFn9NLnbI/AAAAAAAAxMU/2Wj9IOC1LaQxtJGRzcVOTrQWxP9z3RgPwCK8BGAsYHg/s0/2020-03-26.png" group-title="CHILE",Mega
https://unlimited1-cl-isp.dps.live/mega/mega.smil/playlist.m3u8
#EXTINF:-1 tvg-name="CHV Noticias" tvg-logo="https://i2.paste.pics/5bf0db1521a041595f387a893ab6512b.png" group-title="CHILE",Chile Vision Noticias
https://siloh-latam-aka.plutotv.net/lilo/production/Chilevision/master.m3u8
#EXTINF:-1 tvg-name="" tvg-logo="" group-title="CHILE",Universidade Católica Chilena1
https://unlimited1-cl-isp.dps.live/ucvtv2/ucvtv2.smil/playlist.m3u8?DVR
#EXTINF:-1 tvg-name="" tvg-logo="" group-title="CHILE",Universidade Católica Chilena2
https://unlimited2-cl-isp.dps.live/ucvtveventos/ucvtveventos.smil/playlist.m3u8?DVR
'''

def generate_youtube_tv():
    global channel_no
    ydl_opts = {
        'format': 'best',
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)

    with open('../CHILE.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            channel = get_live_info(line)
            if channel is None:
                continue
            try:
                with ydl:
                    result = ydl.extract_info(
                        f"{line}",
                        download=False  # We just want to extract the info
                    )

                    if 'entries' in result:
                        # Can be a playlist or a list of videos
                        video = result['entries'][-1]
                    else:
                        # Just a video
                        video = result
                video_url = video['url']

                channel_no += 1
                channel_name = f"{channel_no}-{line.split('/')[-1]}"
                playlistInfo = f"#EXTINF:-1 tvg-chno=\"{channel_no}\" tvg-id=\"{line}\" tvg-name=\"{channel_name}\" tvg-logo=\"{channel.get('image')}\" group-title=\"ARGENTINA\",{channel.get('title')}\n"                
                write_to_playlist(video_url)
                write_to_playlist("\n")
            except Exception as e:
                print(e)




def write_to_playlist(content):
    global m3u    
    m3u.write(content)


def create_playlist():
    global m3u
    m3u = open("../CHILE.txt", "w")
    m3u.write("#EXTM3U")
    m3u.write("\n")


def close_playlist():
    global m3u
    m3u.close()
def generate_youtube_PlayList():
    create_playlist()

    print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/cl/mi.tv.epg.xmll"')
    print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/cl/gatotv.com.epg.xml"')
    m3u.write(banner)

    generate_youtube_tv()

    m3u.write(banner2)





    close_playlist()



if __name__ == '__main__':
    generate_youtube_PlayList()   
