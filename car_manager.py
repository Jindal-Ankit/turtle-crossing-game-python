from car import Car
import random


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance in (2,3):
            car = Car()
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move()

    def level_up(self):
        for car in self.cars:
            car.level_up()