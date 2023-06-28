import turtle

def repeat_with_delay(times, delay, action):
    """Executes an action a specified number of times with a delay between each execution."""
    for _ in range(times):
        action()
        turtle.delay(delay)

def move_forward():
    """Moves the turtle forward by a certain distance."""
    turtle.forward(100)

def turn_right():
    """Turns the turtle to the right by a certain angle."""
    turtle.right(90)

# Example usage
repeat_with_delay(4, 500, move_forward)
repeat_with_delay(4, 500, turn_right)

turtle.done()