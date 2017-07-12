
#factory Class
class Creator:
    @staticmethod
    def factory_method(type):
        print(type)
        if type == "ConcreteCreator1":
            return ConcreteCreator1()
        if type== 'ConcreteCreator2':
            return ConcreteCreator2()



class ConcreteCreator1:
    def concrete_opreration(self):
        print('Inside some operation mehod', __class__)


class ConcreteCreator2:
    def concrete_opreration(self):
        print('Inside some operation mehod', __class__)