def initialize_my_car(car, model, year):
    car.model = model
    car.year = year

class Car(object):
    pass

c1 = Car()
initialize_my_car(c1, 'Ford', 2015)

print(c1.model)
print(c1.year)