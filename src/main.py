from forest_cli import ForestCLi
from forest_gui import ForestGui

forest = ForestCLi(5, 5, 0.5)
forest.run(5)

forest = ForestGui(40, 40, 0.6)
forest.run(5)


