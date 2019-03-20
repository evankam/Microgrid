from pyfirmata import Arduino,util
import time
import random
from decimal import Decimal
# board = Arduino('COM5')
# board_bis = Arduino('COM8')

# board = Arduino('COM4')

from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style



Largefont = ("Verdana", 12 )
labelfonthouse = ('times', 50, 'bold')
labelfontattributes = ('times', 20)
labelfontnumbers = ("times", 20, 'italic')
style.use("ggplot")

Largefont = ("Verdana", 12 )
labelfonthouse = ('times', 50, 'bold')
labelfontattributes = ('times', 20)
labelfontnumbers = ("times", 20, 'italic')
style.use("ggplot")

root = Tk()
root2=Tk()

label_0 = Label(root2, text = "House1")
label_1 = Label(root2, text = "House2")
label_2 = Label(root2, text = "House3")
label_3 = Label(root2, text = "House4")

label_4 = Label(root2, text = "State:")
label_5 = Label(root2, text = "State:")
label_6 = Label(root2, text = "State:")
label_7 = Label(root2, text = "State:")

label_8 = Label(root2, text = "Charge:")
label_9 = Label(root2, text = "Charge:")
label_10 = Label(root2, text = "Charge:")
label_11 = Label(root2, text = "Charge:")

label_12 = Label(root2, text = "Bank Account:")
label_13 = Label(root2, text = "Bank Account:")
label_14 = Label(root2, text = "Bank Account:")
label_15 = Label(root2, text = "Bank Account:")

label_16 = Label(root2, text = "Initializing")
label_17 = Label(root2, text = "Initializing")
label_18 = Label(root2, text = "Initializing")
label_19 = Label(root2, text = "Initializing")

label_20 = Label(root2, text = "Initializing")
label_21 = Label(root2, text = "Initializing")
label_22 = Label(root2, text = "Initializing")
label_23 = Label(root2, text = "Initializing")

label_24 = Label(root2, text = "Initializing")
label_25 = Label(root2, text = "Initializing")
label_26 = Label(root2, text = "Initializing")
label_27 = Label(root2, text = "Initializing")

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

label_0.grid(row= 0, column = 0, columnspan = 3)
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


f = Figure (figsize = (5,5), dpi = 100)
a = f.add_subplot(111)
b = f.add_subplot(111)
c = f.add_subplot(111)
d = f.add_subplot(111)
canvas = FigureCanvasTkAgg(f)
canvas.get_tk_widget().pack(fill = BOTH, expand = True)


def animate(i):
    pullData = open("sampleData.txt","r").read()
    pullData2 = open("sampleData2.txt","r").read()
    pullData3 = open("sampleData3.txt","r").read()
    pullData4 = open("sampleData4.txt","r").read()#grab list of data
    dataList = pullData.split('\n')
    dataList2 = pullData2.split('\n')
    dataList3 = pullData3.split('\n')
    dataList4 = pullData4.split('\n')#separate
    xlist = []
    ylist = []
    x2list = []
    y2list = []
    x3list = []
    y3list = []
    x4list = []
    y4list = []
    for eachline in dataList:
        if len(eachline)> 1:
            x,y = eachline.split(',')
            xlist.append(int(x))
            ylist.append(int(y))
    for eachline in dataList2:
        if len(eachline)>1:
            x,y = eachline.split(',')
            x2list.append(int(x))
            y2list.append(int(y))
    for eachline in dataList3:
        if len(eachline)> 1:
            x,y = eachline.split(',')
            x3list.append(int(x))
            y3list.append(int(y))
    for eachline in dataList4:
        if len(eachline)>1:
            x,y = eachline.split(',')
            x4list.append(int(x))
            y4list.append(int(y))
    a.clear()
    b.clear()
    c.clear()
    d.clear()
    a.plot(xlist, ylist, marker = 'x', markerfacecolor = 'red', color = 'red')
    b.plot(x2list,y2list, marker = 'x', markerfacecolor = 'blue', color = 'blue')
    c.plot(x3list, y3list, marker = 'x', markerfacecolor = 'green', color = 'green')
    d.plot(x4list,y4list, marker = 'x', markerfacecolor = 'yellow', color = 'yellow')

ani = animation.FuncAnimation(f,animate)
open('sampleData.txt', 'w').close()
open('sampleData2.txt', 'w').close()
open('sampleData3.txt', 'w').close()
open('sampleData4.txt', 'w').close()

def set_label():
    label_16['text'] = house1.supply
    label_17['text'] = house2.supply
    label_18['text'] = house3.supply
    label_19['text'] = house4.supply
    label_20['text'] = str(round(house1.charge,2)) + "%"
    label_21['text'] = str(round(house2.charge,2)) + "%"
    label_22['text'] = str(round(house3.charge,2)) + "%"
    label_23['text'] = str(round(house4.charge,2)) + "%"
    label_24['text'] = str(round(house1.bankaccount,2)) + "$"
    label_25['text'] = str(round(house2.bankaccount,2)) + "$"
    label_26['text'] = str(round(house3.bankaccount,2)) + "$"
    label_27['text'] = str(round(house4.bankaccount,2)) + "$"
    root2.after(2000, set_label)






class House:
    def _init_(self):
        self.supply = 'main Generator'
        self.price = 0
        self.state = 'seller'
        self.firstrelay = 0
        self.secondrelay = 0
        self.charge= 100
        self.bankaccount = 5000
        self.list_events = []
        self.neighbour = []
        self.number = 0


    def connect_to_solar(self):
            first_relay_to_change = self.firstrelay+1
            second_relay_to_change = self.secondrelay+1
            board.digital[first_relay_to_change].write(0)   #turns the first relay on
            board.digital[second_relay_to_change].write(0)  #turns the second relay on
            self.supply = 'own battery'
            if self.number ==1:
                board_bis.digital[2].write(0)
                board_bis.digital[3].write(0)
                board_bis.digital[4].write(1)
            if self.number ==2:
                board_bis.digital[5].write(0)
                board_bis.digital[6].write(0)
                board_bis.digital[7].write(1)
            if self.number ==3:
                board_bis.digital[8].write(0)
                board_bis.digital[9].write(0)
                board_bis.digital[10].write(1) 
            if self.number ==4:
                board_bis.digital[11].write(0)
                board_bis.digital[12].write(0)
                board_bis.digital[13].write(1)  
                

    def connect_to_main(self):
            first_relay_to_change = self.firstrelay+1
            second_relay_to_change = self.secondrelay+1
            board.digital[first_relay_to_change].write(1)   #turns the first relay off
            board.digital[second_relay_to_change].write(0)  #turns the second relay on
            self.supply = 'main generator'
            if self.number ==1:
                board_bis.digital[2].write(0)
                board_bis.digital[3].write(1)
                board_bis.digital[4].write(0)
            if self.number ==2:
                board_bis.digital[5].write(0)
                board_bis.digital[6].write(1)
                board_bis.digital[7].write(0)
            if self.number ==3:
                board_bis.digital[8].write(0)
                board_bis.digital[9].write(1)
                board_bis.digital[10].write(0) 
            if self.number ==4:
                board_bis.digital[11].write(0)
                board_bis.digital[12].write(1)
                board_bis.digital[13].write(0) 

    def connect_to_other_house(self):
            first_relay_to_change = self.firstrelay+1
            second_relay_to_change = self.secondrelay+1
            board.digital[first_relay_to_change].write(0)   #turns the first relay on
            board.digital[second_relay_to_change].write(1)  #turns the second relay off
            self.supply = 'exchange'
            if self.number ==1:
                board_bis.digital[2].write(1)
                board_bis.digital[3].write(0)
                board_bis.digital[4].write(0)
            if self.number ==2:
                board_bis.digital[5].write(1)
                board_bis.digital[6].write(0)
                board_bis.digital[7].write(0)
            if self.number ==3:
                board_bis.digital[8].write(1)
                board_bis.digital[9].write(0)
                board_bis.digital[10].write(0) 
            if self.number ==4:
                board_bis.digital[11].write(1)
                board_bis.digital[12].write(0)
                board_bis.digital[13].write(0) 

    def add_event(self, event):
        self.list_events.append(event)

    def compute_price(self):
        charge = self.charge
        if charge >= 50:
            self.price = (-2/25)*charge+9
        else:
            self.price = (15+10/9) -(2/9)*charge

def solar(time):
    y = (-1/144)*(time**3)*(1/3)+ (65/12)*(time**2)*(0.5)
    y = y/15210
    return(y)

main_generator_price = 3

class Event:
    def _init_(self):
        self.time = 0   #time in minutes
        self.house = house
        self.load_usage = 4    #usage of load in percentages of battery

    def define_event_random(self, house):
        self.time = random.randint(0, 1080)
        self.house = house
        self.load_usage = random.randint(1,50)

class Dispatcher:

    def _init_(self,list_house):
        self.event_list = []
        self.current_time = 0

    def add_events_from_lists(self, list_event):
        for i in range (0,len(list_event)):
            self.event_list.append(list_event[i])
        self.event_list.sort(key=lambda x: x.time, reverse=False)


    def solar_event(self,event, list_house):
        current_time = self.current_time
        for i in range (0,len(list_house)):
            list_house[i].charge += solar(event.time) - solar(self.current_time)
            if list_house[i].charge > 100:
                list_house[i].charge = 100
        self.current_time = event.time

    def run_dispatcher(self,list_house):
        # house1.connect_to_solar()
        # house2.connect_to_solar()
        # house3.connect_to_solar()
        # house4.connect_to_solar()
        for i in range (0,len(self.event_list)):
            time.sleep(2)
            trueindex = str(i+1)
            print("event" + trueindex)
            self.solar_event(self.event_list[i], list_house)
            house_event = self.event_list[i].house
            houseevent= str(house_event)
            list_houses = house_event.neighbour
            time1 = self.event_list[i].time
            if self.event_list[i].load_usage < house_event.charge:               #we use the battery if we have enough power
                house_event.charge += - self.event_list[i].load_usage
                # house_event.connect_to_solar()
                # print(house_event.charge)
                # print(self.event_list[i].load_usage)
                print(houseevent + " use solar")
                house_event.supply = "own solar"
            else:
                list_house_seller = []
                for j in range(0, len(list_houses)):
                    if list_houses[j].charge>self.event_list[i].load_usage:
                                                                 #if not we compute a list of houses having enough load and their prices
                        list_house_seller.append(list_houses[j])
                if len(list_house_seller) ==0:
                    if house_event.bankaccount> main_generator_price*self.event_list[i].load_usage:
                        house_event.bankaccount += - main_generator_price*self.event_list[i].load_usage#we use the main if its cheaper
                        # house_event.connect_to_main()
                        print(houseevent + " use main_generator 1")
                        house_event.supply = "main generator"
                    else:
                        print('no money')
                else:
                    for k in range(0, len(list_house_seller)):
                        list_house_seller[k].compute_price()
                    list_house_seller.sort(key=lambda x: x.price)                        #we sort them by price
                    if list_house_seller[0].price > main_generator_price:
                        if house_event.bankaccount> main_generator_price*self.event_list[i].load_usage:
                            house_event.bankaccount += - main_generator_price*self.event_list[i].load_usage    #we use the main if its cheaper
                            # house_event.connect_to_main()
                            print(houseevent + " use main_generator 2")
                            house_event.supply = "main generator"
                        else:
                            print('no money')
                    else:
                        if house_event.bankaccount> list_house_seller[0].price*self.event_list[i].load_usage:
                            house_event.bankaccount += - list_house_seller[0].price*self.event_list[i].load_usage
                                                                                               #otherwise we connect 2 houses
                            list_house_seller[0].bankaccount += list_house_seller[0].price*self.event_list[i].load_usage

                            list_house_seller[0].charge += - self.event_list[i].load_usage
                            # house_event.connect_to_other_house()
                            # list_house_seller[0].connect_to_other_house()
                            sellerhouse = str(list_house_seller[0])
                            print(houseevent + " buy from " + sellerhouse)
                            house_event.supply = "buying"
                            list_house_seller[0].supply = "selling"
                        else:
                            print('no money')
            for a in range(0, len(list_house)):
                index = str(a+1)
                charge = str(list_house[a].charge)
                bankacc = str(list_house[a].bankaccount)
                print("house" + index + " charge = " + charge )
                print("house" + index + " bank acc = " + bankacc)
            print(self.event_list[i].load_usage)
            pullData1 = open("sampleData.txt","a+")
            pullData1.write(str(time1)+ "," + str(int(house1.charge)) +"\n")
            pullData1.close()
            pullData2 = open("sampleData2.txt","a+")
            pullData2.write(str(time1)+ "," + str(int(house2.charge)) +"\n")
            pullData2.close()
            pullData3 = open("sampleData3.txt","a+")
            pullData3.write(str(time1)+ "," + str(int(house3.charge)) +"\n")
            pullData3.close()
            pullData4 = open("sampleData4.txt","a+")
            pullData4.write(str(time1)+ "," + str(int(house4.charge)) +"\n")
            pullData4.close()
            loop_active = True
            while loop_active:
               root2.update()
               set_label()
               if i == len(self.event_list):
                   root.quit()
                   root2.quit()
                   loop_active = False
               else:
                   break

house1 = House()
house1.supply = 'own battery'
house1.price = 0
house1.state = 'seller'
house1.firstrelay = 7
house1.secondrelay = 8
house1.charge = 100
house1.bankaccount = 500
house1.list_events = []
house1.neighbour= []
house1.number = 1


house2 = House()
house2.supply = 'own battery'
house2.price = 0
house2.state = 'seller'
house2.firstrelay = 5
house2.secondrelay = 6
house2.charge = 100
house2.bankaccount = 500
house2.list_events = []
house2.neighbour= []
house2.number = 2

house3 = House()
house3.supply = 'own battery'
house3.price = 50
house3.state = 'buyer'
house3.firstrelay = 3
house3.secondrelay = 4
house3.charge = 15
house3.bankaccount = 500
house3.list_events = []
house3.neighbour = []
house3.number = 3

house4 = House()
house4.supply = 'own battery'
house4.price = 100
house4.state = 'buyer'
house4.firstrelay = 1
house4.secondrelay = 2
house4.charge = 10
house4.bankaccount = 500
house4.list_events = []
house4.neighbour = []
house4.number = 0

list_house = [house1,house2,house3,house4]
for i in range (0,len(list_house)):
    houses =[house1,house2,house3,house4]
    del houses[i]
    list_house[i].neighbour = houses

event1 = Event()
event1.time = 195
event1.load_usage = 16
event1.house = house1

event2 = Event()
event2.time = 453
event2.load_usage = 26
event2.house = house1

event3 = Event()
event3.time = 490
event3.load_usage = 19
event3.house = house1

event4 = Event()
event4.time = 3
event4.load_usage = 1
event4.house= house1

event5 = Event()
event5.time = 399
event5.load_usage = 13
event5.house = house1

event6 = Event()
event6.time = 267
event6.load_usage = 5
event6.house = house1

event7 = Event()
event7.time = 264
event7.load_usage = 17
event7.house= house2

event8 = Event()
event8.time = 419
event8.load_usage = 25
event8.house= house2

event9 = Event()
event9.time = 735
event9.load_usage = 15
event9.house= house2

event10= Event()
event10.time = 176
event10.load_usage = 21
event10.house= house2

event11 = Event()
event11.time = 291
event11.load_usage = 15
event11.house= house2

event12 = Event()
event12.time = 83
event12.load_usage = 27
event12.house= house2

event13 = Event()
event13.time = 435
event13.load_usage = 23
event13.house= house2

event14 = Event()
event14.time = 186
event14.load_usage = 4
event14.house= house2

event15 = Event()
event15.time = 232
event15.load_usage = 12
event15.house= house3

event16 = Event()
event16.time = 369
event16.load_usage = 13
event16.house= house3

event17 = Event()
event17.time = 770
event17.load_usage = 26
event17.house= house3

event18 = Event()
event18.time = 723
event18.load_usage = 14
event18.house= house3

event19 = Event()
event19.time = 212
event19.load_usage = 24
event19.house= house3

event20 = Event()
event20.time = 161
event20.load_usage = 14
event20.house= house3

event21 = Event()
event21.time = 719
event21.load_usage = 25
event21.house= house4

event22 = Event()
event22.time = 661
event22.load_usage = 20
event22.house= house4

event23 = Event()
event23.time = 409
event23.load_usage = 12
event23.house= house4

event24 = Event()
event24.time = 28
event24.load_usage = 15
event24.house= house4

event25 = Event()
event25.time = 156
event25.load_usage = 7
event25.house= house4


house1.add_event(event1)
house1.add_event(event2)
house1.add_event(event3)
house1.add_event(event4)
house1.add_event(event5)
house1.add_event(event6)


house2.add_event(event7)
house2.add_event(event8)
house2.add_event(event9)
house2.add_event(event10)
house2.add_event(event11)
house2.add_event(event12)
house2.add_event(event13)
house2.add_event(event14)


house3.add_event(event15)
house3.add_event(event16)
house3.add_event(event17)
house3.add_event(event18)
house3.add_event(event19)
house3.add_event(event20)

house4.add_event(event21)
house4.add_event(event22)
house4.add_event(event23)
house4.add_event(event24)
house4.add_event(event25)


dispatcher1 = Dispatcher()
dispatcher1.event_list = []
dispatcher1.current_time = 0

dispatcher1.add_events_from_lists(house1.list_events)
dispatcher1.add_events_from_lists(house2.list_events)
dispatcher1.add_events_from_lists(house3.list_events)
dispatcher1.add_events_from_lists(house4.list_events)

dispatcher1.run_dispatcher(list_house)
