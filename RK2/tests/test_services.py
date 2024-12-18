import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import Part, Supplier, PartSupply
from services import PartService

class TestPartService(unittest.TestCase):
    def setUp(self):
        self.suppliers = [
            Supplier(1, 'Алексей'),
            Supplier(2, 'Николай'),
            Supplier(3, 'Пётр'),
        ]
        
        self.parts = [
            Part(1, "Резистор", 1),
            Part(2, "Диод", 2),
            Part(3, "Транзистор", 1),
            Part(4, "Микрочип", 3),
        ]
        
        self.part_supplies = [
            PartSupply(1, 1, 100),
            PartSupply(2, 1, 200),
            PartSupply(3, 2, 150),
            PartSupply(4, 3, 50),
        ]
        
        self.service = PartService(self.parts, self.suppliers, self.part_supplies)

    def test_find_parts_ending_with_or(self):
        """Тест поиска деталей, заканчивающихся на 'ор'"""
        result = self.service.find_parts_ending_with_or()
        expected = [
            ("Резистор", "Алексей"),
            ("Транзистор", "Алексей")
        ]
        self.assertEqual(result, expected)

    def test_get_suppliers_avg_supply(self):
        """Тест расчета средней поставки деталей"""
        result = self.service.get_suppliers_avg_supply()
        expected = [
            ("Алексей", 150),
            ("Николай", 150),
            ("Пётр", 50)
        ]
        self.assertEqual(result, expected)

    def test_get_suppliers_starting_with_p(self):
        """Тест поиска поставщиков, начинающихся на 'П'"""
        result = self.service.get_suppliers_starting_with_p()
        expected = {
            "Пётр": ["Микрочип"]
        }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
