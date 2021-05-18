# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f"Поехали {self.name}"

    def stop(self):
        return f"\n{self.name} СТОП"

    def turn(self, direction):
        return f"\n{self.name} повернул {direction}"

    def show_speed(self):
        return f"\nСкорость: {self.speed}"


class TownCar(Car):
    def v(self):
        if self.speed > 60:
            return f"\nПревышение скорости {self.speed}"
        else:
            return f"Скорость {self.name}"


class SportCar(Car):
    pass


class WorkCar(Car):
    def v(self):
        if self.speed > 40:
            return f"\nПревышение скорости  {self.speed}"
        else:
            return f"Скорость {self.name}"

class PoliceCar(Car):
    pass


town = TownCar("УАЗ", 70, "синий", False)
print("TownCar\n" + town.go(), town.show_speed(), town.turn("налево"), town.turn("направо"), town.stop())

sport = SportCar("БМВ", 170, "желтый", False)
print("\n" + "SportCar\n" + sport.go(), sport.show_speed(), sport.turn("налево"), sport.stop())

work = WorkCar("КАМАЗ", 30, "черный", False)
print("\n" + "WorkCar\n" + work.go(), work.show_speed(), work.turn("направо"), work.stop())

police = PoliceCar("ЛАДА", 100, "коричневый", True)
print("\n" + "PoliceCar\n" + work.go(), work.show_speed(), work.turn("направо"), work.stop())
