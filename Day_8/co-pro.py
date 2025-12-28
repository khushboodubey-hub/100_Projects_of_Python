from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backward():
    tim.back(10)

def turn_left():
    # tim.left(10)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    # tim.right(10)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s",fun=move_backward)
screen.onkey(turn_left, "a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c") 

screen.exitonclick()



 
' '








