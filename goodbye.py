import turtle          
win = turtle.Screen()  
t = turtle.Turtle()
t.pensize(5)
t.speed(1000)
# G
t.penup()
t.goto(-250, 0)
t.pendown()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(35)
t.penup()
t.goto(-200, 100)
t.pendown()
t.forward(50)
t.left(90)
t.forward(100)

# O

t.penup()
t.left(90)
t.goto(-165, 0)
t.pendown()
t.circle(27)
t.penup()
t.goto(-104, 0)
t.pendown()
t.circle(27)

#d

t.penup()
t.goto(-70, 0)
t.pendown()
for i in range (4):
    t.forward(50)
    t.left(90)
t.penup()
t.goto(-20, 100)
t.pendown()
t.right(90)
t.forward(100)

#b
t.left(90)
t.penup()
t.goto(-10, 0)
t.pendown()
for i in range (4):
    t.forward(50)
    t.left(90)
t.left(90)
t.forward(100)


#y

t.penup()
t.goto(70, 0)
t.pendown()

t.forward(55)
t.left(45)
t.forward(60)
t.backward(60)
t.right(90)
t.forward(60)

#e
t.left(45)
t.penup()
t.goto(130, 0)
t.pendown()
t.forward(100)
t.right(90)
t.forward(50)
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(25)
t.backward(25)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)








