import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#PLL search (using only UDRF)
scramble="L F' L B' U2 L D R L2 U' R2 D L2 U' R2 F2 D F2 R2 F'"
scramble=sv.solve_F2L(scramble, "z2", True, True, True, True, 15, False, 2, "xxxxcross", mv.move_UDLRFB)
scramble=sv.solve_LL_substep(scramble, "", False, True, False, True, 14, False, 1, "OLL", mv.move_UDLRFB)
scramble=sv.solve_LL(scramble, "", 13, True, 1, "PLL", mv.move_UDRF)

"""
z2 U2 L2 D' R' U F B' R' U' F' R2 U L2 F2  // xxxxcross No.2
F U2 R' F' U' F U R2 U2 R' F'  // OLL No.1
1: R2 F2 U' F2 U F2 D' F2 D R2
2: R2 F2 U' F2 D R2 D' R2 U R2
3: U R2 U' R2 D R2 D' F2 U F2 R2
4: U R2 D' F2 D F2 U' F2 U F2 R2
5: R2 F2 U' F2 U F2 D' F2 D R2 U
6: R2 F2 U' F2 U F2 D' F2 D R2 U2
7: R2 F2 U' F2 U F2 D' F2 D R2 U'
8: R2 F2 U' F2 D R2 D' R2 U R2 U
9: R2 F2 U' F2 D R2 D' R2 U R2 U2
10: R2 F2 U' F2 D R2 D' R2 U R2 U'
11: R2 F' U' F U F2 D' F' D F' R2
12: U R2 U' R2 D R2 D' F2 U F2 R2 U
13: U R2 U' R2 D R2 D' F2 U F2 R2 U2
14: U R2 U' R2 D R2 D' F2 U F2 R2 U'
15: U R2 D' F2 D F2 U' F2 U F2 R2 U
16: U R2 D' F2 D F2 U' F2 U F2 R2 U2
17: U R2 D' F2 D F2 U' F2 U F2 R2 U'
18: U R2 F D' F D F2 U' F' U F R2
19: U F' U2 R' U F U' F' U' R U' F
20: U F' U' R F R' U' R F' R' U2 F
21: U2 F' U R' U F U F' U' R U2 F
22: U2 F' U2 R F R' U R F' R' U F
23: D R2 F2 U' F2 U F2 D' F2 D R2 D'
24: D R2 F2 U' F2 D R2 U D2 F2 U F2
25: D R2 F2 U' F2 D R2 D' R2 U R2 D'
26: D2 R2 F2 U' F2 U F2 D' F2 D R2 D2
27: D2 R2 F2 U' F2 D R2 D' R2 U R2 D2
28: D' R2 F2 U' F2 U F2 D' F2 D R2 D
29: D' R2 F2 U' F2 D R2 D' R2 U R2 D
30: R2 U' D R2 U' R2 U R2 D' R2 U R2
31: R2 U' D R2 D' F2 U F2 U' R2 U R2
32: R2 D' F2 R' U' R F2 R' U R D R2
33: R2 F2 U2 D R2 U R2 U D2 F2 D R2
34: R2 F2 U' F2 D R2 U D2 F2 U F2 D
35: R2 F' U' F U F2 D' F' D F' R2 U
36: R2 F' U' F U F2 D' F' D F' R2 U2
37: R2 F' U' F U F2 D' F' D F' R2 U'
38: R' U F U F' U2 R F R' U R F'
39: R' U' R F' R' U2 F U' F' U' R F
40: F R' U' R F' R' U2 F U' F' U' R
41: F' R' U F U F' U2 R F R' U R
42: U D R2 U' R2 D R2 D' F2 U F2 R2 D'
43: U D R2 D' F2 D F2 U' F2 U F2 R2 D'
44: U D2 R2 U' R2 D R2 D' F2 U F2 R2 D2
45: U D2 R2 D' F2 D F2 U' F2 U F2 R2 D2
46: U D' R2 U' R2 D R2 D' F2 U F2 R2 D
47: U D' R2 D' F2 D F2 U' F2 U F2 R2 D
48: U R2 U' R2 U F2 U' F2 D R2 U D' R2
49: U R2 U' R2 D R2 U' R2 U R2 U D' R2
50: U R2 D' R' U' R F2 R' U R F2 D R2
51: U R2 D' F2 U' D2 R2 U' R2 U2 D' F2 R2
52: U R2 F D' F D F2 U' F' U F R2 U
53: U R2 F D' F D F2 U' F' U F R2 U2
54: U R2 F D' F D F2 U' F' U F R2 U'
55: U F2 U' D F2 U' F2 U F2 D' F2 U F2
56: U F2 U' F2 R' U' R F2 R' U R U F2
57: U F' U2 R' U F U' F' U' R U' F U
58: U F' U2 R' U F U' F' U' R U' F U2
59: U F' U2 R' U F U' F' U' R U' F U'
60: U F' U' R F R' U' R F' R' U2 F U
61: U F' U' R F R' U' R F' R' U2 F U2
62: U F' U' R F R' U' R F' R' U2 F U'
63: U F' U' F R' U' R F' R' U R U F
64: U2 D' F2 U' F2 U' D2 R2 D' F2 U F2 R2
65: U2 F2 U' R' U' R F2 R' U R F2 U F2
66: U2 F2 U' F2 U' D2 R2 D' F2 U F2 R2 D'
67: U2 F2 U' F2 D F2 U' F2 U F2 U D' F2
68: U2 F' U R' U F U F' U' R U2 F U
69: U2 F' U R' U F U F' U' R U2 F U2
70: U2 F' U R' U F U F' U' R U2 F U'
71: U2 F' U2 R F R' U R F' R' U F U
72: U2 F' U2 R F R' U R F' R' U F U2
73: U2 F' U2 R F R' U R F' R' U F U'
74: U2 F' U' R' U' R F R' U R F' U F
75: D R2 U' D R2 D' F2 U F2 D' F2 U F2
76: D R2 F2 U' F2 U F2 D' F2 D R2 U D'
77: D R2 F2 U' F2 U F2 D' F2 D R2 U2 D'
78: D R2 F2 U' F2 U F2 D' F2 D R2 U' D'
79: D R2 F2 U' F2 D R2 U D2 F2 U F2 U
80: D R2 F2 U' F2 D R2 U D2 F2 U F2 U2
81: D R2 F2 U' F2 D R2 U D2 F2 U F2 U'
82: D R2 F2 U' F2 D R2 D' R2 U R2 U D'
83: D R2 F2 U' F2 D R2 D' R2 U R2 U2 D'
84: D R2 F2 U' F2 D R2 D' R2 U R2 U' D'
85: D R2 F' U' F U F2 D' F' D F' R2 D'
86: D2 R2 F2 U' F2 U F2 D' F2 D R2 U D2
87: D2 R2 F2 U' F2 U F2 D' F2 D R2 U2 D2
88: D2 R2 F2 U' F2 U F2 D' F2 D R2 U' D2
89: D2 R2 F2 U' F2 D R2 U D2 F2 U F2 D'
90: D2 R2 F2 U' F2 D R2 D' R2 U R2 U D2
91: D2 R2 F2 U' F2 D R2 D' R2 U R2 U2 D2
92: D2 R2 F2 U' F2 D R2 D' R2 U R2 U' D2
93: D2 R2 F' U' F U F2 D' F' D F' R2 D2
94: D' R2 F2 U' F2 U F2 D' F2 D R2 U D
95: D' R2 F2 U' F2 U F2 D' F2 D R2 U2 D
96: D' R2 F2 U' F2 U F2 D' F2 D R2 U' D
97: D' R2 F2 U' F2 D R2 U D2 F2 U F2 D2
98: D' R2 F2 U' F2 D R2 D' R2 U R2 U D
99: D' R2 F2 U' F2 D R2 D' R2 U R2 U2 D
100: D' R2 F2 U' F2 D R2 D' R2 U R2 U' D
101: D' R2 F' U' F U F2 D' F' D F' R2 D
102: R F R' U R F' R2 U F U2 F' U' R
103: R F' R2 U F U F' U' R U' R F R'
104: R F' R' U2 R' U F U2 F' U' R2 F R'
105: R2 U' D R2 U' R2 U R2 D' R2 U R2 U
106: R2 U' D R2 U' R2 U R2 D' R2 U R2 U2
107: R2 U' D R2 U' R2 U R2 D' R2 U R2 U'
108: R2 U' D R2 U' R2 U2 D' F2 D' F2 D R2
109: R2 U' D R2 D' F2 U F2 U' R2 U R2 U
110: R2 U' D R2 D' F2 U F2 U' R2 U R2 U2
111: R2 U' D R2 D' F2 U F2 U' R2 U R2 U'
112: R2 U' D R2 D' F2 U F2 D' F2 U F2 D
113: R2 U' R' F R D R2 D' R' F' R' U R2
114: R2 D' F2 R' U' R F2 R' U R D R2 U
115: R2 D' F2 R' U' R F2 R' U R D R2 U2
116: R2 D' F2 R' U' R F2 R' U R D R2 U'
117: R2 D' F' R F' U' F2 U F R' F' D R2
118: R2 F R U' F' U2 F U R U2 R2 F' R2
119: R2 F2 U2 D R2 U R2 U D2 F2 D R2 U
120: R2 F2 U2 D R2 U R2 U D2 F2 D R2 U2
121: R2 F2 U2 D R2 U R2 U D2 F2 D R2 U'
122: R2 F2 U' F2 D R2 U D2 F2 U F2 U D
123: R2 F2 U' F2 D R2 U D2 F2 U F2 U2 D
124: R2 F2 U' F2 D R2 U D2 F2 U F2 U' D
125: R2 F2 U' F2 R' D R' D' R2 U R U' R
126: R2 F' U' F U R U F' U' F2 R' F' R2
127: R2 F' R2 U2 R' U F U2 F' U' R' F R2
128: R' U R' U' R2 D R D' R F2 U F2 R2
129: R' U F U F' U2 R F R' U R F' U
130: R' U F U F' U2 R F R' U R F' U2
131: R' U F U F' U2 R F R' U R F' U'
132: R' U F U' F' U' R2 F R' U2 R F' R'
133: R' U F' U2 F R U' R' U2 F R' F' R2
134: R' U' R F' R' U2 F U' F' U' R F U
135: R' U' R F' R' U2 F U' F' U' R F U2
136: R' U' R F' R' U2 F U' F' U' R F U'
137: R' U' R' D R2 U' R' U R2 D' R2 U R
138: R' F R' U' R2 U' R2 U R' F' R U R2
139: R' F R' D' F2 U' F2 D R' F' R U R2
140: F U R2 U' R2 D R2 D' F2 U F2 R2 F'
141: F U R2 D' F2 D F2 U' F2 U F2 R2 F'
142: F U F' U' R U2 R F R' U2 R F' R2
143: F R2 F2 U' F2 U F2 D' F2 D R2 U' F'
144: F R2 F2 U' F2 D R2 D' R2 U R2 U' F'
145: F R' U F U F' U2 R F R' U R F2
146: F R' U' R F' R' U2 F U' F' U' R U
147: F R' U' R F' R' U2 F U' F' U' R U2
148: F R' U' R F' R' U2 F U' F' U' R U'
149: F2 U R2 U' R2 D R2 D' F2 U F2 R2 F2
150: F2 U R2 D' F2 D F2 U' F2 U F2 R2 F2
151: F2 R2 F2 U' F2 U F2 D' F2 D R2 U' F2
152: F2 R2 F2 U' F2 D R2 D' R2 U R2 U' F2
153: F2 R' U F U F' U2 R F R' U R F
154: F2 R' U' R F' R' U2 F U' F' U' R F'
155: F' U R2 U' R2 D R2 D' F2 U F2 R2 F
156: F' U R2 D' F2 D F2 U' F2 U F2 R2 F
157: F' U' R2 F R' U2 R F' R' U2 R' U F
158: F' R2 F2 U' F2 U F2 D' F2 D R2 U' F
159: F' R2 F2 U' F2 D R2 D' R2 U R2 U' F
160: F' R' U F U F' U2 R F R' U R U
161: F' R' U F U F' U2 R F R' U R U2
162: F' R' U F U F' U2 R F R' U R U'
163: F' R' U' R F' R' U2 F U' F' U' R F2
search finished in 4.845202s
"""