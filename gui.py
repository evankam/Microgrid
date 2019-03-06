from tkinter import *
import time
import datetime


root = Tk()
label_0 = Label(root, text = "House1")
label_1 = Label(root, text = "House2")
label_2 = Label(root, text = "House3")
label_3 = Label(root, text = "House4")

label_4 = Label(root, text = "State:")
label_5 = Label(root, text = "State:")
label_6 = Label(root, text = "State:")
label_7 = Label(root, text = "State:")

label_8 = Label(root, text = "Charge:")
label_9 = Label(root, text = "Charge:")
label_10 = Label(root, text = "Charge:")
label_11 = Label(root, text = "Charge:")

label_12 = Label(root, text = "Bank Account:")
label_13 = Label(root, text = "Bank Account:")
label_14 = Label(root, text = "Bank Account:")
label_15 = Label(root, text = "Bank Account:")

label_16 = Label(root, text = "Initializing")
label_17 = Label(root, text = "Initializing")
label_18 = Label(root, text = "Initializing")
label_19 = Label(root, text = "Initializing")

label_20 = Label(root, text = "Initializing")
label_21 = Label(root, text = "Initializing")
label_22 = Label(root, text = "Initializing")
label_23 = Label(root, text = "Initializing")

label_24 = Label(root, text = "Initializing")
label_25 = Label(root, text = "Initializing")
label_26 = Label(root, text = "Initializing")
label_27 = Label(root, text = "Initializing")


labelfonthouse = ('times', 40, 'bold')
labelfontattributes = ('times', 20)
labelfontnumbers = ("times", 20, 'italic')

label_0.config(font=labelfonthouse)
label_1.config(font=labelfonthouse)
label_2.config(font=labelfonthouse)
label_3.config(font=labelfonthouse)

label_4.config(font=labelfontattributes)
label_5.config(font=labelfontattributes)
label_6.config(font=labelfontattributes)
label_7.config(font=labelfontattributes)
label_8.config(font=labelfontattributes)
label_9.config(font=labelfontattributes)
label_10.config(font=labelfontattributes)
label_11.config(font=labelfontattributes)
label_12.config(font=labelfontattributes)
label_13.config(font=labelfontattributes)
label_14.config(font=labelfontattributes)
label_15.config(font=labelfontattributes)

label_16.config(font=labelfontnumbers)
label_17.config(font=labelfontnumbers)
label_18.config(font=labelfontnumbers)
label_19.config(font=labelfontnumbers)
label_20.config(font=labelfontnumbers)
label_21.config(font=labelfontnumbers)
label_22.config(font=labelfontnumbers)
label_23.config(font=labelfontnumbers)
label_24.config(font=labelfontnumbers)
label_25.config(font=labelfontnumbers)
label_26.config(font=labelfontnumbers)
label_27.config(font=labelfontnumbers)

label_0.grid(columnspan = 3)
label_1.grid(row = 0, column = 3, columnspan = 3)
label_2.grid(row = 0, column = 6, columnspan = 3)
label_3.grid(row = 0, column = 9, columnspan = 3)

label_4.grid(row = 2, column = 0, sticky = E)
label_5.grid(row = 2, column = 3, sticky = E)
label_6.grid(row = 2, column = 6, sticky = E)
label_7.grid(row = 2, column = 9, sticky = E)

label_8.grid(row = 4, column = 0, sticky = E)
label_9.grid(row = 4, column = 3, sticky = E)
label_10.grid(row = 4, column = 6, sticky = E)
label_11.grid(row = 4, column = 9, sticky = E)

label_12.grid(row = 6, column = 0, sticky = E)
label_13.grid(row = 6, column = 3, sticky = E)
label_14.grid(row = 6, column = 6, sticky = E)
label_15.grid(row = 6, column = 9, sticky = E)

label_16.grid(row = 2, column = 1)
label_17.grid(row = 2, column = 4)
label_18.grid(row = 2, column = 7)
label_19.grid(row = 2, column = 10)

label_20.grid(row = 4, column = 1)
label_21.grid(row = 4, column = 4)
label_22.grid(row = 4, column = 7)
label_23.grid(row = 4, column = 10)

label_24.grid(row = 6, column = 1)
label_25.grid(row = 6, column = 4)
label_26.grid(row = 6, column = 7)
label_27.grid(row = 6, column = 10)

root.mainloop()

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


