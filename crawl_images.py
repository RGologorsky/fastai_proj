# download images
import os
import sys
sys.path.append(".")

from pathlib import Path
from ai_utilities import *

# make train/valid folders
make_train_valid_flag = True
train = 0.8 
valid = 0.2
test  = 0

# Parameters
labels = ['garyfisher', 'specialized', 'diamondback' ]
search_texts = [f"{l} bike" for l in labels]
num_images = 50
engine = "bing"
image_dir = "bike_dataset"
apikey = None

# create dataset directory
path = Path.cwd()/image_dir
#os.makedirs(path, exist_ok=True)

# download images
for i,label in enumerate(labels):
	#os.makedirs(path/label, exist_ok=True)
	search_text = search_texts[i]
	image_download(search_text, num_images, label, engine, image_dir, apikey)
  
 # split into train/valid/test folders
if make_train_valid_flag:
	make_train_valid(path, train, valid, test)