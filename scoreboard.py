FONT = ("Courier", 24, "normal")
TITLE_POSITION=(-250,250)

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(TITLE_POSITION)
        self.write(arg= f'Level = 1',align='left',font=FONT)
        self.level=1

    def game_over_text(self):
        self.goto(0,0)
        self.write(arg='GAME OVER', align='center', font=FONT)

    def rewrite_level(self):
        self.level+=1

        self.clear()
        self.goto(TITLE_POSITION)
        self.write(arg=f'Level = {self.level}', align='left', font=FONT)
