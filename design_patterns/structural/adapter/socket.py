
class Volt:
    def __init__(self, volt):
        self.volt = volt

    def get_volt(self):
        return self.volt

    def set_volt(self, volt):
        self.volt = volt


class Socket:
    def get_volt(self):
        return Volt(120)

class SocketAdapter(Socket):
    def get_120volt(self):
        return self.get_volt()

    def get_12volt(self):
        v = self.get_volt()
        return self.convert(v, 12)

    def get_3volt(self):
        v = self.get_volt()
        return self.convert(v, 3)

    def convert(self, v, i):
        volt = Volt(v.get_volt()/i)
        return volt

def get_voltage(sock_adapter, i):
    if i==3:
        return sock_adapter.get_3volt()
    elif i==12:
        return sock_adapter.get_12volt()
    else:
        return sock_adapter.get_120volt()


if __name__ == "__main__":
    sock_adapter = SocketAdapter()
    v1 = get_voltage(sock_adapter, 3)
    print(v1.get_volt())

    v2 = get_voltage(sock_adapter, 12)
    print(v2.get_volt())

    v3 = get_voltage(sock_adapter, 120)
    print(v3.get_volt())


