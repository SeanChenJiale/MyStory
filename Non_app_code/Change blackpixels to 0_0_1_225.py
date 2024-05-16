# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:28:58 2024

@author: ChenS11
"""
### https://stackoverflow.com/questions/1616767/pil-best-way-to-replace-color#:~:text=You%20can%20apply%20the%20color_to_alpha%20function%20on%20the,much%20more%20efficient%20than%20accessing%20pixels%20using%20getdata.
from PIL import Image
import numpy as np

orig_color = (0,0,0,255)
replacement_color = (0,0,1,255)
img = Image.open(".\Assets\playerasset\playerspritesheet.png").convert('RGBA')
data = np.array(img)
data[(data == orig_color).all(axis = -1)] = replacement_color
img2 = Image.fromarray(data, mode='RGBA')
img2.show()
img2.save("playerspritesheet1.png")
