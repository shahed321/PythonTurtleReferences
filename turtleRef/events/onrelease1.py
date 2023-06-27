import turtle

# Create a turtle object
t = turtle.Turtle()

# Define the function to be called on mouse release
def release_handler(x, y):
    t.color("red")

# Set up the turtle window
window = turtle.Screen()
window.title("Mouse Release Example")

# Bind the release event to the turtle
t.onrelease(release_handler)

# Start the turtle event loop
turtle.mainloop()
