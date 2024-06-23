import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#OLL search (using only URF)
scramble="R U R2 B' U' D F D R' D' L2 U' R2 B2 D' B2 U' L2 D R2 D'"
scramble=sv.solve_F2L(scramble, "z2", True, True, True, True, 15, False, 1, "xxxxcross", mv.move_UDLRFB)
scramble=sv.solve_LL_substep(scramble, "", False, True, False, True, 12, True, 1, "OLL", mv.move_URF)

"""
z2 R U2 L' B' D' L2 F U' R2 B' R2 U L' R'  // xxxxcross No.1
1: F U F' R' F U' F' U R
2: U' R' U' R F R' U R U' F'
3: R' U F U2 F' U' R F U' F'
4: F U F' R' F U' F' U R U
5: F U F' R' F U' F' U R U2
6: F U F' R' F U' F' U R U'
7: U F U R U2 R' U R U R' F'
8: U F' R' F U2 F' R F R' U2 R
9: U F' R' F U' F' R F R' U R
10: U2 R F R' U R F' R' F U' F'
11: U2 R F R' U2 R F' R' F U2 F'
12: U2 R' U' F' U2 F U' F' U' F R
13: U' R' U' R F R' U R U' F' U
14: U' R' U' R F R' U R U' F' U2
15: U' R' U' R F R' U R U' F' U'
16: U' F U' R' U2 R U F' R' U R
17: R' U R U F' U R' U R U2 F
18: R' U F U2 F' U' R F U' F' U
19: R' U F U2 F' U' R F U' F' U2
20: R' U F U2 F' U' R F U' F' U'
21: R' F' R U R' U' R' F R U R
22: U R U2 R F2 R' U2 R' U2 R2 F2 R2
23: U R U2 R' F2 R U2 R' U2 R' F2 R
24: U R U2 R' F' R U2 R' U2 R' F R
25: U R F R' U2 R F' R' U' F U' F'
26: U R' U F U F' U' R U F U' F'
27: U R' U F U2 F' U' R U F U2 F'
28: U R' U' R' F R U R U' R' F' R
29: U F U R U2 R' U R U R' F' U
30: U F U R U2 R' U R U R' F' U2
31: U F U R U2 R' U R U R' F' U'
32: U F U R U' F U F' R' F U' F2
33: U F' U2 R' U' R U' F U' R' U' R
34: U F' R' F U2 F' R F R' U2 R U
35: U F' R' F U2 F' R F R' U2 R U2
36: U F' R' F U2 F' R F R' U2 R U'
37: U F' R' F U' F' R F R' U R U
38: U F' R' F U' F' R F R' U R U2
39: U F' R' F U' F' R F R' U R U'
40: U2 R U2 F U F' U R' U F U F'
41: U2 R F R' U R F' R' F U' F' U
42: U2 R F R' U R F' R' F U' F' U2
43: U2 R F R' U R F' R' F U' F' U'
44: U2 R F R' U2 R F' R' F U2 F' U
45: U2 R F R' U2 R F' R' F U2 F' U2
46: U2 R F R' U2 R F' R' F U2 F' U'
47: U2 R' U' F' U R' U' R F R' U R2
48: U2 R' U' F' U2 F U' F' U' F R U
49: U2 R' U' F' U2 F U' F' U' F R U2
50: U2 R' U' F' U2 F U' F' U' F R U'
51: U2 F U F R' F' U' F' U F R F'
52: U2 F U' R' U2 R U F' U' R' U2 R
53: U2 F U' R' U' R U F' U' R' U R
54: U2 F' U2 F R F' U2 F U2 F R' F'
55: U2 F' U2 F R2 F' U2 F U2 F R2 F'
56: U2 F' U2 F' R2 F U2 F U2 F2 R2 F2
57: U2 F' R' F U2 F' R F U R' U R
58: U' F U' R' U2 R U F' R' U R U
59: U' F U' R' U2 R U F' R' U R U2
60: U' F U' R' U2 R U F' R' U R U'
61: U' F U' F' U' R U' F U' F' U2 R'
62: U' F R F' U' F U F R' F' U' F'
63: R' U R U F' U R' U R U2 F U
64: R' U R U F' U R' U R U2 F U2
65: R' U R U F' U R' U R U2 F U'
66: R' F' R U R' U' R' F R U R U
67: R' F' R U R' U' R' F R U R U2
68: R' F' R U R' U' R' F R U R U'
69: F R U' R' U' F' U' F2 R' F' R F'
70: F2 U F' U' R U2 F U2 F' R' U F'
71: F2 U F' R' F U' F' R F' R' U R
72: F' U F' R' F U' F' R F2 R' U R
73: F' U2 F U2 F R' F' U' F' U F R
search finished in 0.376787s
"""