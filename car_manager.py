from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_SIZE_MULTIPLIER = [1, 2, 3]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# To keep cars on screen add to a list



class CarManager:


    def __init__(self):
        self.traffic = []




    def create_cars(self):
        chance = random.randint(1,5)
        if chance == 1:
            car = Turtle("square")
            car.penup()
            ran_xcor = random.randint(-280,280)
            ran_ycor = random.randint(-240, 260)
            car.shapesize(stretch_wid=1, stretch_len=random.choice(CAR_SIZE_MULTIPLIER))
            car.color(random.choice(COLORS))
            car.goto(300, ran_ycor)
            self.traffic.append(car)


    def create_traffic(self):
        cars = range(20)
        for i in cars:
            car = Turtle("square")
            car.penup()
            ran_xcor = random.randint(-280, 280)
            ran_ycor = random.randint(-240, 260)
            car.shapesize(stretch_wid=1, stretch_len=random.choice(CAR_SIZE_MULTIPLIER))
            car.color(random.choice(COLORS))
            car.goto(ran_xcor, ran_ycor)
            self.traffic.append(car)

    def move_cars(self):
        for car in self.traffic:
            car.backward(STARTING_MOVE_DISTANCE)

