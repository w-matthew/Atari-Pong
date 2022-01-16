from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        """Set ball placement and attributes/settings"""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.i_speed = 0.1

    def start_movement(self):
        """Sets the ball to go into the top right corner at the start of game"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def hit_wall(self):
        """Logic for when ball hits the top/bottom wall"""
        self.y_move *= -1

    def hit_paddle(self):
        """Logic for when ball hits players paddles"""
        self.x_move *= -1
        self.i_speed *= 0.87

    def reset_ball(self):
        """Reset the ball into center of screen for new point"""
        self.goto(0, 0)
        self.hit_paddle()
        self.i_speed = 0.1
