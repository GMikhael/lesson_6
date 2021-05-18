# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:

    name = None
    surname = None
    position = None

    _list = {'wage': 'wage', 'bonus': 'bonus'}

class Position(Worker):

    def __init__(self, name:str, surname:str, wage:float, bonus:float):
        self.name = name
        self.surname = surname
        self._list['wage'] = wage
        self._list['bonus'] = bonus

    def get_full_name(self):
        return self.name + self.surname

    def get_total_income(self):
        return self._list['wage'] + self._list['bonus']


position = Position(name="Petr", surname="Nalich", wage=235, bonus=380)

print(f"ФИО: {position.get_full_name()}")
print(f"Полная ЗП: {position.get_total_income()}")