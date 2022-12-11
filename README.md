# Forest Fire Propagation

The objective of this project is to model and visualize the fire propagation in a forest.  
The forests are build randomly, one of the trees get randomly set on fire and the interface (both CLI and GUI) will display the fire
propagation evolution step by step.

### GUI
<img width="431" alt="forest-fire-gui" src="https://user-images.githubusercontent.com/65605546/206928714-1cbb7bb9-ec7b-48bf-9d4b-2e62ae464c9f.gif">


### CLI
<img width="431" alt="forest-fire-cli" src="https://user-images.githubusercontent.com/65605546/206928759-c3b08b1d-58b2-4ea3-a559-85b85b4f39a1.png">


## OOP Architecture
![class_diagram](https://user-images.githubusercontent.com/65605546/206928736-f18684f6-0b44-45a1-9ba1-ae0c1495ae7d.png)

The project core algorithm is done in the Forest class. It is an abstract class. The Forest class create a grid of Tree objects and manage the fire propagation.  
The display part of the project is done in the ForestCli and ForestGui classes. They both inherit from the Forest class (parent).  
The display and algorithm parts are separated. That way we can modify the algorithm or the CLI/GUI without impacting the others parts of the program.

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

**Run the simulation for both the CLI and GUI**
```
cd src
python main.py
```



