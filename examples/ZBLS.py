import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#ZBLS(FR) search (using only UDRF)
scramble="B' R2 D' F' D2 R2 U2 L2 F' R2 U2 B U2 L2 R' U' L F2 R B R'"
scramble=sv.solve_F2L(scramble, "z2", True, True, False, True, 14, False, 1, "xxxcross", mv.move_UDLRFB)
scramble=sv.solve_LL_substep(scramble, "", False, False, False, True, 12, True, 1, "VHLS", mv.move_UDRF)

"""
z2 U2 L B2 R U F B2 D2 B L' D F'  // xxxcross No.1
1: U F U R U' R2 F' R
2: R U2 R2 F R F2 U F
3: U F U R U' R2 F' R U
4: U F U R U' R2 F' R U2
5: U F U R U' R2 F' R U'
6: R U2 R2 F D' F D F2 R
7: R U2 R2 F R F2 U F U
8: R U2 R2 F R F2 U F U2
9: R U2 R2 F R F2 U F U'
10: R U2 R' F' U F R U' R'
11: R U' R' F R' F' R2 U2 R'
12: U F R2 U F' R F U' R2 F'
13: U F R2 F' U R U' F R2 F'
14: U2 D R2 U' F R F' U R2 D'
15: U' F U R U' R2 F' R2 U2 R'
16: R U R' U R' U' F' U F R
17: R U R' U F U R U' R' F'
18: R U F' U2 F U2 F R2 F' R
19: R U2 R2 F D' F D F2 R U
20: R U2 R2 F D' F D F2 R U2
21: R U2 R2 F D' F D F2 R U'
22: R U2 R2 F R F' U' F' U2 F
23: R U2 R' U2 F' U' F R U2 R'
24: R U2 R' F' U F U R U2 R'
25: R U2 R' F' U F R U' R' U
26: R U2 R' F' U F R U' R' U2
27: R U2 R' F' U F R U' R' U'
28: R U' R2 U' F' U F R2 U' R'
29: R U' R' F R' F' R2 U2 R' U
30: R U' R' F R' F' R2 U2 R' U2
31: R U' R' F R' F' R2 U2 R' U'
32: R2 U' F R F' R' U2 R U' R2
33: R' D' F' U' F U D R2 U R'
34: F' U' F U F R' F' R2 U R'
35: U R U' R' U2 F' U F R U R'
36: U R2 U2 R' U' R U' R F R F'
37: U F R2 U F' R F U' R2 F' U
38: U F R2 U F' R F U' R2 F' U2
39: U F R2 U F' R F U' R2 F' U'
40: U F R2 F' U R U' F R2 F' U
41: U F R2 F' U R U' F R2 F' U2
42: U F R2 F' U R U' F R2 F' U'
43: U2 D R2 U' F R F' U R2 U D'
44: U2 D R2 U' F R F' U R2 U2 D'
45: U2 D R2 U' F R F' U R2 U' D'
46: U' R U' R' F' U' F U2 R U R'
47: U' F U R U' R2 F' R2 U2 R' U
48: U' F U R U' R2 F' R2 U2 R' U2
49: U' F U R U' R2 F' R2 U2 R' U'
50: U' F' U2 F R' F R2 U R' U' F'
51: R U R2 F' U F U2 F' U' F R
52: R U R' U R' U' F' U F R U
53: R U R' U R' U' F' U F R U2
54: R U R' U R' U' F' U F R U'
55: R U R' U F U R U' R' F' U
56: R U R' U F U R U' R' F' U2
57: R U R' U F U R U' R' F' U'
58: R U R' F U R' F R F' U' F'
59: R U R' F' U2 F U2 F R' F' R
60: R U F' U2 F U2 F R2 F' R U
61: R U F' U2 F U2 F R2 F' R U2
62: R U F' U2 F U2 F R2 F' R U'
63: R U2 R2 F R F' U' F' U2 F U
64: R U2 R2 F R F' U' F' U2 F U2
65: R U2 R2 F R F' U' F' U2 F U'
66: R U2 R' U R' F R F' R U2 R'
67: R U2 R' U2 F' U' F U' R U' R'
68: R U2 R' U2 F' U' F R U2 R' U
69: R U2 R' U2 F' U' F R U2 R' U2
70: R U2 R' U2 F' U' F R U2 R' U'
71: R U2 R' U' F' U2 F U R U R'
72: R U2 R' F' U F U R U2 R' U
73: R U2 R' F' U F U R U2 R' U2
74: R U2 R' F' U F U R U2 R' U'
75: R U2 R' F' U2 F U' R' F R F'
76: R U2 F R' U F R F' U' F' R'
77: R U' R2 U' F' U F R2 U' R' U
78: R U' R2 U' F' U F R2 U' R' U2
79: R U' R2 U' F' U F R2 U' R' U'
80: R U' R2 F2 D' F' D F' R2 U2 R'
81: R U' R' F R' F' R U' R U' R'
82: R U' F D R2 D' F2 U F U R'
83: R F' U2 F U F D R2 D' F' R'
84: R2 U' F R F' R' U2 R U' R2 U
85: R2 U' F R F' R' U2 R U' R2 U2
86: R2 U' F R F' R' U2 R U' R2 U'
87: R' D' F' U' F U D R2 U R' U
88: R' D' F' U' F U D R2 U R' U2
89: R' D' F' U' F U D R2 U R' U'
90: R' F' R' U' R F R' U R' U R'
91: F R' F' R F' U' F U R U R'
92: F' U' F U F R' F' R2 U R' U
93: F' U' F U F R' F' R2 U R' U2
94: F' U' F U F R' F' R2 U R' U'
95: U D F U D' R U' R2 D F' D' R
96: U R U' R' U2 F' U F R U R' U
97: U R U' R' U2 F' U F R U R' U2
98: U R U' R' U2 F' U F R U R' U'
99: U R2 U2 R' U' R U' R F R F' U
100: U R2 U2 R' U' R U' R F R F' U2
101: U R2 U2 R' U' R U' R F R F' U'
102: U R' F U R2 U' R F' U2 R2 U2 R2
103: U F U D R2 F R F' R2 U' D' F'
104: U F U R2 U' R F' R' U R' U' R'
105: U F U R2 D R' U' R D' R F' R
106: U F U R2 D2 R' U' R D2 R F' R
107: U F U R' U' F' U R U2 R U R'
108: U F U R' F' R2 U F U2 F' U R'
109: U F U R' F' R' F R' U' R F' R2
110: U F D R2 U F R F' U' R2 D' F'
111: U F R D2 R' U R U' D2 R2 F' R
112: U F R2 D R2 U R U' R2 D' F' R
113: U F R2 D R' U R2 U' D' F' U R
114: U F' U' F2 R' F2 U' F U R2 U R'
115: U2 R U' R' F' U F U' F R' F' R
116: U2 R U' F D R2 D' F2 U F U2 R'
117: U2 R2 D R2 U' R' D' F R F U2 F2
118: U2 R' U2 R U R' F U R2 U' R' F'
119: U2 F R' F' R F' U' F U R U' R'
120: U2 F R' F' R F' U' F U2 R U2 R'
121: U' R U' R' U2 F' U F U' R U R'
122: U' R U' R' F' U' F U2 R U R' U
123: U' R U' R' F' U' F U2 R U R' U2
124: U' R U' R' F' U' F U2 R U R' U'
125: U' F U R U' R2 F' R U' R U' R'
126: U' F' U2 F R' F R2 U R' U' F' U
127: U' F' U2 F R' F R2 U R' U' F' U2
128: U' F' U2 F R' F R2 U R' U' F' U'
129: U' F' U' F2 R' F2 U' F U R2 U' R'
130: D R U2 R' U2 F' U' F D' R U2 R'
131: D R U' R' F R' F' R D' R U2 R'
132: D2 R U2 R' U2 F' U' F D2 R U2 R'
133: D2 R U' R' F R' F' R D2 R U2 R'
134: D' R U2 R' U2 F' U' F D R U2 R'
135: D' R U' R' F R' F' R D R U2 R'
136: R U D' R2 U F' U F U' R2 D R'
137: R U D' R2 U' F' U' F U2 R2 D R'
138: R U R2 U' F' U2 F U2 F' U' F R
139: R U R2 F U F2 U F2 U2 F' U R
140: R U R2 F R U R' U' F2 U F R
141: R U R2 F' U F U2 F' U' F R U
142: R U R2 F' U F U2 F' U' F R U2
143: R U R2 F' U F U2 F' U' F R U'
144: R U R2 F' U F U' F' U2 F U R
145: R U R2 F' U2 F U R U2 R' U' R
146: R U R' U D R' U' F' U F R D'
147: R U R' U D F U R U' R' F' D'
148: R U R' U D2 R' U' F' U F R D2
149: R U R' U D2 F U R U' R' F' D2
150: R U R' U D' R' U' F' U F R D
151: R U R' U D' F U R U' R' F' D
152: R U R' U R' F R F' U2 F' U2 F
153: R U R' U R' F R F' U' F' U F
154: R U R' U F R' F' R U R U' R'
155: R U R' U F R' F' R U2 R U2 R'
156: R U R' U2 R U2 R' U2 R' F R F'
157: R U R' U2 R' U' F R' F' R U R
158: R U R' U2 F' U' F2 R' F' R2 U' R'
159: R U R' F U R' U' F' U F R F'
160: R U R' F U R' F R F' U' F' U
161: R U R' F U R' F R F' U' F' U2
162: R U R' F U R' F R F' U' F' U'
163: R U R' F U2 F' U' F R U' R' F'
164: R U R' F R U R2 F R F' U' F'
165: R U R' F' U2 F U2 F R' F' R U
166: R U R' F' U2 F U2 F R' F' R U2
167: R U R' F' U2 F U2 F R' F' R U'
168: R U2 R2 U2 F D' F' U2 F2 D F2 R
169: R U2 R2 U' R' F R F' U F R F'
170: R U2 R2 F R F D' F U F' D F2
171: R U2 R2 F R F2 U' F U F' U F
172: R U2 R2 F2 U' F' D' F U D F2 R
173: R U2 R2 F' U F2 D' F D F2 U' R
174: R U2 R2 F' U' F2 D' F D F2 U R
175: R U2 R' U R' F R F' U' R U' R'
176: R U2 R' U R' F R F' R U2 R' U
177: R U2 R' U R' F R F' R U2 R' U2
178: R U2 R' U R' F R F' R U2 R' U'
179: R U2 R' U2 F' U' F U' R U' R' U
180: R U2 R' U2 F' U' F U' R U' R' U2
181: R U2 R' U2 F' U' F U' R U' R' U'
182: R U2 R' U' F' U2 F U R U R' U
183: R U2 R' U' F' U2 F U R U R' U2
184: R U2 R' U' F' U2 F U R U R' U'
185: R U2 R' F D R' U R' U' R D' F'
186: R U2 R' F' U2 F U' R' F R F' U
187: R U2 R' F' U2 F U' R' F R F' U2
188: R U2 R' F' U2 F U' R' F R F' U'
189: R U2 F R' U F R F' U' F' R' U
190: R U2 F R' U F R F' U' F' R' U2
191: R U2 F R' U F R F' U' F' R' U'
192: R U' R2 U' D' F' U F D R2 U' R'
193: R U' R2 U' F D' F D F U F R
194: R U' R2 U' F D' F2 U F' D F2 R
195: R U' R2 U' F' U F R U R U2 R'
196: R U' R2 U' F' U F2 D R' D' R2 F'
197: R U' R2 F R2 F' U' F' U F U' R'
198: R U' R2 F2 D' F U' F2 D F' U R
199: R U' R2 F2 D' F' D F' R2 U2 R' U
200: R U' R2 F2 D' F' D F' R2 U2 R' U2
201: R U' R2 F2 D' F' D F' R2 U2 R' U'
202: R U' R' U F' U' F2 R' F' R2 U2 R'
203: R U' R' U' R U' R2 F' U' F U R
204: R U' R' F R' F' U' R2 U' R2 U2 R
205: R U' R' F R' F' R U' R U' R' U
206: R U' R' F R' F' R U' R U' R' U2
207: R U' R' F R' F' R U' R U' R' U'
208: R U' F D R D' F' R U' R' U' R'
209: R U' F D R2 D' F2 U F U R' U
210: R U' F D R2 D' F2 U F U R' U2
211: R U' F D R2 D' F2 U F U R' U'
212: R U' F R2 U' R2 U R2 U F' U R'
213: R U' F R2 D' F2 U F2 D F' U R'
214: R U' F2 D R D' R' F' R F' U2 R'
215: R F' U2 R' U2 F' U' F R F U2 R'
216: R F' U2 F U F D R2 D' F' R' U
217: R F' U2 F U F D R2 D' F' R' U2
218: R F' U2 F U F D R2 D' F' R' U'
219: R F' U' F U F U R2 U' F' U R
220: R F' U' F R U R' U F R2 F' R
221: R2 U' F R U R2 U' R2 F' R' U2 R'
222: R2 F2 U' F R F' R' U2 R U' F2 R2
223: R' U' D' R' F R F' U D R2 U R'
224: R' D' F D F2 U' F' U F2 R2 U R'
225: R' D' F' U' F U2 F2 U F2 U' D R
226: R' F2 D' F' D F2 U' F U R2 U R'
227: R' F' U' F U R2 U' R' U R U R'
228: R' F' U' F U R' D R' U R D' R2
229: R' F' R2 U' F U F' R2 F R2 U R'
230: R' F' R' U' R F R' U R' U R' U
231: R' F' R' U' R F R' U R' U R' U2
232: R' F' R' U' R F R' U R' U R' U'
233: F U R U' R' F' R U2 R2 F R F'
234: F R' F2 U' F U F R F' R U R'
235: F R' F' U' F R F' R' U R2 U R'
236: F R' F' R F' U' F U R U R' U
237: F R' F' R F' U' F U R U R' U2
238: F R' F' R F' U' F U R U R' U'
239: F2 U F U' R' U' F' U F2 R2 U R'
240: F2 U' F2 U F R' F2 R F R U R'
241: F' U2 F U F' U F2 R' F' R2 U2 R'
242: F' U2 F U' F' U2 F2 R' F' R2 U R'
243: F' R' F' U' F R F R' U R2 U R'
search finished in 0.533041s
"""
