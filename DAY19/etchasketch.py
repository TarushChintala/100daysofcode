import turtle

pen = turtle.Turtle()

def move_forward():
    pen.forward(10)

def move_backward():
    pen.backward(10)

def turn_left():
    pen.left(10)

def turn_right():
    pen.right(10)

def clear():
    pen.home()
    pen.clear()


turtle.listen()

turtle.onkeypress(key="w",fun=move_forward)
turtle.onkeypress(key="s",fun=move_backward)
turtle.onkeypress(key="d",fun=turn_right)
turtle.onkeypress(key="a",fun=turn_left)
turtle.onkeypress(key="c",fun=clear)

turtle.exitonclick()

