import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#F2L#1(solve BL slot) search
scramble="R D' B L' B U' F' D B' F2 R' B2 U2 R2 B2 L' D2 F2 L U2"
scramble=sv.solve_F2L(scramble, "z2", False, False, False, False, 8, False, 1, "cross", mv.move_UDLRFB)
scramble=sv.solve_F2L(scramble, "", True, False, False, False, 7, True, 1, "F2L#1", mv.move_UDLRFB)

"""
z2 F' U' D F2 L B  // cross No.1
1: U L' U2 L2 U' L'
2: U L' U' L2 U2 L'
3: L D F2 U2 D' L'
4: F L F2 U2 L' F'
5: U L' U L' B L2 B'
6: U L' U L' B2 L2 B2
7: U L' U2 D' B2 D L
8: U L' U2 L2 U' L' U
9: U L' U2 L2 U' L' U2
10: U L' U2 L2 U' L' U'
11: U L' U' D2 R2 D2 L
12: U L' U' L2 U2 L' U
13: U L' U' L2 U2 L' U2
14: U L' U' L2 U2 L' U'
15: U F2 L2 F2 L' U L'
16: U' L D2 R2 U' D2 L'
17: L U L2 U2 L2 U' L'
18: L U L2 U' L2 U2 L'
19: L U' D2 R2 U' D2 L'
20: L D F2 U2 D' L' U
21: L D F2 U2 D' L' U2
22: L D F2 U2 D' L' U'
23: L D F2 U2 F D' L'
24: L D F2 U2 F2 D' L'
25: L D F2 U2 F' D' L'
26: L' F' L' F L2 U2 L'
27: F L F2 U2 L' U F'
28: F L F2 U2 L' U2 F'
29: F L F2 U2 L' U' F'
30: F L F2 U2 L' F' U
31: F L F2 U2 L' F' U2
32: F L F2 U2 L' F' U'
33: F L F2 U2 F L' F'
34: F L F2 U2 F2 L' F'
35: F L F2 U2 F' L' F'
search finished in 0.031978s
"""