import turtle
import random
turtle.speed(100)

def getcolour(): # procedure to give me a random colour
    colnum = random.randint(1,3) #sets colnum to a random number
    if colnum == 1:
        pc = "Red"
    elif colnum == 2:
        pc = "Blue"
    elif colnum == 3:
        pc = "Green"
    return pc #outputs the colour name
    

def square(): #subroutine to draw a square
    for i in range(4):
        turtle.fd(50)
        turtle.right(90)

def nextshape(): #a new subroutine
    turtle.pu()
    turtle.forward(50)
    turtle.pd()

def restart(): #moves turtle back to start
    turtle.pu()
    turtle.backward(500)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.pd()

def gotostart(): #moves to top left of grid
    turtle.pu()
    turtle.setx(-300)
    turtle.sety(300)
    turtle.pd()



gotostart()
for i in range (10): #10 rows please
    for i in range (10): #10 squares please
        myColour = getcolour() #sets a random colour
        turtle.fillcolor(myColour)
        turtle.begin_fill()
        square()
        turtle.end_fill()
        nextshape()
    restart()
