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
img = np.zeros((250,250,3),np.uint8)
fontpath = "/home/dani/Researches/Google-Fonts-Matcher/fonts-main/ofl/roboto/Roboto[wdth,wght].ttf"
font = ImageFont.truetype(fontpath, 250)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
draw.text((0,0), "R", font=font, fill=(255,255,255,0))
img = np.array(img_pil)
cv2.imwrite("R.png", img)