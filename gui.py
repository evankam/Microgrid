from tkinter import *
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import args as args

Largefont = ("Verdana", 12 )
labelfonthouse = ('times', 50, 'bold')
labelfontattributes = ('times', 20)
labelfontnumbers = ("times", 20, 'italic')
style.use("ggplot")

f = Figure (figsize = (5,5), dpi = 100)
a = f.add_subplot(111)


def animate(i):
    pullData = open("sample.Data.txt".read()) #grab list of data
    dataList = pullData.split('\n') #separate
    xlist = []
    ylist = []
    for eachline in dataList:
        if len(eachline)> 1:
            x,y = eachline.split(',')
            xlist.append(int(x))
            ylist.append(int(y))
    a.clear()
    a.plot(xlist, ylist)


class frame_maker(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        container.pack(side="top", fill = BOTH, expand = True)
        container.grid_columnconfigure(0, weight = 1)
        container.grid_rowconfigure(0, weight = 1)

        self.frames = {}

        for F in (Start_Page, Graphs):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame (Start_Page)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class Start_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Welcome!", font= labelfonthouse)
        label.pack()

        button1 = tk.Button(self, text = "Graphs",
                            command = lambda: controller.show_frame(Graphs))
        button1.pack()


class Graphs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label2 = tk.Label(self, text = "Graphs!!", font = labelfonthouse)
        label2.pack()
        button2 = tk.Button(self, text = "Back to List", command = lambda: controller.show_frame(Start_Page))
        button2.pack()

        # f = Figure (figsize = (5,5), dpi = 100)
        # a = f.add_subplot(111)
        # a.plot([1,2,3,4,5,6,7,8], [10,9,8,7,6,5,4,3])

        canvas = FigureCanvasTkAgg(f, self)
        # canvas.show()
        canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)

        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = True)



app = frame_maker()
ani = animation.FuncAnimation(f,animate, interval = 2000)
app.mainloop()




# root = Tk()
# list_frame = Frame(root, side = N)


# canvas = Canvas(root, width = 100, height = 500)
# canvas.grid(row = 8)
# blackline = canvas.create_line(0,0,100,0)
# redline = canvas.create_line(0, 500, 100, 500, fill = 'red')

# root.mainloop()
#
# def set_label():
#     label_16['text'] = house1.supply
#     label_17['text'] = house2.supply
#     label_18['text'] = house3.supply
#     label_19['text'] = house4.supply
#     label_20['text'] = str(round(house1.charge,2)) + "%"
#     label_21['text'] = str(round(house2.charge,2)) + "%"
#     label_22['text'] = str(round(house3.charge,2)) + "%"
#     label_23['text'] = str(round(house4.charge,2)) + "%"
#     label_24['text'] = str(round(house1.bankaccount,2)) + "$"
#     label_25['text'] = str(round(house2.bankaccount,2)) + "$"
#     label_26['text'] = str(round(house3.bankaccount,2)) + "$"
#     label_27['text'] = str(round(house4.bankaccount,2)) + "$"
#     root.after(2000, set_label)

# label_0 = tk.Label(self, text = "House1")
#         label_1 = tk.Label(self, text = "House2")
#         label_2 = tk.Label(self, text = "House3")
#         label_3 = tk.Label(self, text = "House4")
#
#         label_4 = tk.Label(self, text = "State:")
#         label_5 = tk.Label(self, text = "State:")
#         label_6 = tk.Label(self, text = "State:")
#         label_7 = tk.Label(self, text = "State:")
#
#         label_8 = tk.Label(self, text = "Charge:")
#         label_9 = tk.Label(self, text = "Charge:")
#         label_10 = tk.Label(self, text = "Charge:")
#         label_11 = tk.Label(self, text = "Charge:")
#
#         label_12 = tk.Label(self, text = "Bank Account:")
#         label_13 = tk.Label(self, text = "Bank Account:")
#         label_14 = tk.Label(self, text = "Bank Account:")
#         label_15 = tk.Label(self, text = "Bank Account:")
#
#         label_16 = tk.Label(self, text = "Initializing")
#         label_17 = tk.Label(self, text = "Initializing")
#         label_18 = tk.Label(self, text = "Initializing")
#         label_19 = tk.Label(self, text = "Initializing")
#
#         label_20 = tk.Label(self, text = "Initializing")
#         label_21 = tk.Label(self, text = "Initializing")
#         label_22 = tk.Label(self, text = "Initializing")
#         label_23 = tk.Label(self, text = "Initializing")
#
#         label_24 = tk.Label(self, text = "Initializing")
#         label_25 = tk.Label(self, text = "Initializing")
#         label_26 = tk.Label(self, text = "Initializing")
#         label_27 = tk.Label(self, text = "Initializing")
#
#         label_0.config(font=labelfonthouse)
#         label_1.config(font=labelfonthouse)
#         label_2.config(font=labelfonthouse)
#         label_3.config(font=labelfonthouse)
#
#         label_4.config(font=labelfontattributes)
#         label_5.config(font=labelfontattributes)
#         label_6.config(font=labelfontattributes)
#         label_7.config(font=labelfontattributes)
#         label_8.config(font=labelfontattributes)
#         label_9.config(font=labelfontattributes)
#         label_10.config(font=labelfontattributes)
#         label_11.config(font=labelfontattributes)
#         label_12.config(font=labelfontattributes)
#         label_13.config(font=labelfontattributes)
#         label_14.config(font=labelfontattributes)
#         label_15.config(font=labelfontattributes)
#
#         label_16.config(font=labelfontnumbers)
#         label_17.config(font=labelfontnumbers)
#         label_18.config(font=labelfontnumbers)
#         label_19.config(font=labelfontnumbers)
#         label_20.config(font=labelfontnumbers)
#         label_21.config(font=labelfontnumbers)
#         label_22.config(font=labelfontnumbers)
#         label_23.config(font=labelfontnumbers)
#         label_24.config(font=labelfontnumbers)
#         label_25.config(font=labelfontnumbers)
#         label_26.config(font=labelfontnumbers)
#         label_27.config(font=labelfontnumbers)
#
#         label_0.grid(row= 0, column = 0, columnspan = 3)
#         label_1.grid(row = 0, column = 3, columnspan = 3)
#         label_2.grid(row = 0, column = 6, columnspan = 3)
#         label_3.grid(row = 0, column = 9, columnspan = 3)
#
#         label_4.grid(row = 2, column = 0, sticky = E)
#         label_5.grid(row = 2, column = 3, sticky = E)
#         label_6.grid(row = 2, column = 6, sticky = E)
#         label_7.grid(row = 2, column = 9, sticky = E)
#
#         label_8.grid(row = 4, column = 0, sticky = E)
#         label_9.grid(row = 4, column = 3, sticky = E)
#         label_10.grid(row = 4, column = 6, sticky = E)
#         label_11.grid(row = 4, column = 9, sticky = E)
#
#         label_12.grid(row = 6, column = 0, sticky = E)
#         label_13.grid(row = 6, column = 3, sticky = E)
#         label_14.grid(row = 6, column = 6, sticky = E)
#         label_15.grid(row = 6, column = 9, sticky = E)
#
#         label_16.grid(row = 2, column = 1)
#         label_17.grid(row = 2, column = 4)
#         label_18.grid(row = 2, column = 7)
#         label_19.grid(row = 2, column = 10)
#
#         label_20.grid(row = 4, column = 1)
#         label_21.grid(row = 4, column = 4)
#         label_22.grid(row = 4, column = 7)
#         label_23.grid(row = 4, column = 10)
#
#         label_24.grid(row = 6, column = 1)
#         label_25.grid(row = 6, column = 4)
#         label_26.grid(row = 6, column = 7)
#         label_27.grid(row = 6, column = 10)
