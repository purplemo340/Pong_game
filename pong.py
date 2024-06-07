from turtle import Turtle
class Score1(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.change()

    def change(self):
        self.reset()
        self.color("white")
        self.penup()
        self.goto(x=-100, y=200)
        self.write(self.score1)
class Score2(Turtle):
    def __init__(self):
        super().__init__()
        self.score2 = 0
        self.change()

    def change(self):
        self.reset()
        self.color("white")
        self.penup()
        self.goto(x=100, y=200)
        self.write(self.score2)

class Middle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=300)
        self.pendown()
        while self.ycor() != -300:
            self.penup()
            self.goto(x=0, y=self.ycor()-10)
            self.pendown()
            self.goto(x=0, y=self.ycor() - 10)
