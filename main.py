from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def controls():
    def move_forwards():
        tim.forward(10)

    def move_backwards():
        tim.backward(10)

    def move_clockwise():
        tim.rt(10)

    def move_counterclockwise():
        tim.lt(10)
    screen.onkey(key="w", fun=move_forwards)
    screen.onkey(key="s", fun=move_backwards)
    screen.onkey(key="a", fun=move_counterclockwise)
    screen.onkey(key="d", fun=move_clockwise)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
controls()
screen.onkey(key="c", fun=clear)

screen.exitonclick()
