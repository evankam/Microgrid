import houses
class Event:
    def _init_(self):
        self.time = 0   #time in minutes
        self.house = house
        self.load_usage = 4    #usage of load in percentages of battery

    def define_event_random(self, house):
        self.time = random.randint(0, 1080)
        self.house = house
        self.load_usage = random.randint(1,50)
event1 = Event()
event1.time = 195
event1.load_usage = 16
event1.house = houses.house1

event2 = Event()
event2.time = 453
event2.load_usage = 26
event2.house = houses.house1

event3 = Event()
event3.time = 490
event3.load_usage = 19
event3.house = houses.house1

event4 = Event()
event4.time = 3
event4.load_usage = 1
event4.house= houses.house1

event5 = Event()
event5.time = 399
event5.load_usage = 13
event5.house = houses.house1

event6 = Event()
event6.time = 267
event6.load_usage = 5
event6.house = houses.house1

event7 = Event()
event7.time = 264
event7.load_usage = 17
event7.house= houses.house2

event8 = Event()
event8.time = 419
event8.load_usage = 25
event8.house= houses.house2

event9 = Event()
event9.time = 735
event9.load_usage = 15
event9.house= houses.house2

event10= Event()
event10.time = 176
event10.load_usage = 21
event10.house= houses.house2

event11 = Event()
event11.time = 291
event11.load_usage = 15
event11.house= houses.house2

event12 = Event()
event12.time = 83
event12.load_usage = 27
event12.house= houses.house2

event13 = Event()
event13.time = 435
event13.load_usage = 23
event13.house= houses.house2

event14 = Event()
event14.time = 186
event14.load_usage = 4
event14.house= houses.house2

event15 = Event()
event15.time = 232
event15.load_usage = 12
event15.house= houses.house3

event16 = Event()
event16.time = 369
event16.load_usage = 13
event16.house= houses.house3

event17 = Event()
event17.time = 770
event17.load_usage = 26
event17.house= houses.house3

event18 = Event()
event18.time = 723
event18.load_usage = 14
event18.house= houses.house3

event19 = Event()
event19.time = 212
event19.load_usage = 24
event19.house= houses.house3

event20 = Event()
event20.time = 161
event20.load_usage = 14
event20.house= houses.house3

event21 = Event()
event21.time = 719
event21.load_usage = 25
event21.house= houses.house4

event22 = Event()
event22.time = 661
event22.load_usage = 20
event22.house= houses.house4

event23 = Event()
event23.time = 409
event23.load_usage = 12
event23.house= houses.house4

event24 = Event()
event24.time = 28
event24.load_usage = 15
event24.house= houses.house4

event25 = Event()
event25.time = 156
event25.load_usage = 7
event25.house= houses.house4


houses.house1.add_event(event1)
houses.house1.add_event(event2)
houses.house1.add_event(event3)
houses.house1.add_event(event4)
houses.house1.add_event(event5)
houses.house1.add_event(event6)


houses.house2.add_event(event7)
houses.house2.add_event(event8)
houses.house2.add_event(event9)
houses.house2.add_event(event10)
houses.house2.add_event(event11)
houses.house2.add_event(event12)
houses.house2.add_event(event13)
houses.house2.add_event(event14)


houses.house3.add_event(event15)
houses.house3.add_event(event16)
houses.house3.add_event(event17)
houses.house3.add_event(event18)
houses.house3.add_event(event19)
houses.house3.add_event(event20)

houses.house4.add_event(event21)
houses.house4.add_event(event22)
houses.house4.add_event(event23)
houses.house4.add_event(event24)
houses.house4.add_event(event25)
