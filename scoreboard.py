from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))


    #increase r score if l_paddle is not hits the ball
    def r_scoreboard(self):
        self.r_score+=1
        self.update_scoreboard()

    # increase l score if l_paddle is not hits the ball
    def l_scoreboard(self):
        self.l_score+=1
        self.update_scoreboard()