from operator import itemgetter
from data import suppliers, parts, part_supplies


def task_1():
    """Список всех деталей, у которых название заканчивается на 'ор', и имена поставщиков"""
    res_1 = [(p.name, s.name) 
             for p in parts 
             for s in suppliers 
             if p.supplier_id == s.supplier_id and p.name.endswith('ор')]
    return res_1


def task_2():
    """Список поставщиков со средней поставкой деталей, отсортированный по средней поставке"""
    res_2_unsorted = []
    for s in suppliers:
        total_quantity = sum(ps.quantity for ps in part_supplies if ps.supplier_id == s.supplier_id)
        count_details = len([ps for ps in part_supplies if ps.supplier_id == s.supplier_id])
        
        if count_details > 0:
            avg_quantity = total_quantity / count_details
            res_2_unsorted.append((s.name, avg_quantity))

    return sorted(res_2_unsorted, key=itemgetter(1), reverse=True)


def task_3():
    """Список всех поставщиков, у которых имя начинается с буквы 'П', и детали, которые они поставляют"""
    res_3 = {}
    for s in suppliers:
        if s.name.startswith('П'):
            s_parts = [p.name for p in parts if p.supplier_id == s.supplier_id]
            res_3[s.name] = s_parts
    return res_3
