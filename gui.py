from tkinter import *
import time
import datetime


root = Tk()
label_1 = Label(root, text = "state")
label_2 = Label(root, text = "charge")
label_3 = Label(root, text = "0", bg = "white")
label_4 = Label(root, text = "0", fg ="red", bg = "white")
label_0 = Label(root, text = "House1")
label_5 = Label(root, text = "House2")
label_6 = Label(root, text = "Bank Account")
label_7 = Label(root, text = "0", bg = "white")

labelfont = ('times', 60, 'bold')
labelfont2 = ('times', 30, 'bold')

label_0.config(font = labelfont)
label_5.config(font = labelfont)
label_1.config(font = labelfont2)
label_2.config(font = labelfont2)
label_3.config(font= labelfont2)
label_4.config(font = labelfont2)
label_6.config(font= labelfont2)
label_7.config(font= labelfont2)


label_0.grid(columnspan = 2)
label_1.grid(row=1, sticky = E)
label_2.grid(row=2, sticky = E)
label_3.grid(row= 1, column =1)
label_4.grid(row = 2, column =1 )
label_5.grid(row = 0, column = 6, columnspan = 2)
label_6.grid(row = 3, sticky =E)
label_7.grid(row = 3, column = 1)



def set_label():
    label_3['text'] = house3.supply
    label_4['text'] = str(round(house3.charge,2)) + "%"
    label_7['text'] = str(round(house3.bankaccount,2)) + "$"
    root.after(2000, set_label)


