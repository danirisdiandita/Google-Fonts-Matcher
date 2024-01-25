

import os 


downloaded_fonts = os.listdir('/home/dani/Downloads/googlefonts')
downloaded_fonts = set(downloaded_fonts)
all_fonts = []
with open('fontLink.txt') as f: 
    all_fonts = f.read().splitlines()

all_fonts = [font_[len('https://fonts.google.com/specimen/'):].replace('+', '-') + '.zip' for  font_ in all_fonts]
# 

notyetfonts = [font_ for font_ in all_fonts if font_ not in downloaded_fonts]
print(len(all_fonts))
print(len(notyetfonts))
