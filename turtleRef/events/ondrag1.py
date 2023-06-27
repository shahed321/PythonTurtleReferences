import turtle

# Create a turtle object
t = turtle.Turtle()

# Define the function to move the turtle
def drag_handler(x, y):
    t.ondrag(None)  # Disable the event inside the event handler
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(drag_handler)  # Re-enable the event

# Set up the turtle window
window = turtle.Screen()
window.title("Drag Turtle Example")

# Bind the drag event to the turtle
t.ondrag(drag_handler)

# Start the turtle event loop
turtle.mainloop()
