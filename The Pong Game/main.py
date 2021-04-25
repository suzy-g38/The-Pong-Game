from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

ball = Ball()
scoreboard = Scoreboard()
scoreboard.middle_line()

screen.listen()
screen.onkey(left_paddle.move_up, "Up")
screen.onkey(left_paddle.move_down, "Down")
screen.onkey(right_paddle.move_up, "w")
screen.onkey(right_paddle.move_down, "s")



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.speed_increment)

    #Detect collision with wall
    ball.make_move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.make_bounce_y()

    #Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.make_bounce_x()


    #Detect Left Paddle miss
    if ball.xcor() < -380:
        ball.reset()
        ball.make_bounce_x()
        scoreboard.update_right_scoreboard()

    # Detect Right Paddle miss
    if ball.xcor() > 380:
        ball.reset()
        ball.make_bounce_x()
        scoreboard.update_left_scoreboard()


screen.exitonclick()