"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02 import exceptions as ex


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        self.max_cargo = max_cargo
        Vehicle.__init__(self, weight, fuel, fuel_consumption)

    def load_cargo(self, plus : int):
        if self.max_cargo < self.cargo + plus:
            raise ex.CargoOverload
        else:
            self.cargo += plus

    def remove_all_cargo(self) -> int:
        cargo = self.cargo
        self.cargo = 0
        return cargo