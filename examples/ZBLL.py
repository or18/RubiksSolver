import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#ZBLL search (using only URF)
scramble="R2 U2 B L2 F R2 U2 R2 D2 F U2 F2 D F' D' B' R' B2 U' R2 B2"
scramble=sv.solve_F2L(scramble, "z y'", True, True, False, True, 14, False, 1, "xxxcross", mv.move_UDLRFB)
scramble=sv.solve_LL_substep(scramble, "", False, False, False, True, 14, False, 1, "VHLS", mv.move_URF)
scramble=sv.solve_LL(scramble, "", 16, True, 1, "ZBLL", mv.move_URF)

"""
z y' L' R2 F L2 F2 U' L2 R' B2 D R F  // xxxcross No.1
U R' F' U F U2 F' U' F2 R F'  // VHLS No.1
1: F' U2 F' U R' F' R F U F' U2 F2 R U R'
2: U R2 U R2 F' R U2 R' U' R U' R' F R2 U' R2
3: U2 F U R' F' R2 F R2 U' R' U R2 U' F' U R'
4: U2 F U2 F' U R' U F U2 F' U' R U2 F U' F'
5: U2 F U2 F' U2 R F R' U2 R F' R' U F U' F'
6: U2 F' U2 F2 R U' R' U F2 R' F2 R U2 F2 U' F'
7: U' F U' R F' R' U' F U' F' U2 R F R' U F'
8: U' F' U R' U' F2 U R F' U' F U F' R' F' R
9: F U R U R2 F2 U' R F2 R' U F2 R2 U2 R' F'
10: F U F R' F' R F R' F' R U' R U R' U' F'
11: F R2 U R F R F2 U F R U2 R U2 R2 U2 F'
12: F' U2 F2 R2 F' R2 F' U2 F U' R' U2 F' U' F R
13: F' U2 F' U R' F' R F U F' U2 F2 R U R' U
14: F' U2 F' U R' F' R F U F' U2 F2 R U R' U2
15: F' U2 F' U R' F' R F U F' U2 F2 R U R' U'
16: F' U' R' F2 R F2 U R U' R' U' F2 U' F2 U F'
search finished in 37.150107s
"""