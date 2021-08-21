import random
from turtle import Turtle
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.generate_car()

    def generate_car(self):
        random_chance = random.randint(1, 15)
        if random_chance == 1:
            car = Turtle()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.shape('square')
            car.penup()
            car.goto(350, random.randint(-250, 250))
            car.color(random.choice(COLORS))
            self.car_list.append(car)
            self.hideturtle()

    def car_move(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += 1
