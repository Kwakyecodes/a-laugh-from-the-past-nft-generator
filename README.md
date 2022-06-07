# A Laugh From The Past NFT Collection Generator 
This is the official Python script that I used to generate A Laugh From The Past nft collection. 
Collectively, this project collects memes from different years from the internet and then combines a number of them
to form beautiful collages. The memes are collected from the years 2010 to 2021. The point of this project is to take a
peak into the past and essentially, appreciate the development of memes and perhaps experience some sort of nostalgia.
 
## Files in this project and their description

### constants.py
If you want to produce an nft collection similar to this, you should check out constants.py first. In this file, I define some of the
constants that also define the nft collection and what it should look like. By changing some of the variables there, you can reproduce another nft collection in the same way this A Laugh From The Past was made.

### backgrounds.py
This python script generates the backgrounds that will be used for the collages. 

### memes.py
This python script downloads and saves memes from specific years.

### helpers.py
helpers.py contains functions that will be essential in the generation of collages using the memes and backgrounds that have already been generated.

### collages.py
This is the main file for the production of collages using the memes and the backgrounds. This files takes memes from specific years and randomly paste the memes of different backgrounds to make collages. The collage is then saves in self-descriptive directory.

### banner.py
This python script generates a 1400 by 400 image (as recommended by OpenSea) of random memes from all years on a black background.

### requirements.txt
Lists the python libraries used for this project.