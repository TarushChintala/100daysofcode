from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("Black")
screen.setup(800,600)
screen.tracer(0)



l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.move_up,"Up")
screen.onkeypress(r_paddle.move_down,"Down")
screen.onkeypress(l_paddle.move_up,"w")
screen.onkeypress(l_paddle.move_down,"s")


game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    #Detect Top/Bottom wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #Detect Paddle collision
    if ball.xcor() > 320 and r_paddle.distance(ball) < 50:
            ball.paddle_bounce()

    if ball.xcor() < -320 and l_paddle.distance(ball) < 50:
            ball.paddle_bounce()


    #Detect Miss
    if ball.xcor() > 390:
        score.l_point()
        ball.move_speed = 0.07
        ball.goto(0,0)
        ball.paddle_bounce()


    if ball.xcor() < -390:
        score.r_point()
        ball.move_speed = 0.07
        ball.goto(0, 0)
        ball.paddle_bounce()

    if score.r_score > 9 or score.l_score > 9:
        game = False

screen.exitonclick()