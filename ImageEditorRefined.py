#libaries/frameworks
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

#create window
root=Tk()
root.title("Photo Editor")
root.geometry("1280x720")

#open image
def imageOpen():
    global img_path, img1, imgg
    for m in range (0,v1.get()+1):
        img = Image.open(img_path)
        img.thumbnail((350,350))
        imgg = img.filter(ImageFilter.BoxBlur(m))
        img1 = ImageTk.PhotoImage(imgg)
        Canvas.create_image(300, 210, image = img1)
        Canvas.image=img1

# create canvas to display image
Canvas = Canvas(root, width="600", height="420", relief=RIDGE, bd=2)
Canvas.place(x=15, y=150)


root.mainloop()