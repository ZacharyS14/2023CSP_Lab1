# Import Turtle
import turtle as trtl

# Declare Turtles.
# ONLY USE THE lines TURTLE!!!!
box = trtl.Turtle()
lines = trtl.Turtle()
wn = trtl.Screen()

# Setup Screen
def setupScreen():
    global wn
    wn.setup(1000, 700)

# Create the box on the screen
def setupBox():
    box.speed(0)
    box.penup()
    box.goto(-490, -300)
    box.pendown()
    box.forward(980)
    box.left(90)
    box.forward(630)
    box.left(90)
    box.forward(980)
    box.left(90)
    box.forward(630)
    box.hideturtle()


# Code for 80 point version goes here
def v80():
    lines.speed(20)
    lines.penup()
    lines.goto(-490, -300)
    lines.pendown()
    endX = (490)
    endY = (-290)
    startX = (-490)
    startY = (-300)
    for x in range(32):
        lines.goto(endX, endY)
        lines.goto(startX, startY)
        startX += 30
        endY += 20
        lines.goto(startX,startY)


# Code for the 90 point version goes here
def v90():
    # Calling the 80 point function - don't copy-paste from earlier method!!
    v80()
    lines.goto(490, -300)
    endX = (-490)
    endY = (-290)
    startX = (490)
    startY = (-300)
    for x in range(32):
        lines.goto(endX, endY)
        lines.goto(startX, startY)
        startX -= 30
        endY += 20
        lines.goto(startX,startY)




# Code for the 100 point version here
def v100():
    # Calling the 90 point function - don't copy-paste from earlier method!!
    v90()
    lines.goto(-490, 330)
    endX = (490)
    endY = (320)
    startX = (-490)
    startY = (320)
    for x in range(32):
        lines.goto(endX, endY)
        lines.goto(startX, startY)
        startX += 30
        endY -= 20
        lines.goto(startX,startY)
    lines.goto(490, 330)
    endX = (-490)
    endY = (320)
    startX = (490)
    startY = (330)
    for x in range(32):
        lines.goto(endX, endY)
        lines.goto(startX, startY)
        startX -= 30
        endY -= 20
        lines.goto(startX, startY)


# Code for the 110 point version here
def v110():
    # Calling the 100 point function - don't copy-paste from earlier method!!
    v100()
    lines.penup()
    lines.goto(300, -200)
    lines.pendown()
    endX = (300)
    endY = (-90)
    startX = (-300)
    startY = (-100)
    for x in range(32):
        lines.goto(endX, endY)
        lines.goto(startX, startY)
        startX += 17
        endY += 7
        lines.goto(startX, startY)
    lines.penup()
    lines.goto(300, -200)
    lines.pendown()
    endX = (-300)
    endY = (-90)
    startX = (300)
    startY = (-100)
    for x in range(32):
        lines.goto(endX, endY)
        lines.goto(startX, startY)
        startX -= 17
        endY += 7
        lines.goto(startX, startY)
    lines.penup()
    lines.goto(300, -200)
    lines.pendown()
    endX = (300)
    endY = (90)
    startX = (-300)
    startY = (100)
    for x in range(32):
        lines.goto(endX, endY)
        lines.goto(startX, startY)
        startX += 17
        endY -= 7
        lines.goto(startX, startY)
    lines.penup()
    lines.goto(300, -200)
    lines.pendown()
    endX = (-300)
    endY = (90)
    startX = (300)
    startY = (100)
    for x in range(32):
        lines.goto(endX, endY)
        lines.goto(startX, startY)
        startX -= 17
        endY -= 7
        lines.goto(startX, startY)


setupScreen()
setupBox()
v110()





wn.mainloop()