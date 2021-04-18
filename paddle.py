from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.showturtle()

    def move_up(self):
        new_ycor=self.ycor()+20
        self.goto(self.xcor(),new_ycor)


    def move_down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)


