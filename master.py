from tkinter import messagebox, simpledialog

from pyfirmata import Arduino,util
import time
import random
from tkinter import *
from decimal import Decimal
import houses
import gui2
import events
import Dispatcher
import otherfunctions
from tkinter import *
import matplotlib


matplotlib.use("TkAgg")
import tkinter.simpledialog
import tkinter.messagebox

root3= Tk()
w = Label(root3, text="Test")
w.pack()
messagebox.showinfo("Welcome to the Microgrid Program", "Please click the OK button")

S = simpledialog.askstring("Choose a Season", "What's the season would you like to see in the demo? (Summer, Fall, Winter, Spring)")

output = "Your season is, {}".format(S)
root3.destroy()


def doSummer():
    messagebox.showinfo("Warning!", "Are you sure you want to change to Summer?")
    S = simpledialog.askstring("Please answer one of the following", "Yes/No")
    if S == "Yes":
        gui2.label_29['text'] = "Summer"
        season =1
        dispatcher1 = Dispatcher.Dispatcher()
        dispatcher1.event_list = []
        dispatcher1.current_time = 0

        dispatcher1.add_events_from_lists(houses.house1.list_events)
        dispatcher1.add_events_from_lists(houses.house2.list_events)
        dispatcher1.add_events_from_lists(houses.house3.list_events)
        dispatcher1.add_events_from_lists(houses.house4.list_events)

        dispatcher1.run_dispatcher(houses.list_house,season)
    else:
        gui2.root.destroy()
        gui2.root2.destroy()

def doFall():
    messagebox.showinfo("Warning!", "Are you sure you want to change to Fall?")
    S = simpledialog.askstring("Please answer one of the following", "Yes/No")
    if S == "Yes":
        gui2.label_29['text'] = "Fall"
        season =2
        dispatcher1 = Dispatcher.Dispatcher()
        dispatcher1.event_list = []
        dispatcher1.current_time = 0

        dispatcher1.add_events_from_lists(houses.house1.list_events)
        dispatcher1.add_events_from_lists(houses.house2.list_events)
        dispatcher1.add_events_from_lists(houses.house3.list_events)
        dispatcher1.add_events_from_lists(houses.house4.list_events)

        dispatcher1.run_dispatcher(houses.list_house,season)
    else:
        gui2.root.destroy()
        gui2.root2.destroy()

def doWinter():
    messagebox.showinfo("Warning!", "Are you sure you want to change to Winter?")
    S = simpledialog.askstring("Please answer one of the following", "Yes/No")
    if S == "Yes":
        gui2.label_29['text'] = "Winter"
        season =3
        dispatcher1 = Dispatcher.Dispatcher()
        dispatcher1.event_list = []
        dispatcher1.current_time = 0

        dispatcher1.add_events_from_lists(houses.house1.list_events)
        dispatcher1.add_events_from_lists(houses.house2.list_events)
        dispatcher1.add_events_from_lists(houses.house3.list_events)
        dispatcher1.add_events_from_lists(houses.house4.list_events)

        dispatcher1.run_dispatcher(houses.list_house,season)
    else:
        gui2.root.destroy()
        gui2.root2.destroy()
def doSpring():
    messagebox.showinfo("Warning!", "Are you sure you want to change to Spring?")
    S = simpledialog.askstring("Please answer one of the following", "Yes/No")
    if S == "Yes":
        gui2.label_29['text'] = "Spring"
        season =4
        dispatcher1 = Dispatcher.Dispatcher()
        dispatcher1.event_list = []
        dispatcher1.current_time = 0

        dispatcher1.add_events_from_lists(houses.house1.list_events)
        dispatcher1.add_events_from_lists(houses.house2.list_events)
        dispatcher1.add_events_from_lists(houses.house3.list_events)
        dispatcher1.add_events_from_lists(houses.house4.list_events)

        dispatcher1.run_dispatcher(houses.list_house,season)
    else:
        gui2.root.destroy()
        gui2.root2.destroy()
def closeWindow():
    gui2.root.destroy()
    gui2.root2.destroy()

if S == "Summer":
    season = 1
if S == "Fall":
    season = 2
if S == "Winter":
    season = 3
if S == "Spring":
    season = 4

menu = Menu(gui2.root2)
gui2.root2.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="File", menu = subMenu)
subMenu.add_command(label = "Scenario 1 = Summer", command = doSummer)
subMenu.add_command(label = "Scenario 2 = Fall", command = doFall)
subMenu.add_command(label = "Scenario 3 = Winter", command = doWinter)
subMenu.add_command(label = "Scenario 4 = Spring", command = doSpring)
subMenu.add_separator()
subMenu.add_command(label = "Exit", command = closeWindow)

dispatcher1 = Dispatcher.Dispatcher()
dispatcher1.event_list = []
dispatcher1.current_time = 0

dispatcher1.add_events_from_lists(houses.house1.list_events)
dispatcher1.add_events_from_lists(houses.house2.list_events)
dispatcher1.add_events_from_lists(houses.house3.list_events)
dispatcher1.add_events_from_lists(houses.house4.list_events)

dispatcher1.run_dispatcher(houses.list_house,season)




