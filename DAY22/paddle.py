from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(5, 1)
        self.up()
        self.goto(position)



    def move_up(self):
        if self.ycor() < 230:
            new_y = self.ycor() + 20
            self.setpos(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            self.setpos(self.xcor(), new_y)






