import time
from tkinter import Tk, Canvas, Label

from src.forest import Forest


class ForestGui(Forest):
    GUI_WIDTH = 800
    GUI_HEIGHT = 800
    STEP_DURATION_SEC = 1

    def __init__(self, row_num, col_num, tree_probability):
        super().__init__(row_num, col_num, tree_probability)
        self.gui = None
        self.canvas = None
        self.proportion_trees_label = None
        self.initialize_gui()

    def initialize_gui(self):
        self.gui = Tk()
        self.gui.title("Forest Fire Propagation")
        self.gui.geometry(f"{ForestGui.GUI_WIDTH}x{ForestGui.GUI_HEIGHT}")
        self.proportion_trees_label = Label(self.gui,
                                            text="Percentage of remaining trees: " + str(
                                                self.get_trees_proportion()) + "%")
        self.proportion_trees_label.pack()

        self.canvas = Canvas(self.gui, background="ivory", width=ForestGui.GUI_WIDTH, height=ForestGui.GUI_HEIGHT)
        self.canvas.pack()
        self.gui.update()

    def get_tree_color(self, tree):
        if tree.state == 0:
            return "ivory"
        elif tree.state == 1:
            return "green"
        elif tree.state == 2:
            return "red"
        elif tree.state == 3:
            return "grey"

    def draw_forest(self):
        TREE_WIDTH = ForestGui.GUI_WIDTH / self.col_num
        TREE_HEIGHT = (ForestGui.GUI_HEIGHT - 50) / self.row_num
        for y in range(0, self.row_num):
            for x in range(0, self.col_num):
                draw_x = x * TREE_WIDTH
                draw_y = y * TREE_HEIGHT
                print(y, x)
                tree_color = self.get_tree_color(self.grid[y][x])
                self.canvas.create_rectangle(draw_x, draw_y, draw_x + TREE_WIDTH, draw_y + TREE_HEIGHT, fill=tree_color)

    def update_labels(self):
        self.proportion_trees_label["text"] = "Percentage of remaining trees: " + \
                                              str(self.get_trees_proportion()) + "%"

    def run(self, num_generation=None):
        init_position = self.get_random_starting_tree()
        self.tree_fire_queue.append(init_position)
        while True:
            self.draw_forest()
            self.gui.update()
            self.burn_trees()
            self.update_labels()
            self.propagate_fire()
            time.sleep(ForestGui.STEP_DURATION_SEC)
