import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Welcome to Turtle Crossing Game!!')

car = CarManager()
scoreboard = Scoreboard()

player = Player()
screen.onkey(fun=player.move,key="space")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    for car_item in car.car_list:
        if player.distance(car_item) < 20:
        # if car_item.distance(player) < 20: -- 为什么报错TypeError: 'int' object is not callable？？？
            scoreboard.game_over_text()
            game_is_on = False
        elif player.finish() == 1:
            scoreboard.rewrite_level()
            car.speed_up()
            player.reset()
        else:
            pass


screen.exitonclick()