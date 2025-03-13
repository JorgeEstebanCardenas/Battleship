import os
from Ship import Ship
from logger_setup import setup_logger
from Board import Board


class Game():

    def __init__(self):
        self.logger = setup_logger()
        self.board = Board()
        self.shots = 0

        self.setup_ships()

    def start_game(self):
        finished = False

        print("Game is starting")

        while not finished:
            # self.clear_screen()
            self.display()
            
            finished = self.handle_input()


            
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def display(self):
        self.board.print()


    def handle_input(self):
        user_input = input("Enter two integers separated by a space (or press Enter to quit): ")
        
        if not user_input.strip():
            print("===================================")
            print("Game ended")

            self.print_stats()
            return True

        try:
            x, y = map(int, user_input.split())

            print("===================================")

   
            if self.shoot(x, y):
                print(f"Hit on ({x},{y})")
            else:
                print(f"Miss on ({x},{y})")

            self.shots += 1


        except ValueError:
            print("Invalid input. Please enter two integers.")
        
        return False

    def print_stats(self):

        print("\nGAME STATS")

        print("----------------------------------")

        print(f"Total shots: {self.shots}")
        print(f"You got {self.board.total_hits - self.board.remaining_hits} out of {self.board.total_hits} hits")
        print(f"Hit rate: {self.get_hit_rate():.0%} ({self.board.total_hits - self.board.remaining_hits} out of {self.shots})")


    def get_hit_rate(self):
        return ((self.board.total_hits - self.board.remaining_hits)/self.shots)


    def setup_ships(self) -> None:
        print("Setting up ships")

        self.board.add_ship(5)
        self.board.add_ship(4)
        self.board.add_ship(3)
        self.board.add_ship(3)
        self.board.add_ship(2)

    def shoot(self, x: int, y: int) -> bool:
        return self.board.check_for_ship(x,y)

   
        



if __name__ == '__main__':
    G = Game()

    G.start_game()
