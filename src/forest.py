import random

from position import Position
from tree import Tree
from random import choices
from abc import ABC, abstractmethod


class Forest(ABC):
    def __init__(self, row_num, col_num, tree_probability):
        self.row_num = row_num
        self.col_num = col_num
        self.grid = None
        self.tree_num = 0
        self.tree_fire_queue = []
        self.tree_fire = []
        self.initialize_grid(tree_probability)

    def initialize_grid(self, tree_probability):
        grid = []
        for row in range(0, self.row_num):
            current_row = []
            for col in range(0, self.col_num):
                tree_state = choices([0, 1], weights=[1 - tree_probability, tree_probability])[0]
                tree = Tree(tree_state)
                current_row.append(tree)
                if tree.state == 1:
                    self.tree_num = self.tree_num + 1
            grid.append(current_row)
        self.grid = grid

    @abstractmethod
    def draw_forest(self):
        pass

    def check_coordinates_valid(self, position):
        # invalid condition for the row
        if position.row < 0 or position.row >= self.row_num:
            return False
        # invalid condition for the col
        if position.col < 0 or position.col >= self.col_num:
            return False
        # invalid condition for no tree
        if self.grid[position.row][position.col].state == 0 or self.grid[position.row][position.col].state == 3:
            return False
        return True

    def find_neighbors(self, tree_position):
        valid_neighbors = []
        left_tree_coord = Position(tree_position.row, tree_position.col - 1)
        if self.check_coordinates_valid(left_tree_coord):
            valid_neighbors.append(left_tree_coord)

        right_tree_coord = Position(tree_position.row, tree_position.col + 1)
        if self.check_coordinates_valid(right_tree_coord):
            valid_neighbors.append(right_tree_coord)

        top_tree_coord = Position(tree_position.row - 1, tree_position.col)
        if self.check_coordinates_valid(top_tree_coord):
            valid_neighbors.append(top_tree_coord)

        bottom_tree_coord = Position(tree_position.row + 1, tree_position.col)
        if self.check_coordinates_valid(bottom_tree_coord):
            valid_neighbors.append(bottom_tree_coord)

        return valid_neighbors

    def burn_trees(self):
        for position in self.tree_fire:
            self.grid[position.row][position.col].state = 3
            self.tree_num = self.tree_num - 1

    def propagate_fire(self):
        new_positions_queue = []
        self.tree_fire = []
        while self.tree_fire_queue:
            tree_position = self.tree_fire_queue.pop(0)
            self.grid[tree_position.row][tree_position.col].state = 2
            self.tree_fire.append(tree_position)
            new_positions = self.find_neighbors(tree_position)
            new_positions_queue = new_positions_queue + new_positions
        self.tree_fire_queue = new_positions_queue

    def get_trees_proportion(self):
        return 100 * self.tree_num / (self.row_num * self.col_num)

    def get_random_starting_tree(self):
        random_index = random.randint(0, self.row_num * self.col_num)
        current_index = 0
        for y in range(0, self.row_num):
            for x in range(0, self.col_num):
                if current_index >= random_index and self.grid[y][x].state == 1:
                    return Position(y, x)
                else:
                    current_index = current_index + 1

    @abstractmethod
    def run(self, num_generation=None):
        pass