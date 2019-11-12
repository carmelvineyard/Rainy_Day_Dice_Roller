import random
import turtle

window = turtle.Screen()
window.bgcolor("maroon")
window.setup(width=800, height=600)
window.tracer(0)
window.title("Rainy Day Dice Roller")

#Objects to go in the window

#writing
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("silver")
pen.penup()
pen.hideturtle()
pen.goto(0, 280)
pen.write("Click a die to roll", align="center", font=("Verdana", 24, "normal"))

#Label_4
pen4 = turtle.Turtle()
pen4.speed(0)
pen4.shape("square")
pen4.color("maroon")
pen4.penup()
pen4.hideturtle()
pen4.goto(-200, 0)
pen4.write("D4", align="center", font=("Verdana", 24, "normal"))

#Label_6
pen6 = turtle.Turtle()
pen6.speed(0)
pen6.shape("square")
pen6.color("maroon")
pen6.penup()
pen6.hideturtle()
pen6.goto(0, 0)
pen6.write("D6", align="center", font=("Verdana", 24, "normal"))

#Label_20
pen20 = turtle.Turtle()
pen20.speed(0)
pen20.shape("square")
pen20.color("maroon")
pen20.penup()
pen20.hideturtle()
pen20.goto(200, 0)
pen20.write("D20", align="center", font=("Verdana", 24, "normal"))


#D4
d4 = turtle.Turtle()
d4.speed(0)
d4.shape("triangle")
d4.color("white")
d4.shapesize(stretch_wid=2,stretch_len=2)
d4.penup()
d4.goto(-200, 0)


#D6
d6 = turtle.Turtle()
d6.speed(0)
d6.shape("square")
d6.color("white")
d6.shapesize(stretch_wid=2,stretch_len=2)
d6.penup()
d6.goto(0, 0)


#D20
d20 = turtle.Turtle()
d20.speed(0)
d20.shape("circle")
d20.color("white")
d20.shapesize(stretch_wid=2,stretch_len=2)
d20.penup()
d20.goto(200, 0)
