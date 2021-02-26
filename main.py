import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
tim.pensize(15)
tim.speed("fastest")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


def walk():
    var = [0, 90, 180, 270]
    tim.forward(20)
    tim.setheading(random.choice(var))
    tim.color(random.choice(colours))


for i in range(200):
    walk()

screen.exitonclick()
