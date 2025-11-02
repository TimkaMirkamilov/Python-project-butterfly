import turtle
import colorsys

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
t.width(2)
t.hideturtle()
turtle.tracer(20)

h = 0

for i in range(200):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)

    # Верхние крылья
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(90)
    t.circle(100 + i, 60)
    t.left(120)
    t.circle(100 + i, 60)

    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(90)
    t.circle(-(100 + i), 60)
    t.right(120)
    t.circle(-(100 + i), 60)

    # Нижние крылья (зеркально вниз)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(270)
    t.circle(100 + i, 60)
    t.right(120)
    t.circle(100 + i, 60)

    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(270)
    t.circle(-(100 + i), 60)
    t.left(120)
    t.circle(-(100 + i), 60)

    # Плавный переход цвета
    h += 0.008
    if h > 1:
        h -= 1

turtle.done()
