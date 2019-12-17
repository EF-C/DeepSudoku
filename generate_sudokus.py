from random import shuffle

import numpy as np


class Generator:

    def __init__(self):
        """
        Initializes the board and starts the recursive function to fill the board
        """

        self.SUDOKU_SIZE = 9
        # 0 is an empty space in the board
        self.board = np.zeros((self.SUDOKU_SIZE, self.SUDOKU_SIZE), dtype="int")
        # the locations that haven'
        self.free_locations = [(x, y) for x in range(0, self.SUDOKU_SIZE) for y in range(0, self.SUDOKU_SIZE)]

        self.backtrack()

        print(self.board)

    def valid_value(self, value, location):
        """check if the given value is valid in this location
        :param value: int
            A given value which is to be placed on the board
        :param location: int
            The location in the board where the value is to be placed
        :return: False if the sudoku rules prohibit this value on this location, if valid return True
        """

        def valid_row(row):
            return not (value in self.board[row])

        def valid_column(column):
            col = self.board[::, column: column + 1]
            return not (value in col)

        def valid_cell():
            square_root = np.sqrt(self.SUDOKU_SIZE)
            if square_root - np.floor(square_root) != 0:
                # A cell can only exist if the square root of the sudoku size is a perfect square
                # If it isn't we create a sudoku without cells (so e.g. 5x5 board is still possible)
                return True

            cell_index = (location[0] // square_root, location[1] // square_root)

            left = int(cell_index[0] * square_root)
            right = int((cell_index[0] + 1) * square_root)
            up = int(cell_index[1] * square_root)
            down = int((cell_index[1] + 1) * square_root)

            cell = self.board[left: right, up: down]
            return not (value in cell)

        if valid_cell() and valid_row(location[0]) and valid_column(location[1]):
            return True
        return False

    def backtrack(self):
        """
        A recursive function which adds values to the board.
        :return:
        """
        if len(self.free_locations) == 0:
            return True

        position_index = 0
        location = self.free_locations[position_index]
        values = []
        for i in range(0, self.SUDOKU_SIZE):
            values.append(i + 1)
        shuffle(values)

        for i in range(0, len(values)):
            if self.valid_value(values[i], location):
                self.board[location] = values[i]
                self.free_locations.remove(location)
                if self.backtrack():
                    return True
                else:
                    self.board[location] = 0
                    self.free_locations.append(location)
        return False


if __name__ == '__main__':
    Generator()
