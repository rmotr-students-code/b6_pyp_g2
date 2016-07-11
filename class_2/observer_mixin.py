class Observer(object):
    def add_observer(self, observer):
        if not hasattr(self, 'observer_list'):
            self.observer_list = []

        self.observer_list.append(observer)

    def notifyAll(self, change):
        for observer in self.observer_list:
            observer(change)


class Collection(object):
    def __init__(self):
        self.data = []

    def add_element(self, element):
        raise NotImplementedError()

    def get_element(self):
        raise NotImplementedError()


class Queue(Collection):

    def add_element(self, element):
        self.data.insert(0, element)

    def get_element(self):
        return self.data.pop()


class Stack(Observer, Collection):
    def add_element(self, element):
        self.data.append(element)
        self.notifyAll("New element added to the stack: %s" % element)

    def get_element(self):
        elem = self.data.pop()
        return elem


def stack_has_changed(change):
    print(change)


def element_removed_from_stack(change):
    print("Element removed!")


s = Stack()

s.add_observer(stack_has_changed)
s.add_observer(element_removed_from_stack)

s.add_element(4)


class Vehicle(object):
    def __init__(self, model):
        self.model = model
        self.gas = 0

    def put_gas(self, gas_amount):
        self.gas += gas_amount


class Car(Vehicle):
    def move(self):
        print("I'm moving")


class Airplane(Vehicle):
    def move(self):
        print("I'm flying")
