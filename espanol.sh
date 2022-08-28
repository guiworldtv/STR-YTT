#!/bin/bash

# ESPANHA - update the streams

$resultado = wget http://www.atp.com.br/extranet/servicoBanco/service.asmx

sed -e "pipe:///usr/bin/env streamlink --stdout --default-stream best --url $(wget -r https://raw.githubusercontent.com/davidmuma/log_dobleM/master/TDTChannels.m3u -O ESPANOL.M3U )/"

exit 0
