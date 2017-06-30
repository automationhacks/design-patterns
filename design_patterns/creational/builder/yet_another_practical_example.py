"""
Example from: https://davidcorne.com/2013/01/21/builder-pattern/#more-680
"""

from abc import ABCMeta, abstractmethod


class Vehicle(object):
    """
    Product which we want to build
    """
    def __init__(self, type_name):
        self.type = type_name
        self.wheels = None
        self.doors = None
        self.seats = None

    def view(self):
        print(
            'This vehicle is {} with {} wheels {} doors {} seat'.format(self.type, self.wheels, self.doors, self.seats))


class VehicleBuilder(metaclass=ABCMeta):
    """
    Builder class providing abstracted structure
    """
    @abstractmethod
    def make_wheels(self):
        pass

    @abstractmethod
    def make_doors(self):
        pass

    @abstractmethod
    def make_seats(self):
        pass


class CarBuilder(VehicleBuilder):
    """
    Concrete builder for a car product
    """
    def __init__(self):
        self.vehicle = Vehicle('Car')

    def make_wheels(self):
        self.vehicle.wheels = 4

    def make_doors(self):
        self.vehicle.doors = 3

    def make_seats(self):
        self.vehicle.seats = 5


class BikeBuilder(VehicleBuilder):
    def __init__(self):
        self.vehicle = Vehicle('Bike')

    def make_wheels(self):
        self.vehicle.wheels = 2

    def make_doors(self):
        self.vehicle.doors = 0

    def make_seats(self):
        self.vehicle.seats = 2


class VehicleManufacturer(object):
    """
    Director class which will keep the concrete builder
    """

    def __init__(self):
        self._builder = None

    def create(self):
        """
        Creates and returns a vehicle using self._builder
        :return:
        """

        if self._builder:
            self._builder.make_wheels()
            self._builder.make_doors()
            self._builder.make_seats()
            return self._builder.vehicle

if __name__ == '__main__':
    bmw = VehicleManufacturer()
    bmw._builder = CarBuilder()

    m3_sedan = bmw.create()
    m3_sedan.view()

    bmw._builder = BikeBuilder()
    s_1000_rr = bmw.create()
    s_1000_rr.view()