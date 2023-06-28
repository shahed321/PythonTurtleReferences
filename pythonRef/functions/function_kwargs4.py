import turtle

def draw_shapes(**kwargs):
    for shape, options in kwargs.items():
        if shape == "square":
            draw_square(**options)
        elif shape == "circle":
            draw_circle(**options)
        elif shape == "triangle":
            draw_triangle(**options)
        elif shape == "polygon":
            sides = options.get("sides", 5)
            draw_polygon(sides, **options)

def draw_square(size=100, color="black"):
    square_turtle = turtle.Turtle()
    square_turtle.color(color)
    for _ in range(4):
        square_turtle.forward(size)
        square_turtle.right(90)

def draw_circle(radius=50, color="black"):
    circle_turtle = turtle.Turtle()
    circle_turtle.color(color)
    circle_turtle.circle(radius)

def draw_triangle(size=100, color="black"):
    triangle_turtle = turtle.Turtle()
    triangle_turtle.color(color)
    for _ in range(3):
        triangle_turtle.forward(size)
        triangle_turtle.left(120)

def draw_polygon(sides=5, size=100, color="black"):
    polygon_turtle = turtle.Turtle()
    polygon_turtle.color(color)
    angle = 360 / sides
    for _ in range(sides):
        polygon_turtle.forward(size)
        polygon_turtle.right(angle)

# Create a turtle screen
screen = turtle.Screen()

# Call the draw_shapes function with keyword arguments
draw_shapes(square={"size": 150, "color": "red"},
            circle={"radius": 80, "color": "blue"},
            triangle={"size": 120, "color": "green"},
            polygon={"sides": 6, "size": 90, "color": "orange"})

# Close the turtle graphics window
turtle.done()
