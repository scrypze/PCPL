from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, lenthSide, color):
        super().__init__(lenthSide, lenthSide, color)

    @classmethod
    def name(cls):
        return "Квадрат"

    def __repr__(self):
        return "Фигура: {}, Цвет: {}, Сторона: {}, Площадь: {}".format(
            self.name(), self.color.color, self.width, self.area()
        )
