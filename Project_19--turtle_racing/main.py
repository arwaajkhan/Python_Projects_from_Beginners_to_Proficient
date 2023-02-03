import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "yellow", "orange", "violet"]
turtle_list = []
is_race_on = False

b = -100
for c in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(c)
    new_turtle.goto(x=-230, y=b)
    b += 40
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_turtle = turtle.pencolor()
            if winner_turtle == user_bet:
                print(f"You've won the race! The {winner_turtle} is the winner.")
            else:
                print(f"You've lost the race! The {winner_turtle} is the winner.")
        turtle.forward(random.randint(0, 10))










screen.exitonclick()

# def move_forward():
#     t.forward(10)
#
#
# def move_backward():
#     t.backward(10)
#
#
# def counter_clockwise():
#     t.left(10)
#
#
# def clockwise():
#     t.right(10)
#
#
# def clear():
#     t.clear()
#     t.penup()
#     t.home()
#     t.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear)
