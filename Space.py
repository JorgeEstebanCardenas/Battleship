from Ship import Ship

class Space():

    def __init__(self):
        self.ship = None
        self.empty = True

    def add_ship(self, ship: 'Ship') -> None:
        self.ship = ship

        self.empty = False