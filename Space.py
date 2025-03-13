from Ship import Ship
from Enums import States

class Space():

    def __init__(self):
        self.ship = None
        self.state = States.EMPTY
        self.state_icons = {
            States.EMPTY: ".",
            States.HIT: "H",
            States.MISS: "M",
            States.SHIP: "0"
        }

    def add_ship(self, ship: 'Ship') -> None:
        self.ship = ship

        self.state = States.SHIP

    def is_empty(self):
        return self.state != States.SHIP

    def hit(self):
        if self.state is States.SHIP:
            self.state = States.HIT
            return True
        
        else:
            self.state = States.MISS
            return False

    def get_icon(self):
        return self.state_icons[self.state]