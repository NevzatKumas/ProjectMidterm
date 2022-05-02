#libaries/frameworks
from fileinput import filename
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL import ImageFilter
from soupsieve import select

from imageEditor import selectionImage


#creates window
root = tk.Tk()
root.title('Image Editor')

entryMessage = Label(root, text = "Welcome to a user-level simple photo editor")
entryMessage.pack()

selectEditMessage = Label(root, text = "Please select your type of edit")
selectEditMessage.pack()

root.geometry("640x480")


#path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])

#selects between blur and rotate
def editSelection(args):
    if args == 1:
        blur()
        print("blur")
    if args == 2:
        rotate()
        print("rotate")
    if args == 3:
        crop()
        print("crop")

# def imageSelection(pictureSelected):
#     if pictureSelected == 1:
#          beachImage = Image.open("images/beach.jpg")
#          beachImage.show()
#          print("beach")
#     if pictureSelected == 2:
#          catImage = Image.open("images/cat.jpg")
#          catImage.show()
#          print("cat")
#     if pictureSelected == 3:
#          dogImage = Image.open("images/dog.jpg")
#          dogImage.show()
#          print("dog")

# def nextMenu():
#     root = tk.Tk()
#     root.title('Image selector')

#     selectImageMessage = Label(root, text = "Please select your image")
#     selectImageMessage.pack()

#     root.geometry("640x480")

#     beachButton =  tk.Button(root, text="Beach",command=lambda:imageSelection(1))
#     catButton =  tk.Button(root, text="Cat",command=lambda:imageSelection(2))
#     dogButton =  tk.Button(root, text="Dog",command=lambda:imageSelection(3))

#     beachButton.pack(pady=10)
#     catButton.pack(pady=20)
#     dogButton.pack(pady=30)

#     backButton = Button(root, text="Back",command=root.destroy)
#     backButton.pack(pady=30)

#shows original image followed by the edit (blur)

    #nextMenu()
def blur():
    try:
        filename = filedialog.askopenfile(filetypes=[("Image File",'.jpg')])
        selectedImage = 
        # selectedImage = Image.open(imagePath)
        # selectedImage =tk.PhotoImage(selectedImage)
        if selectedImage == "images/beach.jpg":
            selectedImage.filter(ImageFilter.BLUR)
            selectedImage.show()
            selectedImage.save("images/beachBlur.jpg")
        if selectedImage == "images/cat.jpg":
            selectedImage.filter(ImageFilter.BLUR)
            selectedImage.show()
            selectedImage.save("images/catBlur.jpg")
        if selectedImage == "images/dog.jpg":
            selectedImage.filter(ImageFilter.BLUR)
            selectedImage.show()
            selectedImage.save("images/dogBlur.jpg")
    except IOError:
        pass
    #_____.filter(ImageFilter.BLUR)
    #_____.show()
    #_____.save("_____.jpg")
    

    
#shows original image followed by the edit (rotate)
def rotate():
    global selectedImage
    #nextMenu()


def crop():
    #nextMenu()
    global selectedImage

#buttons for blur, rotate, and close
blurButton = tk.Button(root, text="Blur",command=lambda:editSelection(1))
rotateButton = tk.Button(root, text="Rotate",command=lambda:editSelection(2))
cropButton = tk.Button(root, text="Crop",command=lambda:editSelection(3))

blurButton.pack(pady=10)
rotateButton.pack(pady=20)
cropButton.pack(pady=30)

btnClose = Button(root, text="Close",command=root.destroy)
btnClose.pack(pady=30)

#to keep window open until closed
root.mainloop()
