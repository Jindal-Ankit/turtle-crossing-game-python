from turtle import Turtle
from all_constants import *

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-1 * (SCREEN_SIZE[0]/2-50),  SCREEN_SIZE[1]/2- 50)
        self.level = 0
        self.refresh_score()

    def increase_level(self):
        self.level += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Arial", 24, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
