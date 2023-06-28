import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle object
t = turtle.Turtle()

# Define a callback function that moves the turtle forward by a given distance
def move_forward(distance):
    t.forward(distance)

# Register the callback function with the turtle screen
screen.onkey(lambda: move_forward(100), "Up")

# Enable listening for key events
screen.listen()

# Keep the turtle window open until it is manually closed
turtle.done()
