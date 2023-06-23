import turtle

class Class2:
    def __init__(self):
        self.window = turtle.Screen()
        self.pen = turtle.Turtle()

    def draw_square(self, size):
        for _ in range(4):
            self.pen.forward(size)
            self.pen.right(90)

    def draw_circle(self, radius):
        self.pen.circle(radius)

    def draw_triangle(self, size):
        for _ in range(3):
            self.pen.forward(size)
            self.pen.left(120)

    def close_window(self):
        self.window.bye()

# Example usage
drawing = Class2()
drawing.draw_square(100)
drawing.draw_circle(50)
drawing.draw_triangle(120)
## drawing.close_window()

turtle.done()
