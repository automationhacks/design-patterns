class Engine:
    # Subsystem 1
    def __init__(self):
        self.spin = 0  # motor spin in revs per min

    def start(self, spin):
        if spin > 1500:
            self.spin = spin // 15


class StarterMotor:
    # Subsystem 2

    def __init__(self):
        self.spin = 0  # starter motor spin in revs per min

    def start(self, charge):
        if charge > 50:
            self.spin = 2500  # if enough power, spin fast


class Battery:
    def __init__(self):
        self.charge = 0  # % charged, flat by default


class Car:
    # Facade object
    def __init__(self):
        self.battery = Battery()
        self.starter = StarterMotor()
        self.engine = Engine()

    def turn_key(self):
        self.starter.start(self.battery.charge)  # Use battery to start starter motor
        self.engine.start(self.starter.spin)  # Use starter motor to spin the engine

        if self.engine.spin > 0:  # if spin is non zero, the car has started.
            print('Engine started')
        else:
            print('Engine not started')

    def jump(self):
        self.battery.charge = 100
        print('Jumped')


if __name__ == '__main__':
    mercedes = Car()
    mercedes.turn_key()
    mercedes.jump()
    mercedes.turn_key()
