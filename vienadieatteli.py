from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox

gamewindow = Tk()
gamewindow.title("Vienādie attēli")
gamewindow.configure(bg = "black")
gamewindow.resizable(1, 1)

Img1 = ImageTk.PhotoImage(Image.open("img1.jpg"))
Img2 = ImageTk.PhotoImage(Image.open("img2.jpg"))
Img3 = ImageTk.PhotoImage(Image.open("img3.jpg"))
Img4 = ImageTk.PhotoImage(Image.open("img4.jpg"))
Img5 = ImageTk.PhotoImage(Image.open("img5.jpg"))

ImageList = [Img1, Img1, Img2, Img2, Img3, Img3, Img4, Img4, Img5, Img5]

myLabel = Label(image = Img1)

bgImg = ImageTk.PhotoImage(Image.open("img6.jpg"))

btn0 = Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn0, 0))
btn1 = Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn1, 1))
btn2 = Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn2, 2))
btn3 = Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn3, 3))
btn4 = Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn4, 4))
btn5 = Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn5, 5))
btn6 = Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn6, 6))
btn7 = Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn7, 7))
btn8 = Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn8, 8))
btn9 = Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn9, 9))

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

random.shuffle(ImageList)

count = 0
correctAnswer = 0
answers = []
answer_dict = {}
answerCount = 0

def reset():
    global count, correctAnswer, answers, answer_dict, answerCount
    btn0.config (status = NORMAL)
    btn1.config (status = NORMAL)
    btn2.config (status = NORMAL)
    btn3.config (status = NORMAL)
    btn4.config (status = NORMAL)
    btn5.config (status = NORMAL)
    btn6.config (status = NORMAL)
    btn7.config (status = NORMAL)
    btn8.config (status = NORMAL)
    btn9.config (status = NORMAL)

    btn0["image"] = "pyimage6"
    btn1["image"] = "pyimage6"
    btn2["image"] = "pyimage6"
    btn3["image"] = "pyimage6"
    btn4["image"] = "pyimage6"
    btn5["image"] = "pyimage6"
    btn6["image"] = "pyimage6"
    btn7["image"] = "pyimage6"
    btn8["image"] = "pyimage6"

    random.shuffle(ImageList)

    count = 0
    correctAnswer = 0
    answers = []
    answer_dict = {}
    answerCount = 0

#def infologs():
    #gamewindow = Toplevel()
    #gamewindow.title("Info par programmu")
    #gamewindow.geometry("500x500")
    #apraksts = 

def btnClick(btn, number):
    global count, correctAnswers, answers, answer_dict
    if btn["image"] == "pyimage" and count < 2:
        btn["image"] = ImageList[number]
        count +- 1
        answers.append(number)
        answer_dict[btn] = ImageList(number)
    if len(answers) == 2:
        if ImageList[answers[0]] == ImageList[answers[1]]:
            for key in answer_dict:
                key ["state"] = DISABLED
            correctAnswer =+ 2
            if correctAnswer == 2:
                messagebox.showinfo("Vienādie attēli", "Esi uzminējis!")
                correctAnswer = 0
                if correctAnswer == 5:
                    messagebox.askquestion("Vienādie attēli", "Tu uzvarēji!", "Tu zaudēji!")
            else:
                messagebox.showinfo("Vienādie attēli", "Neuzminēji!")
                for key in answer_dict:
                    key["image"] = "pyimage6"
            count = 0
            answers = []
            answer_dict = {}
    return 0

galvenaIzvelne = Menu(gamewindow)
gamewindow.config(menu = galvenaIzvelne)

opcijas = Menu(galvenaIzvelne, tearoff = False)
galvenaIzvelne.add_cascade(label = "Opcijas", menu = opcijas)

opcijas.add_command(label = "Jauna spēle", command = gamewindow.reset)
opcijas.add_command(label = "Iziet", command = gamewindow.quit)

#galvenaIzvelne.add_command(label = "Par programmu", command = infoLogs)





gamewindow.mainloop()