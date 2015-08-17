__author__ = 'Ashish'
import turtle

def draw_square(some_turtle):

        some_turtle.forward(100)
        some_turtle.left(120)
        some_turtle.forward(100)
        some_turtle.left(120)
        some_turtle.forward(100)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    sq = turtle.Turtle()
    sq.speed(1000)

    for i in range(1,50):
        draw_square(sq)
        sq.right(10)

    window.exitonclick()

draw_art()

