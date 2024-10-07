from turtle import Turtle

STARTING_POSITIONS = [(0,0) , (-20,0) , (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        segment = Turtle("square")
        segment.color("white")
        segment.up()
        segment.setpos(position)
        self.segment_list.append(segment)

    def extend_snake(self):
        self.add_segment(self.segment_list[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.segment_list) - 1, 0, -1):
            x_coord = self.segment_list[seg_num - 1].xcor()
            y_coord = self.segment_list[seg_num - 1].ycor()
            self.segment_list[seg_num].goto(x_coord, y_coord)
        self.segment_list[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)