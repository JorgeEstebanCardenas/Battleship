import os
from Ship import Ship
from logger_setup import setup_logger
from Board import Board


class Game():

    def __init__(self):
        self.logger = setup_logger()
        self.board = Board()

        self.setup_ships()

    def start_game(self):
        finished = False

        print("Game is starting")

        while not finished:
            # self.clear_screen()
            print("===================================")

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
            print(f"You got {self.board.total_hits - self.board.remaining_hits} out of {self.board.total_hits} hits")
            return True

        try:
            x, y = map(int, user_input.split())
   
            if self.shoot(x, y):
                print(f"Hit on ({x},{y})")
            else:
                print(f"Miss on ({x},{y})")


        except ValueError:
            print("Invalid input. Please enter two integers.")
        
        return False

       


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
