#!/bin/bash 

for font in $(find fonts-main -name '*.ttf')
do  
    name=$(dirname $font)
    name=$(basename $name )
    mkdir -p /usr/share/fonts/truetype/$name 
    cp $font /usr/share/fonts/truetype/$name/
    # echo $font 
done 