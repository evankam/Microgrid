from tkinter import messagebox, simpledialog


import houses
import gui2
import events
import Dispatcher
from tkinter import *
import matplotlib


matplotlib.use("TkAgg")
import tkinter.simpledialog
import tkinter.messagebox

S = "Summer"

def doSummer():
    messagebox.showinfo("Warning!", "Changing Season to Summer")

    gui2.label_29['text'] = "Summer"
    houses.house1.charge = 100
    houses.house2.charge = 100
    houses.house3.charge = 50
    houses.house4.charge = 10
    open('sampleData.txt', 'w').close()
    open('sampleData2.txt', 'w').close()
    open('sampleData3.txt', 'w').close()
    open('sampleData4.txt', 'w').close()
    gui2.a.cla()
    gui2.b.cla()
    gui2.c.cla()
    gui2.d.cla()
    season =1
    dispatcher1 = Dispatcher.Dispatcher()
    dispatcher1.event_list = []
    dispatcher1.current_time = 0

    dispatcher1.add_events_from_lists(houses.house1.list_events)
    dispatcher1.add_events_from_lists(houses.house2.list_events)
    dispatcher1.add_events_from_lists(houses.house3.list_events)
    dispatcher1.add_events_from_lists(houses.house4.list_events)

    dispatcher1.run_dispatcher(houses.list_house,season)

def doFall():
    messagebox.showinfo("Warning!", "Changing Season to Fall")

    gui2.label_29['text'] = "Fall"
    houses.house1.charge = 100
    houses.house2.charge = 100
    houses.house3.charge = 50
    houses.house4.charge = 10
    open('sampleData.txt', 'w').close()
    open('sampleData2.txt', 'w').close()
    open('sampleData3.txt', 'w').close()
    open('sampleData4.txt', 'w').close()
    gui2.a.cla()
    gui2.b.cla()
    gui2.c.cla()
    gui2.d.cla()
    season = 2
    dispatcher1 = Dispatcher.Dispatcher()
    dispatcher1.event_list = []
    dispatcher1.current_time = 0

    dispatcher1.add_events_from_lists(houses.house1.list_events)
    dispatcher1.add_events_from_lists(houses.house2.list_events)
    dispatcher1.add_events_from_lists(houses.house3.list_events)
    dispatcher1.add_events_from_lists(houses.house4.list_events)

    dispatcher1.run_dispatcher(houses.list_house,season)



def doWinter():
    messagebox.showinfo("Warning!", "Changing Season to Winter")

    gui2.label_29['text'] = "Winter"
    houses.house1.charge = 100
    houses.house2.charge = 100
    houses.house3.charge = 50
    houses.house4.charge = 10
    open('sampleData.txt', 'w').close()
    open('sampleData2.txt', 'w').close()
    open('sampleData3.txt', 'w').close()
    open('sampleData4.txt', 'w').close()
    gui2.a.cla()
    gui2.b.cla()
    gui2.c.cla()
    gui2.d.cla()
    season =3
    dispatcher1 = Dispatcher.Dispatcher()
    dispatcher1.event_list = []
    dispatcher1.current_time = 0

    dispatcher1.add_events_from_lists(houses.house1.list_events)
    dispatcher1.add_events_from_lists(houses.house2.list_events)
    dispatcher1.add_events_from_lists(houses.house3.list_events)
    dispatcher1.add_events_from_lists(houses.house4.list_events)

    dispatcher1.run_dispatcher(houses.list_house,season)



def doSpring():
    messagebox.showinfo("Warning!", "Changing Season to Spring")

    gui2.label_29['text'] = "Spring"
    houses.house1.charge = 100
    houses.house2.charge = 100
    houses.house3.charge = 50
    houses.house4.charge = 10
    open('sampleData.txt', 'w').close()
    open('sampleData2.txt', 'w').close()
    open('sampleData3.txt', 'w').close()
    open('sampleData4.txt', 'w').close()
    gui2.a.cla()
    gui2.b.cla()
    gui2.c.cla()
    gui2.d.cla()
    season =4
    dispatcher1 = Dispatcher.Dispatcher()
    dispatcher1.event_list = []
    dispatcher1.current_time = 0

    dispatcher1.add_events_from_lists(houses.house1.list_events)
    dispatcher1.add_events_from_lists(houses.house2.list_events)
    dispatcher1.add_events_from_lists(houses.house3.list_events)
    dispatcher1.add_events_from_lists(houses.house4.list_events)

    dispatcher1.run_dispatcher(houses.list_house,season)



def closeWindow():
    gui2.root.destroy()
    gui2.root2.destroy()

gui2.label_29['text'] = S

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




