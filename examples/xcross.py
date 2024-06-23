import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#xcross(BL slot solved) search with pre-rotation z2
scramble="F2 D2 U2 F' R2 B' R2 D2 B D2 L U' L2 U' B2 L' F' U' R2"
scramble=sv.solve_F2L(scramble, "z2", True, False, False, False, 9, True, 1, "xcross", mv.move_UDLRFB)

"""
start creating corner move table
created corner move table in 0.000000s and save to RubiksSolver/table/corner_move_table
start creating multi move table
created multi move table in 40.742637s and save to RubiksSolver/table/5edges_move_table
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
created prune table in 21.237136s and saved to RubiksSolver/table/edge016182022_corner12_prune_table
1: z2 U2 L2 R' D R2 U' F' L'
2: z2 U2 L2 R' D R2 F' U' L'
3: z2 R B D2 L U' R B2 R
4: z2 R B D2 L B2 U' R B2
5: z2 F2 L D' F R F L F'
6: z2 U2 D L2 R' D R2 U' F' L'
7: z2 U2 D L2 R' D R2 F' U' L'
8: z2 U2 D2 L2 R' D R2 U' F' L'
9: z2 U2 D2 L2 R' D R2 F' U' L'
10: z2 U2 D' L2 R' D R2 U' F' L'
11: z2 U2 D' L2 R' D R2 F' U' L'
12: z2 U2 L2 R' U F2 U2 D L' F
13: z2 U2 L2 R' U F2 U2 D F L'
14: z2 U2 L2 R' D R2 U' F L' F2
15: z2 U2 L2 R' D R2 U' F2 L' F
16: z2 U2 L2 R' D R2 U' F' L' U
17: z2 U2 L2 R' D R2 U' F' L' U2
18: z2 U2 L2 R' D R2 U' F' L' U'
19: z2 U2 L2 R' D R2 F2 U' L' F
20: z2 U2 L2 R' D R2 F2 U' F L'
21: z2 U2 L2 R' D R2 F' U' L' U
22: z2 U2 L2 R' D R2 F' U' L' U2
23: z2 U2 L2 R' D R2 F' U' L' U'
24: z2 U2 L2 F' U L' R2 B' R' B2
25: z2 U2 F L2 F' U L R U' B2
26: z2 U2 F L2 F' U R U' L B2
27: z2 U2 F L2 F' L U R U' B2
28: z2 U2 B D2 B' U L R U' B2
29: z2 U2 B D2 B' U R U' L B2
30: z2 U2 B D2 B' L U R U' B2
31: z2 U' L2 B2 R D2 F' U' B2 R
32: z2 U' B L' D2 L2 B' R U' B2
33: z2 U' B L' D2 B' L2 R U' B2
34: z2 D R B D2 L U' R B2 R
35: z2 D R B D2 L B2 U' R B2
36: z2 D F2 L D' F R F L F'
37: z2 D2 R B D2 L U' R B2 R
38: z2 D2 R B D2 L B2 U' R B2
39: z2 D2 F2 L D' F R F L F'
40: z2 D' R B D2 L U' R B2 R
41: z2 D' R B D2 L B2 U' R B2
42: z2 D' F2 L D' F R F L F'
43: z2 L U R F B D' L' R2 D
44: z2 L R B L U F' L2 B L
45: z2 L R B' U2 R' F U R B2
46: z2 L R2 U2 R2 U R F U' B2
47: z2 L2 U R F L' D' R2 D F2
48: z2 L2 U' B2 R D2 F' U' B2 R
49: z2 L2 R U R' U2 F' L' R B2
50: z2 L2 R F' L2 U' L B U B
51: z2 L2 R' D R U' F' U2 L' R
52: z2 L' D' F2 L D' F' R F L
53: z2 L' F2 L D' R D2 B D2 L
54: z2 R U L2 F' U B' L2 B L'
55: z2 R U R' U2 L2 F' L' R B2
56: z2 R U B2 R' U2 L F' R B2
57: z2 R U' L F R B2 U2 R' F
58: z2 R U' L F B2 L U2 F' L'
59: z2 R U' L F2 B2 L F' U2 L'
60: z2 R D2 B D2 L U' R B2 R'
61: z2 R B D2 L U' R B2 U R
62: z2 R B D2 L U' R B2 U2 R
63: z2 R B D2 L U' R B2 U' R
64: z2 R B D2 L U' R B2 R U
65: z2 R B D2 L U' R B2 R U2
66: z2 R B D2 L U' R B2 R U'
67: z2 R B D2 L B2 U' R B2 U
68: z2 R B D2 L B2 U' R B2 U2
69: z2 R B D2 L B2 U' R B2 U'
70: z2 R B L U' R B2 U2 R' F2
71: z2 R B L U' R B2 R' U2 F2
72: z2 R B L U' B2 L U2 L' F2
73: z2 R B L U' B2 L U2 F2 L'
74: z2 R B' L U2 R' F2 U R B2
75: z2 R B' L U2 F2 R' U R B2
76: z2 R2 D L2 U R D R2 F' L'
77: z2 R2 D L2 U R D F' L' R2
78: z2 R2 D L2 R U F2 D L' F
79: z2 R2 D L2 R U F2 D F L'
80: z2 R2 D L2 R D R2 U F' L'
81: z2 R2 D L2 R' U F' L2 B L
82: z2 R2 D2 F2 R D' R2 B L D2
83: z2 R' U F2 D2 F' D' L2 F' L
84: z2 R' D L2 R U' F' U2 L' R
85: z2 R' D R U' L2 F' U2 L' R
86: z2 R' F2 D' B L' U2 L2 R' D2
87: z2 R' B2 R2 U' L F R B2 R'
88: z2 F2 U L D' F R F L F'
89: z2 F2 U2 L D' F R F L F'
90: z2 F2 U' L D' F R F L F'
91: z2 F2 L D' F R F L U F'
92: z2 F2 L D' F R F L U2 F'
93: z2 F2 L D' F R F L U' F'
94: z2 F2 L D' F R F L F' U
95: z2 F2 L D' F R F L F' U2
96: z2 F2 L D' F R F L F' U'
97: z2 F2 L2 U2 L' D' F2 L R F'
98: z2 F2 L2 U2 L' D' F2 L F' R
99: z2 F' D F' L D' R F L F'
100: z2 B D2 B2 R B L U' R B2
101: z2 B2 R B L B U' R F B2
search finished in 0.031514s
"""