import turtle as t
import random

race_is_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

x = 0
for color in colors:
    new_turtles = t.Turtle(shape="turtle")
    new_turtles.penup()
    new_turtles.color(color)
    new_turtles.goto(x=-230, y=-100 + x)
    x += 40
    turtles.append(new_turtles)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in turtles:
        distance = random.randint(1, 10)
        direction_right = random.randint(1, 5)
        direction_left = random.randint(1, 5)
        turtle.forward(distance)
        turtle.right(direction_right)
        turtle.left(direction_left)
        if turtle.xcor() > 230:
            winner_color = turtle.pencolor()
            race_is_on = False
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winner_color} turtle is the winner!")


screen.exitonclick()