import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#xxxxcross(BL&BR&FR&FL slots solved) search with pre-rotation z2 y2
scramble="B F2 U F2 R2 D' B2 U' B2 U2 L2 D' R' B L' D' L2 B2 U' F2 D'"
scramble=sv.solve_F2L(scramble, "z2 y2", True, True, True, True, 15, True, 1, "xxxxcross", mv.move_UDLRFB)

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
created prune table in 12.060405s and saved to RubiksSolver/table/edge416182022_corner18_prune_table
1: z2 y2 U D' L F' L U2 R2 U2 L2 B U' L2 B R'
2: z2 y2 U L F' L' B2 U L2 U' F' U' D2 F B R
3: z2 y2 U F R2 D L2 B' R F2 R U D2 F R F
4: z2 y2 U2 R2 U D R' U L2 R' F' R' B R2 U2 F2
5: z2 y2 D L2 D' F R2 D F' R D R F D2 R' B
6: z2 y2 D R B2 U R' B2 L2 D2 R' B' L F D2 B2
7: z2 y2 R2 U' D2 L U2 L' U D' L2 B U R2 F' R
8: z2 y2 R2 D L U' B U2 B' L' U' L2 B R2 F' R
9: z2 y2 R2 D B R2 F' D F' D R U' F' L F2 L'
10: z2 y2 R' U' D L R F U L' F' D2 R F2 R F
11: z2 y2 F' U R D2 B' D' B2 L' U' L2 D2 F2 B' L
12: z2 y2 U D R2 B2 L F' R2 F' U' L D2 B' L F B2
13: z2 y2 U D2 L B' U' L' B R' D L F' L B L2 R2
14: z2 y2 U D2 L B' U' L' B R' D L2 B L' F' L' R2
15: z2 y2 U D' L F' L U2 R2 U2 L2 B U' L2 B R' U
16: z2 y2 U D' L F' L U2 R2 U2 L2 B U' L2 B R' U2
17: z2 y2 U D' L F' L U2 R2 U2 L2 B U' L2 B R' U'
18: z2 y2 U D' L F' L' R2 D2 R2 D2 R2 B U' L2 B R'
19: z2 y2 U D' L F' R B2 R2 B2 L' R' B U' L2 B R'
20: z2 y2 U D' F D L R D R2 U2 F D' L' B2 L2 F2
21: z2 y2 U L F' L' B2 U L2 U' F' U' D2 F B R U
22: z2 y2 U L F' L' B2 U L2 U' F' U' D2 F B R U2
23: z2 y2 U L F' L' B2 U L2 U' F' U' D2 F B R U'
24: z2 y2 U L' F R2 D' B L2 D2 R' F2 L U B' U' F2
25: z2 y2 U R D R F2 B' L' D R2 F2 U2 B D2 B2 R
26: z2 y2 U R D R F2 B' L' D R2 B2 D2 B U2 F2 R
27: z2 y2 U R B' R2 D' F L D2 R F2 L U2 D2 F R
28: z2 y2 U R2 U2 D R2 U B2 L2 F R' D R2 F R' B
29: z2 y2 U R2 U2 D B2 L2 B R' F L' U R U2 L R'
30: z2 y2 U R2 D L' B2 L' R2 D2 R' B R' U R2 F R
31: z2 y2 U R2 D B2 L2 R D2 B2 L' U B' U' R F R
32: z2 y2 U R' B2 R2 B' R2 D' F2 L' B2 R2 F U2 B' L'
33: z2 y2 U F R2 D L2 R F2 R' B' R2 U D2 F R F
34: z2 y2 U F R2 D L2 B' R F2 R U D2 F R F U
35: z2 y2 U F R2 D L2 B' R F2 R U D2 F R F U2
36: z2 y2 U F R2 D L2 B' R F2 R U D2 F R F U'
37: z2 y2 U F2 U' R2 B' U' R' F' L2 R' F2 R2 U' L2 R'
38: z2 y2 U F2 L2 U' F B' U L' U2 D' B2 D' F' U2 R'
39: z2 y2 U B2 R2 B2 D' F' R' F2 U2 L F2 R' B2 U' F
40: z2 y2 U2 D L' U' D2 L U' R' D' B2 R2 U' F' U2 B'
41: z2 y2 U2 D R2 U2 L2 R F' L' F2 L2 D' L' D2 B R2
42: z2 y2 U2 R2 U D R' U L2 R' F' R' B R2 U2 F2 U
43: z2 y2 U2 R2 U D R' U L2 R' F' R' B R2 U2 F2 U2
44: z2 y2 U2 R2 U D R' U L2 R' F' R' B R2 U2 F2 U'
45: z2 y2 U2 R2 U R2 U R' D L' D2 L' F2 R' B R' F
46: z2 y2 U2 F2 U' L' U L' U' F D2 R U' D' L2 D F
47: z2 y2 U2 F2 L2 U' L2 D' L2 R' B L2 R D' R2 B' R'
48: z2 y2 U2 F2 L' U' L2 F D2 L F' L R F B L2 B'
49: z2 y2 U2 F' L' U R2 B2 R F' L D R2 F2 U B' L
50: z2 y2 U' R U F2 U L' B2 U L2 R2 B' R2 F' U L2
51: z2 y2 U' R2 D R2 F2 L2 F B2 D' B' R D' B' R B
52: z2 y2 U' F' R D L2 D' L U' B' R' D2 F R U F'
53: z2 y2 D L2 U' R' U R2 B R2 B2 D F2 D2 F' D' B2
54: z2 y2 D L2 D L' F L' B' R' B D F' R2 D2 L R'
55: z2 y2 D L2 D' F R2 D F' R D R F D2 R' B U
56: z2 y2 D L2 D' F R2 D F' R D R F D2 R' B U2
57: z2 y2 D L2 D' F R2 D F' R D R F D2 R' B U'
58: z2 y2 D L2 R D2 B' D2 L2 F2 L2 R' D R B2 U F
59: z2 y2 D L2 F' U D' R2 B' L D' F' R2 F' L D2 B2
60: z2 y2 D L2 F' B' D' F2 B D R B U' F2 R U2 F2
61: z2 y2 D L' R D2 L' D' F2 L D2 L' B2 U B' R' F
62: z2 y2 D R B2 U R' B2 L2 D2 R' B' L F D2 B2 U
63: z2 y2 D R B2 U R' B2 L2 D2 R' B' L F D2 B2 U2
64: z2 y2 D R B2 U R' B2 L2 D2 R' B' L F D2 B2 U'
65: z2 y2 D R2 F D R' F2 D' F' L2 D2 B' U D' F B2
66: z2 y2 D R' B2 U' F2 L2 R2 U' F2 U2 B' R F' R F2
67: z2 y2 D F2 D' R U' D2 R2 F' R B2 U B D R D
68: z2 y2 D B L2 B L' R' B2 D' F2 R' D' F2 B2 L' F'
69: z2 y2 D2 L D L2 R' D' R U2 R2 U' L U' B R' F'
70: z2 y2 D2 L2 U2 F2 L2 F' U' L D2 F2 U' L2 F2 R F'
71: z2 y2 D2 L2 D' R2 B L' R2 U B2 L2 F' B2 L' F' R'
72: z2 y2 D2 R' B2 D2 R F2 L2 D' F U D2 R U2 L' F
73: z2 y2 D2 B R2 B U R B' L' B L' D R2 D B L2
74: z2 y2 D2 B' R U' B' U2 D2 F' L U2 D2 R F' U' R
75: z2 y2 D2 B' R2 F' L R F' D' R2 U F' L D2 L2 B'
76: z2 y2 D2 B' R2 F' L F' R D' R F' U L2 D2 L B'
77: z2 y2 D2 B' R' F R' U' F' L2 D2 R2 F' D L2 U' R'
78: z2 y2 D' L2 D' B U2 R' B D' F' U2 L' D' L2 D2 B'
79: z2 y2 D' F2 L2 U2 D' F' L' R2 B2 U2 R D B2 R2 F'
80: z2 y2 L R' U2 L2 F' U D' R U' B' L U' F' L D2
81: z2 y2 L F L B' U D L F R2 F' D2 R' U2 B D'
82: z2 y2 L B2 D R' D' F2 B' L R2 B' D R F B2 L'
83: z2 y2 L2 U R' D L2 U R U' F' B D2 F R F R
84: z2 y2 L2 U' R2 U' F B2 R2 U2 F' U2 D B2 R' U F
85: z2 y2 L2 D R' U B L D B' D2 F2 U D F' L2 F2
86: z2 y2 L2 D2 R' F R D L2 B' D2 F U2 L2 D B2 R
87: z2 y2 L2 F' B L2 D' F2 D F2 U B2 R U' B' L2 D'
88: z2 y2 L' R2 B L D B2 R2 F' D2 R D' L' U' D F2
89: z2 y2 L' F L F R2 D R2 D F' L2 D R' F R2 B
90: z2 y2 L' F R2 D2 L' R2 D' R' D2 F D R2 B2 U B'
91: z2 y2 R U R B' D R2 F L R' D2 R F2 D2 F R
92: z2 y2 R U R2 F D L2 F2 R' B' R2 U D2 F R F
93: z2 y2 R U F L R U2 B R' D' B2 D F B' L F2
94: z2 y2 R U B2 D R2 D' F' U2 R' U2 L D2 L F R
95: z2 y2 R U2 D2 F' U2 L B2 U D2 R F2 L F' U L
96: z2 y2 R2 U' D2 L U2 L' U D' L2 B U R2 F' R U
97: z2 y2 R2 U' D2 L U2 L' U D' L2 B U R2 F' R U2
98: z2 y2 R2 U' D2 L U2 L' U D' L2 B U R2 F' R U'
99: z2 y2 R2 U' B2 D2 F2 U F2 L' D' L' R' F' R2 B R2
100: z2 y2 R2 D L U' B U2 B' L' U' L2 R2 F' R2 B R'
101: z2 y2 R2 D L U' B U2 B' L' U' L2 B R2 F' R U
102: z2 y2 R2 D L U' B U2 B' L' U' L2 B R2 F' R U2
103: z2 y2 R2 D L U' B U2 B' L' U' L2 B R2 F' R U'
104: z2 y2 R2 D L2 B U' L R2 F L' R' B2 D B2 R2 F
105: z2 y2 R2 D L2 B L' U' L R2 F R' B2 D B2 R2 F
106: z2 y2 R2 D L2 B2 U2 B L2 B2 L' U' L R' F' U' F'
107: z2 y2 R2 D F U2 F' L2 B2 R' F2 U2 D' L' U' D F'
108: z2 y2 R2 D B L2 B L R' U2 F2 U' L U' F2 U' F
109: z2 y2 R2 D B R2 F' D F' D R U' F' L F2 L' U
110: z2 y2 R2 D B R2 F' D F' D R U' F' L F2 L' U2
111: z2 y2 R2 D B R2 F' D F' D R U' F' L F2 L' U'
112: z2 y2 R2 D B R2 F' D F' D R F2 U' F' R U2 R'
113: z2 y2 R2 D B R2 F' D2 R U2 L' U' F' U2 F L F2
114: z2 y2 R2 D B R2 F' D2 F2 R U L' F' U2 F L F2
115: z2 y2 R2 D B R2 F' D2 F2 R U F' U2 F' R U2 R'
116: z2 y2 R2 D B2 L2 U B' R' F2 U2 R' D F2 D2 R F'
117: z2 y2 R2 D B' R' F2 L R2 B' R2 U2 D' L' U' D F'
118: z2 y2 R2 D' F' U2 R2 D2 L R' B D' F' L' D2 B' L'
119: z2 y2 R2 D' F' B R2 D2 F U' R' F' B L F2 L' B'
120: z2 y2 R2 D' B R U2 F' B2 L U L D L' B2 D F'
121: z2 y2 R2 F R2 D2 F B' L D L' U' F' U2 B2 U2 R
122: z2 y2 R2 F2 L2 D B2 U' L2 R F L2 R U' L2 B' R'
123: z2 y2 R2 B D L2 U R D B' R' B2 U L2 U R' F
124: z2 y2 R2 B L B2 U2 L U' B2 D B' U2 L R' U F
125: z2 y2 R2 B L B2 U2 L U' B2 D B' U2 R' U L F
126: z2 y2 R' U B2 R U2 F2 U L2 R' D2 L U' B R' F
127: z2 y2 R' U' D L R F U L' F' D2 R F2 R F U
128: z2 y2 R' U' D L R F U L' F' D2 R F2 R F U2
129: z2 y2 R' U' D L R F U L' F' D2 R F2 R F U'
130: z2 y2 R' D L' D2 L' F2 D' R F2 D2 R F R2 B R2
131: z2 y2 R' B R' U D' R' F B' L' R2 D F2 B D2 R2
132: z2 y2 F R B2 R B' R D R F U' F D2 F R F
133: z2 y2 F R2 F' D B' L2 D' R2 F L' D2 R' U F B'
134: z2 y2 F B' U' R' D2 R F U' L F2 D2 B2 D R D'
135: z2 y2 F2 U' D' F2 D2 R U L2 R' F' R' B R2 U2 F2
136: z2 y2 F2 D2 R' B R U' F' D' F2 D2 F2 L2 R U L2
137: z2 y2 F2 L D F U R2 F2 R F D' F B' L D2 R'
138: z2 y2 F2 L2 U' L D L2 D R2 B' R' U' F' D' L' D
139: z2 y2 F2 B L2 B U B R2 B D L' R B2 L' U F
140: z2 y2 F2 B2 D B2 D2 L D L' U' F D2 F L2 R F
141: z2 y2 F' U R D2 B' D' B2 L' U' L2 D2 F2 B' L U
142: z2 y2 F' U R D2 B' D' B2 L' U' L2 D2 F2 B' L U2
143: z2 y2 F' U R D2 B' D' B2 L' U' L2 D2 F2 B' L U'
144: z2 y2 F' U F' L' U R' D' L' F L' R2 F2 U L B2
145: z2 y2 F' L F' D F' D F D L U' L2 D' R2 B' R'
146: z2 y2 F' L B U D2 F' U' L B' D' R2 B L' U' R'
147: z2 y2 F' R2 D2 L2 D B D R2 U B' L' B D2 R F'
148: z2 y2 F' B' U2 L U' F D' F U2 D2 B2 D F' D' R'
149: z2 y2 F' B' U2 L U' F D' F' D B2 U2 D2 F D' R'
150: z2 y2 B2 U L B2 D' B U' D2 R D R2 D' F2 D F
151: z2 y2 B2 U R F2 L U2 R U B' R U' F' B R B'
152: z2 y2 B2 U2 F' U' L2 F2 D2 L B2 R D2 F R2 U' B'
153: z2 y2 B' U L R D2 R' F' L' B2 U' B' L' R' B2 L'
154: z2 y2 B' U' D R' D F2 U2 R' B R F' D2 L' F2 D2
155: z2 y2 B' D2 L2 F' D' B L2 B L' B' L U' R2 F2 R
156: z2 y2 B' D2 L2 F' L2 D' R2 F2 L' D2 L' D F D2 R
search finished in 174.367667s
"""