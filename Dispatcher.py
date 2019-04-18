import time
import otherfunctions
import houses
import gui2
from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import houses



class Dispatcher:
    def _init_(self,list_house):
        self.event_list = []
        self.current_time = 0
    

    def add_events_from_lists(self, list_event):
        for i in range (0,len(list_event)):
            self.event_list.append(list_event[i])
        self.event_list.sort(key=lambda x: x.time, reverse=False)


    def solar_event(self,event, list_house,season):
        current_time = self.current_time
        for i in range (0,len(list_house)):
            list_house[i].charge += otherfunctions.solar(event.time,season) - otherfunctions.solar(self.current_time,season)
            if list_house[i].charge > 100:
                list_house[i].charge = 100
        self.current_time = event.time

    def run_dispatcher(self,list_house,season):
        houses.house1.connect_to_solar()
        houses.house2.connect_to_solar()
        houses.house3.connect_to_solar()
        houses.house4.connect_to_solar()
        for i in range (0,len(self.event_list)):

            time.sleep(2)
            if i>0 and house_event.supply == 'exchange' and list_house_seller[0].supply == 'exchange':
                house_event.connect_to_solar()
                list_house_seller[0].connect_to_solar()
            self.solar_event(self.event_list[i], list_house,season)
            time1 = self.event_list[i].time
            house_event = self.event_list[i].house
            houseevent= str(house_event)
            list_houses = house_event.neighbour
            time1 = self.event_list[i].time
            if self.event_list[i].load_usage < house_event.charge:               #we use the battery if we have enough power
                house_event.charge += - self.event_list[i].load_usage
                house_event.connect_to_solar()
            else:
                list_house_seller = []
                for j in range(0, len(list_houses)):
                    if list_houses[j].charge>self.event_list[i].load_usage:
                                                                 #if not we compute a list of houses having enough load and their prices
                        list_house_seller.append(list_houses[j])
                if len(list_house_seller) ==0:
                    if house_event.bankaccount> otherfunctions.main_generator_price*self.event_list[i].load_usage:
                        house_event.bankaccount += - otherfunctions.main_generator_price*self.event_list[i].load_usage#we use the main if its cheaper
                        house_event.connect_to_main()
                        # print(houseevent + " use main_generator 1")
                    else:
                        print('no money')
                else:
                    for k in range(0, len(list_house_seller)):
                        list_house_seller[k].compute_price()
                    list_house_seller.sort(key=lambda x: x.price)                        #we sort them by price
                    if list_house_seller[0].price > otherfunctions.main_generator_price:
                        if house_event.bankaccount> otherfunctions.main_generator_price*self.event_list[i].load_usage:
                            house_event.bankaccount += - otherfunctions.main_generator_price*self.event_list[i].load_usage    #we use the main if its cheaper
                            house_event.connect_to_main()
                            # print(houseevent + " use main_generator 2")
                        else:
                            print('no money')
                    else:
                        if house_event.bankaccount> list_house_seller[0].price*self.event_list[i].load_usage:
                            house_event.bankaccount += - list_house_seller[0].price*self.event_list[i].load_usage
                                                                                               #otherwise we connect 2 houses
                            list_house_seller[0].bankaccount += list_house_seller[0].price*self.event_list[i].load_usage

                            list_house_seller[0].charge += - self.event_list[i].load_usage
                            house_event.connect_to_other_house()
                            list_house_seller[0].connect_to_other_house()
                            sellerhouse = str(list_house_seller[0])
                            # print(houseevent + " buy from " + sellerhouse)
                        else:
                            print('no money')
            # for a in range(0, len(list_house)):
            #     index = str(a+1)
            #     charge = str(list_house[a].charge)
            #     bankacc = str(list_house[a].bankaccount)
            #     print("house" + index + " charge = " + charge )
            #     print("house" + index + " bank acc = " + bankacc)
            # print(self.event_list[i].load_usage)
            pullData1 = open("sampleData.txt","a+")
            pullData1.write(str(time1)+ "," + str(int(houses.house1.charge)) +"\n")
            pullData1.close()
            pullData2 = open("sampleData2.txt","a+")
            pullData2.write(str(time1)+ "," + str(int(houses.house2.charge)) +"\n")
            pullData2.close()
            pullData3 = open("sampleData3.txt","a+")
            pullData3.write(str(time1)+ "," + str(int(houses.house3.charge)) +"\n")
            pullData3.close()
            pullData4 = open("sampleData4.txt","a+")
            pullData4.write(str(time1)+ "," + str(int(houses.house4.charge)) +"\n")
            pullData4.close()
            loop_active = True
            while loop_active:
                gui2.root2.update()
                gui2.set_label()
                if i == len(self.event_list):
                    gui2.root.quit()
                    gui2.root2.quit()
                    loop_active = False
                else:
                    break

