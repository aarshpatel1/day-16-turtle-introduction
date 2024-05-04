# import another_module
# print(another_module.another_variable)

# import turtle
# my_turtle = turtle.Turtle()


# from turtle import Turtle, Screen
#
# my_turtle = Turtle()
# my_turtle.shape("turtle")
# my_turtle.color("purple")
# my_turtle.forward(100)
#
# print(my_turtle)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()  # making object named table

table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])  # use add_column method
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"  # changed value of align attribute

print(table)
