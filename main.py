import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import numpy as np


# REQUIRES FIREFOX TO WORK


class Minesweeper:

    def __init__(self):
        """Launches Firefox, navigates to minesweeper, and populates starting board"""

        print("Initializing Minesweeper...")

        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.actionChains = ActionChains(self.driver)
        self.driver.get(f'http://minesweeperonline.com/#200')
        self.driver.maximize_window()

        self.board = np.ndarray((16, 30))
        self.board.fill(10)

        self.numbered_cells = {}

    def get_board(self):
        """Updates the board"""

        """key:
            10 - unclicked cell
             0 - empty cell
           1-8 - indicates how many adjacent bombs
            -1 - flagged
        """
        print("Getting board...")

        self.numbered_cells = {}

        for row in range(16):
            for col in range(30):
                # print(f"Row: {row}, Column: {col}")
                elem = self.driver.find_element_by_id(f"{row + 1}_{col + 1}")
                cell_class = elem.get_attribute("class")

                if "blank" in cell_class:
                    self.board[row, col] = int(10)
                elif "open" in cell_class:
                    self.board[row, col] = int(cell_class[-1])
                    if int(cell_class[-1]) != 0:
                        self.numbered_cells[(row, col)] = int(cell_class[-1])
                elif "bombflagged" in cell_class:
                    self.board[row, col] = int(-1)

    def click(self, mode='left', cell=(1, 1)):
        """Performs either a left or right click at cell
           cell: a tuple ranging from (1, 1) to (16, 30)"""

        elem = self.driver.find_element_by_id(f"{cell[0]}_{cell[1]}")

        if mode == "left":
            elem.click()
        elif mode == "right":
            action = ActionChains(self.driver)
            action.context_click(elem).perform()

        print(f"{mode} clicked {cell}")

    def safe_flag(self):
        """If a cell with value x only touches x number of cells, flag all its adjacent cells"""

        for cell in self.numbered_cells:
            print(f"On cell: {cell}")
            if self.numbered_cells[cell] == self.enumerate_adjacent_blank_cells(cell):

                for ad_cell in self.get_adjacent_cells(cell):
                    cell_plus_one = tuple(np.add(ad_cell, (1, 1)))
                    self.click(mode="right", cell=cell_plus_one)

    def safe_click(self):
        """If a cell with value x has x adjacent flags, click all other adjacent cells"""

    def expected(self):
        """for a given board state, simulate all valid arrangements of bombs
           find the probability of a bomb being in each cell
           flag the near 100% cells
           click the near 0% cells"""

# = = = = = = = = Helper Functions = = = = = = = =

    def get_adjacent_cells(self, cell):
        """For a given cell, return a list of tuples for its adjacent cells"""

        adjacent_cells = []

        # up left
        test_cell = tuple(np.add(cell, (-1, -1)))
        if not (test_cell[0] < 0 or test_cell[1] < 0 or test_cell[0] > 15 or test_cell[1] > 29):
            adjacent_cells.append(test_cell)
        # up mid
        test_cell = tuple(np.add(cell, (-1, 0)))
        if not (test_cell[0] < 0 or test_cell[1] < 0 or test_cell[0] > 15 or test_cell[1] > 29):
            adjacent_cells.append(test_cell)
        # up right
        test_cell = tuple(np.add(cell, (-1, 1)))
        if not (test_cell[0] < 0 or test_cell[1] < 0 or test_cell[0] > 15 or test_cell[1] > 29):
            adjacent_cells.append(test_cell)
        # left
        test_cell = tuple(np.add(cell, (0, -1)))
        if not (test_cell[0] < 0 or test_cell[1] < 0 or test_cell[0] > 15 or test_cell[1] > 29):
            adjacent_cells.append(test_cell)
        # right
        test_cell = tuple(np.add(cell, (0, 1)))
        if not (test_cell[0] < 0 or test_cell[1] < 0 or test_cell[0] > 15 or test_cell[1] > 29):
            adjacent_cells.append(test_cell)
        # down left
        test_cell = tuple(np.add(cell, (1, -1)))
        if not (test_cell[0] < 0 or test_cell[1] < 0 or test_cell[0] > 15 or test_cell[1] > 29):
            adjacent_cells.append(test_cell)
        # down mid
        test_cell = tuple(np.add(cell, (1, 0)))
        if not (test_cell[0] < 0 or test_cell[1] < 0 or test_cell[0] > 15 or test_cell[1] > 29):
            adjacent_cells.append(test_cell)
        # down right
        test_cell = tuple(np.add(cell, (1, 1)))
        if not (test_cell[0] < 0 or test_cell[1] < 0 or test_cell[0] > 15 or test_cell[1] > 29):
            adjacent_cells.append(test_cell)

        return adjacent_cells

    def enumerate_adjacent_blank_cells(self, cell):
        """For a given cell, return the number of adjacent blank cells
           cell: a tuple ranging from (1, 1) to (16, 30)"""

        adjacent = 0
        adjacent_cells = self.get_adjacent_cells(cell)

        for cell in adjacent_cells:
            if self.board[cell] == 10:
                adjacent += 1

        return adjacent

    def enumerate_adjacent_flagged_cells(self, cell):
        """For a given cell, return the number of adjacent flagged cells
           cell: a tuple ranging from (1, 1) to (16, 30)"""

    def print_board(self):
        """Prints the updated board"""

        t1 = time.time()
        self.get_board()
        print(f"Getting board took: {time.time() - t1} seconds")

        for row in range(16):
            for col in range(30):
                print(f"{'{0:0=2d}'.format(int(self.board[row, col]))} ", end='')
            print("")


if __name__ == '__main__':

    game = Minesweeper()

    game.click()

    # game.get_board()

    # game.safe_flag()




