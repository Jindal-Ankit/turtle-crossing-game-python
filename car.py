from turtle import Turtle
import random
from all_constants import *


COLOURS = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple"]
STARTING_MOVEMENT_SPEED = 5
right_screen_size = SCREEN_SIZE[0]/2


CAR_GENERATION_RANGE_X = (0 + right_screen_size/2, right_screen_size - 20)
CAR_GENERATION_RANGE_Y = ( -1 * (SCREEN_SIZE[1]/2 - 80), (SCREEN_SIZE[1] /2- 80))
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLOURS))
        self.penup()
        self.setheading(180)
        self.starting_position()
        self.speed = STARTING_MOVEMENT_SPEED
        print(CAR_GENERATION_RANGE_X, CAR_GENERATION_RANGE_Y)

    def starting_position(self):
        starting_position_x = random.randint(int(CAR_GENERATION_RANGE_X[0]),int(CAR_GENERATION_RANGE_X[1]))
        starting_position_y = random.randint(int(CAR_GENERATION_RANGE_Y[0]),int(CAR_GENERATION_RANGE_Y[1]))
        self.goto(starting_position_x, starting_position_y)


    def move(self):
        self.forward(10)

    def level_up(self):
        self.speed += STARTING_MOVEMENT_SPEED

    def is_crossed_screen(self):
        if self.xcor() <= -1 * right_screen_size:
            return True
        else:
            return False