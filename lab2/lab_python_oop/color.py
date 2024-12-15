class ShapeColor:
    def __init__(self, color: str):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
