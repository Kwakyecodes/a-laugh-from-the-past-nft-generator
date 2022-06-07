#### GENERATE BACKGROUNDS ####

import constants as keys
from PIL import Image, ImageDraw


path = "backgrounds/" 
size = keys.BACKGROUND_SIZE
colors = keys.COLOR_TABLE
shape = [(0, 0), size]

for color in colors:
    color_id = colors[color]
    
    img = Image.new("RGB", size)
  
    # create  rectangle image
    img1 = ImageDraw.Draw(img)  
    img1.rectangle(shape, fill = color_id)
    img = img.save(path + f"{color}.jpg")