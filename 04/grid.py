import turtle

turtle.penup()
turtle.left(180)
turtle.forward(300)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.pendown()

count = 4
while (count>0):
        turtle.forward(500)
        turtle.left(90)
        count = count - 1

count = 4
while (count>0):
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(500)
        turtle.left(180)
        turtle.forward(500)
        turtle.left(90)
        count = count - 1

turtle.forward(100)

count = 4
while (count>0):
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(500)
        turtle.left(180)
        turtle.forward(500)
        count = count - 1


turtle.exitonclick()
