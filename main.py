import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
tim.pensize(15)
tim.speed("fastest")
t.colormode(255)

def random_color():
    r = (random.randint(0, 255))
    g = (random.randint(0, 255))
    b = (random.randint(0, 255))
    random_color(r, g, b)
    return random_color


def walk():
    var = [0, 90, 180, 270]
    tim.forward(20)
    tim.setheading(random.choice(var))
    tim.color(random_color())


for i in range(200):
    walk()

screen.exitonclick()
