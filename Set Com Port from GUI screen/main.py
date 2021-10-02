import serial 
from tkinter import Tk, Label, Button,Entry,StringVar,messagebox
import serial.tools.list_ports
import csv
import pandas as pd
from functools import partial  
##import serial
import pandas as pd
import ast
##import threading
import time
global ser
def connect():
    global ser
    print(com_number.get())
    portvar=com_number.get()
    ser = serial.Serial("COM"+str(portvar), 9600)    
def startdata():
    Serialdata()
def Serialdata():
    global ser
##    ser = serial.Serial(str(portvar), 9600) 
    rows_ax = []
    rows_ay = []
    rows_az = []
    try:
        
        time.sleep(0.2)
        data = ser.readline()
        bin_data = data.decode()
        str_data = bin_data.rstrip()
        res = ast.literal_eval(str_data)
    ##            print(res[0])
        valAx = Label(root, text=res[0],fg="white",bg="#9bbffa", font=("Arial", 12))
        valAx.place(x=35,y=10)

        valAy = Label(root, text=res[1],fg="white",bg="#9bbffa", font=("Arial", 12))
        valAy.place(x=35,y=40)

        valAz = Label(root, text=res[2],fg="white", bg="#9bbffa", font=("Arial", 12))
        valAz.place(x=35,y=70)
        
        rows_ax.append(res[0])
        rows_ay.append(res[1])
        rows_az.append(res[2])
        #print(rows_ax)
        dict = {'Val 1':rows_ax,
                'Val 2':rows_ay,
                'Val 3':rows_az}
        print(dict)
        df = pd.DataFrame(dict)
        
     # saving the dataframe
        df.to_csv('file1.csv')
        root.after(5, Serialdata)

##    root.after(5, Serialdata)
    except:
##        messagebox.showinfo("Error","Wrong port")
##        ser.flush()
        root.after(5, Serialdata)
root = Tk()
root.title("Accelerometer Data")
root.geometry("350x150")
root.resizable(0, 0)
root.configure(bg='#9bbffa')

Ax = Label(root, text="Val 1",fg="white",bg="#9bbffa", font=("Arial", 12))
Ax.place(x=5,y=10)

Ay = Label(root, text="Val 2",fg="white",bg="#9bbffa", font=("Arial", 12))
Ay.place(x=5,y=40)

Az = Label(root, text="Val 3",fg="white", bg="#9bbffa", font=("Arial", 12))
Az.place(x=5,y=70)

button_start = Button(root, text="Start",width="10",fg="white", bg="#fa89a4",command=Serialdata)
button_start.place(x=150,y=10)
##
##button_stop = Button(root, text="Stop",width="10",fg="white", bg="#fa89a4",command=stopdata)
##button_stop.place(x=150,y=40)

##
##
com_number = StringVar()  
comportval = Entry(root,textvariable= com_number)
comportval.place(x = 140, y = 100,width="100")
##connect = partial(connect, com_number)
##
button_connect = Button(root, text="Connect", width="10", fg="white", bg="#fa89a4",command=connect)
button_connect.place(x=150, y=70)
##root.after(5, Serialdata)
root.mainloop()
