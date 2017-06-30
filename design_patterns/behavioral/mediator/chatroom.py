
class User:
    def __init__(self, mediator, user):
        self.mediator = mediator
        self.name = user
        self.mediator.add_user(self)


    def send(self, msg):
        print(self.name + ' sends message ' + msg)
        print('-' * 50)
        self.mediator.send_message(msg, self.name)

    def recieve(self, msg):
        print(self.name + ' recieves message ' + msg)

class Mediator:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, msg, name):
        for user in self.users:
            if user.name != name:
                user.recieve(msg)


if __name__ == "__main__":
    mediator = Mediator()
    u1 = User(mediator, 'Geetika')
    u2 = User(mediator, 'Deepika')
    u3 = User(mediator, 'Rajesh')

    u1.send('First msg')




