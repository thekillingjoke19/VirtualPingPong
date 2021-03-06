from turtle import Screen,Turtle
from Paddle import Paddle
from Ball import Ball
from ScoreBoard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Let the game begin")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(r_paddle.go_up, "Up", )

screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")

screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detection with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()

    # detection with paddle misses
    if ball.xcor() > 380:
        ball.speed("fastest")

        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
