from turtle import Turtle
import time
pong1=[(-200, -20), (-200, 0), (-200,20)]
pad=[]
class Paddle:
    def __init__(self):
        for x in pong1:
            new_paddle=Turtle()
            new_paddle.color("white")
            new_paddle.penup()
            new_paddle.shape("square")
            new_paddle.goto(x)
            pad.append(new_paddle)
