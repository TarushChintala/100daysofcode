from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.speed = STARTING_MOVE_DISTANCE
        self.create_car()


    def create_car(self):
        car = Turtle('square')
        car.shapesize(1, 2)
        car.setheading(180)
        car.up()
        car.color(choice(COLORS))
        car.setpos(x=320, y=randint(-230, 230))
        self.car_list.append(car)


    def move_cars(self):
        for cars in range(0,len(self.car_list)):
            self.car_list[cars].forward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
