from turtle import Turtle, Screen
from pong import Score1, Score2, Middle
from paddle import Paddle

import time
screen=Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
s1=Score1()
s2=Score2()
mid=Middle()
paddle1=Paddle()
screen.update()



screen.exitonclick()