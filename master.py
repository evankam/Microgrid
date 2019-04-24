from pyfirmata import Arduino,util
import time
import random
from tkinter import *
from decimal import Decimal
import houses
import gui2
import events
import Dispatcher
import otherfunctions

season = 1

dispatcher1 = Dispatcher.Dispatcher()
dispatcher1.event_list = []
dispatcher1.current_time = 0

dispatcher1.add_events_from_lists(houses.house1.list_events)
dispatcher1.add_events_from_lists(houses.house2.list_events)
dispatcher1.add_events_from_lists(houses.house3.list_events)
dispatcher1.add_events_from_lists(houses.house4.list_events)

dispatcher1.run_dispatcher(houses.list_house,season)




