from turtle import Screen,Turtle
import time
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
screen=Screen()
screen.bgcolor("Black")
screen.setup(width=800,height=600)
screen.title("PONG GAME")
#tracer is use to enable/disable the animation 0=off
screen.tracer(0)
screen.listen()
ball=Ball()
scoreboard=Scoreboard()
left_paddle=Paddle((-360,0))
right_paddle=Paddle((360,0))


is_game_on=True
while is_game_on:
    time.sleep(ball.ball_speed)
    ball.move()
    #detect collision with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounceY()

    #check collision with  paddle
    if ball.distance(right_paddle)<50 or ball.xcor()>340 or ball.distance(left_paddle)<50 or ball.ycor()<-320:
        ball.bounceX()


    #if ball goes out of screen from Right side
    if ball.xcor()>400:
        ball.reset_positionX()
        time.sleep(0.5)
        scoreboard.l_scoreboard()
        print("out")

        # if ball goes out of screen from Left side
    if ball.xcor() < -400:
            ball.reset_positionY()
            time.sleep(0.5)
            scoreboard.r_scoreboard()
            print("out")
    #method used to keep update screen bcoz we used tracer method
    screen.update()
    screen.onkey(right_paddle.move_up,"Up")
    screen.onkey(right_paddle.move_down,"Down")
    screen.onkey(left_paddle.move_up,"w")
    screen.onkey(left_paddle.move_down,"s")





screen.exitonclick()