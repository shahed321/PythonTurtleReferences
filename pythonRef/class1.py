import turtle

class Class1:
    def __init__(self):
        self.pen = turtle.Turtle()

    def draw_square(self, size):
        for _ in range(4):
            self.pen.forward(size)
            self.pen.right(90)

# Example usage
drawing = Class1()
drawing.draw_square(100)

turtle.done()
