import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#F2L#3, 4(solve BR&FR) search
scramble="R2 D' L2 U2 F' D2 B2 R2 B D2 L2 F L D' F R B' D' F' D"
scramble=sv.solve_F2L(scramble, "z2 y'", True, False, False, True, 12, False, 1, "xxcross", mv.move_UDLRFB)
scramble=sv.solve_F2L(scramble, "", True, True, True, True, 10, True, 1, "F2L#3, 4", mv.move_UDLRFB)

"""
z2 y' L F' B' U L2 R' U B2 D2 L  // xxcross No.1
1: U B U L2 D F' D' L2 B'
2: U2 F' R' U' R F B U B'
3: U' F R' F' U' R F' U' F
4: U' B' D' R2 B U2 B' D B
5: U' B' D' F R F' R D B
6: L U' B' D' R2 D B U L'
7: R' F R' F2 U' F R U R2
8: B' D2 F U F2 U' F' D2 B
9: U R2 U' B U' F' B' U F R2
10: U F B U L2 F L2 B' U' F'
11: U F2 B U' B' R2 F R2 U F2
12: U B U D2 F' U' F U D2 B'
13: U B U L2 D F' D' L2 B' U
14: U B U L2 D F' D' L2 B' U2
15: U B U L2 D F' D' L2 B' U'
16: U B U2 B' R' B' R2 B U R
17: U B U' D2 F' U F U2 D2 B'
18: U B U' B' U' B' D' R2 D B
19: U B D2 F R' F' R U D2 B'
20: U B L2 D F D' L B L B2
21: U B2 L' D L' D F D2 L2 B2
22: U2 L2 D L2 F' L2 D2 B' D L2
23: U2 F' R' U' R F B U B' U
24: U2 F' R' U' R F B U B' U2
25: U2 F' R' U' R F B U B' U'
26: U2 F' R' U' R B U B' U' F
27: U2 B2 D2 F D' L2 D F' D2 B2
28: U2 B2 R2 U B U B2 U2 R2 B2
29: U' F R' F' U' R F' U' F U
30: U' F R' F' U' R F' U' F U2
31: U' F R' F' U' R F' U' F U'
32: U' F' R' U2 R F U2 B U B'
33: U' B2 L2 D2 F' D2 L2 B' U' B'
34: U' B' D' R2 B U2 B' D B U
35: U' B' D' R2 B U2 B' D B U2
36: U' B' D' R2 B U2 B' D B U'
37: U' B' D' F R F' R D B U
38: U' B' D' F R F' R D B U2
39: U' B' D' F R F' R D B U'
40: D' F' L2 D' B2 D L2 U F D
41: D' F' L' U L F D R' U R
42: L U' B U' L' B D2 R D2 B2
43: L U' B' D' R2 D B U L' U
44: L U' B' D' R2 D B U L' U2
45: L U' B' D' R2 D B U L' U'
46: R2 U2 B' R' B R2 U R U R2
47: R' F R' F2 U' F R U R2 U
48: R' F R' F2 U' F R U R2 U2
49: R' F R' F2 U' F R U R2 U'
50: R' B' R U' B' R B U B R
51: R' B' R F B R D R D' F'
52: B' U2 D' B U B' U R2 D B
53: B' U2 B U B' U D' R2 D B
54: B' D2 F U F2 U' F' D2 B U
55: B' D2 F U F2 U' F' D2 B U2
56: B' D2 F U F2 U' F' D2 B U'
search finished in 0.125221s
"""
