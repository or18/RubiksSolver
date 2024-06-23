import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#1LLL search (using only URF)
scramble="B2 U' F' B L' F2 R2 F2 U F' U2 F' L2 F U2 F' B U2 D2 L2 U2"
scramble=sv.solve_F2L(scramble, "z2", True, True, True, True, 15, False, 1, "xxxxcross", mv.move_UDLRFB)
scramble=sv.solve_LL(scramble, "", 16, True, 1, "1LLL", mv.move_URF)

"""
z2 U D F2 B2 L B2 L D2 R' F2 D B' L' F' D'  // xxxxcross No.1
1: F U F R' F' R2 U' R' U R U' R' F'
2: F U F R' F' R2 U' R' U R U' R' F' U
3: F U F R' F' R2 U' R' U R U' R' F' U2
4: F U F R' F' R2 U' R' U R U' R' F' U'
5: F R2 U2 F R F' R U' R' U R' U2 R2 F'
6: U2 F U' R' F' U' F2 R' F' R U R2 U' R' F'
7: U2 F U' R' F' U' F' U F' R2 F U' F' R' F2
8: U' F U2 F' R U2 F U' R' U F R F2 U2 R'
9: R' F U F' R' F' R U' R U R' F2 U' F' R
10: F R2 U2 F R F' R U' R' U R' U2 R2 F' U
11: F R2 U2 F R F' R U' R' U R' U2 R2 F' U2
12: F R2 U2 F R F' R U' R' U R' U2 R2 F' U'
13: U R U F' R U2 R' U2 R' F U F R F' U2 R'
14: U R U2 R' U2 R' U' F U F R F' R U' R' F'
15: U F' U F U R U2 R' F R F' U2 F' U2 F R'
16: U2 F U R' U' F' U2 F U2 F' U' F R2 U' R' F'
17: U2 F U2 R' U' F' U R U2 R U F U' F' U2 R'
18: U2 F U' R' F' U' F2 R' F' R U R2 U' R' F' U
19: U2 F U' R' F' U' F2 R' F' R U R2 U' R' F' U2
20: U2 F U' R' F' U' F2 R' F' R U R2 U' R' F' U'
21: U2 F U' R' F' U' F' U F' R2 F U' F' R' F2 U
22: U2 F U' R' F' U' F' U F' R2 F U' F' R' F2 U2
23: U2 F U' R' F' U' F' U F' R2 F U' F' R' F2 U'
24: U' F U2 F' R U2 F U' R' U F R F2 U2 R' U
25: U' F U2 F' R U2 F U' R' U F R F2 U2 R' U2
26: U' F U2 F' R U2 F U' R' U F R F2 U2 R' U'
27: R U2 R2 U' R2 U' R2 U2 R U' F R U R' U' F'
28: R2 F' U F U' F' U2 F U R2 U2 R' F' U' F R
29: R' U' F' U F2 R U R2 U F2 U' F2 U' R F' R
30: R' U' F' R U2 F2 R' F2 U' R F' R' F2 R U F2
31: R' F U F' R' F' R U' R U R' F2 U' F' R U
32: R' F U F' R' F' R U' R U R' F2 U' F' R U2
33: R' F U F' R' F' R U' R U R' F2 U' F' R U'
34: F U' R2 U2 F R' F' R U' R U R' U2 R2 U F'
35: F R U R' F' U F U' R U' R' U R U' R' F'
36: F R2 U' R F' R' U R2 U R' F R U' F2 U2 F
37: F R' F' R2 F' U2 F R' U' R2 U R' U2 F R' F'
38: F2 U F R' F2 R2 U' R' U2 F U2 R' F' R U F'
39: F' U F2 U2 F U2 F R' F R U' F' U' F' U F'
search finished in 32.618734s
"""