class Prototype:
    _type = None
    _value = None

    def clone(self):
        pass

    def get_type(self):
        return self._type

    def get_value(self):
        return self._value
