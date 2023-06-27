import turtle

# Create a turtle object
t = turtle.Turtle()

# Define the starting position of the turtle
start_x, start_y = 0, 0

# Define the function to be called on mouse release
def release_handler(x, y):
    global start_x, start_y
    t.penup()  # Lift the pen up
    t.goto(start_x, start_y)  # Go back to the starting position
    t.pendown()  # Put the pen down
    t.goto(x, y)  # Draw a line to the released position
    start_x, start_y = x, y  # Update the starting position

# Set up the turtle window
window = turtle.Screen()
window.title("Draw on Release Example")

# Bind the release event to the turtle
t.onrelease(release_handler)

# Start the turtle event loop
turtle.mainloop()
