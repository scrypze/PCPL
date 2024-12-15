from lab_python_oop.shape import Shape
from lab_python_oop.color import ShapeColor

class Rectangle(Shape):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = ShapeColor(color)

    def area(self):
        return self.width * self.height

    @classmethod
    def name(cls):
        return "Прямоугольник"

    def __repr__(self):
        return "Фигура: {}, Цвет: {}, Ширина: {}, Высота: {}, Площадь: {}".format(
            self.name(), self.color.color, self.width, self.height, self.area()
        )
