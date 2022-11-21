from turtle import Turtle



FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-290, 260)
        self.display_score()


    def increase_level(self):
        self.level += 1
        self.display_score()


    def display_score(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align='left', font=FONT)


    def finish(self):
        game_over = Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.write("Game Over", move=False, align='center', font=FONT)