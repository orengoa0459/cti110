# This program draws a snowflake.
# 06/20/2019
# CTI-110 P4T1a - Snowflake
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
# 3.) Define function branch()
#      a. range(4)
# 4.) Define function flake()
#      a. range(4)
# 5.) Define mainFlake()
#      a. range(8)
# 6.) Display snowflake with function mainFlake().

import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(3)
t.speed(1000)   
t.pencolor("white")     
t.shape("triangle")
win.bgcolor("white")

# Define function branch().
def branch():
    for i in range(4):
        t.forward(10)
        t.right(45)
        t.forward(25)
        t.backward(25)
        t.left(90)
        t.forward(25)
        t.backward(25)
        t.right(45)
# Define function flake()
def flake():
    for i in range(4):
        t.forward(15)
        t.left(90)
# Define function mainFlake()
def mainFlake():
    for i in range(8):
        t.forward(45)
        t.right(60)
        branch()
        t.forward(10)
        t.right(45)
        flake()
        t.left(45)
        t.backward(50)
        t.left(105)
# Set border color to black and fill color to blue.        
t.color("black", "blue")
t.begin_fill()
t.goto(0,0)
# Function mainFlake begins.
mainFlake()
t.end_fill()



 

    

    

