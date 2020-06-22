class Car:
    def __init__(self, speed, units):
        self.speed = speed
        self.units = units

    def about_car(self):
        return "Car with the maximum speed of " + str(self.speed) + " " + self.units


class Boat:
    def __init__(self, speed):
        self.speed = speed

    def about_car(self):
        print("Boat with the maximum speed of " + str(self.speed )+ " knots")


car = Car(151, 'km/h')
print(car.about_car())
boat = Boat(77)
boat.about_car()
