import turtle
import random
john = turtle.Turtle()
turtle.colormode(255)
colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown",
    "black", "white", "gray", "cyan", "magenta", "light blue", "dark blue",
    "light green", "dark green", "light gray", "dark gray", "gold", "silver",
    "violet", "indigo", "turquoise", "beige", "chocolate", "coral", "khaki",
    "lavender", "lime", "maroon", "navy", "olive", "plum", "salmon", "tan",
    "teal", "tomato", "wheat"
]

#Challenge 1: Draw a Square
# sides = 0
# while sides < 4:
#     john.forward(100)
#     john.right(90)
#     sides += 1


#challenge2: draw a dashed line
# for number in range(10):
#     john.forward(10)
#     john.penup()
#     john.forward(10)
#     john.pendown()

#challenge3: draw all polygons from 3side to 10 sided
# num = 0
# sides = 2
# for _ in range(10):
#     degree = 360
#     # john.forward(100)
#     sides += 1
#     degree = degree / sides
#     num=0

#     while num <= sides -1:
#         john.right(degree)
#         john.forward(100)
#         num += 1

#challenge4: draw a random walk
# john.speed("fastest")
# john.pensize(10)
# directions = [0,90,180,270]
# randomdirection = [john.right(90), john.left(90)]
# for _ in range(0, 10000):
#     john.setheading(random.choice(directions))
#     john.forward(10)
#     john.pencolor(random.choice(colors))
#     john.pensize(random.randint(1,10))
directions = [0,90,180,270]
# john.pensize(10)
# for _ in range(200):
num=0  
#     john.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#     john.forward(10)
#     john.setheading(random.choice(directions))
john.speed("fastest")
for _ in range(100):
    
    john.circle(100)
    john.forward(0)
    john.setheading(num)
    john.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    num +=5

screen = turtle.Screen()
screen.colormode(255)
screen.exitonclick()