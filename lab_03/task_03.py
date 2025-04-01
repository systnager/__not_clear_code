class Renderer:
    def render(self, shape):
        raise NotImplementedError


class VectorRenderer(Renderer):
    def render(self, shape):
        print(f"Drawing {shape.name} as vectors")


class RasterRenderer(Renderer):
    def render(self, shape):
        print(f"Drawing {shape.name} as pixels")


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer
        self.name = self.__class__.__name__

    def draw(self):
        self.renderer.render(self)


class Circle(Shape):
    pass


class Square(Shape):
    pass


class Triangle(Shape):
    pass


if __name__ == "__main__":
    triangle_vector = Triangle(VectorRenderer())
    square_raster = Square(RasterRenderer())
    circle_vector = Circle(VectorRenderer())
    triangle_vector.draw()
    square_raster.draw()
    circle_vector.draw()
