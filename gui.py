from tkinter import *
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import args as args

root3 = Tk()
root3.geometry("640x640+0+0")

label1 = Label(root3, text = "Enter season number=").place(x=10, y=200)

name = StringVar()
entry_box = Entry(root3, textvariable = name, width = 25).place(x=200,y=200)
list=[]


def print_it():
    open('new.txt', 'w').close()
    pullData1 = open("new.txt","a+")
    pullData1.write(str(name.get()))
    x_list = []
    pullData1 = open("new.txt","r")
    f1 = pullData1.readlines()
    for x in f1:
        x_list.append(x)
        return x_list[0]

print_season = Button(root3, text = "print", width =30, height = 5, command = print_it).place(x=250,y=300)
exit = Button(root3, text = "exit", width =5, height = 5, command = root3.destroy).place(x=250,y=450)
root3.mainloop()

season = str(print_it())
print(season)







