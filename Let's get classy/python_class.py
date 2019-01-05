# TSB - Create Class in python - rocket positions (x,y) and graph

import matplotlib.pyplot as plt

class Rocket():
    def __init__(self, x=0, y=0):
        # each rocket has (x, y) position; user or calling function has choice of passing in x and y values or by default they are set at 0
        self.x = x
        self.y = y

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

# Make a series of rockets - x,y postions
rockets = []
rockets.append(Rocket())
rockets.append(Rocket(0, 2))
rockets.append(Rocket(1, 4))
rockets.append(Rocket(2, 6))
rockets.append(Rocket(3, 7))
rockets.append(Rocket(5, 9))
rockets.append(Rocket(8, 15))

