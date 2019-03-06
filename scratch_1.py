from tkinter import *
import time
import datetime

def doNothing():
    print("ok")

root = Tk()
# # # theLabel = Label(root, text = "this is too easy")
# # # theLabel.pack()

# # topFrame = Frame(root)
# # topFrame.pack()
# # bottomFrame = Frame(root)
# # bottomFrame.pack(side = BOTTOM)
# # button1 = Button(topFrame, text = "button1", fg = "red")
# # button2 = Button(topFrame, text = "button2", fg = "green")
# # button3 = Button(bottomFrame, text = "button3", fg = "white")
# #
# # button1.pack(side = LEFT)
# # button2.pack(side = LEFT)
# # # button3.pack()
#
# one = Label(root, text = "one", fg = "white", bg = "red")
# one.pack()
# two = Label(root, text = "two", fg = "black", bg = "green")
# two.pack(fill=X)
# three = Label(root, text = "three", fg = "black", bg = "blue")
# three.pack(side = LEFT, fill = Y)
# a = 3
# label_1 = Label(root, text = "state")
# label_2 = Label(root, text = "charge")
# label_3 = Label(root, text = str(a))
# label_4 = Label(root, text = str(a), fg ="red", bg = "white")
# # entry_1 = Entry(root)
# # entry_2 = Entry(root)
# labelfont = ('times', 100, 'bold')
# label_0 = Label(root, text = "House1")
# label_0.config(font = labelfont)
# label_0.grid(columnspan = 2)
# label_1.grid(row=1, sticky = E)
# label_2.grid(row=2, sticky = E)
# label_3.grid(row= 1, column =1)
# label_4.grid(row = 2, column =1 )
# entry_1.grid(row=0, column= 1)
# entry_2.grid(row=1, column=1)
# c = Checkbutton(root, text = "Keep me logged in")
# c.grid(columnspan = 2)
# import tkinter as tk

#
# def set_label():
#     currentTime = datetime.datetime.now()
#     label_3['text'] = currentTime
#     label_4['text'] = str(a+1)
#     root.after(2000, set_label)
# #
#
# # label = Label(root, text="placeholder")
# # label.pack()
#
# set_label()

menu = Menu(root)
root.config(menu = menu)

subMenu = Menu(menu)
menu.add_cascade(label = "scenario", menu = subMenu)
subMenu.add_command(label="scenario 1", command = doNothing)
subMenu.add_command(label="scenario 2", command = doNothing)
subMenu.add_separator()
subMenu.add_command(label="scenario 3", command = doNothing)
subMenu.add_command(label="scenario 4", command = doNothing)
subMenu.add_separator()
subMenu.add_command(label="quit", command= menu.quit)

root.mainloop()


