import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#Last two slots(BR&FR)+Last Layer search(using only URF)
scramble="B2 U R2 D F2 R2 D F2 U' L2 U2 F L2 U' B' L2 U' L R2 B2"
scramble=sv.solve_F2L(scramble, "z2", True, False, False, True, 12, False, 1, "xxcross", mv.move_UDLRFB)
scramble=sv.solve_LL(scramble, "", 18, True, 1, "L2SLL", mv.move_URF)

"""
z2 D R2 B' U' L D' B2 U' R2 F'  // xxcross No.1
1: U R' U' F U F R' F' U' F2 U' F R' U2 R' U R'
2: U' R' F R' F2 U' F U F R' U R U' R2 F' U R2
3: U R' U' F U F R' F' U' F2 U' F R' U2 R' U R' U
4: U R' U' F U F R' F' U' F2 U' F R' U2 R' U R' U2
5: U R' U' F U F R' F' U' F2 U' F R' U2 R' U R' U'
6: U2 R2 F2 R' F R U2 F2 R' F2 U' R2 F R U R F2 R'
7: U2 F2 R2 F' U2 R2 U' R2 U' R2 F' U2 F R U2 R2 F' R
8: U2 F' U' R2 F R F2 U' F R2 F2 U2 R' U2 F2 R' U' F
9: U' R' F R' F2 U' F U F R' U R U' R2 F' U R2 U
10: U' R' F R' F2 U' F U F R' U R U' R2 F' U R2 U2
11: U' R' F R' F2 U' F U F R' U R U' R2 F' U R2 U'
12: R U2 F2 U R2 U F R2 U2 F2 R2 U' R U F' U2 F R'
13: F2 R' F' U2 F' R2 F2 R F' R2 U2 R' F2 R F R' U F
search finished in 342.534593s
"""