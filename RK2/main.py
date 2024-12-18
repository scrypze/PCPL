from models import Part, Supplier, PartSupply
from services import PartService

def create_test_data():
    """Создание тестовых данных"""
    suppliers = [
        Supplier(1, 'Алексей'),
        Supplier(2, 'Николай'),
        Supplier(3, 'Пётр'),
    ]

    parts = [
        Part(1, "Резистор", 1),
        Part(2, "Конденсатор", 2),
        Part(3, "Транзистор", 1),
        Part(4, "Диод", 3),
    ]

    part_supplies = [
        PartSupply(1, 1, 100),
        PartSupply(2, 1, 200),
        PartSupply(3, 2, 150),
        PartSupply(4, 3, 50),
        PartSupply(1, 3, 300),
    ]

    return parts, suppliers, part_supplies

def main():
    """Основная функция"""
    parts, suppliers, part_supplies = create_test_data()
    service = PartService(parts, suppliers, part_supplies)

    print('Задание Д1')
    res_1 = service.find_parts_ending_with_or()
    print(res_1)

    print('\nЗадание Д2')
    res_2 = service.get_suppliers_avg_supply()
    print(res_2)

    print('\nЗадание Д3')
    res_3 = service.get_suppliers_starting_with_p()
    print(res_3)

if __name__ == '__main__':
    main()
