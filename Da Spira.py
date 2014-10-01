from turtle import Turtle
from random import random


#What I am porting from code.org


muddy = Turtle()
muddy.pensize(7)


def random_color():
    return(random(),random(),random())


while True:
    for count in range(4):
        muddy.pencolor(random_color())
        muddy.forward(100)
        muddy.right(90)        
    muddy.right(10) 
    muddy.pencolor(random_color())
        muddy.forward(100)
        muddy.right(90)        
    muddy.right(10)


while True: random_color() 

