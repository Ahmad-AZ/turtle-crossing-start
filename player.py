from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 30
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.shape('turtle')
        self.setheading(90)
        self.goto(STARTING_POSITION[0], STARTING_POSITION[1])



    def move_forward(self):
        self.forward(MOVE_DISTANCE)


    def update_position(self):
        self.goto(STARTING_POSITION)