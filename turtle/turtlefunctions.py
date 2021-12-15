
def jump(turtle, x:float, y:float) -> None:
    '''makes Turtle object (turtle) jump to coordinates (x, y)'''
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

if __name__ == "__main__":
    print("Why run this? It's kinda a boring Module.")
