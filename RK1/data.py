from models import Part, Supplier, PartSupply

# Поставщики
suppliers = [
    Supplier(1, 'Алексей'),
    Supplier(2, 'Николай'),
    Supplier(3, 'Пётр'),
]

# Детали
parts = [
    Part(1, "Резистор", 1),
    Part(2, "Конденсатор", 2),
    Part(3, "Транзистор", 1),
    Part(4, "Диод", 3),
]

# Поставки деталей
part_supplies = [
    PartSupply(1, 1, 100),
    PartSupply(2, 1, 200),
    PartSupply(3, 2, 150),
    PartSupply(4, 3, 50),
    PartSupply(1, 3, 300),
]
