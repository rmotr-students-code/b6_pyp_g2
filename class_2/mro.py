class GroundVehicle(object):
    def move(self):
        print("The ground vehicle is moving")


class FlyingVehicle(object):
    def movex(self):
        print("The flying vehicle is moving")


class Airplane(FlyingVehicle, GroundVehicle):
    pass


a = Airplane()
a.move()