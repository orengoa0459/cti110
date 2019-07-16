# This program draws initials AMO.
# 06/20/2019
# CTI-110 P4T1a - Initials
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
# 3.) Set turtle to draw  letter "A", "M", "O".
#       use t.circle() to create letter "O".
# 4.) Display initials "AMO".

import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.speed(10)
t.pensize(8)            
t.pencolor("white")     
t.shape("turtle")
win.bgcolor("green")

#Letter "A"
t.penup()
t.goto(-120,0)
t.pendown()
t.left(60)
t.forward(90)
t.right(120)
t.forward(90)
t.penup()
t.goto(-120,45)
t.pendown()
t.goto(-30,45)

#Letter "M"
t.penup()
t.goto(0,0)
t.pendown()
t.goto(35,70)
t.goto(50,35)
t.goto(65,70)
t.goto(100,0)

#Letter "O"
t.penup()
t.goto(130,15)
t.pendown()
t.circle(42)
