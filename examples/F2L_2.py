import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#F2L#2(solve BR) search
scramble="R2 U F B2 U2 L U B' D2 L2 D' R2 D L2 D' B2 R2 L2 D2 B'"
scramble=sv.solve_F2L(scramble, "z2", True, False, False, False, 10, False, 1, "xcross", mv.move_UDLRFB)
scramble=sv.solve_F2L(scramble, "", True, True, False, False, 7, True, 1, "F2L#2", mv.move_UDLRFB)

"""
z2 L2 D F' B U' L D' B  // xcross No.1
1: R U2 R' U B U B'
2: R U' B U B2 R' B
3: R2 U B U' B2 R2 B
4: R2 U2 F' U2 F2 R2 F'
5: R2 U2 B U2 B2 R2 B
6: R2 F2 U2 F' U2 F2 R2
7: R2 F' U2 F2 U2 F' R2
8: R2 B2 D B D' R2 B
9: R2 B2 D2 F' D2 B2 R2
10: R2 B' R2 D2 F D2 B
11: F R2 F2 U2 F U2 R2
12: F2 D2 L2 B' L2 D2 F2
13: F2 R2 F U2 F U2 R2
14: B2 U2 R2 B' R2 U2 B2
15: B' R2 B2 U2 B' U2 R2
search finished in 0.031250s
"""