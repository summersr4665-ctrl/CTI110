# Rashaad Summers
# 04/05/2026
# P4LAB1
# The program uses turtle graphics that draws a triangle and a square using loops.

import turtle

# ----- Setup screen -----
screen = turtle.Screen()
screen.bgcolor("lightblue")   # Background color

# ----- Create turtle -----
t = turtle.Turtle()
t.color("black")
t.pensize(3)

# ----- Move turtle to starting position -----
t.penup()
t.goto(-50, -50)
t.pendown()

# =========================
# Draw Square (using FOR loop)
# =========================
for side in range(4):
    t.forward(100)
    t.left(90)

# =========================
# Move to top of square
# =========================
t.penup()
t.goto(-50, 50)
t.pendown()

# =========================
# Draw Triangle (using WHILE loop)
# =========================
count = 0

while count < 3:
    t.forward(100)
    t.left(120)
    count += 1

# ----- Finish -----
t.hideturtle()
turtle.done()