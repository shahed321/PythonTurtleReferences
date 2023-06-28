import turtle

def draw_square(turt, size):
    for _ in range(4):
        turt.forward(size)
        turt.right(90)

# Create a turtle object
my_turtle = turtle.Turtle()

# Set the speed of the turtle
my_turtle.speed(1)

# Call the draw_square function with the turtle object and size argument
draw_square(my_turtle, 100)

# Close the turtle graphics window
turtle.done()
