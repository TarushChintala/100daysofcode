from turtle import Turtle, Screen
from random import randint

screen = Screen()

screen.setup(500,400)

turtle_list = []
colors = ["red", "blue", "green", "yellow", "orange", "violet"]
game = True


for i in range(0,6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.up()
    turtle.setpos(x= -230, y= -125 + i * 50)
    turtle_list.append(turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle are you betting on? Enter your colour: ").lower()

if user_bet:
    while game:
            for i in turtle_list:
                if i.xcor() > 230:
                    winner = i
                    game = False
                    if user_bet == winner.pencolor():
                        print(f"You Win! {winner.pencolor()} came first")
                    else:
                        print(f"You Lose! {winner.pencolor()} came first")
                else:
                    i.forward(randint(0, 10))



screen.exitonclick()