from turtle import Turtle
from all_constants import *

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.go_to_start()


    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def is_at_finish_line(self):
        y_cor = self.ycor()
        if y_cor >= 280:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(0, -1 * (SCREEN_SIZE[1]/2 - 20))