from turtle import Turtle
STYLE = ("Courier", 40)


class Scoreboard(Turtle):
    def __init__(self):
        """Sets the scoreboard attributes/settings and initializes values used
        other functions"""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.winner = ""
        self.write_board()

    def add_l_point(self):
        """Adds a point for the left player if ball ends up crossing right side"""
        self.l_score += 1
        self.write_board()

    def add_r_point(self):
        """Adds a point for the right player if ball ends up crossing left side"""
        self.r_score += 1
        self.write_board()

    def write_board(self):
        """Sets the numbers for scoreboard. Places text in top with middle alignment"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=STYLE)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=STYLE)

    def end_game(self):
        """Text for ending game. Deals with which side won"""
        self.goto(0, 0)
        self.write(f"Player {self.winner} Wins!", align="center", font=STYLE)
