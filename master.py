from pyfirmata import Arduino,util
import time
import random
#from tkinter import *
from decimal import Decimal
import houses
#import gui
#import gui2
import events
import Dispatcher
import otherfunctions


# board = Arduino('COM4')

# house1.connect_to_main() #red and yellow LED
# house2.connect_to_main()
# house3.connect_to_main()
# house4.connect_to_main()
# #
# house1.connect_to_other_house()
# house2.connect_to_other_house()
# house3.connect_to_other_house()
# house4.connect_to_other_house()

# house1.connect_to_solar()
# house2.connect_to_solar()
# house3.connect_to_solar()
#house4.connect_to_solar()

#hey just a test for github




dispatcher1 = Dispatcher()
dispatcher1.event_list = []
dispatcher1.current_time = 0

dispatcher1.add_events_from_lists(house1.list_events)
dispatcher1.add_events_from_lists(house2.list_events)
dispatcher1.add_events_from_lists(house3.list_events)
dispatcher1.add_events_from_lists(house4.list_events)

dispatcher1.run_dispatcher(list_house)




