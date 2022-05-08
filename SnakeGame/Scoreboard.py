import turtle
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        with open("data.txt", "r") as file:
            self.highest_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} Highest Score: {self.highest_score}", align="center",
                   font=('Arial', '8', 'normal'))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align="center", font=('Arial', '15', 'normal'))

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score  = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_scoreboard(self):
        self.score += 1

        self.update_scoreboard()
