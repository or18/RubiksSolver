import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#xxcross(BL&FL slots solved) search with pre-rotation z2 y
scramble="L2 B U2 B' F2 U2 B U2 R2 D2 F2 L2 R' U L D' L2 R' F R2"
scramble=sv.solve_F2L(scramble, "z2 y", True, False, False, True, 11, True, 1, "xxcross", mv.move_UDLRFB)

"""
start creating prune table
d=0, 0.000022%
d=1, 0.000258%
d=2, 0.002929%
d=3, 0.032433%
d=4, 0.334345%
d=5, 3.060159%
d=6, 21.462485%
d=7, 77.584540%
d=8, 99.950649%
d=9, 100.000000%
d=10, 100.000000%
d=11, 100.000000%
created prune table in 9.696173s and saved to RubiksSolver/table/edge616182022_corner21_prune_table
1: z2 y R B2 L' F' D' F2 U F' B D'
2: z2 y U2 L2 B L U D F' U B2 L D2
3: z2 y U2 L' R' D F' U' B' U2 L2 B D2
4: z2 y U2 B U2 L' R B U L2 D' F' B
5: z2 y U2 B U2 L' B R U L2 D' F' B
6: z2 y U2 B R B' L' D F' U B D2 F'
7: z2 y D2 L' R' D B' U R2 D2 B D2 F
8: z2 y D2 F2 R' F U' F D B' R' U' F2
9: z2 y D' L' D2 B D' L2 F' L2 U L B
10: z2 y L R F B2 U L2 D' L2 F' D' B'
11: z2 y L R B2 D F' R2 D' R2 F D2 B'
12: z2 y L R B2 D' L2 U B L2 F' D' B2
13: z2 y L R B2 D' L2 U' F2 B L2 D' B2
14: z2 y L R B' U B' D F' R2 U' B2 D
15: z2 y L' R U D R2 B D R F' R D2
16: z2 y L' R D2 B U R D F' B R D2
17: z2 y R B2 L2 F2 L F' U D' F' B D'
18: z2 y R B2 L' F' D' F2 U F' B U D'
19: z2 y R B2 L' F' D' F2 U F' B U2 D'
20: z2 y R B2 L' F' D' F2 U F' B U' D'
21: z2 y R B' L B' U D F' R2 U' B2 D
22: z2 y F R2 D' F' L' U R2 B D2 R D
23: z2 y F' D L' U' L2 U2 F' D2 F2 L D'
24: z2 y F' L' B2 D' B' U F L' U L2 D'
25: z2 y B2 L' B' L2 R B2 U2 D' B' U' F'
search finished in 0.047282s
"""