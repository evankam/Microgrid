import time
import otherfunctions
import houses
import gui2
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
            list_house[i].charge += otherfunctions.solar(event.time) - otherfunctions.solar(self.current_time)
            if list_house[i].charge > 100:
                list_house[i].charge = 100
        self.current_time = event.time

    def run_dispatcher(self,list_house):
        for i in range (0,len(self.event_list)):
            time.sleep(2)
            trueindex = str(i+1)
            print("event" + trueindex)
            self.solar_event(self.event_list[i], list_house)
            time1 = self.event_list[i].time
            house_event = self.event_list[i].house
            houseevent= str(house_event)
            list_houses = house_event.neighbour
            if self.event_list[i].load_usage < house_event.charge:               #we use the battery if we have enough power
                house_event.charge += - self.event_list[i].load_usage
                house_event.connect_to_solar()
                # print(house_event.charge)
                # print(self.event_list[i].load_usage)
                print(houseevent + " use solar")
            else:
                list_house_seller = []
                for j in range(0, len(list_houses)):
                    if list_houses[j].charge>self.event_list[i].load_usage:
                                                                 #if not we compute a list of houses having enough load and their prices
                        list_house_seller.append(list_houses[j])
                if len(list_house_seller) ==0:
                    if house_event.bankaccount> main_generator_price*self.event_list[i].load_usage:
                        house_event.bankaccount += - main_generator_price*self.event_list[i].load_usage#we use the main if its cheaper
                        house_event.connect_to_main()
                        print(houseevent + " use main_generator 1")
                    else:
                        print('no money')
                else:
                    for k in range(0, len(list_house_seller)):
                        list_house_seller[k].compute_price()
                    list_house_seller.sort(key=lambda x: x.price)                        #we sort them by price
                    if list_house_seller[0].price > main_generator_price:
                        if house_event.bankaccount> main_generator_price*self.event_list[i].load_usage:
                            house_event.bankaccount += - main_generator_price*self.event_list[i].load_usage    #we use the main if its cheaper
                            house_event.connect_to_main()
                            print(houseevent + " use main_generator 2")
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
                            print(houseevent + " buy from " + sellerhouse)
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
            pullData1.write(str(i)+ "," + str(int(houses.house2.charge)) +"\n")
            pullData1.close()
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

