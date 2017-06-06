"""
Provide an interface for creating families of related or dependent
objects without specifying their concrete classes.
"""

import abc
from abc import abstractmethod


class AbstractGameFactory(metaclass=abc.ABCMeta):
    @abstractmethod
    def make_character(self):
        pass

    @abstractmethod
    def make_obstacle(self):
        pass


class Obstacle:
    def action(self):
        pass


class Character:
    def interact_with(self, obstacle):
        pass


class Kitty(Character):
    def interact_with(self, obstacle):
        print('Kitty has encountered a')
        obstacle.action()


class KungFuGuy(Character):
    def interact_with(self, obstacle):
        print('Kung Fu guy encountered a')
        obstacle.action()


class Puzzle(Obstacle):
    def action(self):
        print('puzzle')


class NastyWeapon(Obstacle):
    def action(self):
        print('nasty weapon')


# concrete factories
class KittiesAndPuzzles(AbstractGameFactory):
    def make_character(self):
        return Kitty()

    def make_obstacle(self):
        return Puzzle()


class KillAndDismember(AbstractGameFactory):
    def make_character(self):
        return KungFuGuy()

    def make_obstacle(self):
        return NastyWeapon()


class GameEnvironment:
    def __init__(self, factory):
        self.factory = factory
        self.p = factory.make_character()
        self.ob = factory.make_obstacle()

    def play(self):
        self.p.interact_with(self.ob)

g1 = GameEnvironment(KittiesAndPuzzles())
g1.play()

g2 = GameEnvironment(KillAndDismember())
g2.play()
