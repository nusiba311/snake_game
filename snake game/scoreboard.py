from turtle import Turtle
with open("high_score_data.txt") as file:
    contents = file.read()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(contents)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}',
        align="center", font=('Courier', 16, 'normal'))

    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("high_score_data.txt","w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


