import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle object
t = turtle.Turtle()

# Define a callback function that moves the turtle forward by a given distance
def move_forward(distance):
    t.forward(distance)

# Define a separate function to handle the key event and call the callback function
def on_up_arrow():
    move_forward(100)

# Register the callback function with the turtle screen
screen.onkey(on_up_arrow, "Up")

# Enable listening for key events
screen.listen()

# Keep the turtle window open until it is manually closed
turtle.done()
