from forest import Forest


class ForestCLi(Forest):

    def __init__(self, row_num, col_num, tree_probability):
        super().__init__(row_num, col_num, tree_probability)

    def get_symbol(self, tree_state):
        if tree_state.state == 0:
            return "."
        elif tree_state.state == 1:
            return "T"
        elif tree_state.state == 2:
            return "F"
        elif tree_state.state == 3:
            return "B"

    def draw_forest(self):
        for row_trees in self.grid:
            row_tree_symbol = [self.get_symbol(tree) for tree in row_trees]
            print(" ".join(row_tree_symbol))

    def run(self, num_generation):
        init_position = self.get_random_starting_tree()
        self.tree_fire_queue.append(init_position)
        for num_generation in range(1, num_generation + 1):
            print()
            print("### Forest after {} generation ###".format(num_generation))
            self.burn_trees()
            self.propagate_fire()
            self.draw_forest()
            print("Proportion of trees: " + str(self.get_trees_proportion()) + "%")
