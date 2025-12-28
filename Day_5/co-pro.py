# oop = object oriented programing
# for example waiter 
# In procedural programing
# has: is_holding_plate = True 
#      tables_responsible = [4,5,6]
# does: def take_order(table, order):
#             "takes order to chef"
#       def takes_payment(amount):
#             "add maoney to restaurant"
# In oop
# waiter = class
# betty,henry,bob = waiter = object
# has = attributes
# does = methods

# # import another_module
# # print(another_module.another_variable)

# # instead of this
# # import turtle
# # toto = turtle.Turtle()

# # we do this

from turtle import Turtle, Screen

toto = Turtle()
toto.shape("turtle")
toto.color("cadetblue")
toto.forward(100)
toto.left(90)
toto.forward(100)
toto.left(90)
toto.forward(100)
toto.left(90)
toto.forward(100)
my_screen = Screen()
my_screen.canvheight
my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()

# # table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# # table.add_row(["Adelaide", 1295, 1158259, 600.5])
# # table.add_row(["Brisbane", 5905, 1857594, 1146.4])
# # table.add_row(["Darwin", 112, 120900, 1714.7])
# # table.add_row(["Hobart", 1357, 205556, 619.5])
# # table.add_row(["Sydney", 2058, 4336374, 1214.8])
# # table.add_row(["Melbourne", 1566, 3806092, 646.9])
# # table.add_row(["Perth", 5386, 1554769, 869.4])

# table.add_column("pokemon name", ["chespin", "quilladin", "Froakie"])
# table.add_column("pokemon type", ["Grass", "Grass","Water"])
# table.align = "l"

# print(table)

















# solved these error using ctrl shift p and recomended python interpreter