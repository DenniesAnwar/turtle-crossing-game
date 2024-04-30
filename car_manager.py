from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_SIZE_MULTIPLIER = [1, 3, 5]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):


    def __init__(self):
        super().__init__()

        self.shape("square")
        self.penup()
        self.create_cars()



    def create_cars(self):
        ran_cor = random.randint(-280,280)
        self.shapesize(stretch_wid=1, stretch_len=random.choice(CAR_SIZE_MULTIPLIER))
        self.color(random.choice(COLORS))
        self.goto(ran_cor, ran_cor)
        self.forward(STARTING_MOVE_DISTANCE)


    def create_traffic(self):
        self.create_cars()



