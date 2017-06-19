"""
Separate construction of complex obj from its representation such as it can be repeatable
for other representations
"""

from abc import ABCMeta, abstractmethod


class Director:
    """
    Constructs an obj using builder interface
    """
    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder._build_part_a()
        self._builder._build_part_b()
        self._builder._build_part_c()


class Builder(metaclass=ABCMeta):
    """
    Abstract interface for creating parts of a product
    """
    def __init__(self):
        self.product = Product()

    @abstractmethod
    def _build_part_a(self):
        pass

    @abstractmethod
    def _build_part_b(self):
        pass

    @abstractmethod
    def _build_part_c(self):
        pass


class ConcreteBuilder(Builder):
    """
    Construct and assemble parts of the product by implementing builder interface
    Defines and keeps track of the representation it creates
    Provides an interface for retrieving the product
    """
    def _build_part_a(self):
        pass

    def _build_part_b(self):
        pass

    def _build_part_c(self):
        pass


class Product:
    """
    Complex object under construction
    """
    def __init__(self):
        pass


def main():
    concrete_builder = ConcreteBuilder()
    director = Director()
    director.construct(concrete_builder)
    product = concrete_builder.product


if __name__ == '__main__':
    main()
