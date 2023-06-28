import turtle

def draw_shapes(**kwargs):
    for shape, color in kwargs.items():
        if shape == "square":
            draw_square(color=color)
        elif shape == "circle":
            draw_circle(color=color)
        elif shape == "triangle":
            draw_triangle(color=color)

def draw_square(color):
    square_turtle = turtle.Turtle()
    square_turtle.color(color)
    for _ in range(4):
        square_turtle.forward(100)
        square_turtle.right(90)

def draw_circle(color):
    circle_turtle = turtle.Turtle()
    circle_turtle.color(color)
    circle_turtle.circle(50)

def draw_triangle(color):
    triangle_turtle = turtle.Turtle()
    triangle_turtle.color(color)
    for _ in range(3):
        triangle_turtle.forward(100)
        triangle_turtle.left(120)

# Create a turtle screen
screen = turtle.Screen()

# Call the draw_shapes function with keyword arguments
draw_shapes(square="red", circle="blue", triangle="green")

# Close the turtle graphics window
turtle.done()
