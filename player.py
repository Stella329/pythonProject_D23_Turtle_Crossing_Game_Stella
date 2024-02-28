STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.shape('turtle')
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)

    def finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            return 1




