from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#LEVELS = [1, 2, 3, 4, 5, 6]

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.create_cars()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(x=330, y=random.randint(-250, 250))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move(self):
        for cars in self.all_cars:
            cars.forward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

