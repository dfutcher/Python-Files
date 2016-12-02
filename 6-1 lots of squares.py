import turtle
import random #allows me to use random numbers

turtle.speed(0) #turtle goes fast >>>>>

def square():
    for i in range(4):
        turtle.fd(50)
        turtle.right(90)

def nextshape():
    turtle.pu()
    turtle.fd(50)
    turtle.pd()

def restart():
    turtle.pu()
    turtle.backward(500)
    turtle.rt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.pd()

def gotostart():
    turtle.pu()
    turtle.setx(-300)
    turtle.sety(200)
    turtle.pd()

def getcolour():
    colourNumber = random.randint(1, 3)
    if colourNumber == 1:
        colour = "Red"
    elif colourNumber == 2:
        colour = "Blue"
    elif colourNumber == 3:
        colour = "Green"
    return colour
    
# Program starts here
gotostart()


for i in range (10): #draws 10 rows
    for i in range (10): #draws 10 squares on a row
        myColour = getcolour() #sets myColour to random colour
        turtle.fillcolor(myColour)
        turtle.begin_fill()
        square()
        turtle.end_fill()
        nextshape()
    restart() #goes back to beginning of row and drops down a line


