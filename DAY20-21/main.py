from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game = True

while game:
    screen.update()
    time.sleep(0.1)
    score.show_score()
    snake.move_snake()

#DETECT FOOD COLLISION
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend_snake()

#DETECT WALL COLLISION
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game = False
        score.game_over()

#DETECT SNAKE COLLISION
    for segment in snake.segment_list[1:]:
       if snake.head.distance(segment) < 10:
            game = False
            score.game_over()













screen.exitonclick()