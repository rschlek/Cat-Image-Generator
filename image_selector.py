import os
import random
from PIL import Image

def __str_append(str, add):
    str += add
    return str

cat_dir = __str_append(os.path.dirname(__file__),'\\Cat Images')

class image_selector:
    def __init__(self):
        
        # initializing the cat image file path list
        self.cat_q = []

        # looping through directory and getting all images paths
        for filename in os.listdir(cat_dir):
            print(type(os.path.join(cat_dir, filename)))
            self.cat_q.append(os.path.join(cat_dir, filename))
        
        # shuffling list so that image order is random
        random.shuffle(self.cat_q)
            

    '''
    method to get a cat image
    '''
    def get_cat_image(self):
        image_path = self.cat_q.pop(0)
        self.cat_q.append(image_path)
        return Image.open(image_path)