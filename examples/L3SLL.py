import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#Last three slots(BR&FR&FL)+Last Layer search (using only URF)
scramble="D' F U' F2 R2 U2 B2 L2 D B2 F2 U2 L' D2 B R F2 R U2"
scramble=sv.solve_F2L(scramble, "z2", True, False, False, False, 10, False, 1, "xcross", mv.move_UDLRFB)
scramble=sv.solve_LL(scramble, "", 18, True, 1, "L3SLL", mv.move_URF)

"""
z2 U2 R' F' U2 L D' F R2  // xcross No.1
1: F' U F' R U2 R2 U2 F' U F2 U F R' F2 R2 F2
2: U R' F' U' F R U' F U F' R F U2 R2 U' F' R'
3: F' U F' R U2 R2 U2 F' U F2 U F R' F2 R2 F2 U
4: F' U F' R U2 R2 U2 F' U F2 U F R' F2 R2 F2 U2
5: F' U F' R U2 R2 U2 F' U F2 U F R' F2 R2 F2 U'
6: U R' F' U' F R U' F U F' R F U2 R2 U' F' R' U
7: U R' F' U' F R U' F U F' R F U2 R2 U' F' R' U2
8: U R' F' U' F R U' F U F' R F U2 R2 U' F' R' U'
9: U F' R U R F U2 F2 U R U' F2 R U2 F R2 U' F2
10: U2 R' U' F U F2 U2 R2 F U F' R F' U R U' F R2
search finished in 345.210285s
"""