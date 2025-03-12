from Space import Space
from Ship import Ship

class Board():

    def __init__(self):
        self.board = [[Space() for i in range(10)] for i in range(10)]
        self.ships = []

    def check_ship_position(self, ship: 'Ship') -> bool:
        if ship.is_vertical:
            for i in range(ship.length):
                if not self.board[ship.x][ship.y + i].empty:
                    return False
        else:
            for i in range(ship.length):
                if not self.board[ship.x + i][ship.y].empty:
                    return False
                
        return True

            

    def add_ship(self, ship_length: int) -> None:

        ship = Ship.random_ship(ship_length)

        accepted = False

        while not accepted:
            if not self.check_ship_position(ship):
                ship = Ship.random_ship(ship.length)
            else:
                accepted = True

        if ship.is_vertical:
            for i in range(ship.length):
                self.board[ship.x][ship.y + i].add_ship(ship)

        else:
            for i in range(ship.length):
                self.board[ship.x + i][ship.y].add_ship(ship)

        self.ships.append(ship)

    def check_for_ship(self, x:int, y:int) -> bool:
        if not self.board[x][y].empty:
            print(f"Hit on ({x},{y})")

        return not self.board[x][y].empty


    def print(self):
        for line in self.board:
            for space in line:
                print(" ." if space.empty else " 0", end=" ")
            print("\n")

            
