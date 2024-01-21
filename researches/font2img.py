# import glob 
# import os 
# from PIL import ImageFont, ImageDraw, Image
# extensions = set([])
# folder_path = '/home/dani/Researches/Google-Fonts-Matcher/fonts-main'
# file_lists = glob.glob(f'{folder_path}/**/*', recursive=True)
# fonts = []
# for file_path in file_lists: 
#     fname, ext_ = os.path.splitext(file_path)
#     fname = os.path.basename(fname)
#     if ext_ == '.ttf': 
#         fonts.append(fname)
#     if file_path.__contains__("Roboto"): 
#         print(file_path) # /home/dani/Researches/Google-Fonts-Matcher/fonts-main/ofl/roboto/Roboto[wdth,wght].ttf

from PIL import ImageFont, ImageDraw, Image 
import cv2 
import numpy as np 
import subprocess
img = np.zeros((250,2500,3),np.uint8)
# fontpath = "../fonts-main/ofl/nokora/Nokora-Black.ttf"
# fontpath = '../fonts-main/ofl/montserrat/Montserrat-Italic[wght].ttf'
fontpath = '../fonts-main/ofl/montserrat/Montserrat[wght].ttf'
result = subprocess.run(['fc-scan', '--format', "%{fullname}\n", fontpath], capture_output=True, text=True)
print(result.stdout.strip('\n').split('\n'))
font = ImageFont.FreeTypeFont(fontpath, size=250, index=1)
nn = font.get_variation_names()
print(nn)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
draw.text((0,0), "Montserrat", font=font, fill=(255,255,255,0))
img = np.array(img_pil)
cv2.imwrite("R.png", img)