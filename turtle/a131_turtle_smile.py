import turtle # there are lots of goodies in this Module for us to use
import turtlefunctions
# there is only one function in this Module so far

jump = turtlefunctions.jump

def emoticon(t,x,y):
    'turtle t draws a smiley face with chin at coordinate (x, y)' # set turtle direction and pen size
    t.pensize(3)
    t.setheading(0)
# move to (x, y) and draw head
    jump(t, x, y)
    t.circle(100)
# draw right eye
    jump(t, x+35, y+120)
    t.dot(25)
# draw left eye
    jump(t, x-35, y+120)
    t.dot(25)
# draw smile
    jump(t, x-60.62, y+65)
    t.setheading(-60)
    t.circle(70, 120) # smile is a 120 degree section of a circle, a built-in function

def olympic(t):
    '''has turtle t draw the olympic rings'''
    t.pensize(3)
    jump(t, 0, 0) # bottom of top center circle t.setheading(0)
    t.circle(100) # top center circle turtlefunctions.
    jump(t, -220, 0)
    t.circle(100) # top left circle turtlefunctions.
    jump(t, 220, 0)
    t.circle(100) # top right circle turtlefunctions.
    jump(t, 110, -100)
    t.circle(100) # bottom right circle turtlefunctions.
    jump(t, -110, -100)
    t.circle(100) # bottom left circle

if __name__ == "__main__":
    screen = turtle.Screen() #creating an object named screen from the class Screen
    turtle = turtle.Turtle() #creating an object called turtle from the class Turtle

    ask = input("Enter your name to get a drawing")

    if len(ask) < 7:
        emoticon(turtle, -100, 100)
    else:
        olympic(turtle)
