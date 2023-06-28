import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle object
t = turtle.Turtle()

# Define a lambda function to move the turtle forward by a given distance
move_forward = lambda distance: t.forward(distance)

# Use the lambda function to move the turtle forward by 100 units
move_forward(100)

# Keep the turtle window open until it is manually closed
turtle.done()
