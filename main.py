import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize player & Initialized star sequence
player = Player()
traffic = CarManager()
traffic.create_traffic()
# Game mechanics
screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    traffic.create_cars()
    traffic.move_cars()



screen.exitonclick()
