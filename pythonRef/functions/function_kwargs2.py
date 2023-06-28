import turtle

def draw_shapes(**kwargs):
    for shape, params in kwargs.items():
        if shape == "square":
            draw_square(**params)
        elif shape == "circle":
            draw_circle(**params)
        elif shape == "triangle":
            draw_triangle(**params)

def draw_square(color="black", size=100):
    square_turtle = turtle.Turtle()
    square_turtle.color(color)
    for _ in range(4):
        square_turtle.forward(size)
        square_turtle.right(90)

def draw_circle(color="black", radius=50):
    circle_turtle = turtle.Turtle()
    circle_turtle.color(color)
    circle_turtle.circle(radius)

def draw_triangle(color="black", size=100):
    triangle_turtle = turtle.Turtle()
    triangle_turtle.color(color)
    for _ in range(3):
        triangle_turtle.forward(size)
        triangle_turtle.left(120)

# Create a turtle screen
screen = turtle.Screen()

# Call the draw_shapes function with keyword arguments
draw_shapes(square={"color": "red", "size": 150},
            circle={"color": "blue", "radius": 80},
            triangle={"color": "green", "size": 120})

# Close the turtle graphics window
turtle.done()
