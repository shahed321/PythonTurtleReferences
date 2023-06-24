import turtle

def move_forward(x, y):
    turtle.forward(100)

def turn_left():
    turtle.left(90)

def turn_right():
    turtle.right(90)

# Create a turtle instance
my_turtle = turtle.Turtle()

# Register event handlers
turtle.onscreenclick(move_forward)  # Move turtle forward on click
turtle.onkey(turn_left, 'Left')     # Turn turtle left when 'Left' key is pressed
turtle.onkey(turn_right, 'Right')   # Turn turtle right when 'Right' key is pressed

turtle.listen()  # Start listening to events
turtle.mainloop()  # Run the turtle event loop
