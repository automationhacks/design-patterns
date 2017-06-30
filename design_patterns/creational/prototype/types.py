import copy
from prototype.prototype import Prototype


# concrete prototype:
class Type1(Prototype):
    def __init__(self, number):
        self._type = "Type1"
        self._value = number

    def clone(self):
        return copy.copy(self)


class Type2(Prototype):
    def __init__(self, number):
        self._type = "Type2"
        self._value = number

    def clone(self):
        return copy.copy(self)

