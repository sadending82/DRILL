import turtle

turtle.shape('turtle')

Posx = 0
Posy = 0
count = 5

while(count >= 0):
    turtle.penup()
    turtle.goto(Posx, Posy + (count * 100))
    turtle.pendown()
    turtle.goto(Posx + 500, Posy + (count * 100))
    count -= 1

count = 5

while(count >= 0):
    turtle.penup()
    turtle.goto(Posx + (count * 100), Posy + 500)
    turtle.pendown()
    turtle.goto(Posx + (count * 100), Posy)
    count -= 1


turtle.exitonclick()


