import turtle

def draw_square(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

# Create a turtle instance
my_turtle = turtle.Turtle()

# Register the event handler
turtle.onclick(draw_square)  # Draw a square on mouse click

turtle.mainloop()  # Run the turtle event loop
