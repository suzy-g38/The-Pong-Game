from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed_increment = 0.1


    def make_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def make_bounce_y(self):
        self.y_move *= -1

    def make_bounce_x(self):
        self.x_move *= -1
        self.speed_increment *= 0.9


    def reset(self):
        self.goto(0,0)
        self.speed_increment = 0.1



