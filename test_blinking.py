# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:29:26 2019

@author: Joer
"""

from pyfirmata import Arduino,util
import time
import random
from decimal import Decimal


board = Arduino('COM8')

board.digital[2].write(1)
board.digital[4].write(1)
