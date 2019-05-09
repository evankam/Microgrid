import houses
import random

class Event:
    def _init_(self):
        self.time = 0   #time in minutes
        self.house = houses.house1
        self.load_usage = 4    #usage of load in percentages of battery

    def define_event_random(self, house):
        self.time = random.randint(1, 780)
        self.house = house
        self.load_usage = random.randint(1,5)


for i in range(0,25):
    event_rand = Event()
    event_rand.define_event_random(houses.house1)
    houses.house1.list_events.append(event_rand)

for i in range(0,25):
    event_rand = Event()
    event_rand.define_event_random(houses.house2)
    houses.house2.list_events.append(event_rand)

for i in range(0,25):
    event_rand = Event()
    event_rand.define_event_random(houses.house3)
    houses.house3.list_events.append(event_rand)

for i in range(0,25):
    event_rand = Event()
    event_rand.define_event_random(houses.house4)
    houses.house4.list_events.append(event_rand)

# print(houses.house4.list_events[0].load_usage,houses.house3.list_events[0].load_usage,houses.house2.list_events[0].load_usage,houses.house1.list_events[0].load_usage)
# event1 = Event()
# event1.time = 195
# event1.load_usage = 16
# event1.house = houses.house1
#
# event2 = Event()
# event2.time = 453
# event2.load_usage = 26
# event2.house = houses.house1
#
# event3 = Event()
# event3.time = 490
# event3.load_usage = 19
# event3.house = houses.house1
#
# event4 = Event()
# event4.time = 3
# event4.load_usage = 1
# event4.house= houses.house1
#
# event5 = Event()
# event5.time = 399
# event5.load_usage = 13
# event5.house = houses.house1
#
# event6 = Event()
# event6.time = 267
# event6.load_usage = 5
# event6.house = houses.house1
#
# event7 = Event()
# event7.time = 264
# event7.load_usage = 17
# event7.house= houses.house2
#
# event8 = Event()
# event8.time = 419
# event8.load_usage = 25
# event8.house= houses.house2
#
# event9 = Event()
# event9.time = 735
# event9.load_usage = 15
# event9.house= houses.house2
#
# event10= Event()
# event10.time = 176
# event10.load_usage = 21
# event10.house= houses.house2
#
# event11 = Event()
# event11.time = 291
# event11.load_usage = 15
# event11.house= houses.house2
#
# event12 = Event()
# event12.time = 83
# event12.load_usage = 27
# event12.house= houses.house2
#
# event13 = Event()
# event13.time = 435
# event13.load_usage = 23
# event13.house= houses.house2
#
# event14 = Event()
# event14.time = 186
# event14.load_usage = 4
# event14.house= houses.house2
#
# event15 = Event()
# event15.time = 232
# event15.load_usage = 12
# event15.house= houses.house3
#
# event16 = Event()
# event16.time = 369
# event16.load_usage = 13
# event16.house= houses.house3
#
# event17 = Event()
# event17.time = 770
# event17.load_usage = 26
# event17.house= houses.house3
#
# event18 = Event()
# event18.time = 723
# event18.load_usage = 14
# event18.house= houses.house3
#
# event19 = Event()
# event19.time = 212
# event19.load_usage = 24
# event19.house= houses.house3
#
# event20 = Event()
# event20.time = 161
# event20.load_usage = 14
# event20.house= houses.house3
#
# event21 = Event()
# event21.time = 719
# event21.load_usage = 25
# event21.house= houses.house4
#
# event22 = Event()
# event22.time = 661
# event22.load_usage = 20
# event22.house= houses.house4
#
# event23 = Event()
# event23.time = 409
# event23.load_usage = 12
# event23.house= houses.house4
#
# event24 = Event()
# event24.time = 28
# event24.load_usage = 15
# event24.house= houses.house4
#
# event25 = Event()
# event25.time = 156
# event25.load_usage = 7
# event25.house= houses.house4
#
# event26	=	Event()
# event26.time=	170
# event26.load_usage=	11
# event26.house=	houses.house1
#
# event27	=	Event()
# event27.time=	660
# event27.load_usage=	5
# event27.house=	houses.house1
#
# event28	=	Event()
# event28.time=	402
# event28.load_usage=	5
# event28.house=	houses.house1
#
# event29 =	Event()
# event29.time=	656
# event29.load_usage=	17
# event29.house=	houses.house1
#
# event30	=	Event()
# event30.time=	464
# event30.load_usage=	11
# event30.house=	houses.house1
#
# event31	=	Event()
# event31.time=	562
# event31.load_usage=	14
# event31.house=	houses.house1
#
# event32	=	Event()
# event32.time=	356
# event32.load_usage=	11
# event32.house=	houses.house1
#
# event33	=	Event()
# event33.time=	515
# event33.load_usage=	22
# event33.house=	houses.house1
#
# event34	=	Event()
# event34.time=	275
# event34.load_usage=	22
# event34.house=	houses.house1
#
# event35	=	Event()
# event35.time=	94
# event35.load_usage=	13
# event35.house=	houses.house1
#
# event36=	Event()
# event36.time=	122
# event36.load_usage=	14
# event36.house=	houses.house1
#
# event37	=	Event()
# event37.time=	359
# event37.load_usage=	1
# event37.house=	houses.house1
#
# event38	=	Event()
# event38.time=	96
# event38.load_usage=	15
# event38.house=	houses.house1
#
# event39	=	Event()
# event39.time=	136
# event39.load_usage=	22
# event39.house=	houses.house1
#
# event40	=	Event()
# event40.time=	703
# event40.load_usage=	19
# event40.house=	houses.house1
#
# event41	=	Event()
# event41.time=	229
# event41.load_usage=	23
# event41.house=	houses.house1
#
# event42	=	Event()
# event42.time=	253
# event42.load_usage=	19
# event42.house=	houses.house1
#
# event43	=	Event()
# event43.time=	193
# event43.load_usage=	3
# event43.house=	houses.house1
#
# event44	=	Event()
# event44.time=	380
# event44.load_usage=	22
# event44.house=	houses.house1
#
# event45	=	Event()
# event45.time=	504
# event45.load_usage=	12
# event45.house=	houses.house1
#
# event46	=	Event()
# event46.time=	455
# event46.load_usage=	13
# event46.house=	houses.house1
#
# event47	=	Event()
# event47.time=	649
# event47.load_usage=	10
# event47.house=	houses.house1
#
# event48	=	Event()
# event48.time=	288
# event48.load_usage=	1
# event48.house=	houses.house1
#
# event49	=	Event()
# event49.time=	460
# event49.load_usage=	24
# event49.house=	houses.house1
#
# event50	=	Event()
# event50.time=	505
# event50.load_usage=	26
# event50.house=	houses.house1
#
# event51	=	Event()
# event51.time=	241
# event51.load_usage=	13
# event51.house=	houses.house1
#
# event52	=	Event()
# event52.time=	160
# event52.load_usage=	25
# event52.house=	houses.house1
#
# event53	=	Event()
# event53.time=	144
# event53.load_usage=	11
# event53.house=	houses.house1
#
# event54	=	Event()
# event54.time=	497
# event54.load_usage=	19
# event54.house=	houses.house2
#
# event55	=	Event()
# event55.time=	505
# event55.load_usage=	12
# event55.house=	houses.house2
#
# event56	=	Event()
# event56.time=	332
# event56.load_usage=	4
# event56.house=	houses.house2
#
# event57	=	Event()
# event57.time=	695
# event57.load_usage=	24
# event57.house=	houses.house2
#
# event58	=	Event()
# event58.time=	643
# event58.load_usage=	7
# event58.house=	houses.house2
#
# event59	=	Event()
# event59.time=	78
# event59.load_usage=	2
# event59.house=	houses.house2
#
# event60	=	Event()
# event60.time=	661
# event60.load_usage=	21
# event60.house=	houses.house2
#
# event61	=	Event()
# event61.time=	538
# event61.load_usage=	29
# event61.house=	houses.house2
#
# event62	=	Event()
# event62.time=	515
# event62.load_usage=	26
# event62.house=	houses.house2
#
# event63	=	Event()
# event63.time=	287
# event63.load_usage=	17
# event63.house=	houses.house2
#
# event64	=	Event()
# event64.time=	54
# event64.load_usage=	5
# event64.house=	houses.house2
#
# event65	=	Event()
# event65.time=	404
# event65.load_usage=	8
# event65.house=	houses.house2
#
# event66	=	Event()
# event66.time=	411
# event66.load_usage=	10
# event66.house=	houses.house2
#
# event67	=	Event()
# event67.time=	283
# event67.load_usage=	14
# event67.house=	houses.house2
#
# event68	=	Event()
# event68.time=	4
# event68.load_usage=	13
# event68.house=	houses.house2
#
# event69	=	Event()
# event69.time=	467
# event69.load_usage=	6
# event69.house=	houses.house2
#
# event70	=	Event()
# event70.time=	36
# event70.load_usage=	28
# event70.house=	houses.house2
#
# event71	=	Event()
# event71.time=	395
# event71.load_usage=	13
# event71.house=	houses.house2
#
# event72	=	Event()
# event72.time=	438
# event72.load_usage=	6
# event72.house=	houses.house2
#
# event73	=	Event()
# event73.time=	313
# event73.load_usage=	25
# event73.house=	houses.house2
#
# event74	=	Event()
# event74.time=	508
# event74.load_usage=	20
# event74.house=	houses.house2
#
# event75	=	Event()
# event75.time=	326
# event75.load_usage=	26
# event75.house=	houses.house2
#
# event76	=	Event()
# event76.time=	380
# event76.load_usage=	2
# event76.house=	houses.house2
#
# event77	=	Event()
# event77.time=	378
# event77.load_usage=	5
# event77.house=	houses.house2
#
# event78	=	Event()
# event78.time=	651
# event78.load_usage=	18
# event78.house=	houses.house3
#
# event79	=	Event()
# event79.time=	546
# event79.load_usage=	20
# event79.house=	houses.house3
#
# event80	=	Event()
# event80.time=	503
# event80.load_usage=	15
# event80.house=	houses.house3
#
# event81	=	Event()
# event81.time=	302
# event81.load_usage=	6
# event81.house=	houses.house3
#
# event82	=	Event()
# event82.time=	656
# event82.load_usage=	22
# event82.house=	houses.house3
#
# event83	=	Event()
# event83.time=	7
# event83.load_usage=	23
# event83.house=	houses.house3
#
# event84	=	Event()
# event84.time=	708
# event84.load_usage=	29
# event84.house=	houses.house3
#
# event85	=	Event()
# event85.time=	34
# event85.load_usage=	9
# event85.house=	houses.house3
#
# event86	=	Event()
# event86.time=	136
# event86.load_usage=	6
# event86.house=	houses.house3
#
# event87	=	Event()
# event87.time=	181
# event87.load_usage=	2
# event87.house=	houses.house3
#
# event88	=	Event()
# event88.time=	685
# event88.load_usage=	5
# event88.house=	houses.house3
#
# event89	=	Event()
# event89.time=	197
# event89.load_usage=	16
# event89.house=	houses.house3
#
# event90	=	Event()
# event90.time=	127
# event90.load_usage=	8
# event90.house=	houses.house3
#
# event91	=	Event()
# event91.time=	587
# event91.load_usage=	15
# event91.house=	houses.house4
#
# event92	=	Event()
# event92.time=	83
# event92.load_usage=	9
# event92.house=	houses.house4
#
# event93	=	Event()
# event93.time=	23
# event93.load_usage=	17
# event93.house=	houses.house4
#
# event94	=	Event()
# event94.time=	183
# event94.load_usage=	27
# event94.house=	houses.house4
#
# event95	=	Event()
# event95.time=	330
# event95.load_usage=	22
# event95.house=	houses.house4
#
# event96	=	Event()
# event96.time=	418
# event96.load_usage=	28
# event96.house=	houses.house4
#
# event97	=	Event()
# event97.time=	299
# event97.load_usage=	24
# event97.house=	houses.house4
#
# event98	=	Event()
# event98.time=	317
# event98.load_usage=	21
# event98.house=	houses.house4
#
# event99	=	Event()
# event99.time=	548
# event99.load_usage=	22
# event99.house=	houses.house4
#
# event100	=	Event()
# event100.time=	639
# event100.load_usage=	27
# event100.house=	houses.house4
#
#
#
# houses.house1.add_event(event1)
# houses.house1.add_event(event2)
# houses.house1.add_event(event3)
# houses.house1.add_event(event4)
# houses.house1.add_event(event5)
# houses.house1.add_event(event6)
# houses.house1.add_event(event26)
# houses.house1.add_event(event27)
# houses.house1.add_event(event28)
# houses.house1.add_event(event29)
# houses.house1.add_event(event30)
# houses.house1.add_event(event31)
# houses.house1.add_event(event32)
# houses.house1.add_event(event33)
# houses.house1.add_event(event34)
# houses.house1.add_event(event35)
# houses.house1.add_event(event36)
# houses.house1.add_event(event37)
# houses.house1.add_event(event39)
# houses.house1.add_event(event39)
# houses.house1.add_event(event40)
# houses.house1.add_event(event41)
# houses.house1.add_event(event42)
# houses.house1.add_event(event43)
# houses.house1.add_event(event44)
# houses.house1.add_event(event45)
# houses.house1.add_event(event46)
# houses.house1.add_event(event47)
# houses.house1.add_event(event48)
# houses.house1.add_event(event49)
# houses.house1.add_event(event50)
# houses.house1.add_event(event51)
# houses.house1.add_event(event52)
# houses.house1.add_event(event53)
#
#
# houses.house2.add_event(event7)
# houses.house2.add_event(event8)
# houses.house2.add_event(event9)
# houses.house2.add_event(event10)
# houses.house2.add_event(event11)
# houses.house2.add_event(event12)
# houses.house2.add_event(event13)
# houses.house2.add_event(event14)
# houses.house2.add_event(event54)
# houses.house2.add_event(event55)
# houses.house2.add_event(event56)
# houses.house2.add_event(event57)
# houses.house2.add_event(event58)
# houses.house2.add_event(event59)
# houses.house2.add_event(event60)
# houses.house2.add_event(event61)
# houses.house2.add_event(event62)
# houses.house2.add_event(event63)
# houses.house2.add_event(event64)
# houses.house2.add_event(event65)
# houses.house2.add_event(event66)
# houses.house2.add_event(event67)
# houses.house2.add_event(event68)
# houses.house2.add_event(event69)
# houses.house2.add_event(event70)
# houses.house2.add_event(event71)
# houses.house2.add_event(event72)
# houses.house2.add_event(event73)
# houses.house2.add_event(event74)
# houses.house2.add_event(event75)
# houses.house2.add_event(event76)
# houses.house2.add_event(event77)
#
#
# houses.house3.add_event(event15)
# houses.house3.add_event(event16)
# houses.house3.add_event(event17)
# houses.house3.add_event(event18)
# houses.house3.add_event(event19)
# houses.house3.add_event(event20)
# houses.house3.add_event(event78)
# houses.house3.add_event(event79)
# houses.house3.add_event(event80)
# houses.house3.add_event(event81)
# houses.house3.add_event(event82)
# houses.house3.add_event(event83)
# houses.house3.add_event(event84)
# houses.house3.add_event(event85)
# houses.house3.add_event(event86)
# houses.house3.add_event(event87)
# houses.house3.add_event(event88)
# houses.house3.add_event(event89)
# houses.house3.add_event(event90)
#
# houses.house4.add_event(event21)
# houses.house4.add_event(event22)
# houses.house4.add_event(event23)
# houses.house4.add_event(event24)
# houses.house4.add_event(event25)
# houses.house4.add_event(event91)
# houses.house4.add_event(event92)
# houses.house4.add_event(event93)
# houses.house4.add_event(event94)
# houses.house4.add_event(event95)
# houses.house4.add_event(event96)
# houses.house4.add_event(event97)
# houses.house4.add_event(event98)
# houses.house4.add_event(event99)
# houses.house4.add_event(event100)

