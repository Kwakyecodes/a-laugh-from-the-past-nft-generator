#### GENERATE MEME COLLAGES FOR ALL YEARS AND COMBINATIONS OF YEARS ####

import os
import sys
import constants as keys
from helpers import memes_random_picker, make_collage

dates = [date for date in keys.DATES]
search_queries = keys.SEARCH_QUERIES


for date in dates:
    
    memes_directories = []
    for search_query in search_queries:
        sq_path = search_query.replace(" ", "_")
        memes_directories.append(f"meme_images/{date}_{sq_path}")
        
    all_memes = [os.path.join(memes_directories[0], filename) for filename in os.listdir(memes_directories[0]) if os.path.isfile(os.path.join(memes_directories[0], filename))] + [os.path.join(memes_directories[1], filename) for filename in os.listdir(memes_directories[1]) if os.path.isfile(os.path.join(memes_directories[1], filename))] + [os.path.join(memes_directories[2], filename) for filename in os.listdir(memes_directories[2]) if os.path.isfile(os.path.join(memes_directories[2], filename))]
    
    randomized_picks = memes_random_picker(img_paths=all_memes)
    
    collages_directory = f"collages/{date}"
    
    print("Making", date, "meme collages")
    
    
    for ind, pick in enumerate(randomized_picks):
        if len(pick) == keys.MEME_COUNT_PER_COLLAGE:
            filename = f"{date}_{ind+1}.jpg"
            file_path = os.path.join(collages_directory, filename)
            try:
                make_collage(img_paths=pick, save_as=file_path)
            except:
                continue
        
         
print("All done!")