#! /usr/bin/python3

banner1 = r'''
###########################################################################
#                                                                         #
#                                  >> https://github.com/guiworldtv       #
###########################################################################

#EXTM3U

#EXTINF:-1 tvg-chno="2" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/6/63/Repretel_2_CDR.png",Canal 2 CDR
http://190.7.192.164:8004/play/s46

#EXTINF:-1 tvg-chno="4" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Repretel_4_logo.png/1200px-Repretel_4_logo.png",Canal 4 Repretel
https://d3bgcstab9qhdz.cloudfront.net:443/hls/canal4_720.m3u8

#EXTINF:-1 tvg-chno="6" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Repretel_6_logo.png/768px-Repretel_6_logo.png",Canal 6 Repretel
http://190.7.192.164:8002/play/s11

#EXTINF:-1 tvg-chno="7" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Teletica_Logo.png/670px-Teletica_Logo.png",Teletica
http://45.90.105.74:25461/live/budtvsports/wTu27rKVNU/18621.m3u8

#EXTINF:-1 tvg-chno="8" tvg-logo="https://pbs.twimg.com/profile_images/1510311834800246787/sfWgWmqk.jpg",Canal 8 Multimedios
https://mdstrm.com/live-stream-playlist/5a7b1e63a8da282c34d65445.m3u8

#EXTINF:-1 tvg-chno="9" tvg-logo="https://www.canal9.cr/IMAGES/Logo%20Canal%209%202D%20Color.png",Canal 9 CR
http://201.201.149.86:8080/livestream/stream.m3u8

#EXTINF:-1 tvg-chno="10" tvg-logo="https://static3.teletica.com/Files/Sizes/2017/10/20/img_teletica_radio_780x520-33655625_380x260.jpg",Teletica Radio
https://m6gdar5eyn93-hls-live.5centscdn.com:443/TeleticaRadio/5444e8d6d0436ccb78704882f542e5ac.sdp/TeleticaRadio/StreamExterno1/chunks.m3u8

#EXTINF:-1 tvg-chno="11" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Repretel_11_logo.png/150px-Repretel_11_logo.png",Canal 11 Repretel
https://d3bgcstab9qhdz.cloudfront.net:443/hls/canal11_720.m3u8

#EXTINF:-1 tvg-chno="13" tvg-logo="https://i0.wp.com/directostv.teleame.com/wp-content/uploads/2016/06/canal-trece-costa-rica.png?resize=500%2C300&ssl=1",Canal 13 Sinart
http://45.228.232.204:16000/play/a03q/index.m3u8

#EXTINF:-1 tvg-chno="14" tvg-logo="https://pbs.twimg.com/profile_images/1314328513349144577/7dTHR_gg.jpg",Tv Sur Canal 14
https://5bf8041cb3fed.streamlock.net:443/TVSURCANAL14/TVSURCANAL14/chunklist_w2106647137.m3u8

#EXTINF:-1 tvg-chno="15" tvg-logo="https://www.ucr.ac.cr/medios/fotos/pri_xx-large/2007/logo_canal_15_Oct_2007.jpg",Canal 15 UCR
http://163.178.170.127:1935/quinceucr/quinceucr/playlist.m3u8

#EXTINF:-1 tvg-chno="16" tvg-logo="https://i0.wp.com/directostv.teleame.com/wp-content/uploads/2018/07/san-jose-tv-costa-rica.png",San José TV
https://rtmp.info:443/sanjosetv/envivo/chunklist_w1786370191.m3u8

#EXTINF:-1 tvg-chno="17" tvg-logo="https://www.radioextremacr.com/img/logo.png",Extrema TV
https://627bb251f23c7.streamlock.net:444/ExtremaTV/ExtremaTV/playlist.m3u8

#EXTINF:-1 tvg-chno="18" tvg-logo="https://costaricatelevision.com/sites/default/files/2022-09/_Telered%252520Television.png",Telered
http://k4.usastreams.com:80/ARBtv/teleplus/chunklist_w160108401.m3u8

#EXTINF:-1 tvg-chno="19" tvg-logo="https://mastelevisioncr.com/wp-content/uploads/2022/05/cropped-cropped-WhatsApp-Image-2020-08-02-at-12.42.47-300x300-1-150x150.jpeg",Telesistema
https://59ef525c24caa.streamlock.net/ARBtv/ARBtv/chunklist_w1753795779.m3u8

#EXTINF:-1 tvg-chno="20" tvg-logo="https://geomedios.fcs.ucr.ac.cr/wp-content/uploads/2019/12/49174364_1931189920267968_6676580851234373632_o.jpg",Teleuno
https://5d16127744872.streamlock.net:443/TVUNO/TVUNO/chunklist_w766285163.m3u8

#EXTINF:-1 tvg-chno="21" tvg-logo="https://i0.wp.com/directostv.teleame.com/wp-content/uploads/2022/09/Trivisio%CC%81n-Canal-36-en-vivo-Online.png",Trivisión Canal 36
https://liveingesta119.cdnmedia.tv:443/trivision36live/dvrlive-1500/chunklist.m3u8?DVR

#EXTINF:-1 tvg-chno="22" tvg-logo="https://i0.wp.com/directostv.teleame.com/wp-content/uploads/2016/06/Extra-TV.png",Extra Tv 42
http://177.234.254.38:8000/play/a02j/index.m3u8

#EXTINF:-1 tvg-chno="24" tvg-logo="https://www.tvn14.com/wp-content/uploads/2021/02/TVN-HD_LOGO_COLOR-SIN-FONDO.png",TVN 14 San Carlos
http://tvn.obix.tv:1935/TVN/CH14.stream_720p/chunklist_w1881922243.m3u8

#EXTINF:-1 tvg-chno="25" tvg-logo="https://i2.paste.pics/cbcfd98188337b1bf79a92b1afb60ad3.png",San Vito TV
https://stmv.streamingvip.click/sanvitotv/sanvitotv/playlist.m3u8

#EXTINF:-1 tvg-chno="26" tvg-logo="https://www.tvsantacruzcr.net/img/logotvsc_2.png",Santa Cruz TV
https://rtmp.info/tvsantacruz/envivo/playlist.m3u8

#EXTINF:-1 tvg-chno="27" tvg-logo="https://i2.paste.pics/e82bca2c48209fe7ff1a9a559f36689f.png",Cartago TV
http://vip.hispanotv.org:80/live/acevedo22/acevedo22/283547.m3u8

#EXTINF:-1 tvg-chno="28" tvg-logo="https://mir-s3-cdn-cf.behance.net/project_modules/max_632/cf47d1109272269.5fd018f6d6a01.jpg",Noticias en Linea CR
https://rtmp.info/noticiasenlineatv/envivo/playlist.m3u8

#EXTINF:-1 tvg-chno="30" tvg-logo="https://i2.paste.pics/3238d7371f23b09198d794d2979411b9.png",Nicoya TV
https://59ef525c24caa.streamlock.net:443/nicoyatv/nicoyatv/chunklist_w221500905.m3u8

#EXTINF:-1 tvg-chno="31" tvg-logo="https://i2.paste.pics/b89953d1d7327bb67304a18eb0bc354a.png",Tica Visión
https://62fc643fbf1aa.streamlock.net:443/HBTV/HBTV/chunklist_w1022063060.m3u8

#EXTINF:-1 tvg-chno="32" tvg-logo="https://i2.paste.pics/dd383084a4c255e8445fb60f9001b9e6.png",Canal Tv +
https://59ef525c24caa.streamlock.net/Tvpluscr/Tvpluscr/playlist.m3u8

#EXTINF:-1 tvg-chno="33" tvg-logo="https://i2.paste.pics/0965c9e6c38022659717eeaac157e453.png",Canal Norte Informativo
https://videohd.live:19360/8076/8076.m3u8

#EXTINF:-1 tvg-chno="34" tvg-logo="https://i0.wp.com/directostv.teleame.com/wp-content/uploads/2017/10/telesur-costa-rica.png",Telesur CR
https://stmv.streamingvip.click:443/telesur/telesur/chunklist_w935279612.m3u8

#EXTINF:-1 tvg-chno="35" tvg-logo="https://serenotv.com/wp-content/uploads/2022/05/Canal-multizonas-en-vivo-300x238.jpeg",Canal Multizonas TV
https://cloudvideo.servers10.com:8081/8214/index.m3u8

#EXTINF:-1 tvg-chno="36" tvg-logo="https://i2.paste.pics/e82bca2c48209fe7ff1a9a559f36689f.png",Cartago Medios
https://tvdatta.com:3384/live/cartagomedioslive.m3u8

#EXTINF:-1 tvg-chno="37" tvg-logo="http://costaricatelevision.com/sites/default/files/styles/tv_list/public/2022-09/stv-sarapiquitv-costa-rica.png.webp?itok=srO54ZBa",Sarapiquí TV
https://lstv.duckdns.org:449/hls/stv.m3u8

#EXTINF:-1 tvg-chno="38" tvg-logo="https://image.roku.com/developer_channels/prod/cb20a7cb94abfe34e8aec64a16664d6ea8330cec1c1bddcfe23f139e5b274d4f.png",Telebrunca CR
http://k4.usastreams.com/telebrunca/telebrunca/playlist.m3u8

#EXTINF:-1 tvg-chno="39" tvg-logo="https://www.doutico.com/wpimages/wpd2c31b06_05_06.jpg",Guatuso TV
https://5cf4a2c2512a2.streamlock.net:443/8162/8162/chunklist_w1967293068.m3u8

#EXTINF:-1 tvg-chno="40" tvg-logo="https://moratvonline.com//assets/img/moratv.png",Mora TV
https://stmv1.zcastbr.com:443/moratv1/moratv1/chunklist_w1410193899.m3u8

#EXTINF:-1 tvg-chno="41" tvg-logo="https://i2.paste.pics/e71dbd173c7d1e13f92e019c7a9ac89f.png",Canal 9 Tv Sur
https://5d16127744872.streamlock.net:443/TVSUR/TVSUR/chunklist_w149460811.m3u8

#EXTINF:-1 tvg-chno="42" tvg-logo="https://geomedios.fcs.ucr.ac.cr/wp-content/uploads/2019/07/Limon_TV_Logo.png",Limón TV
http://k4.usastreams.com/limontv1/limontv1/playlist.m3u8

#EXTINF:-1 tvg-chno="43" tvg-logo="http://costaricatelevision.com/sites/default/files/styles/tv_list/public/2022-09/los-santos-tv-costa-rica.png.webp?itok=ki81X3MW",Los Santos TV
https://lstv.duckdns.org:449/hls/lstv.m3u8

#EXTINF:-1 tvg-chno="44" tvg-logo="https://pbs.twimg.com/profile_images/1563188156630982656/hG2sn8s-.jpg",Tica TV +
https://cloudvideo.servers10.com:8081/8030/index.m3u8

#EXTINF:-1 tvg-chno="45" tvg-logo="https://i2.paste.pics/83fb31ad5340bda41b8e6f5930e1d4fc.png",TV Curre PZ
http://k6.usastreams.online/Tvcurre/Tvcurre/playlist.m3u8?fbclid=IwAR3riiUSzxi-bKYUwIW_yy3mpK3ZuejRq5beBdOLmHmm9YJ-C1LoDZIF8IM

#EXTINF:-1 tvg-chno="46" tvg-logo="https://www.retroplustv.com/wp-content/uploads/2022/03/logo_1.png",Retroplus 3
https://59f1cbe63db89.streamlock.net:1443/retroplussenal3/_definst_/retroplussenal3/chunklist_w893080974.m3u8

#EXTINF:-1 tvg-chno="50" tvg-logo="https://i2.paste.pics/580c3e6758f8535bbacfb32fa3155259.png",Humor TV 24/7 CR
https://srv.panelcast.net/humor247/humor247/playlist.m3u8

#EXTINF:-1 tvg-chno="51" tvg-logo="https://dreikotv.online/wp-content/uploads/2021/09/cropped-logo-dreiko-arts-TV-2020.png",Dreiko Tv CR
https://stmv3.voxtvhd.com.br/dreikotv/dreikotv/playlist.m3u8

#EXTINF:-1 tvg-chno="52" tvg-logo="https://www.doutico.com/wpimages/wpe9343c85_05_06.jpg",Canal Pura Vida
https://cp.panelchs.com:1936/84598/84598/chunklist_w1217069703.m3u8

#EXTINF:-1 tvg-chno="54" tvg-logo="https://i2.paste.pics/c62d925b201bdb9d034e4d582d62abf2.png",MZ Sports HD
https://cloudvideo.servers10.com:8081/8248/tracks-v1a1/mono.m3u8

#EXTINF:-1 tvg-chno="55" tvg-logo="https://static.mytuner.mobi/media/tvos_radios/D8WaYFxSEv.png",RBM TV 1
https://stmv.streamingvip.click:443/television/television/chunklist_w358875487.m3u8

#EXTINF:-1 tvg-chno="56" tvg-logo="https://static.mytuner.mobi/media/tvos_radios/D8WaYFxSEv.png",RBM TV 2
https://stmv.streamingvip.click:443/rbmtv2/rbmtv2/chunklist_w649736912.m3u8

#EXTINF:-1 tvg-chno="60" tvg-logo="https://vmlatino.com/wp-content/uploads/2022/03/VM-LATINO-transp.png",VM Latino
https://59ef525c24caa.streamlock.net/vmtv/vmlatino/playlist.m3u8

#EXTINF:-1 tvg-chno="61" tvg-logo="https://i2.paste.pics/ade26f32ba4868798ef1593a34e57ef7.png",Soy Plancha TV
https://59ef525c24caa.streamlock.net:443/vmtv/soyplancha/chunklist_w1610921083.m3u8

#EXTINF:-1 tvg-chno="62" tvg-logo="https://www.canal38cr.com/wp-content/uploads/2019/10/cropped-Logo-Nuevo-400.jpg",Canal 38
https://rtmp.info:443/canal38/envivo/chunklist_w1890885019.m3u8

#EXTINF:-1 tvg-chno="63" tvg-logo="https://canal1cr.com/wp-content/uploads/2022/02/cropped-Canal-1-1.png",Canal 1 CR
https://59ef525c24caa.streamlock.net:443/canal1cr/canal1cr/chunklist_w183311120.m3u8

#EXTINF:-1 tvg-chno="64" tvg-logo="https://www.88stereo.com/wp-content/uploads/2017/05/88Stereo-logoweb.png",88 Estéreo
http://k3.usastreams.com:80/CableLatino/88stereo/chunklist_w190584519.m3u8

#EXTINF:-1 tvg-chno="65" tvg-logo="https://i2.paste.pics/ef00f6c7d85171624dff85e2c38fc975.png",Colosal TV
http://tv.ticosmedia.com:1935/COLOSAL/COLOSAL/chunklist_w534755227.m3u8

#EXTINF:-1 tvg-chno="66" tvg-logo="https://i2.paste.pics/0c73fe6bc691b4aa4d1ac9cc3f93e500.png",Urbano TV
https://59ef525c24caa.streamlock.net:443/tvurbano/tvurbano/chunklist_w248233257.m3u8

#EXTINF:-1 tvg-chno="67" tvg-logo="https://i0.wp.com/directostv.teleame.com/wp-content/uploads/2016/06/Colosal-TV.png",Colosal 88.3
http://tv2.ticosmedia.com:1935/canal3/canal3/playlist.m3u8

#EXTINF:-1 tvg-chno="68" tvg-logo="https://cdn6.aptoide.com/mundoandroid2020/15ee2631cca3f82c7b3cc2cf2bc0bba6_icon.png",Zona Música CR
http://vip.hispanotv.org:80/live/acevedo22/acevedo22/283548.m3u8

#EXTINF:-1 tvg-chno="69" tvg-logo="https://www.nicepng.com/png/detail/206-2060818_logo-top-latino-png-top-latino-tv-logo.png",Top Latino TV
https://5cefcbf58ba2e.streamlock.net:543/tltvweb/tvweb.stream/chunklist_w1499609849.m3u8

#EXTINF:-1 tvg-chno="70" tvg-logo="https://www.coolstreaming.us/img/ch/image20830898359.jpg",A son de Salsa
https://cloud01.mipaneltv.xyz:443/asondesalsa/asondesalsa/chunklist_w435560915.m3u8

#EXTINF:-1 tvg-chno="71" tvg-logo="https://latinosradio.cl/wp-content/uploads/2020/10/logo-latinos-radio-2.png",Latinos Radio TV
https://mediacpstreamchile.com:1936/latinosmedia-1/latinosmedia-1/chunklist_w1968389713.m3u8

#EXTINF:-1 tvg-chno="72" tvg-logo="https://platcon.tv/img/p/1/1/9/119-home_default.jpg",TV urban moon tropical
https://srv.panelcast.net/urbantv/urbantv/playlist.m3u8

#EXTINF:-1 tvg-chno="73" tvg-logo="https://platcon.tv/img/p/1/1/5/115-large_default.jpg",TV salsa moon tropical
https://srv.panelcast.net:443/musictv/musictv/chunklist_w1084927877.m3u8

#EXTINF:-1 tvg-chno="74" tvg-logo="https://www.getmeradio.com/stations/voiceoverradiotv-2278/logos/512x512.png",Voice Over Radio TV
http://vip.hispanotv.org:80/live/acevedo22/acevedo22/283551.m3u8

#EXTINF:-1 tvg-chno="75" tvg-logo="https://i0.wp.com/directostv.teleame.com/wp-content/uploads/2017/10/Teleritmo-en-vivo-Online-1.png",Teleritmo
https://mdstrm.com/live-stream-playlist/57b4dc126338448314449d0c.m3u8?uid=D4rMshhUyzljy2UXzEdxzm7N8r4EiI18&sid=KOhl3BXyIrYst7OzNMpBPkuMnAQNKm10&pid=KWcOmLuQAKLkxciTtr4giEXPWEUFGk41&an=screen&at=web-app&av=v5.2.288&ref=https%3A%2F%2Fwww-multimedios-com.cdn.ampproject.org%2Fv%2Fs%2Fwww.multimedios.com%2Fvideo%2Fteleritmo%2Fv2615%3Famp%3D%26amp_gsa%3D1%26amp_js_v%3Da9%26usqp%3Dmq331AQKKAFQArABIIACAw%253D%253D&res=373x210&without_cookies=false&listenerid=&dnt=true

#EXTINF:-1 tvg-chno="80" tvg-logo="https://i2.paste.pics/508ad957b4f4585f59b0d4c265bbac61.png",Vintage Music
https://59ef525c24caa.streamlock.net:443/vmtv/tvvintage/chunklist_w1339648818.m3u8

#EXTINF:-1 tvg-chno="81" tvg-logo="https://i2.paste.pics/e63c9721b2261a3213ea1a4e69776d0f.png",Oldies Hits TV
https://video01.logicahost.com.br:443/oldieshits/oldieshits/chunklist_w854322906.m3u8

#EXTINF:-1 tvg-chno="82" tvg-logo="https://pbs.twimg.com/profile_images/1143426603/IQChannel.jpg",IQ Channel CR
https://rtmp.info:443/iqtv/envivo/chunklist_w394233529.m3u8

#EXTINF:-1 tvg-chno="83" tvg-logo="https://videotourchannel.com/wp-content/uploads/2022/05/LOGO-MASTER-VECTORIZADO-01-1024x663.png",Vídeo Tour Channel 
http://vip.hispanotv.org:80/live/acevedo22/acevedo22/151567.m3u8

#EXTINF:-1 tvg-chno="84" tvg-logo="https://i0.wp.com/directostv.teleame.com/wp-content/uploads/2018/01/Retro-Music-Television-Live-TV-Online.png?resize=1068%2C601&ssl=1",Retro Music TV
https://stream.mediawork.cz:443/retrotv/retrotvHQ1/chunklist_w1085777026.m3u8

#EXTINF:-1 tvg-chno="85" tvg-logo="https://cdn-profiles.tunein.com/s142621/images/logoq.png",V Classic TV 
https://5eaccbab48461.streamlock.net:1936/8112/8112/chunklist_w363472295.m3u8

#EXTINF:-1 tvg-chno="86" tvg-logo="https://recuerdosretro.com/wp-content/uploads/2022/03/cropped-logo_new_web10.png",Recuerdos Retro
https://593b04c4c5670.streamlock.net:443/8002/8002/chunklist_w1859962777.m3u8

#EXTINF:-1 tvg-chno="88" tvg-logo="https://platcon.tv/img/p/1/1/7/117-home_default.jpg",Retroplus 1
https://59f1cbe63db89.streamlock.net:1443/retroplustv/_definst_/retroplustv/chunklist_w1948717984.m3u8

#EXTINF:-1 tvg-chno="89" tvg-logo="https://platcon.tv/img/p/1/1/8/118-large_default.jpg",Retroplus 2
https://59f1cbe63db89.streamlock.net:1443/retroplussenal2/_definst_/retroplussenal2/chunklist_w1246759008.m3u8



#EXTINF:-1 tvg-chno="91" tvg-logo="https://lh3.googleusercontent.com/-c1tQj7-qPkg/YUDkxJFOB8I/AAAAAAAAAOw/QlkimYlh_Mc4IQrr8g6488Xc64HVeJV2gCLcBGAsYHQ/w480/El_Trece.png",Canal 13 FHD
https://live-01-02-eltrece.vodgc.net:443/eltrecetv/tracks-v4a1/mono.m3u8

#EXTINF:-1 tvg-chno="92" tvg-logo="https://lh3.googleusercontent.com/-c1tQj7-qPkg/YUDkxJFOB8I/AAAAAAAAAOw/QlkimYlh_Mc4IQrr8g6488Xc64HVeJV2gCLcBGAsYHQ/w480/El_Trece.png",Canal 13 HD
http://vip.hispanotv.org:80/live/acevedo22/acevedo22/151382.m3u8

#EXTINF:-1 tvg-chno="93" tvg-logo="https://lh3.googleusercontent.com/-c1tQj7-qPkg/YUDkxJFOB8I/AAAAAAAAAOw/QlkimYlh_Mc4IQrr8g6488Xc64HVeJV2gCLcBGAsYHQ/w480/El_Trece.png",Canal 13 (INT)
http://vip.hispanotv.org:80/live/acevedo22/acevedo22/151381.m3u8



#EXTINF:-1 tvg-chno="97" tvg-logo="https://lh3.googleusercontent.com/-mCGw9w72UsQ/YUDlY4_9CtI/AAAAAAAAAO4/OXF1sRluaS0m74yTTadIZOukowPpHOB8wCLcBGAsYHQ/h120/Canal_9.png",Canal 9
http://tvstarlife.com:25461/live/geovany/geovany/318.m3u8

#EXTINF:-1 tvg-chno="98" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/0/0a/Logo_Televisi%C3%B3n_P%C3%BAblica_Argentina.png",TV Pública
http://tvstarlife.com:25461/live/geovany/geovany/338.m3u8

#EXTINF:-1 tvg-chno="99" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/f/f6/Logotipo_de_America_TV.JPG",América TV
http://vip.hispanotv.org:80/live/acevedo22/acevedo22/151390.m3u8

#EXTINF:-1 tvg-chno="100" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/TN_todo_noticias_logo.svg/290px-TN_todo_noticias_logo.svg.png",TN Noticias
http://45.90.105.74:25461/live/budtvsports/wTu27rKVNU/1811.m3u8

#EXTINF:-1 tvg-chno="101" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Canal_26_logo_%282022%29.svg/588px-Canal_26_logo_%282022 %29.svg.png",Canal 26
http://200.115.193.177:80/live/26hd-720/chunklist_w1196091674.m3u8

#EXTINF:-1 tvg-chno="102" tvg-logo="https://assets.iproup.com/assets/jpg/2021/04/17689.jpg",Crónica HD
http://vip.hispanotv.org:80/live/acevedo22/acevedo22/151402.m3u8

#EXTINF:-1 tvg-chno="103" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/C5N_%282017%29.png/606px-C5N_%282017 %29.png",C5N
http://tvstarlife.com:25461/live/geovany/geovany/283.m3u8

#EXTINF:-1 tvg-chno="104" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/8/82/A24_%282019-1%29.png",A24
http://tvstarlife.com:25461/live/geovany/geovany/313.m3u8

#EXTINF:-1 tvg-chno="108" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Azteca_Uno_logo.webp/245px-Azteca_Uno_logo.webp.png",Azteca 1
http://tvstarlife.com:25461/live/geovany/geovany/27241.m3u8

#EXTINF:-1 tvg-chno="109" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Azteca_7_%282016_Blank%29.svg/440px-Azteca_7_%282016_Blank %29.svg.png",Azteca 7
http://tvstarlife.com:25461/live/geovany/geovany/5135.m3u8

#EXTINF:-1 tvg-chno="110" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/4f/Las_Estrellas_logo_%282016%29.png",Las Estrellas
http://tvstarlife.com:25461/live/geovany/geovany/24565.m3u8

#EXTINF:-1 tvg-chno="111" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Canal_5_2016.svg/724px-Canal_5_2016.svg.png",Canal 5
http://mon-key.us:25461/live/luis8876/luis8876/32.m3u8

#EXTINF:-1 tvg-chno="112" tvg-logo="https://www.cineytele.com/wp-content/uploads/2018/09/AZ-MUNDO-NI-1024x320.jpg",Azteca Mundo
http://tvstarlife.com:25461/live/geovany/geovany/27297.m3u8

#EXTINF:-1 tvg-chno="113" tvg-logo="https://selectra.mx/sites/selectra.mx/files/styles/_default_mobile/public/images/logos/canl-nueve-100x100.png",Nu9ve
http://tvstarlife.com:25461/live/geovany/geovany/5137.m3u8

#EXTINF:-1 tvg-chno="114" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Logo-Imagen-TV-MX.png/800px-Logo -Imagen-TV-MX.png",Imagen TV
http://vip.hispanotv.org:80/live/acevedo22/acevedo22/150934.m3u8

#EXTINF:-1 tvg-chno="115" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",América TV HD
http://8.243.108.57:8000/play/a02o

#EXTINF:-1 tvg-chno="116" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Latina HD
http://8.243.108.57:8000/play/a02p

#EXTINF:-1 tvg-chno="117" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Panamericana
http://8.243.108.57:8000/play/a03q

#EXTINF:-1 tvg-chno="118" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Perú Mágico
http://8.243.108.57:8000/play/a03w

#EXTINF:-1 tvg-chno="119" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",CHV HD
http://8.243.108.57:8000/play/a00s

#EXTINF:-1 tvg-chno="120" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",TVN HD
http://8.243.108.57:8000/play/a00r

#EXTINF:-1 tvg-chno="121" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Canal 13 CH
http://8.243.108.57:8000/play/a03d

#EXTINF:-1 tvg-chno="122" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Mega HD
http://8.243.108.57:8000/play/a022

#EXTINF:-1 tvg-chno="123" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",La Red HD
http://8.243.108.57:8000/play/a00l

#EXTINF:-1 tvg-chno="124" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",TV + HD
http://8.243.108.57:8000/play/a021

#EXTINF:-1 tvg-chno="125" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Canal 24 Horas HD
http://8.243.108.57:8000/play/a02y

#EXTINF:-1 tvg-chno="126" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Caracol HD
http://8.243.108.57:8000/play/a02z

#EXTINF:-1 tvg-chno="127" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",RCN HD
http://8.243.108.57:8000/play/a01t

#EXTINF:-1 tvg-chno="130" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Ucvtvlogo2014mejorado.png/200px-Ucvtvlogo2014mejorado.png",UCV Chile
https://unlimited10-cl.dps.live/ucvtv2/ucvtv2.smil/ucvtv2/livestream1/chunks.m3u8

#EXTINF:-1 tvg-chno="131" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/NBC_Universo_logo.svg/1280px-NBC_Universo_logo.svg.png",NBC Universo
http://br0ss.xyz:8090/live/Juanpa/Juanpa123/16225.m3u8

#EXTINF:-1 tvg-chno="132" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Logo_Univision.svg/1280px-Logo_Univision.svg.png",Univisión NY
http://mon-key.us:25461/live/luis8876/luis8876/609.m3u8

#EXTINF:-1 tvg-chno="133" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Logo_Univision.svg/1280px-Logo_Univision.svg.png",Univisión LA
http://vip.hispanotv.org:80/live/acevedo22/acevedo22/319738.m3u8

#EXTINF:-1 tvg-chno="134" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Logo_Univision.svg/1280px-Logo_Univision.svg.png",Univisión PX
https://v-px.mybtv.net:443/live/28/1920x1080.m3u8

#EXTINF:-1 tvg-chno="136" tvg-logo="https://www.vhv.rs/dpng/d/438-4383272_unimas-logo-png-transparent-png.png",Unimás NY
https://v-ny.mybtv.net:443/live/713/1280x720.m3u8

#EXTINF:-1 tvg-chno="137" tvg-logo="https://www.vhv.rs/dpng/d/438-4383272_unimas-logo-png-transparent-png.png",Unimás LA
https://v-ca.mybtv.net:443/live/147/1280x720.m3u8

#EXTINF:-1 tvg-chno="138" tvg-logo="https://www.vhv.rs/dpng/d/438-4383272_unimas-logo-png-transparent-png.png",Unimás PX
https://v-px.mybtv.net:443/live/56/1920x1080.m3u8

#EXTINF:-1 tvg-chno="141" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Telemundo_logo_2018.svg/300px-Telemundo_logo_2018.svg.png",Telemundo NY
https://v-ny.mybtv.net:443/live/659/1920x1080.m3u8

#EXTINF:-1 tvg-chno="142" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Telemundo_logo_2018.svg/300px-Telemundo_logo_2018.svg.png",Telemundo LA
https://v-ca.mybtv.net:443/live/140/1920x1080.m3u8

#EXTINF:-1 tvg-chno="143" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Telemundo_logo_2018.svg/300px-Telemundo_logo_2018.svg.png",Telemundo PX
https://v-px.mybtv.net:443/live/39/1920x1080.m3u8

#EXTINF:-1 tvg-chno="145" tvg-logo="https://www.televisiongratis.tv/components/com_televisiongratis/images/telemundo-puerto-rico-en-vivo-1391.png",Telemundo Puerto Rico 
https://nbculocallive.akamaized.net:443/hls/live/2037499/puertorico/stream1/master_1080.m3u8

#EXTINF:-1 tvg-chno="148" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",E! Entertainment HD
http://8.243.108.57:8000/play/a02m

#EXTINF:-1 tvg-chno="149" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",ID Investigation HD
http://8.243.108.57:8000/play/a016

#EXTINF:-1 tvg-chno="150" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",History Channel HD
http://8.243.108.57:8000/play/a005

#EXTINF:-1 tvg-chno="151" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",History 2 HD
http://8.243.108.57:8000/play/a034

#EXTINF:-1 tvg-chno="152" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Nat Geo HD
http://8.243.108.57:8000/play/a023

#EXTINF:-1 tvg-chno="153" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Animal Planet HD
http://8.243.108.57:8000/play/a02g

#EXTINF:-1 tvg-chno="154" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Discovery Channel HD
http://8.243.108.57:8000/play/a032

#EXTINF:-1 tvg-chno="155" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",H&H HD
http://8.243.108.57:8000/play/a01h

#EXTINF:-1 tvg-chno="156" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Discovery Theater HD
http://8.243.108.57:8000/play/a01i

#EXTINF:-1 tvg-chno="157" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Discovery World HD
http://8.243.108.57:8000/play/a024

#EXTINF:-1 tvg-chno="160" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",CNN Español 
http://45.5.119.202:8000/play/a02h/index.m3u8

#EXTINF:-1 tvg-chno="161" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",France 24 HD
http://8.243.108.57:8000/play/a02v

#EXTINF:-1 tvg-chno="162" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",El Gourmet HD
http://8.243.108.57:8000/play/a018

#EXTINF:-1 tvg-chno="163" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Comedy Central HD
http://8.243.108.57:8000/play/a015

#EXTINF:-1 tvg-chno="164" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Kanal Drama HD
http://8.243.108.57:8000/play/a02a

#EXTINF:-1 tvg-chno="165" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Movistar Plus
http://8.243.108.57:8000/play/a03r

#EXTINF:-1 tvg-chno="166" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Pasiones HD
http://8.243.108.57:8000/play/a00t

#EXTINF:-1 tvg-chno="167" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Sun Channel HD
http://8.243.108.57:8000/play/a01f

#EXTINF:-1 tvg-chno="168" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Trutv HD
http://8.243.108.57:8000/play/a017

#EXTINF:-1 tvg-chno="170" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Cartoon Network HD
http://8.243.108.57:8000/play/a02b

#EXTINF:-1 tvg-chno="171" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Disney Channel HD
http://8.243.108.57:8000/play/a00u

#EXTINF:-1 tvg-chno="172" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Disney Junior HD
http://8.243.108.57:8000/play/a012

#EXTINF:-1 tvg-chno="173" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Discovery Kids HD
http://8.243.108.57:8000/play/a01g

#EXTINF:-1 tvg-chno="190" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Claro Música 
http://45.5.119.202:8000/play/a04k/index.m3u8

#EXTINF:-1 tvg-chno="191" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",MTV
http://45.5.119.202:8000/play/a01s/index.m3u8

#EXTINF:-1 tvg-chno="192" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",MTV 00s
http://45.5.119.202:8000/play/a00l/index.m3u8

#EXTINF:-1 tvg-chno="193" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",MTV 80s
http://45.5.119.202:8000/play/a02t/index.m3u8

#EXTINF:-1 tvg-chno="194" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",MTV HD
http://45.5.119.202:8000/play/a033/index.m3u8

#EXTINF:-1 tvg-chno="195" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",MTV Hits
http://45.5.119.202:8000/play/a02s/index.m3u8

#EXTINF:-1 tvg-chno="196" tvg-logo="https://ayuda.tigo.com.pa/hc/article_attachments/9373342049683/MicrosoftTeams-image.png",Vix + La Liga
http://144.217.5.253:25461/streaming/clients_normal.php?username=malotv&password=gratis&stream=153656&extension=m3u8&token=Q0FYAkZRGwoVBwwOAgdWAFFXW1dQU1QBBwIFVwBSBVJaVQAGDV0BBAITGBsVR0ZVAw48W1EXXwQHBldWVB0QF0sGQjxcXRsKFQADCVIHAwFAT0FGXFgAFwgFTUESWFZAAkEBVQIIDRIbE1FBElZGXgMPPFZQQwxWVxdbDRddXk4aDF48UVxUUVlVFgNEAhYcQAoQQhcPC0BeWU1BAFhGEFkXVUEPGwgIDwYWFURQW0UMFxFLFw9HdmAXTUEHSUYHVhBZDFsbAxJaAkEBRB8WWRE8EVdGQRdQU1gEEUALEFMaTxIOVEFmU1hfWlwFR11fDBBBCBcFRxkQWA4NC0VdEGcTWQcXAxsBAQcNDkRO

#EXTINF:-1 tvg-chno="197" tvg-logo="https://ayuda.tigo.com.pa/hc/article_attachments/9373342049683/MicrosoftTeams-image.png",Vix + La Liga 2
http://vip.hispanotv.org:80/live/acevedo22/acevedo22/322964.m3u8

#EXTINF:-1 tvg-chno="198" tvg-logo="https://ayuda.tigo.com.pa/hc/article_attachments/9373342049683/MicrosoftTeams-image.png",Vix + La Liga 3
http://vip.hispanotv.org:80/live/acevedo22/acevedo22/322273.m3u8

#EXTINF:-1 tvg-chno="199" tvg-logo="https://soyreferee.com/u/fotografias/m/2022/7/20/f804x452-19661_71594_0.jpg",Vix + Liga MX
https://linear-193.frequency.stream:443/193/hls/master/playlist_1280x720.m3u8

#EXTINF:-1 tvg-chno="200" tvg-logo="https://ticourbano.com/wp-content/uploads/2020/01/FUTV-Costa-Rica-2020.jpg",Futv HD
http://vip.hispanotv.org:80/live/acevedo22/acevedo22/151545.m3u8

#EXTINF:-1 tvg-chno="201" tvg-logo="https://ticourbano.com/wp-content/uploads/2020/01/FUTV-Costa-Rica-2020.jpg",Futv HD Opc 2
http://190.83.119.67:8000/play/a0t3

#EXTINF:-1 tvg-chno="202" tvg-logo="https://ticourbano.com/wp-content/uploads/2020/01/FUTV-Costa-Rica-2020.jpg",Futv HD Opc 3
http://160.20.164.171:8001/play/a00x

#EXTINF:-1 tvg-chno="203" tvg-logo="https://imagenes.gatotv.com/logos/canales/oscuros/tigo_sports-mediano.png",Tigo Sports CR
http://vip.hispanotv.org:80/live/acevedo22/acevedo22/155308.m3u8

#EXTINF:-1 tvg-chno="204" tvg-logo="https://imagenes.gatotv.com/logos/canales/oscuros/tigo_sports-mediano.png",Tigo Sports CR Opc 2
http://tvstarlife.com:25461/live/geovany/geovany/97360.m3u8

#EXTINF:-1 tvg-chno="205" tvg-logo="https://imagenes.gatotv.com/logos/canales/oscuros/tigo_sports-mediano.png",Tigo Sports CR Opc 3
http://190.61.99.191:8000/play/a062/index.m3u8

#EXTINF:-1 tvg-chno="207" tvg-logo="https://streann.akamaized.net/upload2/1640365537761.png",TD + HD
http://vip.hispanotv.org:80/live/acevedo22/acevedo22/151542.m3u8

#EXTINF:-1 tvg-chno="208" tvg-logo="https://streann.akamaized.net/upload2/1640365537761.png",TD + HD Opc 2
http://160.20.164.171:8001/play/a07c

#EXTINF:-1 tvg-chno="209" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/TD_M%C3%A1s_2_Logo.svg/1024px-TD_M%C3 %A1s_2_Logo.svg.png",TD + 2 HD
http://vip.hispanotv.org:80/live/acevedo22/acevedo22/151543.m3u8

#EXTINF:-1 tvg-chno="210" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/TD_M%C3%A1s_2_Logo.svg/1024px-TD_M%C3 %A1s_2_Logo.svg.png",TD + 2 HD Opc 2
http://160.20.164.171:8001/play/a07d

#EXTINF:-1 tvg-chno="215" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Espn MX HD
http://181.78.1.217:8146/play/a07i

#EXTINF:-1 tvg-chno="216" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Espn 2 MX HD
http://181.78.1.217:8146/play/a07k

#EXTINF:-1 tvg-chno="217" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Espn 3 MX HD
http://181.78.1.217:8146/play/a07j

#EXTINF:-1 tvg-chno="218" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Espn 4 HD
http://45.5.119.202:8000/play/a029/index.m3u8

#EXTINF:-1 tvg-chno="219" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Espn Sur HD
http://8.243.108.57:8000/play/a02l

#EXTINF:-1 tvg-chno="220" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Espn 2 Sur HD
http://8.243.108.57:8000/play/a013

#EXTINF:-1 tvg-chno="221" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Espn  Chile HD
http://8.243.108.57:8000/play/a01s

#EXTINF:-1 tvg-chno="222" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Espn  Perú HD
http://8.243.108.57:8000/play/a00n

#EXTINF:-1 tvg-chno="223" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Espn 2 HD
http://8.243.108.57:8000/play/a00c

#EXTINF:-1 tvg-chno="224" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Espn 2 HD
http://8.243.108.57:8000/play/a00i

#EXTINF:-1 tvg-chno="225" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Espn 3 Arg HD
http://8.243.108.57:8000/play/a00x

#EXTINF:-1 tvg-chno="226" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Espn 4 HD
http://8.243.108.57:8000/play/a01m

#EXTINF:-1 tvg-chno="227" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Espn Extra HD
http://8.243.108.57:8000/play/a027

#EXTINF:-1 tvg-chno="228" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Fox Sports 1 HD
http://8.243.108.57:8000/play/a033

#EXTINF:-1 tvg-chno="229" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Fox Sports 2 HD
http://8.243.108.57:8000/play/a01n

#EXTINF:-1 tvg-chno="230" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Fox Sports 3 HD
http://8.243.108.57:8000/play/a00y

#EXTINF:-1 tvg-chno="231" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Fox Sports Premium 
http://201.222.45.69:8000/play/a00c/index.m3u8

#EXTINF:-1 tvg-chno="232" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Espn 4
http://201.222.45.69:8000/play/a02k/index.m3u8

#EXTINF:-1 tvg-chno="233" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Fox Sports 2
http://201.222.45.69:8000/play/a033/index.m3u8

#EXTINF:-1 tvg-chno="234" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Fox Sports 3
http://201.222.45.69:8000/play/a034/index.m3u8

#EXTINF:-1 tvg-chno="235" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Fox Sports 2
http://45.5.119.202:8000/play/a00i/index.m3u8

#EXTINF:-1 tvg-chno="236" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Fox Sports 3
http://45.5.119.202:8000/play/a02r/index.m3u8

#EXTINF:-1 tvg-chno="237" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",TNT Sports HD
http://8.243.108.57:8000/play/a00b

#EXTINF:-1 tvg-chno="238" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",EL Canal del Fútbol HD
http://8.243.108.57:8000/play/a03c

#EXTINF:-1 tvg-chno="239" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",GolTV HD
http://8.243.108.57:8000/play/a02n

#EXTINF:-1 tvg-chno="240" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Gol Perú HD
http://8.243.108.57:8000/play/a02r

#EXTINF:-1 tvg-chno="241" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Win Sports HD
http://8.243.108.57:8000/play/a00e

#EXTINF:-1 tvg-chno="242" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Win Sports + HD
http://8.243.108.57:8000/play/a02f

#EXTINF:-1 tvg-chno="243" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Movistar Deportes HD
http://8.243.108.57:8000/play/a02j

#EXTINF:-1 tvg-chno="244" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",TyC Sports HD
http://8.243.108.57:8000/play/a02q

#EXTINF:-1 tvg-chno="290" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/The_Simpsons_yellow_logo.svg/400px-The_Simpsons_yellow_logo.svg.png",Los Simpsons 1
https://srv5.zcast.com.br:443/simpsons/simpsons/chunklist_w469095767.m3u8

#EXTINF:-1 tvg-chno="291" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/The_Simpsons_yellow_logo.svg/400px-The_Simpsons_yellow_logo.svg.png",Los Simpsons 2
http://85.202.80.14:80/live/kkkrkDp2a9KNwAwGzpb/QT94uK5NNQw4r4Qs/713.m3u8

#EXTINF:-1 tvg-chno="292" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/The_Simpsons_yellow_logo.svg/400px-The_Simpsons_yellow_logo.svg.png",Los Simpsons 3
http://br0ss.xyz:8090/live/Juanpa/Juanpa123/31990.m3u8

#EXTINF:-1 tvg-chno="293" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/The_Simpsons_yellow_logo.svg/400px-The_Simpsons_yellow_logo.svg.png",Los Simpsons 4
http://45.90.105.74:25461/live/budtvsports/wTu27rKVNU/38722.m3u8

#EXTINF:-1 tvg-chno="294" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/The_Simpsons_yellow_logo.svg/400px-The_Simpsons_yellow_logo.svg.png",Los Simpsons 5
http://45.90.105.74:25461/live/budtvsports/wTu27rKVNU/38706.m3u8

#EXTINF:-1 tvg-chno="295" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/The_Simpsons_yellow_logo.svg/400px-The_Simpsons_yellow_logo.svg.png",Los Simpsons 6
http://tvstarlife.com:25461/live/geovany/geovany/10678.m3u8

#EXTINF:-1 tvg-chno="296" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/The_Simpsons_yellow_logo.svg/400px-The_Simpsons_yellow_logo.svg.png",Los Simpsons 7
http://tvstarlife.com:25461/live/geovany/geovany/10673.m3u8

#EXTINF:-1 tvg-chno="297" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/The_Simpsons_yellow_logo.svg/400px-The_Simpsons_yellow_logo.svg.png",Los Simpsons 8
http://tvstarlife.com:25461/live/geovany/geovany/10611.m3u8

#EXTINF:-1 tvg-chno="298" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/The_Simpsons_yellow_logo.svg/400px-The_Simpsons_yellow_logo.svg.png",Los Simpsons 9
http://tvstarlife.com:25461/live/geovany/geovany/10627.m3u8

#EXTINF:-1 tvg-chno="299" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/The_Simpsons_yellow_logo.svg/400px-The_Simpsons_yellow_logo.svg.png",Los Simpsons 10
https://srv5.zcast.com.br:443/simpsons/simpsons/chunklist_w1106366740.m3u8

#EXTINF:-1 tvg-chno="300" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",A&E HD
http://8.243.108.57:8000/play/a006

#EXTINF:-1 tvg-chno="301" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",AMC HD
http://8.243.108.57:8000/play/a026

#EXTINF:-1 tvg-chno="302" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Atres Series HD
http://8.243.108.57:8000/play/a03e

#EXTINF:-1 tvg-chno="303" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",AXN HD
http://8.243.108.57:8000/play/a009

#EXTINF:-1 tvg-chno="304" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",FX HD
http://8.243.108.57:8000/play/a01r

#EXTINF:-1 tvg-chno="305" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Cinecanal HD
http://8.243.108.57:8000/play/a025

#EXTINF:-1 tvg-chno="306" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Cinemax HD
http://8.243.108.57:8000/play/a014

#EXTINF:-1 tvg-chno="307" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Golden HD
http://8.243.108.57:8000/play/a02k

#EXTINF:-1 tvg-chno="308" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",DHE HD
http://8.243.108.57:8000/play/a031

#EXTINF:-1 tvg-chno="309" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",HBO 2 HD
http://8.243.108.57:8000/play/a02e

#EXTINF:-1 tvg-chno="310" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",HBO Family HD
http://8.243.108.57:8000/play/a035

#EXTINF:-1 tvg-chno="311" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",HBO HD
http://8.243.108.57:8000/play/a028

#EXTINF:-1 tvg-chno="312" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",HBO POP HD
http://8.243.108.57:8000/play/a00d

#EXTINF:-1 tvg-chno="313" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",HBO Xtreme HD
http://8.243.108.57:8000/play/a038

#EXTINF:-1 tvg-chno="318" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Paramount HD
http://8.243.108.57:8000/play/a02c

#EXTINF:-1 tvg-chno="319" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Star Channel HD
http://8.243.108.57:8000/play/a02x

#EXTINF:-1 tvg-chno="320" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Star Channel HD
http://8.243.108.57:8000/play/a00j

#EXTINF:-1 tvg-chno="321" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Sony HD
http://8.243.108.57:8000/play/a007

#EXTINF:-1 tvg-chno="322" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Space HD
http://8.243.108.57:8000/play/a00a

#EXTINF:-1 tvg-chno="323" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Studio Universal HD
http://8.243.108.57:8000/play/a02d

#EXTINF:-1 tvg-chno="324" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",TNT HD
http://8.243.108.57:8000/play/a00w

#EXTINF:-1 tvg-chno="325" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",TNT Series HD
http://8.243.108.57:8000/play/a01q

#EXTINF:-1 tvg-chno="326" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Warner Channel HD
http://8.243.108.57:8000/play/a008

#EXTINF:-1 tvg-chno="329" tvg-logo="https://img.freepik.com/vector-premium/insignia-iptv-icono-logotipo-ilustracion_100456-1447.jpg",Universal Channel HD
http://8.243.108.57:8000/play/a01l

#EXTINF:-1 tvg-chno="330" tvg-logo="https://ayuda.tigo.com.bo/hc/article_attachments/4707794286227/mceclip6.png",Universal Cinema HD
http://181.175.41.170:8000/play/a0gx

#EXTINF:-1 tvg-chno="331" tvg-logo="https://ayuda.tigo.com.bo/hc/article_attachments/4707831567891/mceclip7.png",Universal Comedy HD
http://181.175.41.170:8000/play/a0gi

#EXTINF:-1 tvg-chno="332" tvg-logo="https://ayuda.tigo.com.bo/hc/article_attachments/4707852817299/mceclip8.png",Universal Crime HD
http://181.175.41.170:8000/play/a0gh

#EXTINF:-1 tvg-chno="333" tvg-logo="https://ayuda.tigo.com.bo/hc/article_attachments/4707774235539/mceclip5.png",Universal Premiere HD
http://181.175.41.170:8000/play/a0ge

#EXTINF:-1 tvg-chno="334" tvg-logo="https://ayuda.tigo.com.bo/hc/article_attachments/4707774235539/mceclip5.png",Universal Premiere 2 HD
http://181.175.41.170:8000/play/a0gf

#EXTINF:-1 tvg-chno="335" tvg-logo="https://ayuda.tigo.com.bo/hc/article_attachments/4707875527955/mceclip9.png",Universal Reality HD
http://181.175.41.170:8000/play/a0gg





#EXTINF:-1 tvg-id="TVPublicaHD.ar" tvg-logo="https://lh3.googleusercontent.com/-x6JNcq2aLCg/YtQgLsrRQKI/AAAAAAAAAqo/_sLdYldWdig0bMS-zrJkYdyOnJJ6uvF6wCNcBGAsYHQ/h120/ver-tv-publica-canal-7-argentina-en-vivo.jpg" group-title="Argentina", TV PUBLICA 2 
http://free.fullspeed.tv/iptv-query?streaming-ip=https://www.youtube.com/channel/UCs231K71Bnu5295_x0MB5Pg/live
#EXTINF:-1 tvg-id="TVPublicaHD.ar" tvg-logo="https://lh3.googleusercontent.com/-x6JNcq2aLCg/YtQgLsrRQKI/AAAAAAAAAqo/_sLdYldWdig0bMS-zrJkYdyOnJJ6uvF6wCNcBGAsYHQ/h120/ver-tv-publica-canal-7-argentina-en-vivo.jpg" group-title="Argentina", TV PUBLICA 3
http://free.fullspeed.tv/iptv-query?streaming-ip=https://www.youtube.com/user/TVPublicaArgentina/live
#EXTINF:-1 tvg-id="TVPublicaHD.ar" tvg-logo="https://lh3.googleusercontent.com/-x6JNcq2aLCg/YtQgLsrRQKI/AAAAAAAAAqo/_sLdYldWdig0bMS-zrJkYdyOnJJ6uvF6wCNcBGAsYHQ/h120/ver-tv-publica-canal-7-argentina-en-vivo.jpg" group-title="Argentina", TV PUBLICA 4
http://free.fullspeed.tv/iptv-query?streaming-ip=https://www.youtube.com/channel/UCaU_cKHQ4IFHvBzQ-tKS1-Q/live

#EXTINF:-1 tvg-id="ElNueve.ar" tvg-country="AR" tvg-logo="https://vignette.wikia.nocookie.net/logopedia/images/f/f7/Canal-nueve-ar2017.png" group-title="Argentina", CANAL 9 35.1 
https://00475e6934d74fe48a80427567a45918.mediatailor.us-east-1.amazonaws.com/v1/manifest/4c8323052bc3dbd9aa2eba0b638d8495561e8377/JW-Octubre-Channel09/0df6d88d-304a-4d15-9cf8-eab1bc9b5e45/3.m3u8








#EXTINF:-1 tvg-id="elnueve" tvg-id="nueve" tvg-logo="https://www.elnueve.com.ar/_next/image?url=%2Flogo%2FlogotipoC9.png&w=256&q=75" group-title="Argentina",El nueve 
https://2a1773fcc0c94a639b422d1cf7ba14b7.mediatailor.us-east-1.amazonaws.com/v1/master/4c8323052bc3dbd9aa2eba0b638d8495561e8377/JW-Octubre-Channel09/live/channel09/live.isml/.m3u8

#EXTINF:-1 tvg-id="elnueve" tvg-id="nueve" tvg-logo="https://www.elnueve.com.ar/_next/image?url=%2Flogo%2FlogotipoC9.png&w=256&q=75" group-title="Argentina",El nueve 2
https://00475e6934d74fe48a80427567a45918.mediatailor.us-east-1.amazonaws.com/v1/master/4c8323052bc3dbd9aa2eba0b638d8495561e8377/JW-Octubre-Channel09/live/channel09/live.isml/b00d164f-be51-473e-a47c-b33aa1f44186.m3u8


#EXTINF:-1 tvg-id="elnueve" tvg-id="nueve" tvg-logo="https://www.elnueve.com.ar/_next/image?url=%2Flogo%2FlogotipoC9.png&w=256&q=75" group-title="Argentina",El nueve 3
https://delivery.cdn.rcs.net.ar/mnp/elnueve_hls/playlist.m3u8


#EXTINF:-1 tvg-id="ElTrece.ar" tvg-country="AR" tvg-logo="https://pbs.twimg.com/profile_images/1344843564535132160/xT96d8Zv_400x400.jpg" group-title="Argentina",CANAL 13 33.1 # 
https://delivery.cdn.rcs.net.ar/mnp/el13_hls/playlist.m3u8

#EXTINF:-1 tvg-id="El Trece" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/45/Eltrece_logotipo_2018.png" , EL TRECE 
https://live-01-02-eltrece.vodgc.net/eltrecetv/index.m3u8|user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0


#EXTINF:-1 tvg-id="El Trece" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/45/Eltrece_logotipo_2018.png" , EL TRECE 2
https://live-01-02-eltrece.vodgc.net/eltrecetv/tracks-v2a1/mono.m3u8|user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0


#EXTINF:-1 tvg-id="Telefe.ar" tvg-logo="https://lh3.googleusercontent.com/-b2keOX5lUv4/YUDkI5UqpzI/AAAAAAAAAOo/I1NXuVoeXKIG-zh2E3nh6QqvhjY_kpq4wCLcBGAsYHQ/w480/Telefe.png",Telefe FHD
http://vip.hispanotv.org:80/live/acevedo22/acevedo22/151384.m3u8

#EXTINF:-1 tvg-id="Telefe.ar" tvg-logo="https://lh3.googleusercontent.com/-b2keOX5lUv4/YUDkI5UqpzI/AAAAAAAAAOo/I1NXuVoeXKIG-zh2E3nh6QqvhjY_kpq4wCLcBGAsYHQ/w480/Telefe.png",Telefe HD 2
https://is-tucuman.cdn.rcs.net.ar/mnp/telefe_hls/playlist.m3u8

#EXTINF:-1 tvg-id="Telefe.ar"  tvg-logo="https://lh3.googleusercontent.com/-b2keOX5lUv4/YUDkI5UqpzI/AAAAAAAAAOo/I1NXuVoeXKIG-zh2E3nh6QqvhjY_kpq4wCLcBGAsYHQ/w480/Telefe.png",Telefe (INT) 3
http://tvstarlife.com:25461/live/geovany/geovany/315.m3u8

#EXTINF:-1 tvg-id="Telefe.ar" tvg-country="AR" tvg-logo="http://x.playerlatino.live/telefe.png" group-title="Argentina", TELEFE 4
https://delivery.cdn.rcs.net.ar/mnp/telefe_hls/playlist.m3u8

#EXTINF:-1 tvg-id="Telefe" tvg-id="Telefe.ar" tvg-logo="https://telefe-static.akamaized.net/media/18154476/logo-telefe-twitter.png" group-title="Argentina",TELEFE COM VPN
https://mitelefe.com/Api/Videos/GetSourceUrl/694564/0/HLS

#EXTINF:-1 tvg-id="Telefe.ar" tvg-country="AR" tvg-logo="http://x.playerlatino.live/telefe.png" group-title="Argentina", TELEFE COM VPN 2
https://telefe.com/Api/Videos/GetSourceUrl/694564/0/HLS?.m3u8

#EXTINF:-1, tvg-id="Telefe" group-title="Argentina" tvg-name="Telefe" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Telefe_Logo.svg/1280px-Telefe_Logo.svg.png",TELEFE COM VPN 3
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/TelefeHD/SA_SAGEMCOM/TelefeHD.m3u8 


#EXTINF:-1  tvg-id="InformacionPeriodistica.ar" group-title="Argentina" tvg-logo="https://i.imgur.com/SQSu9M5.png",Informacion Periodística
https://octubre-live.cdn.vustreams.com/live/ip/live.isml/live-audio_1=128000-video=2800000.m3u8





#EXTINF:-1  tvg-id="NETTVHD.ar" group-title="Argentina" tvg-logo="https://canalnet.tv/_templates/desktop/includes/img/_logo-alt.png",NET TV 
https://unlimited1-buenosaires.dps.live/nettv/nettv.smil/playlist.m3u8











#EXTINF:-1 tvg-id="Encuentro.ar" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Logo_del_canal_Encuentro.svg/150px-Logo_del_canal_Encuentro.svg.png" group-title="Argentina", ENCUENTRO 
https://5fb24b460df87.streamlock.net/live-cont.ar/encuentro/.m3u8

#EXTINF:-1 tvg-id="Encuentro.ar" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Logo_del_canal_Encuentro.svg/150px-Logo_del_canal_Encuentro.svg.png" group-title="Argentina", ENCUENTRO 2
http://free.fullspeed.tv/iptv-query?streaming-ip=https://www.youtube.com/user/encuentro/live


#EXTINF:-1 tvg-id="InformacionPeriodistica.ar" tvg-logo="https://img.ip.digital/sites/default/files/styles/1_1_max_364px/theme/ip_theme/media/ip_logo.png?itok=gzTn1Jjd" group-title="Argentina", IP 
http://free.fullspeed.tv/iptv-query?streaming-ip=https://www.youtube.com/c/IPNoticiasEnVivo/live



#EXTINF:-1 tvg-logo="https://www.ipuntotv.com/IMAGES/TN%20logo%20nuevo.png" group-title="Argentina" ,TN 
https://delivery.cdn.rcs.net.ar/mnp/tn_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-1Ltvq4TxvzE/YT5D2UFQimI/AAAAAAAAALY/irH51w9AkSEys2-buTru_86k_O9u_e-AQCLcBGAsYHQ/w480/C5N.png" group-title="Argentina" , C5N 
https://delivery.cdn.rcs.net.ar/mnp/c5n_hls/playlist.m3u8

#EXTINF:-1 tvg-id="CronicaTV.ar" tvg-logo="https://www.utpba.org/wp-content/uploads/2019/07/cronica-logo.jpg" group-title="Argentina" , CRONICA 
http://free.fullspeed.tv/iptv-query?streaming-ip=https://www.youtube.com/c/cronicatv/live

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-Su_IBL7T52g/YT5AkN3JRrI/AAAAAAAAALI/lQnG3U9ltAk-ckyIPKFkXZieGUgHyX75QCLcBGAsYHQ/w480/A24.png" group-title="Argentina" , A 24 
https://delivery.cdn.rcs.net.ar/mnp/a24_hls/playlist.m3u8

#EXTINF:-1 tvg-id="Canal26HD.ar" tvg-logo="https://plushlamour.com.ar/wp-content/uploads/2021/01/canal3-1.png" group-title="Argentina" , C26 
https://delivery.cdn.rcs.net.ar/mnp/canal26_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://cdn.cnn.com/cnn/.e/img/3.0/global/misc/cnn-logo.png" group-title="Argentina" , CNN 
https://delivery.cdn.rcs.net.ar/mnp/cnn_hls/playlist.m3u8



#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-inqhqQZAAGQ/YUDp5oL3lxI/AAAAAAAAAPY/NmRDCbQRAusmLK-7egIs-op4_u1z12_gACLcBGAsYHQ/w480/AXN.png" group-title="Argentina" , AXN 
https://delivery.cdn.rcs.net.ar/mnp/axn_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://blogger.googleusercontent.com/img/a/AVvXsEhc-UYX7Vn9Ua5K2M2L1pi_ssLWJDJcwsIlw2EG8_kwppO6GVLVEsAVlqRyIhCWjRbgljzMuDnbGHoVPVBA7S9EwhtstmaIVGrP06PLSwJRTKmeZeAtTO2eJrys8XT9VkzaNUxJo-9tmYK_pPUFTg-gtM5Tys8u8uw3kZwA6pt-j60950tzsbdvO9l-" group-title="Argentina" , TNT 
https://delivery.cdn.rcs.net.ar/mnp/tnt_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-iD3Pp52qkYE/YsDywQHYs6I/AAAAAAAAAm4/u0hKfVvSTSU-B-kLAy2QI7vSkMapQgbOACNcBGAsYHQ/h120/ver-space-en-vivo.jpg" group-title="Argentina" , SPACE 
https://delivery.cdn.rcs.net.ar/mnp/space_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-cK4WNqOob_w/YUDpdrZzvEI/AAAAAAAAAPQ/DY9_xUdMjn0yP7ZbOfweOMYBReirkQeUACLcBGAsYHQ/w480/AMC.png" group-title="Argentina" , AMC 
https://delivery.cdn.rcs.net.ar/mnp/amc_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-GO_4vazX3lo/Ys9KMwNGLmI/AAAAAAAAAp8/6SfRXjBNMUQzuoijUxzqi6MHtzazHKx5gCNcBGAsYHQ/h120/ver-universal-tv-en-vivo.jpg" group-title="Argentina" , Universal 
https://delivery.cdn.rcs.net.ar/mnp/universal_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://cdn.mitvstatic.com/channels/ar_fx_m.png" group-title="Argentina" , FX 
https://delivery.cdn.rcs.net.ar/mnp/fx_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://w7.pngwing.com/pngs/722/1014/png-transparent-logo-warner-bros-others-emblem-company-logo-thumbnail.png" group-title="Argentina" , WARNER 
https://delivery.cdn.rcs.net.ar/mnp/warner_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://static.wikia.nocookie.net/logopedia/images/6/61/Sony_Channel_2019.svg/revision/latest/scale-to-width-down/200?cb=20200117013250&path-prefix=es" group-title="Argentina" , SONY 
ttps://delivery.cdn.rcs.net.ar/mnp/sony_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://i.pinimg.com/originals/4b/ab/54/4bab54bc7bad8e728654032c5c817154.png" group-title="Argentina" , CINECANAL 
https://delivery.cdn.rcs.net.ar/mnp/cinecanal_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://media-exp2.licdn.com/dms/image/C560BAQHQ303-nahsMQ/company-logo_200_200/0/1593608716508?e=2147483647&v=beta&t=jIwFx63mao3NBPEYBn-_hS--cPrx5bT5h0jUL6jlAto" group-title="Argentina" , HBO 
https://delivery.cdn.rcs.net.ar/mnp/hbo_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://cdn.mitvstatic.com/channels/ar_hbo-2_m.png" group-title="Argentina" , HBO 2 
https://delivery.cdn.rcs.net.ar/mnp/hbo2_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/HBO_Plus.png/640px-HBO_Plus.png" group-title="Argentina" , HBO PLUS 
https://delivery.cdn.rcs.net.ar/mnp/hboplus_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://cdn.mitvstatic.com/channels/ar_max-up_m.png" group-title="Argentina" , HBO POP 
https://delivery.cdn.rcs.net.ar/mnp/hbopop_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="http://1.bp.blogspot.com/-GGsnT8OYxqU/UJv5NAiymbI/AAAAAAAAXMo/3iytiCwX69s/s1600/isat.jpg" group-title="Argentina" , ISAT h
ttps://delivery.cdn.rcs.net.ar/mnp/isat_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-NDwbXJHYJMc/YT5RpJxdtpI/AAAAAAAAAOY/D1VEo88C3jwfky5Oiwww9TZX3ehLWpSfQCLcBGAsYHQ/w480/Cinemax.png" group-title="Argentina" , CINEMAX 
https://delivery.cdn.rcs.net.ar/mnp/cinemax_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-DRmD9dsKTi0/Ys9XhEvF5uI/AAAAAAAAAqM/NSP5eDAuKuAbbcfdah2I4rVpOvdSWahywCNcBGAsYHQ/w480/ver-tbs-en-vivo.jpg" group-title="Argentina" , TBS 
https://delivery.cdn.rcs.net.ar/mnp/tbs_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-Riqq0wkw9UY/YT5RS6UxToI/AAAAAAAAAOQ/yfkgOB2YSOc_-xEiyvrq96QSYBgcQD8WACLcBGAsYHQ/w480/TCM.png" group-title="Argentina" , TCM 
https://delivery.cdn.rcs.net.ar/mnp/tcm_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyhWjRQbbj9z-e8f_ZdUMB3negMEUlb6q6Rraql-rEHDRIyJTmGUOH5PI3DlCYmUlTy98H68aKLturEdTjDEIGTsytYLV6xBXXLw9etv1ggELuhXd2llW_86v27dpBoDnx9xQkHEcI2I37-q6uVdPcu0Kocm15ApYAoT2-IVIS7UevH2coIZF0vKDG/w480/ver-syfy-en-vivo.jpg" group-title="Argentina" , SYFY 
https://delivery.cdn.rcs.net.ar/mnp/syfy_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://assets3.cbsnewsstatic.com/hub/i/r/2022/02/15/352f4601-c86b-4a90-96ab-cf9cee9ae351/thumbnail/640x274/bdf6b7a51fb96db68b221f8b8a0be974/logo.jpg" group-title="Argentina" , PARAMOUNT 
https://delivery.cdn.rcs.net.ar/mnp/paramount_hls/playlist.m3u8


#EXTINF:-1 tvg-logo="https://static.wikia.nocookie.net/logopedia/images/7/7d/Elgourmet_2015.svg/revision/latest/scale-to-width-down/200?cb=20191030175859" group-title="(COCINA/ESTILO)" , Gourmet 
https://delivery.cdn.rcs.net.ar/mnp/gourmet_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-F2BnsazA7os/Ys31hnU_n3I/AAAAAAAAApQ/0MXv4sr5nusxWpjqfA0hm_aZj8GBqD1gACNcBGAsYHQ/w480/ver-mas-chic-en-vivo.jpg" group-title="(COCINA/ESTILO)" , MAS CHIC 
https://delivery.cdn.rcs.net.ar/mnp/maschic_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://blogger.googleusercontent.com/img/a/AVvXsEhWU7qTkDs3xwDNs8Ma9dfG1R4PEnjNr4tQkQT2VnRCmLimj4dC5VfGeAg__wPr8pzRHzWBfuuqNionC5CJz5ro8ymVHmo1-9LSEEEW1EgC6WEXlvN6Hsxuyso7RjM_4UbPYcSxhS92j6jFMlw-RzUwpTDKfoMxjxvSlfupuoUjMHtcvSF6BHncy1xl=w480" group-title="(COCINA/ESTILO)" , LIFETIME 
https://delivery.cdn.rcs.net.ar/mnp/lifetime_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://blogger.googleusercontent.com/img/a/AVvXsEhVVcU81CJ-9e-tEsH5-VNlr6mg8_PjlqQY4ZuSvc59RPALyd8p0QkfPZl-YwJcH3p7AgUNS0W8v2FFIiRj0B0ACKm4jgobepjqmkf7lloDqobhwoOa5_Abc4YcCJb5VdQnU_YNzDtI2xZqNWcGe3lqBat3qn5EVhm6fBFCO7g4Ch3tKKal2cl_xD0J=w480" group-title="(COCINA/ESTILO)" , GLITZ 
https://delivery.cdn.rcs.net.ar/mnp/glitz_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://exchange4media.gumlet.io/news-photo/98602-MTVlogo.jpg?w=400&dpr=2.6" group-title="Argentina" , MTV 
https://delivery.cdn.rcs.net.ar/mnp/mtv_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://pbs.twimg.com/profile_images/738838081122541568/Xly8mKUw_400x400.jpg" group-title="Argentina", HTV 
https://delivery.cdn.rcs.net.ar/mnp/htv_hls/playlist.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/d/d0/Logocmtvargentina.png" group-title="Argentina", CM 
https://delivery.cdn.rcs.net.ar/mnp/cm_hls/playlist.m3u8
'''


banner2 = r'''


#EXTINF:-1 tvg-logo="https://i.imgur.com/srtddlN.png" group-title="Argentina",TV Publica
https://delivery.cdn.rcs.net.ar/mnp/tvp/output.mpd





#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Telefe_%28nuevo_logo%29.png/800px-Telefe_%28nuevo_logo%29.png"group-title="Argentina",TELEFE 34.1 TDA HD"reproducir con MX PRO"
https://live.obslivestream.com/telecolormux/tracks-v1a1/mono.m3u8










#EXTINF:-1 group-title="Argentina" tvg-logo="https://yt3.ggpht.com/ytc/AKedOLSYU51c8SbrkWZeNBRMFeCnGv0YXPpXuEGBNq-X5g=s88-c-k-c0x00ffffff-no-rj",Encuentro
https://raw.githubusercontent.com/fgillusi/IPTV-Argentina/main/Encuentro.m3u8









#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-TgZv-RGCYoc/XrYHwcpfivI/AAAAAAAA0gw/AuqgxhioqLc1qhSHFDdH1ZftA0PKvOnzQCK8BGAsYHg/s0/2020-05-08.jpg" group-title="(CABLE)", 9LINK CHACO 
http://201.217.245.41:8081/testmelucas/canal9/playlist.m3u8






#EXTINF:-1 group-title="Argentina",el siete (tv publica)
https://raw.githubusercontent.com/fgillusi/IPTV-Argentina/main/Canal7.m3u8

#EXTINF:-1 group-title="Argentina",EL NUEVE HD
https://raw.githubusercontent.com/fgillusi/IPTV-Argentina/main/Canal9.m3u8

#EXTINF:-1 group-title="Argentina",encuentro
https://5fb24b460df87.streamlock.net/live-cont.ar/encuentro/playlist.m3u8

#EXTINF:-1 group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Informaci%C3%B3n_Period%C3%ADstica_IP_Logo.svg/260px-Informaci%C3%B3n_Period%C3%ADstica_IP_Logo.svg.png", IP  24.5         
https://d1nmqgphjn0y4.cloudfront.net/live/ip/live.isml/live-audio_1=128000-video=4499968.m3u8

#EXTINF:-1 group-title="Argentina" tvg-logo="http://www.grupocronica.com.ar/mediakit/wp-content/uploads/2017/10/cronica-hd-con-sombra-grande.png" , CRONICA HD  24.4
https://g5.vxral-slo.transport.edge-access.net/b10/ngrp:cronicatv_video1-100044_all/cronicatv_video1-100044_720p/index.m3u8

#EXTINF:-1 group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/LogoCanal26.png/120px-LogoCanal26.png" , CANAL 26  24.2
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/chunklist_w794690609_b2628000_sleng.m3u8

#EXTINF:-1 group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/A24_%282019-1%29.png/150px-A24_%282019-1%29.png" , A24  36.3
https://g1.vxral-hor.transport.edge-access.net/a15/ngrp:a24-100056_all/a24-100056_720p.m3u8



#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/c/c8/Am%C3%A9rica_TV_%28Nuevo_logo_Junio_2020%29.png" group-title="Argentina", AMERICA HD  36.1
https://prepublish.f.qaotic.net/a07/americahls-100056/playlist_720p.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/b/b0/Canal9.jpg" group-title="Argentina", CANAL 9  35.1 
https://ar-elnueve-elnueve-live.ned.media/live.m3u8?iut=eyJwYXJhbXMiOnsiZXhwIjoxNjI5NDY0OTI5LCJzZXNzaW9uIjoiMTgxLjQ0LjEyOS43MSIsIndoaXRlbGlzdCI6WyIxODEuNDQuMTI5LjcxIl19LCJzaWduYXR1cmUiOiJjNzQ2NTZjMjM0MjI5MmYwMDBhMzExZjNlYWIzMzBlNzVmYjJmNzY1In0=



#EXTINF:-1 tvg-logo="http://images.pluto.tv/channels/5f523aa5523ae000074745ec/colorLogoPNG.png" group-title="Argentina" group-title="NEWS WORLD", TELEFÉ NOTICIAS
http://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5f523aa5523ae000074745ec/master.m3u8?advertisingId=&appName=web&appVersion=unknown&appStoreUrl=&architecture=&buildVersion=&clientTime=0&deviceDNT=0&deviceId=bff334c2-6307-11eb-b3fa-019cb96f121b&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&sid=dffc36b9-57c6-4973-9903-2f83d465ac40&userId=&serverSideAds=true

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/8/8f/Canal13_logo.png" group-title="Argentina", CANAL 13  33.1
http://edge5-sl.cvattv.com.ar/live/c3eds/ArtearHD/SA_SAGEMCOM/ArtearHD-avc1_379968=10016.m3u8



#EXTINF:-1 tvg-logo="https://scontent.fepa11-1.fna.fbcdn.net/v/t1.6435-9/206638151_10223169123710059_3666810289391430657_n.jpg?_nc_cat=101&ccb=1-3&_nc_sid=825194&_nc_eui2=AeGxugJ54qa7RhgKBnLTrHOu14OonvQq8lrXg6ie9CryWkCQzaYyrufVmZGkiprZVM0&_nc_ohc=dbLCQPiMFxEAX9X0jrT&_nc_ht=scontent.fepa11-1.fna&oh=afeef92e5377cb7720df7b2f4afc60c8&oe=6127F95F" group-title="Argentina", SSIPTV ARG TV
http://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5df265697ec3510009df1ef0/master.m3u8?advertisingId=&appName=web&appVersion=unknown&appStoreUrl=&architecture=&buildVersion=&clientTime=0&deviceDNT=0&deviceId=bff1d530-6307-11eb-b3fa-019cb96f121b&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&sid=ec2383fd-6e28-4df5-9d1c-b66eee700e0c&userId=&serverSideAds=true

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Net_TV_logo.png/120px-Net_TV_logo.png" group-title="Argentina", NET TV  27.2
https://unlimited1-us.dps.live/nettv/nettv.smil/nettv/livestream1/playlist.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Paka-paka.svg/245px-Paka-paka.svg.png" group-title="Argentina", PAKA PAKA  22.2
https://5fb24b460df87.streamlock.net/live-cont.ar/pakapaka/playlist.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Logo_The_Simpsons.svg/1200px-Logo_The_Simpsons.svg.png" group-title="Argentina", LOS SIMPSONS
https://videostreaming.cloudserverlatam.com/cloudservertv/cloudservertv/playlist.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/d/d6/Logomagic96.png" group-title="Argentina", MAGIC KIDS
https://live.admefy.com/live/clean_peach_ef224.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Cine.Ar_logo.svg/1280px-Cine.Ar_logo.svg.png" group-title="Argentina", CINEAR  22.4
https://5fb24b460df87.streamlock.net/live-cont.ar/cinear/playlist.m3u8   

#EXTINF:-1 tvg-logo="http://images.pluto.tv/channels/5de91cf02fc07c0009910465/colorLogoPNG.png" group-title="Argentina", TELEFÉ CLÁSICO
http://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5de91cf02fc07c0009910465/master.m3u8?advertisingId=&appName=web&appVersion=unknown&appStoreUrl=&architecture=&buildVersion=&clientTime=0&deviceDNT=0&deviceId=bff1ae23-6307-11eb-b3fa-019cb96f121b&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&sid=a367d0d9-b23d-4bb5-8d48-55f0cbeac4fb&userId=&serverSideAds=true

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/gwVNQhVICXN4Q7djaLyeQGCiMAa4Jum_PqeVaFZ1W90T4Y0G297wC1upnHRcKUbA6Q=w412-h220-rw" group-title="Argentina", GEN TV  17.3
https://videohd.live:19360/8010/8010.m3u8

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-Od4eldPqILM/XjtCKHxeYSI/AAAAAAAAvok/HDnuaXs9cCsFzbr0QrQtw3bYeDB0_5osACK8BGAsYHg/s0/2020-02-05.png" group-title="Argentina", CINCO TV TIGRE  30.1
https://59537faa0729a.streamlock.net/cincotv/cincotv/playlist.m3u8

#EXTINF:-1 tvg-logo="https://neotvdigital.com.ar/imagenes/logo1.png" group-title="Argentina", NEO TV DIGITAL  14.1
https://videostream.shockmedia.com.ar:19360/neotvdigital/neotvdigital.m3u8

#EXTINF:-1 tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMm0MM0BtkhB9xHWsECtnky05aGfA8KKnDSg&usqp=CAU" group-title="Argentina", CANAL 29 QUILMES 18.1
http://inliveserver.com:1935/8386/8386/playlist.m3u8

#EXTINF:-1 tvg-logo="https://serenotv.com/wp-content/uploads/2020/08/canal-telecreativa.jpg" group-title="Argentina", TELECREATIVA LANUS
https://panel.dattalive.com/8012/8012/playlist.m3u8

#EXTINF:-1 tvg-logo="https://image.winudf.com/v2/image1/Y29tLmExMjNmcmVlYXBwcy5mcmVlLmFwcDVkNWVjMWY4ODliOThfaWNvbl8xNTY3NjE5OTcxXzAxNw/icon.png?w=170&fakeurl=1" group-title="Argentina", CANAL 4 TELEAIRE SAN MARTIN
https://stmvideo2.livecastv.com/canal4/canal4/playlist.m3u8

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-SlqJrd0GiYk/XjtCBz2FbhI/AAAAAAAAvog/HkkKzNWrEOYiE08Rdlw-mxsDtzpJ_zD8wCK8BGAsYHg/s0/2020-02-05.png" group-title="Argentina", CANAL 6 MORENO
https://5975e06a1f292.streamlock.net:4443/canal6moreno/canal6moreno/playlist.m3u8

#EXTINF:-1 tvg-logo="http://www.radiosargentina.com.ar/png/VIC2PROV.png" group-title="Argentina", PROVINCIAL TV
http://www.trimi.com.ar/provincial/streaming/mystreamProvincialHSMed.m3u8

#EXTINF:-1 tvg-logo="http://www.canalkzo.com/images/lg_kzo.svg" group-title="Argentina", KZO
http://g2.vxral-slo.transport.edge-access.net/nx-beta/nx.hor.livetx.01/5eaa642772b3a25e2c28699e_540p/index.m3u8



#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/TYC_SPORTS.jpg/800px-TYC_SPORTS.jpg" group-title="Argentina", TyC SPORT 
https://d3055hobuue3je.cloudfront.net/out/v1/b841c366cbe540e6a106c3ba83e5c8d6/index.m3u8


#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-2gN4wEv_qPI/XjtKDwMuIQI/AAAAAAAAvrY/VTtJwZALBykDRnM8ia0Xbqi0FbREvdrZACK8BGAsYHg/s0/2020-02-05.png" group-title="Argentina", GARAGE TV
http://186.0.233.76:1935/Garage/smil:garage.smil/chunklist_w2049053275_b1296000_sleng.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Deutsche_Welle_symbol_2012.svg/150px-Deutsche_Welle_symbol_2012.svg.png" group-title="Argentina" group-title="NEWS WORLD", DW ESPAÑOL
https://dwamdstream104.akamaized.net/hls/live/2015530/dwstream104/stream05/streamPlaylist.m3u8

#EXTINF:-1 tvg-logo="http://tvabierta.weebly.com/uploads/5/1/3/4/51344345/mirador.png" group-title="Argentina", MIRADOR  22.3
https://5fb24b460df87.streamlock.net/live-cont.ar/mirador/playlist.m3u8 

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/4c/Telemax.png" group-title="Argentina", TELEMAX  26.3
https://live-edge01.telecentro.net.ar/live/smil:tlx.smil/playlist.m3u8

#EXTINF:-1 tvg-logo="https://d2ucqd3jt48qxz.cloudfront.net/img/footer-logo.png" group-title="Argentina", ORBE 21  21.2
https://cdn2.zencast.tv:30443/orbe/orbe21smil/playlist.m3u8

#EXTINF:-1 tvg-logo="https://dz92jh1unkapm.cloudfront.net/accounts/5cf95117cb97cae8e2c36676/logo.png" group-title="Argentina", UNIFE TV  25.1
https://dacastmmd.mmdlive.lldns.net/dacastmmd/98adedd6dec04a2d8663899b927f9383/chunklist_b4628000.m3u8

#EXTINF:-1 tvg-logo="http://www.radiosargentina.com.ar/png/VISANTAM.png" group-title="Argentina", SANTA MARIA
http://www.trimi.com.ar/santa_maria/streaming/mystreamSantaMariaHSMed.m3u8



#EXTINF:-1 tvg-logo="http://www.tectv.gob.ar/resources/img/logo.png" group-title="Argentina", TEC TV  22.5
https://g3.mc-hor.transport.edge-access.net/a09/ngrp:gcba_video3-100042_all/gcba_video3-100042_720p.m3u8






#EXTINF:-1, CANAL 26 
http://200.115.193.177/live/26hd-720/.m3u8

#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/ar/mi.tv.epg.xml"



#EXTM3U
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26  (San Justo-Arg.)
http://200.115.193.177/live/26hd-720/.m3u8?CompartilhandoIPTV
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26  (San Justo-Arg.)
http://live-edge01.telecentro.net.ar:1935/live/26hd-720/livestream.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26  (San Justo-Arg.)
http://live-edge01.telecentro.net.ar/live/26hd-720/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26 (San Justo-Arg.)
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/chunklist_w858131162_b414000_sleng.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://panel.dattalive.com:1935/8250/8250/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://uni5rtmp.tulix.tv:1935/bettervida/bettervida/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://moiptvhls-i.akamaihd.net/hls/live/652315/secure/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://api.new.livestream.com/accounts/22636012/events/8242619/live.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://www.coninfo.net:1935/tvcinco/live1/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://azxtv.com/hls/stream.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://103.199.161.254/Content/bbcworld/Live/Channel(BBCworld)/index.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://api.new.livestream.com/accounts/679322/events/3782013/live.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://59d52c5a5ce5e.streamlock.net:4443/canal3rosario/ngrp:canal3rosario_all/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://190.52.32.13:1935/canal4/smil:manifest.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://live.canalnueve.tv/canal.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5b3050bb1b2d8.streamlock.net/viviloendirecto2/canal9/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://panel.dattalive.com:1935/8204/8204/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://stmv4.questreaming.com/fenixlarioja/fenixlarioja/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5f700d5b2c46f.streamlock.net/madryntv/madryntv/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://arcast.net:1935/mp/mp/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://200.115.193.177/live/26hd-720/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://www.trimi.com.ar/provincial/streaming/mystream.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5e7cdf2370883.streamlock.net/tdconline/tdconline/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://panel.dattalive.com/8250/8250/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://s8.stweb.tv/chacra/live/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://59537faa0729a.streamlock.net/cincotv/cincotv/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5fb24b460df87.streamlock.net/live-cont.ar/cinear/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://coninfo.net:1935/chacodxdtv/live/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://dwamdstream102.akamaized.net/hls/live/2015525/dwstream102/index.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://dwamdstream104.akamaized.net/hls/live/2015530/dwstream104/index.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://v4.tustreaming.cl/enlacebpbtv/index.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://euronews-euronews-spanish-2-mx.samsung.wurl.com/manifest/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://d1nmqgphjn0y4.cloudfront.net/live/ip/live.isml/5ee6e167-1167-4a85-9d8d-e08a3f55cff3.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://srv1.zcast.com.br/lavozdetucuman/lavozdetucuman/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://panel.dattalive.com:1935/8250/8250/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://unlimited1-us.dps.live/nettv/nettv.smil/nettv/livestream1/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://stream.live.novotempo.com/tv/smil:tvnuevotiempo.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://wowza.telpin.com.ar:1935/live-powerTV/power.stream/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://rbmn-live.akamaized.net/hls/live/590964/BoRB-AT/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://strm.yandex.ru/kal/rt_hd/rt_hd0.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://www.trimi.com.ar/santa_maria/streaming/mystream.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://panel.seo.tv.bo:3337/live/franzbalboa2live.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://tastemade-es8intl-roku.amagi.tv/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://videostream.shockmedia.com.ar:1936/telejunin/telejunin/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://live-edge01.telecentro.net.ar/live/smil:tlx.smil/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://www.coninfo.net:1935/previsoratv/live/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://wowza.telpin.com.ar:1935/telpintv/smil:ttv.stream.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://wowza.telpin.com.ar:1935/telpintv/ttv.stream/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://live-edge01.telecentro.net.ar/live/smil:trm.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://tv-trtworld.live.trt.com.tr/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://cdnh4.iblups.com/hls/irtp.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://america-crtvg.flumotion.com/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://stratus.stream.cespi.unlp.edu.ar/hls/tvunlp.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://59a564764e2b6.streamlock.net/vallenato/Vallenato2/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5f700d5b2c46f.streamlock.net/vertv/vertv/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top  (Argentina)
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telemax  HD Argent.
http://live-edge01.telecentro.net.ar/live/smil:tlx.smil/chunklist_w950122583_b1828000_sleng.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",24/7 Canal de Noticias
http://59c5c86e10038.streamlock.net:1935/6605140/6605140/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",5RTV Santa Fe
http://api.new.livestream.com/accounts/22636012/events/8242619/live.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",5TV (Corrientes) (480p)
http://www.coninfo.net:1935/tvcinco/live1/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",5TV Corrientes
http://www.coninfo.net:1935/tvcinco/live1/chunklist_w1546509083.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",CANAL PROVINCIAL SAN MIGUEL
http://www.trimi.com.ar/provincial/streaming/mystream.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://200.115.193.177/live/26hd-180/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://200.115.193.177/live/26hd-720/.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://200.115.193.177/live/26hd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://live-edge01.telecentro.net.ar/live/26hd-360/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://live-edge01.telecentro.net.ar/live/26hd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://live-edge01.telecentro.net.ar:1935/live/26hd-720/livestream.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Chacra TV
http://s8.stweb.tv:1935/chacra/live/chunks.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Ciudad TV Chaco
http://coninfo.net:1935/chacodxdtv/live/chunklist_w1251301598.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music TOP
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/chunklist_w1582140541_b364000_sleng.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar/live/msctphd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar/live/musictop.smil/.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/chunklist_w538311571_b364000_sleng.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar:1935/live/msctphd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",TLX
http://live-edge01.telecentro.net.ar/live/tlxhd-720/master.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",TLX
http://live-edge01.telecentro.net.ar/live/smil:tlx.smil/master.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telemax
http://live-edge01.telecentro.net.ar/live/tlxhd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="277" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/277_Canal_XFN.png",Canal XFN * | AR
https://streamconex.com:1936/canalxfn/canalxfn/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1026" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1026_Tele_Mix.png",Tele Mix * | AR
https://panel.dattalive.com:443/8068/8068/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="488" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/488_Anime_Zone_TV.png",Anime Zone TV | AR
http://azxtv.com/hls/stream.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="206" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/206_Paka_Paka.jpg",Paka Paka | AR
https://5fb24b460df87.streamlock.net/live-cont.ar/pakapaka/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="251" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/251_13_Max_Television.png",13 Max Television | AR
http://coninfo.net:1935/13maxhd/live13maxtvnuevo_720p/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="221" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/221_5R_TV_Santa_Fe.png",5R TV Santa Fe | AR
http://api.new.livestream.com/accounts/22636012/events/8242619/live.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="249" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/249_5TV.png",5TV | AR
http://www.coninfo.net:1935/tvcinco/live1/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="252" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/252_Aire_de_Santa_Fe.png",Aire de Santa Fe | AR
https://sc1.stweb.tv/airedigital/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="215" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/215_Azahares_Radio_Multimedia.png",Azahares Radio Multimedia | AR
http://streamyes.alsolnet.com/azaharesfm/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="224" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/224_Cadena_103.png",Cadena 103 | AR
http://arcast.net:1935/cadena103/cadena103/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="799" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/799_Canal_10_Nortevision.jpg",Canal 10 Nortevision | AR
https://vivo.solumedia.com:19360/nortevision/nortevision.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="299" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/299_Canal_10_Rio_Negro.png",Canal 10 Rio Negro | AR
https://panel.dattalive.com:443/8204/8204/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="268" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/268_Canal_12_Madryn_TV.png",Canal 12 Madryn TV | AR
https://5f700d5b2c46f.streamlock.net:443/madryntv/madryntv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="227" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/227_Canal_13_La_Rioja.jpg",Canal 13 La Rioja | AR
http://arcast.net:1935/mp/mp/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="228" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/228_Canal_2_Jujuy.png",Canal 2 Jujuy | AR
http://api.new.livestream.com/accounts/679322/events/3782013/live.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="205" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/205_Canal_2_Sanagasta.jpg",Canal 2 Sanagasta | AR
https://stmvideo1.livecastv.com/canal2/canal2/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="229" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/229_Canal_20_Villamaria.png",Canal 20 Villamaria | AR
https://cronos.aldeaglobal.net.ar/hls/canal20.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1057" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1057_Canal_21_TV.png",Canal 21 TV | AR
https://iptv.ixfo.com.ar:30443/c21tv/hd/c21tv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="230" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/230_Canal_22_Buenos_Aires.jpg",Canal 22 Buenos Aires | AR
https://5f700d5b2c46f.streamlock.net:443/canal22/canal22/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="271" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/271_Canal_26.png",Canal 26 | AR
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26 HD (AR)
https://live-edge01.telecentro.net.ar/live/smil:c26.smil/chunklist.m3u8?ROGERIOTORRES
#EXTINF:-1  tvg-id="256" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/256_Canal_3_Rosario.png",Canal 3 Rosario | AR
https://59d52c5a5ce5e.streamlock.net:4443/canal3rosario/ngrp:canal3rosario_all/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="257" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/257_Canal_4_Bahia_Blanca.png",Canal 4 Bahia Blanca | AR
https://vivo.solumedia.com:19360/bvconline/bvconline.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="258" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/258_Canal_4_Jujuy.png",Canal 4 Jujuy | AR
http://190.52.32.13:1935/canal4/smil:manifest.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="259" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/259_Canal_4_Posadas.png",Canal 4 Posadas | AR
http://iptv.ixfo.com.ar:8081/live/C4POS/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="233" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/233_CANAL_5TV.jpg",CANAL 5TV | AR
https://srv3.zcast.com.br/carlosr/carlosr/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="307" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/307_Canal_6_Entre_Rios.png",Canal 6 Entre Rios | AR
https://stmvideo1.livecastv.com/canal6er/canal6er/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="262" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/262_Canal_6_Posadas.png",Canal 6 Posadas | AR
https://iptv.ixfo.com.ar:30443/live/c6digital/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="264" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/264_Canal_7_Jujuy.png",Canal 7 Jujuy | AR
https://stream.arcast.live/canal7jujuy/ngrp:canal7jujuy_all/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="236" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/236_Canal_9_Litoral.png",Canal 9 Litoral | AR
https://stream.arcast.live/ahora/ahora/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="309" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/309_Canal_9_Televida.png",Canal 9 Televida | AR
https://5b3050bb1b2d8.streamlock.net/viviloendirecto2/canal9/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="273" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/273_Canal_907_FM_Comunicar.png",Canal 907 FM Comunicar | AR
https://panel.dattalive.com/canal907/canal907/chunklist_w1205944599.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="274" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/274_Canal_Cinco_Tigre.png",Canal Cinco Tigre | AR
https://59537faa0729a.streamlock.net/cincotv/cincotv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="275" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/275_Canal_Coop.png",Canal Coop | AR
https://panel.dattalive.com:443/8138/8138/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="302" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/302_Canal_Nueve_TV.png",Canal Nueve TV | AR
https://live.canalnueve.tv/canal.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="801" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/801_Canal_Provincial.jpg",Canal Provincial | AR
https://streaming.telered.com.ar/provincial/streaming/mystream.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="278" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/278_Chacra_TV.png",Chacra TV | AR
https://s8.stweb.tv/chacra/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="237" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/237_Ciudad_TV.jpg",Ciudad TV | AR
http://coninfo.net:1935/chacodxdtv/live/chunklist_w1251301598.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="280" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/280_CL3_Cablevision.png",CL3 Cablevision | AR
http://videostream.shockmedia.com.ar:1935/cl3cable/cl3cable/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="270" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/270_CN_24_7_Neuquen.png",CN 24/7 Neuquen | AR
https://panel.dattalive.com:443/6605140/smil:6605140.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="893" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/893_Complejo_Dance.png",Complejo Dance | AR
https://mediacp.hostradios.com.ar:19360/complejodance/complejodance.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="238" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/238_CPE_TV.jpg",CPE TV | AR
https://stream.arcast.live/cpe/ngrp:cpe_all/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="239" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/239_Fenix.jpg",Fenix | AR
https://stmvideo1.livecastv.com/fenixlarioja/fenixlarioja/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="803" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/803_FM_Metropolitana_100_5_MHZ.png",FM Metropolitana 100.5 MHZ | AR
https://streamtv12.ddns.net:5443/LiveApp/streams/193945633734205616732920.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="216" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/216_Informacion_Periodistica.jpg",Informacion Periodistica | AR
https://d1nmqgphjn0y4.cloudfront.net/live/ip/live.isml/5ee6e167-1167-4a85-9d8d-e08a3f55cff3.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="217" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/217_La_Voz_de_Tucuman.png",La Voz de Tucuman | AR
https://srv1.zcast.com.br/lavozdetucuman/lavozdetucuman/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="212" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/212_Link_TV.png",Link TV | AR
https://panel.dattalive.com:443/8128_1/8128_1/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="283" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/283_Metro_TV_Canal_12_Tucuman.png",Metro TV Canal 12 Tucuman | AR
https://streamtv12.ddns.net:5443/LiveApp/streams/193945633734205616732920.m3u8?token=null&PlaylistM3UCL
#EXTINF:-1  tvg-id="795" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/795_Metropolitana_FM.png",Metropolitana FM | AR
https://panel.dattalive.com/MetropolitanaFM/MetropolitanaFM/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="284" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/284_Multivision.png",Multivisi n | AR
https://panel.dattalive.com:443/8250/8250/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="285" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/285_Net_TV.png",Net TV | AR
https://unlimited1-cl-isp.dps.live/nettv/nettv.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="243" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/243_Power.png",Power | AR
https://live2.tensila.com/1-1-1.power-tv/hls/master.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="912" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/912_Radio_Blu.png",Radio Blu | AR
https://59537faa0729a.streamlock.net:443/radioblu/radioblu/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="210" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/210_Radiocanal_San_Francisco.png",Radiocanal San Francisco | AR
http://204.199.3.2/.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="287" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/287_RTN.png",RTN | AR
http://media.neuquen.gov.ar/rtn/television/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="288" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/288_Sicardi_TV.png",Sicardi TV | AR
https://vivo.solumedia.com:19360/sicarditv/sicarditv.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="289" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/289_TDC_TV_Santa_Fe.png",TDC TV Santa Fe | AR
https://5e7cdf2370883.streamlock.net/tdconline/tdconline/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="308" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/308_Tele_Estrella.png",Tele Estrella | AR
https://stmvideo2.livecastv.com/telestrella/telestrella/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="290" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/290_Telecreativa.png",Telecreativa | AR
https://panel.dattalive.com:443/8012/8012/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="291" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/291_Telediario_Television.png",Telediario Televisi n | AR
https://mediacp.hostradios.com.ar:19360/telediario/telediario.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="245" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/245_Telediez.jpg",Telediez | AR
https://videohd.live:19360/8020/8020.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="292" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/292_Telemax.png",Telemax | AR
http://live-edge01.telecentro.net.ar/live/smil:tlx.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="814" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/814_TeleNord.jpg",TeleNord | AR
http://www.coninfo.net:1935/previsoratv/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="293" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/293_Telpin_Canal_2.png",Telpin Canal 2 | AR
https://wowza.telpin.com.ar:1935/telpintv/smil:ttv.stream.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="294" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/294_Terramia_TV.png",Terramia TV | AR
https://live-edge01.telecentro.net.ar/live/smil:trm.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="296" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/296_TSN_Necochea.png",TSN Necochea | AR
https://panel.dattalive.com:443/tsnnecochea/tsnnecochea/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="788" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/788_TV_Dos_Salta.jpg",TV Dos Salta | AR
https://vivo.solumedia.com:19360/tv2salta/tv2salta.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="248" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/248_Uni_Teve.png",Uni Teve | AR
https://vivo.solumedia.com:19360/uniteve/uniteve.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="493" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/493_Net_TV.png",Net TV | AR
https://unlimited1-cl-isp.dps.live/nettv/nettv.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="24" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/24_Music_Top.png",Music Top | AR
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="208" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/208_CINE_AR.png",CINE.AR | AR
https://5fb24b460df87.streamlock.net/live-cont.ar/cinear/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="207" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/207_Orbe_21.jpg",Orbe 21 | AR
https://cdn2.zencast.tv:30443/orbe/orbe21smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1003" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1003_Sublime_Gracia_TV.png",Sublime Gracia TV | AR
https://5f700d5b2c46f.streamlock.net:443/sublime/sublime/playlist.m3u8?PlaylistM3UCL


#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://www.cxtv.com.br/img/Tvs/Logo/webp-l/d800ee1a28bbee6769de24c5c050c40c.webp",Canal Once
https://vivo.canaloncelive.tv/alivepkgr3/ngrp:cepro_all/playlist.m3u8

#EXTINF:-1  tvg-id="N/A" group-title="N/A" tvg-logo="N/A",LA VOZ DE TUCUMAN
https://srv1.zcast.com.br/lavozdetucuman/lavozdetucuman/.m3u8




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

print('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/mudstein/XML/main/TIZENsiptv.xml"')
print('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/K-vanc/Tempest-EPG-Generator/main/Siteconfigs/Argentina/%5BENC%5D%5BEX%5Delcuatro.com_0.channel.xml"')
print('#EXTM3U x-tvg-url="https://github.com/Nicolas0919/Guia-EPG/raw/master/GuiaEPG.xml.gz"')
print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/ar/mi.tv.epg.xml.gz"')
print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/ar/directv.com.ar.epg.xml.gz"')

print(banner1)

#s = requests.Session()
with open('../ARGENTINA.txt', errors="ignore") as f:
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
print(banner2)
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
    
    

