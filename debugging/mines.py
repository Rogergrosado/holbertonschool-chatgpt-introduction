#!/usr/bin/python3
import random
import os

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        # Initialize the width, height, and number of mines
        self.width = width
        self.height = height
        # Generate a set of random positions for mines
        self.mines = set(random.sample(range(width * height), mines))
        # Initialize the game field and whether each cell is revealed or not
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    # Function to print the game board
    def print_board(self, reveal=False):
        clear_screen()
        # Print column numbers
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            # Print row numbers
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    # If revealed, print the content of the cell
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')  # Mine
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')  # Number of nearby mines
                else:
                    print('.', end=' ')  # Hidden cell
            print()

    # Function to count the number of mines nearby a cell
    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    # Function to reveal a cell and recursively reveal nearby cells
    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False  # Game over if a mine is revealed
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            # If the cell has no nearby mines, reveal nearby cells recursively
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    # Function to check if the player has won
    def has_won(self):
        for y in range(self.height):
            for x in range(self.width):
                if not self.revealed[y][x] and (y * self.width + x) not in self.mines:
                    return False  # Player hasn't won yet
        return True  # All non-mine cells have been revealed

    # Function to start the game loop
    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not self.reveal(x, y):
                    # If a mine is revealed, game over
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                elif self.has_won():
                    # If all non-mine cells are revealed, player wins
                    self.print_board(reveal=True)
                    print("Congratulations! You've won.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    # Start the game
    game = Minesweeper()
    game.play()

