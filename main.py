# Черепашья графика
import turtle


# N = 10
# turtle.speed(0)
# colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange']
#
# turtle.bgcolor('black')
# angle = 360 // len(colors) - 3 # -> 59 для 6 цветов
#
# for x in range(200):
#     turtle.pencolor(colors[x % len(colors)])
#     turtle.width(x // 100 + 1)
#     turtle.forward(x)
#     turtle.left(angle)


# for _ in range(N):
#     for _ in range(4):
#         turtle.forward(50)
#         turtle.left(360 // 4)
#     turtle.right(360 // N)
#
# turtle.penup()
# turtle.goto(70, 70)
# turtle.pendown()
#
# for _ in range(N):
#     turtle.circle(50)
#     turtle.right(360 // N)

def turtle_square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(360 // 4)


# turtle_square(90)

def turtle_flower(radius):
    for _ in range(radius + 1):
        turtle.circle(50)
        turtle.right(360 // radius)


# turtle_flower(12)

def turtle_tree(lenght):
    if lenght < 10:
        return
    turtle.forward(lenght)
    turtle.left(30)
    turtle_tree(lenght * 0.7)
    turtle.right(60)
    turtle_tree(lenght * 0.7)
    turtle.left(30)
    turtle.backward(lenght)


turtle.left(90)

turtle_tree(100)

turtle.mainloop()
