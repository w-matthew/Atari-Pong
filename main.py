# import turtle & time library and classes
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# initialize screen and settings
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong 1972")
screen.tracer(0)
# initialize both paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
# get key presses for both players(1: 'w' & 's' | 2: 'Up Arrow' & 'Down Arrow')
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    # var sets the speed of the ball
    time.sleep(ball.i_speed)
    # start of the game
    screen.update()
    ball.start_movement()
    # detect if it hits top/bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.hit_wall()
    # detect if it hits paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.hit_paddle()
    # for right paddle miss
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.add_l_point()
        # set if left side player wins
        if scoreboard.l_score > 9:
            game_is_on = False
            scoreboard.winner = "L"
    # for left paddle miss
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.add_r_point()
        # set if right side player wins
        if scoreboard.r_score > 9:
            game_is_on = False
            scoreboard.winner = "R"
# print winner
scoreboard.end_game()
# exit program
screen.exitonclick()
