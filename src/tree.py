class Tree:
    def __init__(self, state):
        self.state = state
        # self.has_neighbor_in_fire = False

    def get_symbol(self):
        if self.state == 0:
            return "."
        elif self.state == 1:
            return "T"
        elif self.state == 2:
            return "F"
        elif self.state == 3:
            return "B"

    def set_fire(self):
        if self.has_neighbor_in_fire:
            self.state = 2

    def set_burnt(self):
        self.state = 3
