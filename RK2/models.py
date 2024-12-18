from dataclasses import dataclass

@dataclass
class Part:
    """Деталь"""
    part_id: int
    name: str
    supplier_id: int

@dataclass
class Supplier:
    """Поставщик"""
    supplier_id: int
    name: str

@dataclass
class PartSupply:
    """Поставки деталей для реализации связи многие-ко-многим"""
    part_id: int
    supplier_id: int
    quantity: int
