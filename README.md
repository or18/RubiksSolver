# RubiksSolver
# Overview
Rubik's cube cross, xcross, xxcross, xxxcross, and xxxxcross solver. xcorss, xxcross, xxxcross, and xxxxcross solver can be applied to F2L solver. Last layer(LL) substep solver, LL solver, and LL+AUF solver based on xxxxcross solver are also available. LL substep solver can be applied to OLL, VHLS, or COLL solver. 

# Notes
- For xxxcross, xxxxcross, LL substep, and LL solver, PyPy3 is recommended. 
- For the first search, some tables need to be created. These tables take up approximately 1.3 GB of disk space. <br>
- Memory required <= 1.64 GB <br>
- For the usage, please check the examples.
- If you want to make your own move restrict, you can make like code bellow.
```python
#If you want to search solutions using only U, L, F faces
move_restrict=['U', 'U2', "U'", 'L', 'L2', "L'", 'F', 'F2', "F'"]
```

# How to use
Download the zip file and extract it in a directory of your choice. Go to the directory, and create a python file like examples. Then you can immediately search for cross solutions.

# For Google colab users
You can also start search using PyPy3 in Google Colaboratory. Open a notebook and follow the steps (just copy & paste, and run).
1. Download the zip file from https://www.pypy.org/download.html
```sh
!wget https://downloads.python.org/pypy/pypy3.10-v7.3.16-linux64.tar.bz2
```
2. Unzip the file
```sh
!tar -xf pypy3.10-v7.3.16-linux64.tar.bz2
```
3. Set path
```python
import os
os.environ['PATH']+=':/content/pypy3.10-v7.3.16-linux64/bin/'
```
4. Clone this repository
```sh
!git clone https://github.com/or18/RubiksSolver.git
```
5. Go to /content/RubiksSolver
```sh
cd /content/RubiksSolver
```
6. Start search
```python
%%script pypy3.10
import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#from examples/cross.py
scramble="F2 U L2 F2 D2 U' B2 D2 F2 U' B2 D R F2 D U' B' R' D2 U"
scramble=sv.solve_F2L(scramble, "", False, False, False, False, 5, True, 1, "cross", mv.move_UDLRFB)
```
