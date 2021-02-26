import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


def walk():
    var = [0, 90, 180, 270]
    tim.forward(20)
    tim.setheading(random.choice(var))
    tim.color(random.choice(colours))


for i in range(0, 1000):
    walk()

screen.exitonclick()
