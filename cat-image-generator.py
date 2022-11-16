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
        return image_path

    '''
    mehtod to get last image
    '''
    def go_back_image(self):
        image_path = self.cat_q.pop(len(self.cat_q)-1)
        self.cat_q.insert(image_path)
        return image_path

    '''
    Method to return the next image's dimensions
    width,height
    '''
    def get_next_image_dims(self):
        pass






class gui:
    def __init__(self):
        self.selector = image_selector()
        
        self.WINDOW_HEIGHT = 1000
        self.WINDOW_WIDTH = 1000


        # Window
        self.root = Tk()
        self.root.geometry(str(self.WINDOW_HEIGHT) + "x" + str(self.WINDOW_WIDTH))
        self.root.title("Natalie's Cat Picture Program")
        

        # cat image
        first_image = ImageTk.PhotoImage(Image.open(self.selector.get_cat_image()))
        self.image_label = Label(self.root, image=first_image)
        self.image_label.pack(side=TOP)
        
        # Last cat picture button
        self.old_cat_button = Button(self.root, text="Last Cat Picture", command=self.__prev_picture).pack(side=BOTTOM)

        # New cat Picture Button
        self.cat_button = Button(self.root, text="New Cat Picture", command=self.__new_picture).pack(side=BOTTOM)


        # mainloop
        self.root.mainloop()

    '''
    Method to update the image
    '''
    def __new_picture(self):
        new_image = ImageTk.PhotoImage(Image.open(self.selector.get_cat_image()))
        self.image_label["image"] = new_image
        self.image_label.image=new_image


    '''
    Method to go back an image
    '''
    def __prev_picture(self):
        new_image = ImageTk.PhotoImage(Image.open(self.selector.go_back_image()))
        self.image_label["image"] = new_image
        self.image_label.image=new_image
    
    
    '''
    Method to get current window dimensions, next image dimensions, 
    '''
    def __resize_image(self):
        pass
    
       
        
           










def main():
    g = gui()

if __name__ == "__main__":
    main()