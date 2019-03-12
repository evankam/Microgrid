from pyfirmata import Arduino,util

# board = Arduino('COM5')
board_bis = Arduino('COM3')




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
            # board.digital[first_relay_to_change].write(0)   #turns the first relay on
            # board.digital[second_relay_to_change].write(0)  #turns the second relay on
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
            # board.digital[first_relay_to_change].write(1)   #turns the first relay off
            # board.digital[second_relay_to_change].write(0)  #turns the second relay on
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
            # board.digital[first_relay_to_change].write(0)   #turns the first relay on
            # board.digital[second_relay_to_change].write(1)  #turns the second relay off
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
house4.number = 4



list_house = [house1,house2,house3,house4]
for i in range (0,len(list_house)):
    houses =[house1,house2,house3,house4]
    del houses[i]
    list_house[i].neighbour = houses

house1.connect_to_main()
house2.connect_to_solar()
house3.connect_to_solar()

