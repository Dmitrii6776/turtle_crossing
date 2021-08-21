from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.new_game()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f'Level: {self.score}', font=FONT)

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)

    def new_game(self):
        self.clear()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(-250, 250)
        self.write(f'Level: {self.score}', font=FONT)
