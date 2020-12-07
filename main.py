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

    def get_board(self):
        """Updates the board"""

        """key:
            10 - unclicked cell
             0 - empty cell
           1-8 - indicates how many adjacent bombs
            -1 - flagged
        """

        for row in range(16):
            for col in range(30):
                # print(f"Row: {row}, Column: {col}")
                elem = self.driver.find_element_by_id(f"{row + 1}_{col + 1}")
                cell_class = elem.get_attribute("class")

                if "blank" in cell_class:
                    self.board[row, col] = int(10)
                elif "open" in cell_class:
                    self.board[row, col] = int(cell_class[-1])
                elif "bombflagged" in cell_class:
                    self.board[row, col] = int(-1)

    def click(self, mode='left', cell=(1, 1)):

        elem = self.driver.find_element_by_id(f"{cell[0]}_{cell[1]}")

        if mode == "left":
            elem.click()
        elif mode == "right":
            action = ActionChains(self.driver)
            action.context_click(elem).perform()

        print(f"{mode} clicked {cell}")

    def safe_flag(self):
        """If a cell with value x only touches x number of cells, flag all its adjacent cells"""

    def safe_click(self):
        """If a cell with value x has x adjacent flags, click all other adjacent cells"""

    def expected(self):
        """for a given board state, simulate all valid arrangements of bombs
           find the probability of a bomb being in each cell
           flag the near 100% cells
           click the near 0% cells"""

# = = = = = = = = Helper Functions = = = = = = = =

    def enumerate_adjacent_blank_cells(self):
        """For a given cell, return the number of adjacent blank cells"""

    def enumerate_adjacent_flagged_cells(self):
        """For a given cell, return the number of adjacent flagged cells"""

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

    game.safe_flag()

    # game.safe_click()




