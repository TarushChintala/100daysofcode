from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.up()
        self.setpos(-280,260)
        self.color("black")
        self.write(font= FONT,arg= f"Score = {self.score}")

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(font=FONT, arg=f"Score = {self.score}")

    def game_over(self):
        self.setpos(0,0)
        self.write(font= FONT, arg="GAME OVER",align='center')