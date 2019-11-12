import random
import turtle
import time

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

#The Dice
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


#Keyboard bindings
window.listen()
window.onkeypress(roll_d4, "4")
window.onkeypress(roll_d6, "6")
window.onkeypress(roll_d20, "0")
window.onkeypress(reset, "c")



#Generating the random dice rolls

def roll_d4():
    rand_d4 = random.randint(1, 4)
    time.sleep(2)
    return rand_d4

def roll_d6():
    rand_d6 = random.randint(1, 6)
    time.sleep(2)
    return rand_d4

def roll_d20():
    rand_d20 = random.randint(1, 20)
    time.sleep(2)
    return rand_d20

def reset():
    pen4.write("D4", align="center", font=("Verdana", 24, "normal"))
    pen6.write("D6", align="center", font=("Verdana", 24, "normal"))
    pen20.write("D20", align="center", font=("Verdana", 24, "normal"))






