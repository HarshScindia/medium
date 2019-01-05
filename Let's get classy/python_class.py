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

# show on graph where each rocket is

for index, rocket in enumerate(rockets):
    # Original postion of rockets
    print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))
    plt.plot(rocket.x, rocket.y, 'ro', linewidth=2, linestyle='dashed', markersize = 12)

    # move the rocket one up
    rocket.move_up()
    print("New rocket position %d is at (%d, %d)." % (index, rocket.x, rocket.y))

    #plot the new position
    plt.plot(rocket.x, rocket.y, 'bo', linewidth=2, linestyle='dashed', markersize = 12)

    #move the rocket left
    rocket.move_left()
    plt.plot(rocket.x, rocket.y, 'yo', linewidth=2, linestyle='dashed', markersize = 12)

# show the graph legend to match colors with positions
plt.gca().legend(('original position', '^ - moved up', '< - moved left'))
plt.show()
#plt.legend(loc='upper left')
