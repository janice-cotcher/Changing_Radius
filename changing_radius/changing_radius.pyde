# CS 20 Conditional Branching Example
# Create a circle that changes sizes when a key is pressed

# setting the initial valaue of the global variable radius
radius = 10


def setup ():
    background(0)
    ellipse(150, 150, radius , radius)
    size (300, 300)
    print("Hit + to increase the radius")
    print("Hit - to decrease the radius")


def change_radius():
    """Change the value of a radius"""
    # we need to say that radius is a global variable in order to
    # change the value
    global radius 
    # when the plus sign is pressed, the radius increases by 5 pixels
    if key == "+":
        return radius + 5
    # add code so the radius is decreased by 5 is the minus
    # sign is pressed
    elif key == "-":
        return radius - 5
 

def keyPressed():
    global radius
    radius = change_radius()


def draw():
    global radius
    background(0)
    # a circle with a radius that changes when a key is pressed
    ellipse(150, 150, radius , radius)
    return
