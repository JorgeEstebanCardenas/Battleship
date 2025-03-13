from random import randrange, choice
from logger_setup import setup_logger

class Ship():

    def __init__(self,x: int, y: int, is_vertical: bool, length: int):
        self.x = x
        self.y = y
        self.is_vertical = is_vertical
        self.length = length
        self.health = length

        self.logger = setup_logger()

    def is_sinked(self):
        return self.health <= 0

    @staticmethod
    def random_ship(length: int) -> 'Ship':

        is_vertical = randrange(0, 2)

        if is_vertical:
            x = randrange(0, 10)
            y = randrange(0, 10 - length + 1)
        else:
            x = randrange(0, 10 - length + 1)
            y = randrange(0, 10)


        return Ship(x, y, is_vertical, length)