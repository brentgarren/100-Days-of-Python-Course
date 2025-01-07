from turtle import Turtle, Screen
import colorgram 
import random

color_list = [
    (60, 57, 197), (12, 157, 128), (21, 122, 151), (160, 149, 62), (54, 80, 121),
    (177, 208, 230), (41, 84, 223), (39, 73, 194), (149, 220, 27), (243, 52, 206),
    (195, 147, 51), (26, 221, 236), (31, 30, 206), (92, 65, 189), (205, 130, 203),
    (59, 237, 143), (65, 241, 228), (227, 107, 28), (183, 110, 234), (50, 250, 194),
    (174, 254, 143), (0, 98, 46), (238, 226, 18), (113, 19, 151), (16, 210, 17),
    (255, 132, 193), (90, 71, 85), (244, 127, 84), (8, 77, 46), (92, 228, 216),
    (31, 189, 176), (89, 223, 87), (206, 153, 57), (149, 145, 187), (68, 230, 25),
    (28, 154, 139), (146, 41, 46), (4, 75, 5), (205, 21, 100), (115, 172, 209),
    (86, 198, 154), (190, 4, 26), (147, 177, 43), ]


hirst = Turtle()
hirst.speed("fastest")
hirst.penup()
hirst.hideturtle()
screen = Screen()
screen.colormode(255)

# rgb_colors = []
# colors = colorgram.extract('colors.jpg', 45)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.r
#     b = color.rgb.r
#     new_color = (r, g, b)
#     rgb_colors.append(new_color) 
# print(rgb_colors)


circles = 0
hirst.pensize(20)
for row in range(10):
    for column in range(10):
        hirst.dot(20, random.choice(color_list))
        hirst.forward(50)
    hirst.backward(500)
    hirst.right(90)
    hirst.forward(50)
    hirst.left(90)
    
screen.exitonclick()