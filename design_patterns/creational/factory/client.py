from DesignPatterns.factory_pattern.creator import Creator

def main(creator):
    concrete_creator = Creator()
    obj = concrete_creator.factory_method(creator)
    obj.concrete_opreration()




if __name__ == "__main__":
    main('ConcreteCreator1')
    main('ConcreteCreator2')