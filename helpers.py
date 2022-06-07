#### HELPER FUNCTIONS ####

import constants as keys
from typing import List
import random as r
from PIL import Image


colors = [color for color in keys.COLOR_TABLE]
meme_sizes = keys.MEME_IMG_SIZES
start_points = keys.PLANTING_POINTS


def memes_random_picker(img_paths: List[str]) -> List[List[str]]:
    """Function to randomly pick memes for each collage and return the random picks and left overs"""
    img_paths = [path for path in img_paths if path[-3:] == "jpg" or path[-3:] == "png"] # only pick png and jpg files
    n = len(img_paths)
    randomized_picks = [[] for _ in range(n//4 + 1)]
    curr_index = 0
    
    for i in range(n):
        if i % keys.MEME_COUNT_PER_COLLAGE == 0 and i > 0:
            curr_index += 1
        
        pick = r.choice(img_paths)
        img_paths.remove(pick)
        randomized_picks[curr_index].append(pick)
        
    return randomized_picks


def resize_img(image_path: str, new_size: int) -> None:
    """Resize image and replace the original with new image"""
    img = Image.open(image_path)
    img = img.resize((new_size,new_size), Image.Resampling.LANCZOS)
    img.save(image_path)


def make_collage(img_paths: List[str], save_as: str) -> None:
    """This function takes a list of the paths of the meme images and saves it at save_as"""
    background_color = r.choice(colors)
    background = Image.open(f"backgrounds/{background_color}.jpg")
    
    for ind, point in enumerate(start_points):
        meme_path = img_paths[ind]
        meme_size = meme_sizes[ind]
        resize_img(image_path=meme_path, new_size=meme_size)
        meme = Image.open(meme_path, "r")
        
        background.paste(meme, point)
        
    background.save(save_as)