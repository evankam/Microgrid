# from tkinter import *
# import matplotlib
# matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# from matplotlib.figure import Figure
# import matplotlib.animation as animation
# from matplotlib import style
# import houses
#
# Largefont = ("Verdana", 12 )
# labelfonthouse = ('times', 50, 'bold')
# labelfontattributes = ('times', 20)
# labelfontnumbers = ("times", 20, 'italic')
# style.use("ggplot")
#
# f = Figure (figsize = (4,4), dpi = 100)
# a = f.add_subplot(111)
# b = f.add_subplot(111)
# c = f.add_subplot(111)
# d = f.add_subplot(111)
# # a.plot([1,2,3,4,5,6,7,8], [10,9,8,7,6,5,4,3])
# canvas = FigureCanvasTkAgg(f)
# canvas.get_tk_widget().grid(row = 20)
#
# def animate(i):
#     pullData = open("sampleData.txt","r").read()
#     pullData2 = open("sampleData2.txt","r").read()
#     pullData3 = open("sampleData3.txt","r").read()
#     pullData4 = open("sampleData4.txt","r").read()#grab list of data
#     dataList = pullData.split('\n')
#     dataList2 = pullData2.split('\n')
#     dataList3 = pullData3.split('\n')
#     dataList4 = pullData4.split('\n')#separate
#     xlist = []
#     ylist = []
#     x2list = []
#     y2list = []
#     x3list = []
#     y3list = []
#     x4list = []
#     y4list = []
#     for eachline in dataList:
#         if len(eachline)> 1:
#             x,y = eachline.split(',')
#             xlist.append(int(x))
#             ylist.append(int(y))
#     for eachline in dataList2:
#         if len(eachline)>1:
#             x,y = eachline.split(',')
#             x2list.append(int(x))
#             y2list.append(int(y))
#     for eachline in dataList3:
#         if len(eachline)> 1:
#             x,y = eachline.split(',')
#             x3list.append(int(x))
#             y3list.append(int(y))
#     for eachline in dataList4:
#         if len(eachline)>1:
#             x,y = eachline.split(',')
#             x4list.append(int(x))
#             y4list.append(int(y))
#     a.clear()
#     a.plot(xlist, ylist, marker = 'x', markerfacecolor = 'red', color = 'red')
#     b.clear()
#     b.plot(x2list,y2list, marker = 'x', markerfacecolor = 'blue', color = 'blue')
#     c.clear()
#     c.plot(x3list, y3list, marker = 'x', markerfacecolor = 'green', color = 'green')
#     d.clear()
#     d.plot(x4list,y4list, marker = 'x', markerfacecolor = 'yellow', color = 'yellow')
#
# ani = animation.FuncAnimation(f,animate)
# open('sampleData.txt', 'w').close()
# open('sampleData2.txt', 'w').close()
# open('sampleData3.txt', 'w').close()
# open('sampleData4.txt', 'w').close()
#
# root = Tk()
# root2= Tk()
#
# def doSummer():
#     root.destroy()
#     root2.destroy()
#     season = 1
# def doFall():
#     root.destroy()
#     root2.destroy()
#     season = 2
# def doWinter():
#     root.destroy()
#     root2.destroy()
#     season = 3
# def doSpring():
#     root.destroy()
#     root2.destroy()
#     season = 4
# def closeWindow():
#     root.destroy()
#     root2.destroy()
# menu = Menu(root2)
# root2.config(menu=menu)
# subMenu = Menu(menu)
# menu.add_cascade(label="File", menu = subMenu)
# subMenu.add_command(label = "Scenario 1 = Summer", command = doSummer)
# subMenu.add_command(label = "Scenario 2 = Fall", command = doFall)
# subMenu.add_command(label = "Scenario 3 = Winter", command = doWinter)
# subMenu.add_command(label = "Scenario 4 = Spring", command = doSpring)
# subMenu.add_separator()
# subMenu.add_command(label = "Exit", command = closeWindow)
#
# label_0 = Label(root2, text = "House1")
# label_1 = Label(root2, text = "House2")
# label_2 = Label(root2, text = "House3")
# label_3 = Label(root2, text = "House4")
#
# label_4 = Label(root2, text = "State:")
# label_5 = Label(root2, text = "State:")
# label_6 = Label(root2, text = "State:")
# label_7 = Label(root2, text = "State:")
#
# label_8 = Label(root2, text = "Charge:")
# label_9 = Label(root2, text = "Charge:")
# label_10 = Label(root2, text = "Charge:")
# label_11 = Label(root2, text = "Charge:")
#
# label_12 = Label(root2, text = "Bank Account:")
# label_13 = Label(root2, text = "Bank Account:")
# label_14 = Label(root2, text = "Bank Account:")
# label_15 = Label(root2, text = "Bank Account:")
#
# label_16 = Label(root2, text = "Initializing")
# label_17 = Label(root2, text = "Initializing")
# label_18 = Label(root2, text = "Initializing")
# label_19 = Label(root2, text = "Initializing")
#
# label_20 = Label(root2, text = "Initializing")
# label_21 = Label(root2, text = "Initializing")
# label_22 = Label(root2, text = "Initializing")
# label_23 = Label(root2, text = "Initializing")
#
# label_24 = Label(root2, text = "Initializing")
# label_25 = Label(root2, text = "Initializing")
# label_26 = Label(root2, text = "Initializing")
# label_27 = Label(root2, text = "Initializing")
#
# label_0.config(font=labelfonthouse)
# label_1.config(font=labelfonthouse)
# label_2.config(font=labelfonthouse)
# label_3.config(font=labelfonthouse)
#
# label_4.config(font=labelfontattributes)
# label_5.config(font=labelfontattributes)
# label_6.config(font=labelfontattributes)
# label_7.config(font=labelfontattributes)
# label_8.config(font=labelfontattributes)
# label_9.config(font=labelfontattributes)
# label_10.config(font=labelfontattributes)
# label_11.config(font=labelfontattributes)
# label_12.config(font=labelfontattributes)
# label_13.config(font=labelfontattributes)
# label_14.config(font=labelfontattributes)
# label_15.config(font=labelfontattributes)
#
# label_16.config(font=labelfontnumbers)
# label_17.config(font=labelfontnumbers)
# label_18.config(font=labelfontnumbers)
# label_19.config(font=labelfontnumbers)
# label_20.config(font=labelfontnumbers)
# label_21.config(font=labelfontnumbers)
# label_22.config(font=labelfontnumbers)
# label_23.config(font=labelfontnumbers)
# label_24.config(font=labelfontnumbers)
# label_25.config(font=labelfontnumbers)
# label_26.config(font=labelfontnumbers)
# label_27.config(font=labelfontnumbers)
#
# label_0.grid(row= 0, column = 0, columnspan = 3)
# label_1.grid(row = 0, column = 3, columnspan = 3)
# label_2.grid(row = 0, column = 6, columnspan = 3)
# label_3.grid(row = 0, column = 9, columnspan = 3)
#
# label_4.grid(row = 2, column = 0, sticky = E)
# label_5.grid(row = 2, column = 3, sticky = E)
# label_6.grid(row = 2, column = 6, sticky = E)
# label_7.grid(row = 2, column = 9, sticky = E)
#
# label_8.grid(row = 4, column = 0, sticky = E)
# label_9.grid(row = 4, column = 3, sticky = E)
# label_10.grid(row = 4, column = 6, sticky = E)
# label_11.grid(row = 4, column = 9, sticky = E)
#
# label_12.grid(row = 6, column = 0, sticky = E)
# label_13.grid(row = 6, column = 3, sticky = E)
# label_14.grid(row = 6, column = 6, sticky = E)
# label_15.grid(row = 6, column = 9, sticky = E)
#
# label_16.grid(row = 2, column = 1)
# label_17.grid(row = 2, column = 4)
# label_18.grid(row = 2, column = 7)
# label_19.grid(row = 2, column = 10)
#
# label_20.grid(row = 4, column = 1)
# label_21.grid(row = 4, column = 4)
# label_22.grid(row = 4, column = 7)
# label_23.grid(row = 4, column = 10)
#
# label_24.grid(row = 6, column = 1)
# label_25.grid(row = 6, column = 4)
# label_26.grid(row = 6, column = 7)
# label_27.grid(row = 6, column = 10)
#
# def set_label():
#     label_16['text'] = houses.house1.supply
#     label_17['text'] = houses.house2.supply
#     label_18['text'] = houses.house3.supply
#     label_19['text'] = houses.house4.supply
#     label_20['text'] = str(round(houses.house1.charge,2)) + "%"
#     label_21['text'] = str(round(houses.house2.charge,2)) + "%"
#     label_22['text'] = str(round(houses.house3.charge,2)) + "%"
#     label_23['text'] = str(round(houses.house4.charge,2)) + "%"
#     label_24['text'] = str(round(houses.house1.bankaccount,2)) + "$"
#     label_25['text'] = str(round(houses.house2.bankaccount,2)) + "$"
#     label_26['text'] = str(round(houses.house3.bankaccount,2)) + "$"
#     label_27['text'] = str(round(houses.house4.bankaccount,2)) + "$"
#     root2.after(1500, set_label)
#
#
#
#
# ani = animation.FuncAnimation(f,animate)
# # root.mainloop()
# # root2.mainloop()

