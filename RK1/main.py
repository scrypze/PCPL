from services import task_1, task_2, task_3

def main():
    """Основная функция"""

    print('Задание Д1')
    res_1 = task_1()
    print(res_1)

    print('\nЗадание Д2')
    res_2 = task_2()
    print(res_2)

    print('\nЗадание Д3')
    res_3 = task_3()
    print(res_3)


if __name__ == '__main__':
    main()
