from tkinter import *

root = Tk()

root.geometry('500x250')

def main():
    frame = Frame(root, width=500,height=250,bg='yellow')
    frame.place(x=0,y=0)

    btn1 = Button(frame,text='Home',command=main)
    btn1.place(x=10,y=10)
    btn2 = Button(frame,text='Screen 1',command=screen1)
    btn2.place(x=10,y=50)
    btn3 = Button(frame,text='Screen 2',command=screen2)
    btn3.place(x=10,y=80)

    lab = Label(frame,text="Home")
    lab.place(x=120,y=50)

def screen1():
    frame1 = Frame(root, width=500,height=250,bg='green')
    frame1.place(x=0,y=0)

    btn1 = Button(frame1,text='Home',command=main)
    btn1.place(x=10,y=10)
    btn2 = Button(frame1,text='Screen 1',command=screen1)
    btn2.place(x=10,y=50)
    btn3 = Button(frame1,text='Screen 2',command=screen2)
    btn3.place(x=10,y=80)
    lab = Label(frame1,text="Screen1")
    lab.place(x=120,y=50)

def screen2():
    frame2 = Frame(root, width=500,height=250,bg='red')
    frame2.place(x=0,y=0)

    btn1 = Button(frame2,text='Home',command=main)
    btn1.place(x=10,y=10)
    btn2 = Button(frame2,text='Screen 1',command=screen1)
    btn2.place(x=10,y=50)
    btn3 = Button(frame2,text='Screen 2',command=screen2)
    btn3.place(x=10,y=80)

    lab = Label(frame2,text="Screen2")
    lab.place(x=120,y=50)

main()


root.mainloop()
