import turtle

def draw_circle(x,y):
    turtle.goto(x,y)
    turtle.circle(50)

# Create a turtle instance
my_turtle = turtle.Turtle()

# Register the event handler
turtle.onclick(draw_circle)  # Draw a circle on mouse click

turtle.mainloop()  # Run the turtle event loop
