import turtle

def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order - 1, size / 3)
            turtle.left(angle)

def draw_koch_snowflake(order, size):
    screen = turtle.Screen()
    screen.bgcolor("white")

    fractal_turtle = turtle.Turtle()
    fractal_turtle.speed(1)  # Adjust the speed as needed

    for _ in range(3):
        koch_snowflake(fractal_turtle, order, size)
        fractal_turtle.right(120)

    screen.exitonclick()

# Set the order and size of the Koch snowflake
order = 3
size = 300

# Draw the Koch snowflake
draw_koch_snowflake(order, size)
