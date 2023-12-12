from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox
gamewindow = Tk()
gamewindow.title("Vienādie attēli")

myImg1 = ImageTk.PhotoImage(Image.open("img1.jpg"))
myImg2 = ImageTk.PhotoImage(Image.open("img2.jpg"))
myImg3 = ImageTk.PhotoImage(Image.open("img3.jpg"))
myImg4 = ImageTk.PhotoImage(Image.open("img4.jpg"))
myImg5 = ImageTk.PhotoImage(Image.open("img5.jpg"))
myImg6 = ImageTk.PhotoImage(Image.open("img6.jpg"))

bgImg = ImageTk.PhotoImage(Image.open("img7.jpg"))

btn0 = Button(width = 200, height = 300, image = bgImg)
btn1 = Button(width = 200, height = 300, image = bgImg)
btn2 = Button(width = 200, height = 300, image = bgImg)
btn3 = Button(width = 200, height = 300, image = bgImg)
btn4 = Button(width = 200, height = 300, image = bgImg)
btn5 = Button(width = 200, height = 300, image = bgImg)
btn6 = Button(width = 200, height = 300, image = bgImg)
btn7 = Button(width = 200, height = 300, image = bgImg)
btn8 = Button(width = 200, height = 300, image = bgImg)
btn9 = Button(width = 200, height = 300, image = bgImg)

btn0.grid(row = 0, column = 0)
btn1.grid(row = 0, column = 1)
btn2.grid(row = 0, column = 2)
btn3.grid(row = 0, column = 3)
btn4.grid(row = 0, column = 4)
btn5.grid(row = 1, column = 0)
btn6.grid(row = 1, column = 1)
btn7.grid(row = 1, column = 2)
btn8.grid(row = 1, column = 3)
btn9.grid(row = 1, column = 4)




gamewindow.mainloop()