[![HitCount](https://hits.dwyl.com/or18/RubiksSolver.svg?style=flat-square)](http://hits.dwyl.com/or18/RubiksSolver)
# RubiksSolver
Rubik's cube cross, xcross, xxcross, xxxcross, and xxxxcross solver. Last layer(LL) substep solver, LL solver, and LL+AUF solver based on xxxxcross solver are also available. GUI version is also available.

# Notes
- GUI version is now available. Check [Google colab notebook](https://colab.research.google.com/github/or18/RubiksSolver/blob/main/RubiksSolverApp.ipynb)
  
https://github.com/user-attachments/assets/81ca63aa-755a-43da-b5db-d956ed8eabb6

- Recommended to run on Google Colaboratory, using GPU or TPU.
- For the first search, some tables need to be created. These tables take up approximately 1.3 GB of disk space. 
- Memory required <= 1.64 GB 
- For the usage, please check the examples or Detail
# How to use
1. Clone this repository and go to the directory
```sh
git clone https://github.com/or18/RubiksSolver.git
cd RubiksSolver
```
2. Create a Python program as shown in the examples, and run
   
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
3. Add path
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
6. Create Python file
```python
%%writefile test.py

import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#from examples/cross.py
scramble="F2 U L2 F2 D2 U' B2 D2 F2 U' B2 D R F2 D U' B' R' D2 U"
scramble=sv.solve_F2L(scramble, "", False, False, False, False, 5, True, 1, "cross", mv.move_UDLRFB)
```
7. Run
```sh
!pypy3.10 test.py
```
# Detail
## solve_F2L(scramble, rotation, solve_BL, solve_BR, solve_FR, solve_FL, max_length, full_search, sol_index, name, move_restrict)
### Applications
Cross, xcross, xxcross, xxxcross, xxxxcross, F2L, multi slotting
### Notes
- rotation option: Pre-rotation before search. 
- solve_BL, solve_BR, solve_FR, solve_FL options: solve the F2L slot or not
- max length: Maximum length of solution
- full_search option: If True, search for solutions that satisfy the conditions as much as possible. If no solution was found, print `No solution found`. If already solved, print `already solved`. If False, print the solution at the sol_index like `solution  // name No. sol_index`. If the solution was not found, print `// No solution for name`. If already solved, print `// name`. If this option is True, this function always returns False. If this option is False, return the concatenation of the scramble transformed by pre-rotation and the solution. This option can be used like this code.
```Python
import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#search solutions for F2L#1 (BL) after solve cross
scramble="F2 U L2 F2 D2 U' B2 D2 F2 U' B2 D R F2 D U' B' R' D2 U"
scramble=sv.solve_F2L(scramble, "", False, False, False, False, 8, False, 1, "cross", mv.move_UDLRFB)
scramble=sv.solve_F2L(scramble, "", True, False, False, False, 7, True, 1, "F2L#1 (BL)", mv.move_UDLRFB)
```
- move_restrict option: move restriction option. Use pre-defined ones `move_UDLRFB`, `move_URF`, `move_UDRF`, `move_UDR`, `move_URFB`, `move_UR`, or use original one like `move_ULF=['U', 'U2', "U'", 'L', 'L2', "L'", 'F', 'F2', "F'"]`.
### Examples
```python
import RubiksSolver.solver as sv
import RubiksSolver.move as mv

##If you want to search cross solutions less than 7 moves, using all moves,
scramble="F2 U L2 F2 D2 U' B2 D2 F2 U' B2 D R F2 D U' B' R' D2 U"
scramble=sv.solve_F2L(scramble, "", False, False, False, False, 7, True, 1, "cross", mv.move_UDLRFB)

#If you want to search the shortest cross solution, set the full_search option False, and set sol_index 1.
scramble="F2 U L2 F2 D2 U' B2 D2 F2 U' B2 D R F2 D U' B' R' D2 U"
scramble=sv.solve_F2L(scramble, "", False, False, False, False, 8, False, 1, "cross", mv.move_UDLRFB)

#If you want to search solutions for cross in U(White) face, pre-rotation option can be "z2" or "z2 y", "x2", etc.
scramble="F2 U L2 F2 D2 U' B2 D2 F2 U' B2 D R F2 D U' B' R' D2 U"
scramble=sv.solve_F2L(scramble, "z2", False, False, False, False, 7, True, 1, "cross", mv.move_UDLRFB)

#If you want to search solutions for BL-xcross, set solve_BL option True.
scramble="F2 U L2 F2 D2 U' B2 D2 F2 U' B2 D R F2 D U' B' R' D2 U"
scramble=sv.solve_F2L(scramble, "", True, False, False, False, 9, True, 1, "xcross", mv.move_UDLRFB)

#If you want to search solutions for F2L (BL), set solve_BL option True.
scramble="U2 L' B2 L D2 R' B2 L U2 R' F2 R2 U B U L B R2 B2 R'" #cross solved scramble
scramble=sv.solve_F2L(scramble, "", True, False, False, False, 9, True, 1, "F2L#1(BL)", mv.move_UDLRFB)

#If you want to search solutions for BL&FL-xxcross, set solve_BL and solve_FL options True.
scramble="F2 U L2 F2 D2 U' B2 D2 F2 U' B2 D R F2 D U' B' R' D2 U"
scramble=sv.solve_F2L(scramble, "", True, False, False, True, 11, True, 1, "xxcross", mv.move_UDLRFB)

#If you want to search solutions for F2L (BL&FL) multi slotting, set solve_BL and solve_FL options True.
scramble="U2 L' B2 L D2 R' B2 L U2 R' F2 R2 U B U L B R2 B2 R'" #cross solved scramble
scramble=sv.solve_F2L(scramble, "", True, False, False, True, 11, True, 1, "F2L#1, 2(BL&FL)", mv.move_UDLRFB)

#If you want to search solutions for BL&BR&FL-xxxcross, set solve_BL, solve_BR and solve_FL options True.
scramble="F2 U L2 F2 D2 U' B2 D2 F2 U' B2 D R F2 D U' B' R' D2 U"
scramble=sv.solve_F2L(scramble, "", True, True, False, True, 13, True, 1, "xxxcross", mv.move_UDLRFB)

#If you want to search solutions for xxxxcross, set solve_BL, solve_BR, solve_FR and solve_FL options True.
scramble="F2 U L2 F2 D2 U' B2 D2 F2 U' B2 D R F2 D U' B' R' D2 U"
scramble=sv.solve_F2L(scramble, "", True, True, True, True, 15, True, 1, "xxxxcross", mv.move_UDLRFB)
```
## solve_LL_substep(scramble, rotation, solve_cp, solve_co, solve_ep, solve_eo, max_length, full_search, sol_index, name, move_restrict)
### Applications
OLL, COLL, ZBLS, VHLS, etc.
### Notes
- solve_cp option: solve last layer CP or not
- solve_co option: solve last layer CO or not
- solve_ep option: solve last layer EP or not
- solve_eo option: solve last layer EO or not
- If all four options above are set to True, H perm or AUF can be remained.
- If all four options above are set to False, it is the same as the xxxxcross solver, but it is recommended to use function `solve_F2L` because the search speed becomes much slower.
### Examples
```Python
import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#If you want to search solutions for OLL, set solve_co and solve_eo options True
scramble="U' F R' F U2 B2 R' B2 R B2 L' B2 L U2 F2"
scramble=sv.solve_LL_substep(scramble, "", False, True, False, True, 12, True, 1, "OLL", mv.move_UDLRFB)

#If you want to search solutions for OLL using only U, R, F faces, set move_restrict mv.move_URF
scramble="U' F R' F U2 B2 R' B2 R B2 L' B2 L U2 F2"
scramble=sv.solve_LL_substep(scramble, "", False, True, False, True, 12, True, 1, "OLL", mv.move_URF)

#If you want to search solutions for OLL using only U, L, F faces, please make array for move_restrict
scramble="U' F R' F U2 B2 R' B2 R B2 L' B2 L U2 F2"
move_ULF=['U', 'U2', "U'", 'L', 'L2', "L'", 'F', 'F2', "F'"]
scramble=sv.solve_LL_substep(scramble, "", False, True, False, True, 12, True, 1, "OLL", move_ULF)

#If you want to search solutions for ZBLS or VHLS after solve xxxcross using solve_F2L, set solve_EO option True
scramble="F2 U L2 F2 D2 U' B2 D2 F2 U' B2 D R F2 D U' B' R' D2 U"
scramble=sv.solve_F2L(scramble, "", True, True, False, True, 13, False, 1, "xxxcross", mv.move_UDLRFB)
scramble=sv.solve_LL_substep(scramble, "", False, False, False, True, 12, True, 1, "ZBLS", mv.move_UDLRFB)
```
## solve_LL(scramble, rotation, max_length, full_search, sol_index, name, move_restrict)
### Applications
PLL, ZBLL, 1LLL, last slots+last layer, etc.
### Notes
- AUF can be remained
### Examples
```Python
import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#If you want to search solutions for PLL
scramble="R2 U F2 L2 B2 D' B2 L2 F2 U2 R2 U"
scramble=sv.solve_LL(scramble, "", 14, True, 1, "PLL", mv.move_UDLRFB)

#If you want to search solutions for ZBLL using only U, D, R, F faces
scramble="U F' B U' F U F2 D2 B D2 B' L2 B' L2 F2"
scramble=sv.solve_LL(scramble, "", 14, True, 1, "ZBLL", mv.move_UDRF)
```
## solve_LL_AUF(scramble, rotation, max_length, full_search, sol_index, name, move_restrict)
### Applications
AUF, PLL, ZBLL, 1LLL, etc.
### Notes
- All parts solved
### Examples
```Python
import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#If you want to search CFOP solutions
scramble="L' F D2 L2 D2 B2 L' R2 F2 R2 B2 D2 B2 R' U B' U' F' L2 D2 R"
scramble=sv.solve_F2L(scramble, "", False, False, False, False, 7, False, 1, "cross", mv.move_UDLRFB)
scramble=sv.solve_F2L(scramble, "", True, False, False, False, 9, False, 1, "F2L#1 (BL)", mv.move_UDLRFB)
scramble=sv.solve_F2L(scramble, "", True, False, False, True, 11, False, 1, "F2L#2 (FL)", mv.move_UDLRFB)
scramble=sv.solve_F2L(scramble, "", True, True, False, True, 13, False, 1, "F2L#3 (BR)", mv.move_UDLRFB)
scramble=sv.solve_F2L(scramble, "", True, True, True, True, 15, False, 1, "F2L#4 (FR)", mv.move_UDLRFB)
scramble=sv.solve_LL_substep(scramble, "", False, True, False, True, 12, False, 1, "OLL", mv.move_UDLRFB)
scramble=sv.solve_LL(scramble, "", 14, False, 1, "PLL", mv.move_UDLRFB)
scramble=sv.solve_LL_AUF(scramble, "", 1, False, 1, "AUF", mv.move_UDLRFB)
```
