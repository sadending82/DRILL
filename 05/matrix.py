import turtle
import random

def forward_move():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def left_move():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def back_move():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def right_move():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()



turtle.shape('turtle')


turtle.onkey(forward_move,'w')
turtle.onkey(left_move, 'a')
turtle.onkey(back_move, 's')
turtle.onkey(right_move, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
