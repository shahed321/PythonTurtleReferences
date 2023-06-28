import turtle

def repeat_until(condition, action):
    """Executes an action until the condition is met."""
    while not condition():
        action()

def move_forward():
    """Moves the turtle forward by a certain distance."""
    turtle.forward(100)

def turn_right():
    """Turns the turtle to the right by a certain angle."""
    turtle.right(90)

def is_at_edge():
    """Checks if the turtle is at the edge of the screen."""
    x, y = turtle.position()
    screen_width = turtle.window_width() / 2
    screen_height = turtle.window_height() / 2
    return abs(x) >= screen_width or abs(y) >= screen_height

# Example usage
repeat_until(is_at_edge, move_forward)

turtle.done()