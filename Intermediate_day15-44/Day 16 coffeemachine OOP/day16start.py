
# from turtle import Turtle, Screen


# tom = Turtle()
# print(tom)
# tom.shape("turtle")
# tom.color("blue")
# my_screen = Screen()
# num1 = 100
# num2 = 90
# while num1 > 1:
#     tom.forward(num1)
#     tom.left(num2)
#     tom.forward(num1)
#     num1 -= 1
# tom.color("red")
# while num1 < 500:
#     tom.forward(num1)
#     tom.right(num2)
#     num2 -= 1
#     num1 += 5

# my_screen.exitonclick()
from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name","Type"]
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.add_row(["Bulbasaur", "Grass"])
table.align = "l"
print(table)