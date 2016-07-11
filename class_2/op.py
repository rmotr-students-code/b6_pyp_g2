class Vehicle(object):
    def __init__(self, year):
        self.year = year


class Car(Vehicle):
    def __init__(self, model, year):
        super(Car, self).__init__(year)
        self.model = model

c1 = Car('Ford', year=2015)
c2 = c1
print(c1.model)
print(c1.year)