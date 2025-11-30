#!/usr/bin/python3
import turtle
t=turtle.Turtle()
t.speed(0)
s=turtle.Screen()
s.bgcolor("black")
for i in range(360):
    t.color("yellow")
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.forward(350)
    t.backward(350)
    t.right(10)
turtle.done()