from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align="center", font=("courier", 40, "normal"))
        self.goto(100, 240)
        self.write(self.r_score, align="center", font=("courier", 40, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    # def draw_middle_line(self):
    #     self.goto(0, 300)
        # if self.ycor() < -300:
        #     self.pendown()
        #     self.forward(50)
        #     self.penup()

