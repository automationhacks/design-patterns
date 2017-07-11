class Subsystem1:
    """
    Implement subsystem 1 func
    Handle work assigned by facade object
    Does not have any reference of facade i.e. does not know about the facade
    """
    def operation_1(self):
        pass

    def operation_2(self):
        pass


class Subsystem2:
    """
    Implement subsystem 2 func
    Handle work assigned by facade object
    Does not have any reference of facade i.e. does not know about the facade
    """
    def operation_1(self):
        pass

    def operation_2(self):
        pass


class Facade:
    """
    Know which subsystem is required for request
    Delegates client requests to appropriate subsystem objects
    """
    def __init__(self):
        self._subsystem1 = Subsystem1()
        self._subsystem2 = Subsystem2()

    def operation(self):
        self._subsystem1.operation_1()
        self._subsystem1.operation_2()
        self._subsystem2.operation_1()
        self._subsystem2.operation_2()


def main():
    facade = Facade()
    facade.operation()

if __name__ == '__main__':
    main()
