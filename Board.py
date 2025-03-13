from Space import Space
from Ship import Ship

class Board():

    def __init__(self):
        self.board = [[Space() for i in range(10)] for i in range(10)]
        self.ships = []
        self.remaining_hits = 0
        self.total_hits = 0

    def check_ship_position(self, ship: 'Ship') -> bool:
        if ship.is_vertical:
            for i in range(ship.length):
                if not self.board[ship.x][ship.y + i].is_empty():
                    return False
        else:
            for i in range(ship.length):
                if not self.board[ship.x + i][ship.y].is_empty():
                    return False
                
        return True

            

    def add_ship(self, ship_length: int) -> None:

        ship = Ship.random_ship(ship_length)

        accepted = False

        while not accepted:
            print(f"Trying to fit ship of length {ship_length}")
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
        self.remaining_hits += ship_length
        self.total_hits += ship_length

    def check_for_ship(self, x:int, y:int) -> bool:
        if self.board[x][y].hit():
            self.remaining_hits -= 1

            if self.board[x][y].is_ship_sinked():


                print(f"{self.board[x][y].ship.length} ship sinked")

                
            return True

        return False
    
    def get_remaining_ships(self):
        return [ship.length for ship in self.ships if not ship.is_sinked()]


    def print(self):
        print("     ", end="")
        print("  ".join(str(n) for n in range(10)))

        print("     ", end="")
        print("  ".join("|" for n in range(10)))

        for n, line in enumerate(self.board):
            print(n, end=" - ")

            for space in line:
                print(" " + space.get_icon(), end=" ")
            print("\n")

        print(f"Remaining Ships: {self.get_remaining_ships()}")
        print(f"Remaining hits: {self.remaining_hits}/{self.total_hits}")

            
