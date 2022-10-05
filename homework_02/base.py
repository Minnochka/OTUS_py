from homework_02 import exceptions as ex
from abc import ABC

class Vehicle(ABC):
    weight = 1000
    started = False
    fuel = 10
    fuel_consumption = 5

    def __init__(self, weight = weight, fuel = fuel, fuel_consumption = fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started == False:
            if self.fuel <= 0:
                raise ex.LowFuelError
            else:
                self.started = True

    def move(self, distance : int):
        if self.fuel < self.fuel_consumption * distance:
            raise ex.NotEnoughFuel
        else:
            self.fuel -= self.fuel_consumption * distance