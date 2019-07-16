# This program draws a square and triangle.
# 06/20/2019
# CTI-110 P4T1a - Shapes
# Anthony Orengo

# pseudocode
# 1.) Import turtle
#     win = turtle.Screen()
#     t = turtle.Turtle()
# 2.) Set Display options
#     t.speed()
#     t.pensize()
#     t.pencolor("")
#     t.shape("")
#     win.bgcolor
# 3.) Create loop for square and triangle.
#       a. Set square to range of 4 and triangle to range of 3.
#       b. Divide range by number of sides to determine angle.
# 4.) Display square and triangle.


# Import turtle
# Window
import turtle
win = turtle.Screen()
t = turtle.Turtle()
 
#Display options
# Set pen color to black and turtle shape to turtle.
t.speed(10)
t.pensize(3)
t.pencolor("black")
t.shape("turtle")
win.bgcolor


# Initiate loop for square
for i in range(4):
    t.forward(150)
    t.left(90)
t.penup()
t.goto(0, -180)
t.pendown()
# Initiate loop for triangle
for i in range(3):
    t.forward(180)
    t.left(120)
