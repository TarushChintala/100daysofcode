from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.setpos(0,270)
        self.color("white")

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align= ALIGNMENT, font= FONT)

    def show_score(self):
        self.clear()
        self.write(f"Score = {self.score}", align= ALIGNMENT, font= FONT)


