from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green", "red")
tim.speed("fastest")

screen = Screen()
screen.colormode(255)

for i in range(4):
  tim.forward(100)
  tim.right(90)

tim.right(180)

for i in range(10):
  tim.forward(5)
  tim.penup()
  tim.forward(5)
  tim.pendown()

def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  color = (r,g,b) # this is a tuple  kind of like an array [r,g, b] but its immutable
  return color

def shape(num_sides):
  angle = 360 / num_sides
  for i in range(num_sides):
    tim.forward(100)
    tim.right(angle)

for shape_num in range(3, 11):
  tim.color(random_color())
  shape(shape_num)

tim.pensize(10)
tim.forward(200)

turns = [0, 90, 180, 270]

for i in range(200):
  tim.color(random_color())
  tim.forward(30)
  tim.setheading(random.choice(turns))


# screen = Screen()
# screen.colormode(255)
screen.exitonclick()