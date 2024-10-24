import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle object
my_turtle = turtle.Turtle()

# Draw a square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

# Close the turtle graphics window when clicked
screen.exitonclick()
