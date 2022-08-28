#!/bin/bash

# ESPANHA - update the streams

$(wget https://raw.githubusercontent.com/davidmuma/log_dobleM/master/TDTChannels.m3u

sed -e "pipe:///usr/bin/env streamlink --stdout --default-stream best --url $(wget https://raw.githubusercontent.com/davidmuma/log_dobleM/master/TDTChannels.m3u )/" ESPANOL.M3U

exit 0
