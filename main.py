from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=700, height=400)
user_bet = screen.textinput(title="Enter your bet",
                            prompt="Which turtle will win the race? Enter a color ['red', 'cyan', 'magenta', 'green', 'blue', 'purple']: ")
colors = ["red", "cyan", "magenta", "green", "blue", "purple"]
y_positions = [-80, -40, 0, 40, 80, 120]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-330, y=y_positions[i])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 330:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
