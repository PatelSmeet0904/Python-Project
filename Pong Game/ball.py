from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xMove = 10
        self.yMove = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xMove
        new_y = self.ycor() + self.yMove
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.yMove *= -1

    def bounce_x(self):
        self.xMove *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
