from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars_list = []



    def move_car(self, score):
        for car in self.cars_list:
            car.forward(STARTING_MOVE_DISTANCE+MOVE_INCREMENT * (score - 1))

    def increase_car_speed(self, score):
        for car in self.cars_list:
            car.forward(MOVE_INCREMENT * score)

    def generate_car(self):
            chance = random.randint(1,6)
            if chance == 1:
                car = Turtle("square")
                car.shapesize(stretch_wid=1,stretch_len=2)
                car.penup()
                car.color(random.choice(COLORS))
                car.setheading(180)
                car.goto(300, random.randint(-250,250))
                self.cars_list.append(car)


    def check_collision(self, turtle):
        for car in self.cars_list:
            if car.distance(turtle) <= 35:
                return True
        return False