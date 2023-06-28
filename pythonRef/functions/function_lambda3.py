import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle object
t = turtle.Turtle()

# Define a lambda function to draw a star with a given size
draw_star = lambda size: [t.forward(size), t.right(144),
                           t.forward(size), t.right(144),
                           t.forward(size), t.right(144),
                           t.forward(size), t.right(144),
                           t.forward(size), t.right(144)]

# Use the lambda function to draw a star with a size of 100 units
draw_star(100)

# Keep the turtle window open until it is manually closed
turtle.done()
