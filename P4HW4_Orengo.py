# This program draws a star.
# 06/20/2019
# CTI-110 P4T1a - Star
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
# 3.) Create loop "j" range of 6
#       a. Create nested loop "i" range of 3
#             t.forward (120)       
#             t.left (120)
#       b. Adjust direction of turtle.
#             t.forward(120)  
#             t.right(60)
# 4.) Display star.

import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# Display options
t.pensize(4) # increase pensize (takes integer)
t.speed(100) # increase pen speed (takes integer)
t.pencolor("white") # set pencolor (takes string)
t.shape("turtle")   # set shape of turtle 
win.bgcolor("blue") # set background color

t.penup()
t.goto(-90, 90)
t.pendown()

t.color("black", "white")
t.begin_fill()
# Main loop.
for j in range (6):

    # Nested loop.
    for i in range (3):
        t.forward (120)       
        t.left (120)
        
# Adjust direction of turtle.           
    t.forward(120)  
    t.right(60)
t.end_fill()
