#libaries/frameworks
from logging import root
from tkinter import *
import tkinter as ImageTK
from PIL import Image
from PIL import ImageFilter



#creates window
def mainMenu():
    root = ImageTK.Tk()
    root.title('Image Editor')
    root.geometry("1280x720")

    btn = Button(root,text = "Select Image", command=create)

    root.mainloop()
   

def imageMenu():
    global screen2
    screen2 = ImageTK.TK()
    screen2.title('Image Selector')
    screen2.geometry("1280x720")


#selects between blur and rotate
def selectionMainMenu(args):
    if args == 1:
        blur()
    if args == 2:
        rotate()
    if args == 3:
        crop()

def selectionImage(args):
    if args == 1:
        beachImage()
    if args == 2:
        dogImage()
    if args == 3:
        catImage()

def beachImage():
    beachImage = Image.open("images/beach.jpg")
    beachImage.show()

def dogImage():
    dogImage = Image.open("image/dog.jpg")
    dogImage.show()

def catImage():
    catImage = Image.open("images/cat.jpg")
    catImage.show()

def blur():
    global blurImage
    blurImage = beachImage()
    #saves edited image of original image
    blurEffect = blurImage.filter(ImageFilter.BLUR)
    blurEffect.show()
    blurEffect.save('blurImage.jpg')

#shows original image followed by the edit (rotate)
def rotate():
    global rotateImage
    rotateImage = beachImage() or dogImage() or catImage()
    rotateImage.show()
    if rotateImage is None:
        print("val = none")
    else:
        print(rotateImage)
    

    rotateEffect = rotateImage.rotate(45)
    rotateEffect.show()
    #saves edited image of original image
    rotateEffect.save('rotateImage.jpg')

#shows original image followed by the edit (crop)
def crop():
    global cropImage
    cropImage = beachImage() or dogImage() or catImage()
    cropImage.show()

    cropEffect = cropImage.crop((1,2,300,300))
    cropEffect.show()
    #saves edited image of original image
    cropEffect.save('croppedImage.jpg')

#buttons for blur, rotate, and close
def mainMenu():
    global selection
    blurButton = ImageTK.Button(root, text="Blur",command=lambda:selection(1))
    rotateButton = ImageTK.Button(root, text="Rotate",command=lambda:selection(2))
    cropButton = ImageTK.Button(root, text="Crop",command=lambda:selection(3))
    blurButton.pack(pady=10)
    rotateButton.pack(pady=20)
    cropButton.pack(pady=30)
    closeButton = Button(root, text="Close",command=root.destroy)
    closeButton.pack(pady=30)

def imageSelection():
    beachButton = ImageTK.Button(root, text="Beach",command=lambda:selection(1))
    dogButton = ImageTK.Button(root, text="Dog",command=lambda:selection(2))
    catButton = ImageTK.Button(root, text="Cat",command=lambda:selection(3))
    beachButton.pack(pady=10)
    dogButton.pack(pady=20)
    catButton.pack(pady=30)

#to keep window open until closed
