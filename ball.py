from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(1,1)
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.ball_speed=0.1



    def move(self):
        new_xcor=self.xcor()+self.x_move
        new_ycor=self.ycor()+self.y_move
        self.goto(new_xcor,new_ycor)

    #if ball hits the wall
    def bounceY(self):
        self.y_move*=-1

    def bounceX(self):
        self.x_move *= -1
        self.ball_speed*=0.9

    #reset ball position to centre
    def reset_positionX(self):
        self.goto(0,0)
        self.ball_speed=0.1
        self.bounceX()

    # reset ball position to centre
    def reset_positionY(self):
        self.goto(0, 0)
        self.bounceY()
