from turtle import Screen, Turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch(frequency = 3, curve_size = 250):
    curve_amount = 4

    screen = Screen()
    screen.bgcolor("white")

    turtle = Turtle()
    turtle.speed(0)  
    turtle.penup()
    turtle.goto(-curve_size / 2, 0)
    turtle.pendown()

    for _ in range(curve_amount):
        koch_curve(turtle, frequency, curve_size)
        turtle.right(90)

    screen.mainloop()


if __name__ == "__main__":
    draw_koch()