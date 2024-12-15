from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

import pandas as pd

if __name__ == "__main__":
    N = 14
    
    shape1 = Rectangle(N, N, "синий")
    shape2 = Circle(N, "зелёный")
    shape3 = Square(N, "красный")

    print(shape1)
    print(shape2)
    print(shape3)

    print()

    #Тут использовал внешнюю библиотеку
    data = pd.DataFrame({
    'Имя': ['Эрик', 'Илья', 'Гасан'],
    'Возраст': [18, 19, 19],
    'Город': ['Москва', 'Ульяновск', 'Махачкала']
})

    print(data)