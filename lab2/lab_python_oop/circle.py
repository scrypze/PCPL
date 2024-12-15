import math
from lab_python_oop.shape import Shape
from lab_python_oop.color import ShapeColor

class Circle(Shape):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = ShapeColor(color)

    def area(self):
        return math.pi * self.radius ** 2

    @classmethod
    def name(cls):
        return "Круг"

    def __repr__(self):
        return "Фигура: {}, Цвет: {}, Радиус: {}, Площадь: {}".format(
            self.name(), self.color.color, self.radius, self.area()
        )
