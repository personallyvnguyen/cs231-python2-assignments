import turtle


a = 0
b = 0

turtle.bgcolor('black')
turtle.speed(0)
turtle.pencolor('green')
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()

switch = 0

while True:
    if switch:
        turtle.pencolor('green')
    else:
        turtle.pencolor('red')
    turtle.forward(a)
    turtle.right(b)
    a += 1.5
    b += .5
    switch = not switch
    if b == 200:
        break

turtle.exitonclick()