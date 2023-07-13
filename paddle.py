from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()           # initialise super class.
        # Create and move a Paddle
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # width = 20 and height = 100, turtle is 20*20
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)  # xcor() position do not going to change.

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
