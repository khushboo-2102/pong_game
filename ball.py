# create the ball and make it move.

from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # reverse of increment function
        self.y_move *= -1                # 10 * -1 = -10  # subtract and ball moves in opposite direction(reverse back)

    def bounce_x(self):
        self.x_move *= -1          # bounce back horizontally
        self.move_speed *= 0.9     # 0.9 increases ball speed every time

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()
