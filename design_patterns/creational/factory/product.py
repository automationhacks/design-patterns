class Product:
    def __init__(self):
        print('Initailaiting method of Product class')

    def interface(self):
        print('Interface method')


class ConcreteProduct1(Product):
    def interface1(self):
        print('Overriding interface in Concrete Product1', __class__)


class ConcreteProduct2(Product):
    def interface2(self):
        print('Overriding interface in Concrete Product2', __class__)

