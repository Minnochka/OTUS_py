"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    pass
    #def __init__(self):
        #super.__init__(self, "There is no fuel in the tank")

class NotEnoughFuel(Exception):
    pass
    #def __init__(self):
        #super.__init__(self, "Not enough fuel to cover the distance")

class CargoOverload(Exception):
    pass
    #def __init__(self):
        #super.__init__(self, "The overload has occurred")