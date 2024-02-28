#TODO
# 每次创建多辆车-create multiple cars: in car.py
# 多轮持续创建车-create multiple bunches: in main.py
# control the frequency: using for loop to create chances 概率
# The other classes we created were a single object of the Turtle class. The class we created was in fact a single Turtle Object.. But the CarManager wasn't just one single object, we created a list of Turtle Objects. If the CarManager was a single object but was duplicated many times around the screen, when we'd change the color it would change the color of every single duplication across the screen.But instead we created a list inside the CarManager of turtle objects so we could style, and control each completely by itself.

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self): ##不用inherit（继承对单体而言），因为要创建的多个单体object
        self.car_list = [] ## create multiple cars
        self.create_car()

        self.speed = STARTING_MOVE_DISTANCE ## launching speed, 储存在__init__中方便引用、更改


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
        ## todo to control the show-up frequency: add the chance！！
            car = Turtle('square')
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.goto(x=300, y=random.randint(-250,250)) ## turtle has empty space

            self.car_list.append(car)


    def move(self):
        for item in self.car_list:
            item.new_x = item.xcor() - self.speed
            item.goto(item.new_x, item.ycor())
        ## OR
            # item.backward(self.distance)

        ## OR
        # for num in range(0,len(self.car_list)):
        #     car_item = self.car_list[num]
        #     car_item.new_x = car_item.xcor() - self.distance
        #     car_item.goto(car_item.new_x, car_item.ycor())

    def speed_up(self):
        self.speed += MOVE_INCREMENT

        for item in self.car_list:
            item.speed = self.speed
            print(item.speed)

