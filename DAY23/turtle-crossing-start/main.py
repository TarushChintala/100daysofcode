import time
from turtle import Screen
from player import Player, FINISH_LINE_Y, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()
game_ticker = 0

# MOVING THE PLAYER
screen.onkey(fun=player.move_up, key='w')

screen.listen()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    game_ticker += 1

    #GENERATING CARS
    if game_ticker % 6 == 0:
        car.create_car()
    car.move_cars()

    #CHECKING COLLISION WITH CAR
    for cars in car.car_list:
        if player.distance(cars) < 20:
            score.game_over()
            game_is_on = False

    if player.ycor() > FINISH_LINE_Y:
        player.setpos(STARTING_POSITION)
        car.speed_up()
        score.update_score()

screen.exitonclick()
