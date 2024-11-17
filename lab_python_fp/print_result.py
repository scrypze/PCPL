from field import field
from gen_random import gen_random
from unique import Unique
from sort import data

def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__)
        if isinstance(result, list):
            for item in result:
                if isinstance(item, dict):
                    for key, value in item.items():
                        print(f"{key} = {value}")
                else:
                    print(item)
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            print(result)
        return result
    return wrapper

@print_result
def test_field():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    return list(field(goods, 'title', 'price'))

@print_result
def test_gen_random():
    return list(gen_random(5, 1, 3))

@print_result
def test_unique():
    data = [1, 1, 2, 2, 3, 3, 4, 4]
    return list(Unique(data))

@print_result
def test_sort():
    result_no_lambda = sorted(data, key=abs, reverse=True)
    return result_no_lambda

@print_result
def test_sort_with_lambda():
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    return result_with_lambda

if __name__ == "__main__":
    test_field()
    test_gen_random()
    test_unique()
    test_sort()
    test_sort_with_lambda()
