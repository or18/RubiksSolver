import RubiksSolver.solver as sv
import RubiksSolver.move as mv
import time
#CFOP example solve
scramble="L' D R2 D2 L2 F2 U2 B R2 F2 L2 R2 D U R2 F' D R' D'"
t=time.time()
scramble=sv.solve_F2L(scramble, "z2", False, False, False, False, 8, False, 1, "cross", mv.move_UDLRFB)
scramble=sv.solve_F2L(scramble, "", True, False, False, False, 10, False, 1, "F2L#1", mv.move_UDLRFB)
scramble=sv.solve_F2L(scramble, "", True, False, False, True, 13,False, 1, "F2L#2", mv.move_UDLRFB)
scramble=sv.solve_F2L(scramble, "", True, True, False, True, 14, False, 1, "F2L#3", mv.move_UDLRFB)
scramble=sv.solve_F2L(scramble, "", True, True, True, True, 15, False, 1, "F2L#4", mv.move_UDLRFB)
scramble=sv.solve_LL_substep(scramble, "", False, True, False, True, 14, False, 1, "OLL", mv.move_UDLRFB)
scramble=sv.solve_LL(scramble, "", 16, False, 1, "PLL", mv.move_UDLRFB)
scramble=sv.solve_LL_AUF(scramble, "", 20, False, 1, "AUF", mv.move_UDLRFB)
print(f"solution found in {time.time()-t:.4f}s")

"""
z2 D' L F D' F'  // cross No.1
L U B2 L2 B' L B' L'  // F2L#1 No.1
U L' U L F U F'  // F2L#2 No.1
B U' B'  // F2L#3 No.1
U R U R' U2 F' U2 F  // F2L#4 No.1
R' U' F' U F R  // OLL No.1
L2 D R2 D B2 R D L' D2 R D' L'  // PLL No.1
// AUF
solution found in 32.3155s
"""