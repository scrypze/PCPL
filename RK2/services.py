from typing import List, Dict, Tuple
from operator import itemgetter

from models import Part, Supplier, PartSupply

class PartService:
    def __init__(self, parts: List[Part], suppliers: List[Supplier], part_supplies: List[PartSupply]):
        self.parts = parts
        self.suppliers = suppliers
        self.part_supplies = part_supplies

    def find_parts_ending_with_or(self) -> List[Tuple[str, str]]:
        """Список всех деталей, у которых название заканчивается на 'ор', и имена поставщиков"""
        result = []
        for p in self.parts:
            if p.name.endswith('ор'):
                for s in self.suppliers:
                    if p.supplier_id == s.supplier_id:
                        result.append((p.name, s.name))
        return result

    def get_suppliers_avg_supply(self) -> List[Tuple[str, float]]:
        """Список поставщиков со средней поставкой деталей, отсортированный по средней поставке"""
        result = []
        for s in self.suppliers:
            supplies = [ps for ps in self.part_supplies if ps.supplier_id == s.supplier_id]
            if supplies:
                total_quantity = sum(ps.quantity for ps in supplies)
                avg_quantity = round(total_quantity / len(supplies))
                result.append((s.name, avg_quantity))
        return sorted(result, key=itemgetter(1), reverse=True)

    def get_suppliers_starting_with_p(self) -> Dict[str, List[str]]:
        """Список всех поставщиков, у которых имя начинается с буквы 'П', и детали, которые они поставляют"""
        result = {}
        for s in self.suppliers:
            if s.name.startswith('П'):
                s_parts = [p.name for p in self.parts if p.supplier_id == s.supplier_id]
                result[s.name] = s_parts
        return result
