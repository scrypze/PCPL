from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Вычисление площади фигуры"""
        pass

    @classmethod
    @abstractmethod
    def name(cls):
        """Возврат названия фигуры"""
        pass
