# Forest Fire Propagation

The objective of this project is to model and visualize the fire propagation in a forest.  
The forests are build randomly, one of the trees get randomly set on fire and the interface (both CLI and GUI) will display the fire
propagation evolution step by step.

### GUI
![](forest-fire-gui.gif)

### CLI
<img src="media/forest-fire-cli.png" width="70%">

## OOP Architecture
<img src="media/class_diagram.png" width="70%">

The project core algorithm is done in the Forest class. The Forest class create a grid of Tree and manage the fire propagation.  
The display part of the project are done in the ForestCLi and ForestGui classes. They both inherit from the Forest class (parent).  
The display and algorithm part are separated. That way we can modify the algorithm or the CLI/GUI without impacting the others parts of the program.

## Run the program 
In order to run the program, you first need to create a Python virtual environment and install the necessary libraries:  

**Create virtual environment** 
```
python3 -m venv env
```
**Activate the virtual environment**
```
source env/bin/activate
```
**Install Python libraries**
```
pip install -r requirements.txt
```


