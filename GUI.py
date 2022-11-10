from tkinter import *
import image_selector
from PIL import Image, ImageTk

i = image_selector()

class gui:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("Natalie's Cat Picture Program")
        self.root.mainloop()

        self.image_frame = Frame(self.root) #Defining a frame to place the image
        self.image_frame.pack
        self.button_frame = Frame(self.root) #Defining a frame to place the image


        

g = gui()


