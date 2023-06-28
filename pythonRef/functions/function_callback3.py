import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle object
t = turtle.Turtle()

# Define a callback function that changes the turtle's color
def change_color():
    current_color = t.pencolor()
    if current_color == "red":
        t.pencolor("blue")
    else:
        t.pencolor("red")

# Define a separate function to handle the key event and call the callback function
def on_space():
    change_color()

# Register the callback function with the turtle screen
screen.onkey(on_space, "space")

# Enable listening for key events
screen.listen()

# Keep the turtle window open until it is manually closed
turtle.done()
