from turtle import Turtle

FONT_1 = ("Courier", 14, "normal")
FONT_2 = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.update_sccoreboard()

    def update_sccoreboard(self):
        self.write(f"level: {self.level}", move = False, align = "left", font = FONT_1 )
        
    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_sccoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move = False, align = "center", font = FONT_2 )