#! /usr/bin/python3

banner = r'''
###########################################################################
#                                                                         #

#                                  >> https://github.com/guiworldtv       #
###########################################################################




#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1 group-title="CHILE" tvg-logo="https://i.imgur.com/qLzjO1U.png",065 Mega SD
https://unlimited1-cl-isp.dps.live/mega/mega.smil/playlist.m3u8



#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1 group-title="CHILE" ,CHVNOTICIAS_PLUTOTV
https://siloh-latam-aka.plutotv.net/lilo/production/Chilevision/master.m3u8




#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
#EXTINF:-1  group-title="CHILE" tvg-logo="https://fotos.subefotos.com/ae8059a01777a066979869891e176077o.png",T13
https://unlimited2-cl-isp.dps.live/t13/t13.smil/playlist.m3u8

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


#EXTINF:-1 tvg-name="Mega" tvg-logo="https://lh3.googleusercontent.com/-xqKe__ypgDY/XnzFn9NLnbI/AAAAAAAAxMU/2Wj9IOC1LaQxtJGRzcVOTrQWxP9z3RgPwCK8BGAsYHg/s0/2020-03-26.png" group-title="CHILE",Mega
https://unlimited1-cl-isp.dps.live/mega/mega.smil/playlist.m3u8

#EXTINF:-1 tvg-name="CHV Noticias" tvg-logo="https://i2.paste.pics/5bf0db1521a041595f387a893ab6512b.png" group-title="CHILE",Chile Vision Noticias
https://siloh-latam-aka.plutotv.net/lilo/production/Chilevision/master.m3u8

#EXTINF:-1 tvg-name="" tvg-logo="" group-title="CHILE",Universidade Católica Chilena1
https://unlimited1-cl-isp.dps.live/ucvtv2/ucvtv2.smil/playlist.m3u8?DVR

#EXTINF:-1 tvg-name="" tvg-logo="" group-title="CHILE",Universidade Católica Chilena2
https://unlimited2-cl-isp.dps.live/ucvtveventos/ucvtveventos.smil/playlist.m3u8?DVR

#EXTINF:-1, Canal 13 Entretencion
https://unlimited1-cl-isp.dps.live/13e/13e.smil/playlist.m3u8

#EXTINF:-1, Canal 13 Teleseries
https://unlimited1-us.dps.live/13t/13t.smil/playlist.m3u8

#EXTINF:-1, Canal 13 Prime
https://unlimited1-us.dps.live/13p/13p.smil/playlist.m3u8


'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/guiworldtv/MEU-IPTV-FULL/main/VideoOFFAir.m3u8')
                return
            os.system(f'wget {url} -O temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/guiworldtv/MEU-IPTV-FULL/main/VideoOFFAir.m3u8')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/cl/mi.tv.epg.xmll"')
print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/cl/gatotv.com.epg.xml"')
print(banner)
#s = requests.Session()
with open('../CHILE.txt', errors="ignore") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
    
    
