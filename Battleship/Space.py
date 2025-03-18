from Battleship.Ship import Ship
from Battleship.Enums import States
from colorama import Fore, Style

class Space():

    def __init__(self):
        self.ship = None
        self.state = States.EMPTY
        self.state_icons = {
            States.EMPTY: ".",
            States.HIT: Fore.RED + "H" + Style.RESET_ALL,
            States.MISS: Fore.WHITE + "M" + Style.RESET_ALL,
            States.SHIP: "."
        }

    def add_ship(self, ship: 'Ship') -> None:
        self.ship = ship

        self.state = States.SHIP

    def is_empty(self) -> bool:
        return self.state != States.SHIP

    def hit(self):
        if self.state is States.SHIP:
            self.state = States.HIT
            self.ship.health -= 1
            return True
        elif self.state == States.HIT: 
            return False
    
        else:
            self.state = States.MISS
            return False
        
    def is_ship_sinked(self) -> bool:
        return self.ship.is_sinked()

    def get_icon(self) -> str:
        return self.state_icons[self.state]