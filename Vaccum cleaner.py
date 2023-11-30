import random

class VacuumCleaner:
    def __init__(self, size):
        self.size = size
        self.environment = [[random.choice([0, 1]) for _ in range(size)] for _ in range(size)]
        self.current_position = (random.randint(0, size-1), random.randint(0, size-1))

    def print_environment(self):
        for row in self.environment:
            print(row)
        print()

    def clean(self):
        while any(1 in row for row in self.environment):
            self.print_environment()
            self.clean_current_cell()
            self.move_random()

        print("Cleaning complete!")

    def move_random(self):
        possible_moves = self.get_possible_moves()
        if possible_moves:
            move = random.choice(possible_moves)
            self.current_position = move
            print(f"Move to {move}")
        else:
            print("No more moves available.")

    def get_possible_moves(self):
        moves = []
        x, y = self.current_position

        if x > 0:
            moves.append((x - 1, y))  # Move up
        if x < self.size - 1:
            moves.append((x + 1, y))  # Move down
        if y > 0:
            moves.append((x, y - 1))  # Move left
        if y < self.size - 1:
            moves.append((x, y + 1))  # Move right

        return moves

    def clean_current_cell(self):
        x, y = self.current_position
        if self.environment[x][y] == 1:
            print(f"Cleaning cell at {self.current_position}")
            self.environment[x][y] = 0
        else:
            print(f"Cell at {self.current_position} is already clean.")

# Example usage:
size_of_environment = 5
vacuum_cleaner = VacuumCleaner(size_of_environment)
vacuum_cleaner.clean()
