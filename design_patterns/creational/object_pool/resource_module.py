class ResourceModule:

    _value = 0

    def get_value(self):
        return self._value

    def set_obj_value(self, number):
        print('Number', number)
        self._value = number

    def reset(self):
        self._value = 0