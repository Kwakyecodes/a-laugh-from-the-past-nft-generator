##### Python file to create an Opensea banner for this NFT collection #####

# Import libraries and modules
from PIL import Image
import os
import random as r
import constants as keys


# some important constants
banner_size = keys.BANNER_SIZE
collage_size = keys.BANNER_COLLAGES_SIZE
background_path = "banner/banner.jpg"


# collect collages paths into list collages
collages = []
for date in keys.DATES:
    folder = f"collages/{date}"
    for filename in os.listdir(folder):
        file = os.path.join(folder, filename)
        if not os.path.isfile(file):
            continue
        collages.append(file)
        
background = Image.new(mode = "RGB", size=banner_size)

for i in range(0, banner_size[0], collage_size[0]):
    for j in range(0, banner_size[1], collage_size[0]):
        img = Image.open(r.choice(collages))
        img = img.resize(collage_size, Image.Resampling.LANCZOS)
        planting_point = (i, j)
        background.paste(img, planting_point)
        
background.save(background_path)