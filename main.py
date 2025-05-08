import time
from all_constants import *
from turtle import Screen
from car import Car

from car import Car
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen_size = SCREEN_SIZE
screen = Screen()
screen.setup(width=screen_size[0], height=SCREEN_SIZE[1])
screen.tracer(0)
screen.listen()

player = Player()
carmanager = CarManager()
score_board = ScoreBoard()

screen.onkey(player.move_up, "Up")

game_is_on = True



while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.move_cars()

    #detct collision turtle and car
    for car in carmanager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    # successful turtle crossing
    if player.is_at_finish_line():
        player.go_to_start()
        carmanager.level_up()
        score_board.increase_level()


screen.exitonclick()