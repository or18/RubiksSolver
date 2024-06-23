import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#COLL search (using only URF)
scramble="B2 U2 R2 D B2 R2 U2 R2 D' F2 L' B' R' B D L D F L"
scramble=sv.solve_F2L(scramble, "z2", True, True, False, True, 14, False, 1, "xxxcross", mv.move_UDLRFB)
scramble=sv.solve_LL_substep(scramble, "", False, False, False, True, 14, False, 1, "ZBLS", mv.move_URF)
scramble=sv.solve_LL_substep(scramble, "", True, True, False, True, 14, True, 1, "COLL", mv.move_URF)

"""
z2 L' R2 B' L' B' U' B D2 B' D' B2 L2  // xxxcross No.1
R U' R2 F R F2 U' F U R U R'  // ZBLS No.1
1: U R' U2 R U F R' U R U' F'
2: U R' U2 R U F R' U R U' F' U
3: U R' U2 R U F R' U R U' F' U2
4: U R' U2 R U F R' U R U' F' U'
5: U' F R' U' R2 U' R2 U2 R2 U' R' F'
6: U2 F' U F' U' R U2 F U2 F' R' U F2
7: U' F R' U' R2 U' R2 U2 R2 U' R' F' U
8: U' F R' U' R2 U' R2 U2 R2 U' R' F' U2
9: U' F R' U' R2 U' R2 U2 R2 U' R' F' U'
10: F U F' U' F R' F' U' F U F R F2
11: U2 F' U F' U' R U2 F U2 F' R' U F2 U
12: U2 F' U F' U' R U2 F U2 F' R' U F2 U2
13: U2 F' U F' U' R U2 F U2 F' R' U F2 U'
14: U' R U R2 F' R U2 R U2 R' F R U' R'
15: R U R' F U F' R' F U' F' U R2 U2 R'
16: R2 U' R2 U' R2 U F' U2 F U' F' U' F R2
17: R' F R U2 F' U R U R' F' U2 F2 U' F'
18: R' F' U' F R' F R U2 F2 U' F2 U' F' R
19: F U F' U' F R' F' U' F U F R F2 U
20: F U F' U' F R' F' U' F U F R F2 U2
21: F U F' U' F R' F' U' F U F R F2 U'
22: F' U2 R F R' U' R F' R' F U2 F' U F
23: F' U2 F U2 F R' F' R F U R U' R' F'
search finished in 1.752710s
"""
