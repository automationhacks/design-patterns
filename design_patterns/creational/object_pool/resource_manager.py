from object_pool_pattern.resource_module import ResourceModule


class ObjectPool:
    _instance = None
    _resources = list()

    def __init__(self):
        if ObjectPool._instance != None:
            raise NotImplemented('This is singleton class')

    @staticmethod
    def get_instance():
        if ObjectPool._instance == None:
            ObjectPool._instance = ObjectPool()

        return ObjectPool._instance

    def get_resource(self):
        if len(self._resources) > 0:
            print('Using existing resources')
            return self._resources.pop(0)
        else:
            print('creating new resources')
            return ResourceModule()

    def return_resource(self, resource):
        resource.reset()
        self._resources.append(resource)

if __name__ == "__main__":
    pool = ObjectPool.get_instance()

    one = pool.get_resource()
    two = pool.get_resource()
    print(one, two)

    one.set_obj_value(10)
    two.set_obj_value(20)

    print('one', one.get_value())
    print('two', two.get_value())

    pool.return_resource(one)
    pool.return_resource(two)
    print('List pool', pool)
    one = None
    two = None

    one = pool.get_resource()
    two = pool.get_resource()
    print('List pool2', pool)
    print('One', one.get_value())
    print('Two', two.get_value())
    print(one, two)




