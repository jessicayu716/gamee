from pygame import *
from random import *
from math import *
import os
from glob import *
from getname import *

screen=display.set_mode((600,800))

running=True
 
while running:
    for e in event.get():
        print(e)
        if e.type==QUIT:
            running=False


    display.flip()
quit()
