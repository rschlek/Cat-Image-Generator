import os
import random
from tkinter import *
from PIL import Image, ImageTk



def str_append(str, add):
    str += add
    return str

cat_dir = str_append(os.path.dirname(__file__),'\\Cat Images')

class image_selector:
    def __init__(self):
        
        # initializing the cat image file path list
        self.cat_q = []

        # looping through directory and getting all images paths
        for filename in os.listdir(cat_dir):
            self.cat_q.append(os.path.join(cat_dir, filename))
        
        # shuffling list so that image order is random
        random.shuffle(self.cat_q)
            

    '''
    method to get a cat image
    '''
    def get_cat_image(self):
        image_path = self.cat_q.pop(0)
        self.cat_q.append(image_path)
        image = Image.open(image_path)
        photo_image = PhotoImage(image)
        return photo_image







class gui:
    def __init__(self):
        self.selector = image_selector()
        
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("Natalie's Cat Picture Program")
        
        # cat image
        self.image_label = Label(self.root, image=self.selector.get_cat_image())
        self.image_label.pack(side=TOP)
        
        # Cat Picture Button
        self.cat_button = Button(self.root, text="New Cat Picture", command=self.new_picture).pack(side=BOTTOM)
        
        self.root.mainloop()
       
       def new_picture(self):
           










def main():
    g = gui()

if __name__ == "__main__":
    main()