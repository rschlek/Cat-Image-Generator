from tkinter import *

from image_selector import image_selector


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
       
    '''
    
    ''' 
    def new_picture(self):
        return 

        

g = gui()


