# module that moves a point (x, y) in 4 different directions, and calculates distance
# from another existing point
from math import sqrt

class Rocket():
    def __init__(self, x=0, y=0):
        # each rocket has (x,y) position; user or calling function has choice
        # of passing in x and y value, or by default they are set at 0
