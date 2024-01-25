#!/bin/bash 

ffmpeg -hide_banner -loglevel error -i output.png -vf drawtext='font=Montserrat\:style=Light Italic:text=FFmpeg' output3.png -y 

# /usr/share/fonts/truetype/montserrat/Montserrat-Italic[wght].ttf: Montserrat,Montserrat Thin:style=Light Italic