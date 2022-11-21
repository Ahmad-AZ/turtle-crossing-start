import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()
score = Scoreboard()
cars = CarManager()
screen.onkey(player.move_forward, "Up")






game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()


    # Detet crossing the street
    if player.ycor() > 280:
        player.update_position()
        score.increase_level()
    # Detect collision
    if cars.check_collision(player):
        score.finish()
        game_is_on = False


    cars.generate_car()
    cars.move_car(score.level)




screen.exitonclick()