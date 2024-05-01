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
scoreboard = Scoreboard()
# Game mechanics
screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    traffic.create_cars()
    traffic.move_cars(scoreboard.level)

    for car in traffic.traffic:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() == 260:
        scoreboard.increase_level()
        player.reset()
        traffic.num_chance -= 1
        scoreboard.update_level()
        traffic.create_traffic()




screen.exitonclick()
