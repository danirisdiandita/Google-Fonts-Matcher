import glob 
import os 
extensions = set([])
folder_path = 'fonts-main'
file_lists = glob.glob(f'{folder_path}/**/*', recursive=True)
fonts = []
for file_path in file_lists: 
    fname, ext_ = os.path.splitext(file_path)
    fname = os.path.basename(fname)
    if ext_ == '.ttf': 
        fonts.append(fname)

for idx, font_ in enumerate(fonts): 
    with open('fonts.txt', 'a') as f: 
        if idx == 0:
            f.write(font_)
        else: 
            f.write('\n' + font_)