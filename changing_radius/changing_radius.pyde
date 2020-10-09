# CS 20 Conditional Branching Example
# Create a circle that changes sizes when a key is pressed

# setting the initial valaue of the global variable radius
radius = 10.0


def setup ():
    background(0)
    circle(150, 150, radius)
    size (300, 300)
    print("Hit the UP arrow to increase the radius")
    print("Hit the DOWN arrow to decrease the radius")


def change_radius():
    """Change the value of a radius"""
    # we need to say that radius is a global variable in order to
    # change the value
    global radius 
    # when the plus sign is pressed, the radius increases by 5 pixels
    if keyCode == UP:
        radius = radius + 5
    # add code so the radius is decreased by 5 is the minus
    # sign is pressed
    elif keyCode == DOWN:
        radius = radius - 5
    else:
        print("Invalid Key")
 

def keyPressed():
    global radius
    change_radius()


def draw():
    global radius
    background(0)
    # a circle with a radius that changes when a key is pressed
    circle(150, 150, radius)
    return
