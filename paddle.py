from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        """Set paddle in proper place in window and set attributes/settings"""
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(coordinates)
        self.shapesize(5, 1)

    def go_up(self):
        """function to move paddle up on keystroke"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """function to move paddle up on keystroke"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
