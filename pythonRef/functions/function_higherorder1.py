import turtle

def repeat(times, action):
    """Executes an action a specified number of times."""
    for _ in range(times):
        action()

def square():
    """Draws a square using the turtle module."""
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

# Example usage
repeat(3, square)

turtle.done()