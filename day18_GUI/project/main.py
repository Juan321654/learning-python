import colorgram
from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 30)
# for color in colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   new_color = (r,g,b)
#   rgb_colors.append(new_color)

# print(rgb_colors)
# the colors are just copied frpm the terminal, and now the code above can be commented out, as its not needed anymore
color_list = [(248, 248, 245), (240, 249, 245), (249, 238, 245), (235, 242, 249), (237, 224, 80), (205, 
4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177), (216, 134, 179), (8, 186, 216), (229, 167, 200), (210, 25, 148), (122, 190, 160), (7, 49, 26), (34, 136, 72), (63, 20, 7), (126, 219, 234), (190, 14, 4), (109, 87, 215), (140, 217, 202), (238, 64, 34), (71, 10, 28)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
  tim.dot(20, random.choice(color_list))
  tim.forward(50)

  if dot_count % 10 == 0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)




screen.exitonclick()