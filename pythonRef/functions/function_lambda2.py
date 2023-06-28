import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle object
t = turtle.Turtle()

# Define a lambda function to change the turtle's color
change_color = lambda color: t.pencolor(color)

# Use the lambda function to change the turtle's color to red
change_color("red")

# Define a lambda function to draw a square with a given side length
draw_square = lambda side_length: [t.forward(side_length), t.right(90),
                                   t.forward(side_length), t.right(90),
                                   t.forward(side_length), t.right(90),
                                   t.forward(side_length)]

# Use the lambda function to draw a square with a side length of 100 units
draw_square(100)

# Keep the turtle window open until it is manually closed
turtle.done()
