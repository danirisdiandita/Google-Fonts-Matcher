#!/bin/bash 
# ffmpeg -f lavfi -i color=c=black:s=250x250 -frames:v 1 output.png
python -c "import numpy as np;import cv2;cv2.imwrite('output.png', np.zeros([300,2500,3]))"
# ffmpeg -i output.png -vf drawtext=fontfile="/Users/dani/Researches/Google-Fonts-Matcher/fonts-main/ofl/montserrat/Montserrat[wght].ttf":fontsize=30:fontcolor=black:x=(w-text_w)/2:y=(h-text_h)/2:text='gitu':box=1 -y output2.png -y 
# ffmpeg -hide_banner -loglevel error -i output.png -vf "drawtext=text='Montserrat':x=0:y=0:fontsize=300:fontcolor=white:fontfile=/Users/dani/Researches/Google-Fonts-Matcher/fonts-main/ofl/montserrat/Montserrat\[wght\].ttf:style=Semibold" -c:a copy output2.png -y
# ffmpeg -hide_banner -loglevel error -i output.png -vf "drawtext=text='Whereas disregard and contempt for human rights have resulted':x=0:y=0:fontsize=300:fontcolor=white:font=Montserrat Thin" -c:a copy output2.png -y
ffmpeg -hide_banner -loglevel error -i output.png -vf "drawtext=text='Whereas disregard and contempt for human rights have resulted':x=0:y=0:fontfile=/usr/share/fonts/Roboto/Roboto-Italic.ttf:fontsize=300:fontcolor=white" -c:a copy outputgitu.png -y 

for font in $(ls /usr/share/fonts/Roboto)
do 
    outname=$(basename $font)
    outname_without_ext="${outname%.*}"
    ffmpeg -hide_banner -loglevel error -i output.png -vf "drawtext=text='Whereas disregard and contempt for human rights have resulted':x=0:y=0:fontfile=/usr/share/fonts/Roboto/$font:fontsize=300:fontcolor=white" -c:a copy $outname_without_ext.png -y 
done  