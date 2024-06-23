import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#Last slot(FR)+Last Layer search (using only URF)
scramble="D2 R2 B2 F2 D' F2 D' R2 B2 L2 U2 R2 B' D2 U L D2 U2 F2 L' U2"
scramble=sv.solve_F2L(scramble, "z2", True, True, False, True, 14, False, 1, "xxxcross", mv.move_UDLRFB)
scramble=sv.solve_LL(scramble, "", 16, True, 1, "LSLL", mv.move_URF)

"""
z2 U R F2 L' D2 B' R' D2 B' U' D B R'  // xxxcross No.1
1: R F R F' U R' U2 R2 U R2 F' U F U' R2
2: U' F2 U2 F2 U F2 U F2 U2 R2 U2 F R' F' U2 R2
3: R U' R' U2 F2 U2 F U' F R U R' U' F2 U' F2
4: R F R F' U R' U2 R2 U R2 F' U F U' R2 U
5: R F R F' U R' U2 R2 U R2 F' U F U' R2 U2
6: R F R F' U R' U2 R2 U R2 F' U F U' R2 U'
7: R' F R2 F' U2 F R F2 U2 F2 U R' U' F' U' R'
8: F U' F U2 F2 R2 F' U2 F2 U2 F R' U' R2 F' R
search finished in 20.225830s
"""