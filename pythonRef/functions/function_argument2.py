import turtle

def draw_square(turt, size=100):
    for _ in range(4):
        turt.forward(size)
        turt.right(90)

# Create a turtle object
my_turtle = turtle.Turtle()

# Set the speed of the turtle
my_turtle.speed(1)

# Call the draw_square function with the turtle object and default size
draw_square(my_turtle)  # Using the default size of 100

# Call the draw_square function with the turtle object and a custom size
draw_square(my_turtle, 200)  # Using a custom size of 200

# Close the turtle graphics window
turtle.done()
