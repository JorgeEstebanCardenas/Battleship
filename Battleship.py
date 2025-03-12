import random
from Ship import Ship
from logger_setup import setup_logger
from Board import Board


class Game():

    def __init__(self):
        self.logger = setup_logger()
        self.board = Board()

        self.setup_ships()


    def setup_ships(self) -> None:
        self.logger.info("Setting up ships")

        self.board.add_ship(5)
        self.board.add_ship(4)
        self.board.add_ship(3)
        self.board.add_ship(3)
        self.board.add_ship(2)

    def shoot(self, x: int, y: int) -> bool:
        self.board.check_for_ship(x,y)

    def display(self):
        self.board.print()
        



if __name__ == '__main__':
    G = Game()

    G.display()

    G.shoot(0,0)
    G.shoot(1,1)
    G.shoot(2,2)
    G.shoot(3,3)
    G.shoot(4,4)
    G.shoot(5,5)
    G.shoot(6,6)
    G.shoot(7,7)
    G.shoot(8,8)
    G.shoot(9,9)

    G.display()
