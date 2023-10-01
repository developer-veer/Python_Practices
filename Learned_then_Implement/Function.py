# using Turtle linrary
import turtle as tur

def box():
    for x in range(4):
        veer.speed(1.1)
        veer.forward(120)
        veer.left(90)
        veer.forward(120)
        veer.left(90)
        veer.forward(120)
        veer.left(90)
        veer.forward(120)


wn = tur.Screen()
veer = tur.Turtle()
circ = tur.Turtle()

circ.color("Green")


box()

veer.color("Red")



tur.exitonclick()

