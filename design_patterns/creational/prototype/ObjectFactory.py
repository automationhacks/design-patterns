from prototype.types import Type1, Type2


class object_factory:
    # Manages prototypes.

    __type1_value1 = None
    __type2_value21 = None

    @staticmethod
    def initialize():
        object_factory.__type1_value1 = Type1(1)
        object_factory.__type2_value21 = Type2(2)

    @staticmethod
    def get_type1_value1():
        return object_factory.__type1_value1.clone()

    @staticmethod
    def get_type2_value1():
        return object_factory.__type2_value21.clone()

if __name__ == "__main__":
    object_factory.initialize()

    instance = object_factory.get_type1_value1()
    print('Object1: ', instance.getType(), instance.get_value(), instance)

    instance = object_factory.get_type2_value1()
    print('Object2: ', instance.getType(), instance.get_value(), instance)
