import turtle

def draw_shapes(*args):
    for shape in args:
        if shape == "square":
            draw_square()
        elif shape == "circle":
            draw_circle()
        elif shape == "triangle":
            draw_triangle()

def draw_square():
    square_turtle = turtle.Turtle()
    for _ in range(4):
        square_turtle.forward(100)
        square_turtle.right(90)

def draw_circle():
    circle_turtle = turtle.Turtle()
    circle_turtle.circle(50)

def draw_triangle():
    triangle_turtle = turtle.Turtle()
    for _ in range(3):
        triangle_turtle.forward(100)
        triangle_turtle.left(120)

# Create a turtle screen
screen = turtle.Screen()

# Call the draw_shapes function with variable-length arguments
draw_shapes("square", "circle", "triangle")

# Close the turtle graphics window
turtle.done()
