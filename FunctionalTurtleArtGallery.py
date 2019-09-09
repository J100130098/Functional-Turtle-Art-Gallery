import turtle
Roger=turtle
def hexagon():
    for i in range(6):
        Roger.forward(150)
        Roger.right(60)
def octagon():
    for i in range(8):
        Roger.forward(50)
        Roger.left(45)
def octagonLoop():
    for i in range(80):
        octagon()
        Roger.right(5)
def dodecagon():
    for i in range(12):
        Roger.forward(100)
        Roger.right(30)
def circleSpiral():
    for i in range(40):
        Roger.circle(i*5)
        Roger.right(5)

Roger.bgcolor("pink")
Roger.speed(10000)
octagonLoop()
Roger.penup()
Roger.goto(-300,100)
Roger.pendown()
Roger.color("Dark Green")
Roger.begin_fill()
hexagon()
Roger.end_fill()
Roger.penup()
Roger.goto(300,-100)
Roger.pendown()
Roger.color("Light Coral")
Roger.begin_fill()
dodecagon()
Roger.end_fill()
Roger.penup()
Roger.goto(500,200)
Roger.pendown()
Roger.color("Blue Violet")
circleSpiral()
Roger.exitonclick()