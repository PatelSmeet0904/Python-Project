from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong Game")
screen.tracer(0)

middle_line = Turtle()
middle_line.color("white")
middle_line.hideturtle()
middle_line.pensize(5)
middle_line.penup()
middle_line.right(90)
middle_line.goto(0, 300)

while middle_line.ycor() > -300:
    middle_line.pendown()
    middle_line.forward(20)
    middle_line.penup()
    middle_line.forward(20)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True

while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # score.draw_middle_line()

    # collision with up and down wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # r_paddle miss the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # l_paddle miss the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
