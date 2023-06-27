import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Begin recording the turtle's movements
my_turtle.begin_poly()

# Move the turtle to create the shape
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.right(45)
my_turtle.forward(75)

# End recording the turtle's movements
my_turtle.end_poly()

# Get the generated shape as a polygon object
custom_shape = my_turtle.get_poly()

# Print the custom shape
print(custom_shape)

turtle.mainloop()
