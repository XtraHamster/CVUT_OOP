# Vytvořte rodičovskou třídu Auto a k ní zděděnou třídu Nákladní. Ukažte na nich: Dědičnost, Zapouzdřenost, Polymorfismus

# 1. Layer - Vehicle = parent class
class Vehicle:
    def __init__(self, type, brand, model):
        self.type = type
        self.brand = brand
        self.model = model

    def display(self):
        print(f"This vehicle is {self.type}")
        print(f"It's brand {self.brand} and the model is {self.model}")

# ---------------------------------------------------------------------------------------------------
# Inheritance
# 2. Layer - Vehicle types
class Car:
    def __init__(self, type, brand, model, speed, spz, seats):
        self.speed = speed
        self.spz = spz
        self.seats = seats
        self._a = 'protected member' # Encapsulation
        Vehicle.__init__(self, type, brand, model)

    def details(self):
        print(f"This vehicle is {self.type}")
        print(f"It's brand {self.brand} and the model is {self.model}")
        print(f"Max speed is {self.speed} km/h. SPZ is {self.spz} and It has {self.seats} seats.")

class Ship:
    def __init__(self, type, brand, model, speed, containers):
        self.speed = speed
        self.containers = containers
        Vehicle.__init__(self, type, brand, model)

    def details(self):
        print(f"This vehicle is {self.type}")
        print(f"It's brand {self.brand} and the model is {self.model}")
        print(f"Max speed is {self.speed} km/h and It has space for {self.containers} containers.")

# ---------------------------------------------------------------------------------------------------
# 3. Layer - Car types
class Truck(Car):
    def __init__(self, type, brand, model, speed, spz, seats):
        Car.__init__(self, type, brand, model, speed, spz, seats)
        print(self._a) # Encapsulation

class Passenger_Car(Car):
    def __init__(self, type, brand, model, speed, spz, seats):
        Car.__init__(self, type, brand, model, speed, spz, seats)
    
# Calling classes
a = Vehicle('plane','Boeing','747')
b = Car('car', 'Mercedes', 'S Class', 280, '1AX5998', '5')
c = Truck('truck', 'AVIA', 'D120', 160, '6AY5687', '3')
d = Passenger_Car('passenger car', 'Volkswagen', 'Passat', 210, '7U62548', '5')
ship = Ship('ship','MAERSK', 'EMMA', 47, '15000')

a.display()
b.details()
c.details()
d.details()
ship.details()

# print(b.a) # AttributeError = Protected member cannot be called outside the class