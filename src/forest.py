from tree import Tree
from random import choices


class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col


class Forest:
    def __init__(self, row_num, col_num, tree_probability):
        self.row_num = row_num
        self.col_num = col_num
        self.grid = None
        self.tree_num = 0
        self.tree_fire_queue = []
        self.tree_fire = []
        self.initialize_grid_fixed()
        # self.initialize_grid(tree_probability)

    def initialize_grid(self, tree_probability):
        grid = []
        for row in range(0, self.row_num):
            current_row = []
            for col in range(0, self.col_num):
                tree_state = choices([0, 1], weights=[1 - tree_probability, tree_probability])[0]
                tree = Tree(tree_state)
                current_row.append(tree)
                if tree.state == 2:
                    self.tree_num += self.tree_num + 1
            grid.append(current_row)
        self.grid = grid

    def initialize_grid_fixed(self):
        self.grid = [
            [Tree(0), Tree(0), Tree(0), Tree(0), Tree(0)],
            [Tree(0), Tree(1), Tree(1), Tree(0), Tree(0)],
            [Tree(0), Tree(1), Tree(0), Tree(0), Tree(0)],
            [Tree(0), Tree(1), Tree(1), Tree(1), Tree(0)],
            [Tree(0), Tree(0), Tree(0), Tree(0), Tree(0)]
        ]
        self.tree_num = 6

    def display_forest(self):
        for row_trees in self.grid:
            row_tree_symbol = [tree.get_symbol() for tree in row_trees]
            print(" ".join(row_tree_symbol))

    def check_coordinates_valid(self, position: Position):
        # invalid condition for the row
        if position.row < 0 or position.row > self.row_num:
            return False
        # invalid condition for the col
        if position.col < 0 or position.col > self.col_num:
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
        return self.tree_num / (self.row_num * self.col_num)

    def run(self, num_generation, init_position: Position):
        self.tree_fire_queue.append(init_position)
        for num_generation in range(1, num_generation + 1):
            print()
            print("### Forest after {} generation ###".format(num_generation))
            self.burn_trees()
            self.propagate_fire()
            self.display_forest()
            print("Proportion of trees: " + str(self.get_trees_proportion()))
