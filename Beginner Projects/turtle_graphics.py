#################################################################################################

# A nice little project from Chapter 4 of Think Python (second edition).
# https://greenteapress.com/wp/think-python-2e/

# A slightly different online interactive version can be found here:
# https://runestone.academy/ns/books/published/thinkcspy/PythonTurtle/toctree.html

# The program below is a quick demo combining these two projects.
# I feel this can be entertaining for kids who learn Python.
# They can tweak the code and have a lot of fun :)

#################################################################################################

import turtle
import math

wn = turtle.Screen()
wn.bgcolor("blue")

bob = turtle.Turtle()
bob.shape("turtle")
bob.color("yellow")
bob.pensize(5)
bob.speed(6)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

def star(t):
    for i in range(5):
        t.forward(110)
        t.left(216)

def stamp(t):
    for i in range(10):
        bob.fd(50)
        bob.stamp()
        bob.bk(50)
        bob.right(36)

    bob.rt(90)
    bob.fd(300)

    for j in range(5, 60, 2):
        bob.stamp()
        bob.forward(j)
        bob.right(24)

# Let Bob the Turtle draw a square, followed by a pentagon, a hexagon, and an octagon:
square(bob, 100)
polygon(bob, 5, 70)
polygon(bob, 6, 70)
polygon(bob, 8, 70)

# Move Bob (lift the "pen" first and then put it down after Bob has moved to the right position):
bob.up()
bob.goto(-200, 100)
bob.down()

# Draw an arc
arc(bob, 50, 90)

# Move Bob
bob.up()
bob.fd(50)
bob.down()

# Draw a circle
circle(bob, 30)

# Move Bob
bob.up()
bob.goto(-350, 100)
bob.down()

# Draw a star
star(bob)

# Move Bob
bob.up()
bob.goto(-350, -150)

# Let Bob make stamps
stamp(bob)

# Click the window to quit after all the functions
wn.exitonclick()

#################################################################################################
# Here's a list of the "turtle" methods:
# https://runestone.academy/ns/books/published/thinkcspy/PythonTurtle/SummaryofTurtleMethods.html

# Additional exercises can be found in Think Python (p.37), including drawing flowers using "arc"
# from the "polygon" module. The code is available in the author's GitHub repo:
# https://github.com/AllenDowney/ThinkPython2/blob/master/code/flower.py

#################################################################################################
