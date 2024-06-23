import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#xxxcross(BL&BR&FL slots solved) search with pre-rotation x
scramble="D2 R' F2 R2 F2 U2 R2 D2 R' D2 R D F2 L' B2 F D' B2 L' U' B'"
scramble=sv.solve_F2L(scramble, "x", True, True, False, True, 13, True, 1, "xxxcross", mv.move_UDLRFB)

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
created prune table in 21.661116s and saved to RubiksSolver/table/edge216182022_corner15_prune_table
1: x D R' F U L F2 B R F' L2 B'
2: x L D L2 R2 B' D B2 L' D' R F2
3: x R2 D' L2 R D' B L' B2 D' F2 L2
4: x U D2 L D' B D' L R D B' L R'
5: x D L' B D' R2 D' L D2 R' F2 U B2
6: x D R2 F2 R F' U L F B L2 R B'
7: x D R2 F2 R2 U' R' U2 L B L2 R B'
8: x D R' F U L F2 B R F' L2 B' U
9: x D R' F U L F2 B R F' L2 B' U2
10: x D R' F U L F2 B R F' L2 B' U'
11: x D R' F U L B2 D2 B' L2 F R B'
12: x D R' F U2 L' U' L2 F B L2 R B'
13: x D R' F2 U L B D' F2 D L2 R B'
14: x D F2 U L D2 F' D2 B L2 R B' R2
15: x L D L2 R2 B' D B2 L' D' R F2 U
16: x L D L2 R2 B' D B2 L' D' R F2 U2
17: x L D L2 R2 B' D B2 L' D' R F2 U'
18: x L D L' F' U' F2 L' U2 F R2 B R
19: x L' R' F U' D L B' D2 L2 D F B
20: x R2 D L2 R D' B L' B2 R2 D' F2 L2
21: x R2 D' L2 R D' B L' B2 D' F2 L2 U
22: x R2 D' L2 R D' B L' B2 D' F2 L2 U2
23: x R2 D' L2 R D' B L' B2 D' F2 L2 U'
24: x R2 F D2 L2 B U D L F R' U B2
25: x F' U D F2 L F' B R F2 L2 U B'
26: x F' D F2 U L F B L2 R2 U R' B'
27: x B' U F' R U' B' U' L' F U D F2
28: x B' U F' R U' B' U' F L' U D F2
29: x U D L D' F' D B L' R U' F L' B'
30: x U D2 L D' B D' L R D B' L U R'
31: x U D2 L D' B D' L R D B' L U2 R'
32: x U D2 L D' B D' L R D B' L U' R'
33: x U D2 L D' B D' L R D B' L R' U
34: x U D2 L D' B D' L R D B' L R' U2
35: x U D2 L D' B D' L R D B' L R' U'
36: x U D2 L D' B D' L B R D L B' R'
37: x U D' F L D2 B2 R B' D' L D L R'
38: x U D' F2 U' L2 R D' B L' B2 D' F2 L2
39: x U D' F' D L B L B' D R B' L R2
40: x U D' F' D L2 D L' B L2 B R B' R2
41: x U D' F' B' L2 R D' B D' R2 F L' B2
42: x U L B L F' B' R' F D2 B' D' B L
43: x U L B L B' D R B' R2 B2 R B2 L
44: x U L B L B' D' F' R' F R D2 L R'
45: x U L2 D L' B L2 B R B' R2 B' R' B
46: x U L2 D F2 B' R' F2 D2 F' L' U2 D2 L
47: x U L2 D' R' U2 L F' L' D2 L U2 B2 R'
48: x U L2 R F2 L2 D' B L F2 R' D' L B2
49: x U L2 F L2 F' L2 D L B L2 R U B'
50: x U L2 F' L' R U' F D B' U L U2 F'
51: x U L2 B2 R' B2 D R2 B' R' U R2 U L
52: x U F2 U' F' D F' R U L B L2 R B'
53: x U F' U' L2 D L U B R F' U' F2 B'
54: x U B2 U R D2 F D' B2 U R2 D R D
55: x U B2 R F' R' F2 U' B2 D F2 L B L2
56: x U B' L' B D L B R D2 L2 B' U2 R2
57: x U2 L' D' B2 L U D2 B L' U2 R B L2
58: x U2 R D2 R U2 F U' D' L' F U B R'
59: x U' D R' U F' U F L B R F' L2 B'
60: x U' D R' U F' U F2 L F' B L2 R B'
61: x U' D R' U2 L B R U F U' F L2 B'
62: x U' D R' U2 L B R2 U' R' U F2 L2 B'
63: x U' D F2 L' U' F2 U2 F' U2 F' R2 B R
64: x U' L' F' B' U F2 D2 L U F2 D' B D'
65: x U' F2 L' F L U2 L2 D L B R U' B'
66: x D L2 U' B2 R' B' L2 R U F2 L B L2
67: x D L2 B R' B' R2 U' L2 U F2 L B L2
68: x D L2 B' U2 B2 D2 F R F' U L U B2
69: x D L' U R B' U L2 R B2 D2 L2 B2 R
70: x D L' U R B' U L' U2 L' R' F2 L2 R'
71: x D L' U R B' U R' F2 U2 L2 F2 L2 R'
72: x D L' R' F2 R2 U' B2 L' B U' L U2 R2
73: x D L' F' L U L B R D2 L2 B' U2 R2
74: x D L' B D' R2 D' L D2 R' F2 U B2 U
75: x D L' B D' R2 D' L D2 R' F2 U B2 U2
76: x D L' B D' R2 D' L D2 R' F2 U B2 U'
77: x D L' B D' R2 D' L2 R' B2 L' F2 U B2
78: x D L' B' L' U2 B2 R' U D' L' F2 D' L2
79: x D R2 D' F' D F' R U L B L2 R B'
80: x D R2 F2 R U L B L' F R F' L' B'
81: x D R2 F2 R U F L B L' R F' L' B'
82: x D R2 F2 R U F2 L F' B R F' L2 B'
83: x D R2 F2 R F' U L F B L2 R B' U
84: x D R2 F2 R F' U L F B L2 R B' U2
85: x D R2 F2 R F' U L F B L2 R B' U'
86: x D R2 F2 R2 U' R' U2 L B L2 R B' U
87: x D R2 F2 R2 U' R' U2 L B L2 R B' U2
88: x D R2 F2 R2 U' R' U2 L B L2 R B' U'
89: x D R2 F' R F2 U L F2 B R F' L2 B'
90: x D R' U L F2 B R U F U' F L2 B'
91: x D R' U L F2 B R2 U' R' U F2 L2 B'
92: x D R' U L F' B D R' D' R2 F L2 B'
93: x D R' U L B D' F' D F' R F L2 B'
94: x D R' D F U L F2 B R D' F' L2 B'
95: x D R' F U L F D F D' B L2 R B'
96: x D R' F U L F B D F D' L2 R B'
97: x D R' F U L F B D' F D L2 R B'
98: x D R' F U L F2 D2 B R2 F' L2 R' B'
99: x D R' F U L F2 B R F L' F2 L' B'
100: x D R' F U L F2 B R F2 L' F L' B'
101: x D R' F U L F' B L' F' R F' L' B'
102: x D R' F U L B D' F' D F2 L2 R B'
103: x D R' F U L B R F R' F L2 R B'
104: x D R' F U L B2 D2 B' L2 F R B' U
105: x D R' F U L B2 D2 B' L2 F R B' U2
106: x D R' F U L B2 D2 B' L2 F R B' U'
107: x D R' F U L' B D2 F' L' D2 R F2 B'
108: x D R' F U2 L' U' L2 F B L2 R B' U
109: x D R' F U2 L' U' L2 F B L2 R B' U2
110: x D R' F U2 L' U' L2 F B L2 R B' U'
111: x D R' F D' L2 U D L F2 B R F' B'
112: x D R' F2 U L B D' F2 D L2 R B' U
113: x D R' F2 U L B D' F2 D L2 R B' U2
114: x D R' F2 U L B D' F2 D L2 R B' U'
115: x D R' F2 U L B L' D' F2 D L' R B'
116: x D R' F2 U L B2 D' F2 D B' L2 R B'
117: x D R' F' U F' L B D' F2 D L2 R B'
118: x D F U L B D2 F B R B' L2 U2 R
119: x D F L' R2 B L' D' R2 U2 L' R' F2 L2
120: x D F R' U L' F' B R D2 B D2 F B2
121: x D F R' U' D2 L' U2 R U2 F' U2 B R'
122: x D F2 U L D2 F' D2 B L2 R B' R2 U
123: x D F2 U L D2 F' D2 B L2 R B' R2 U2
124: x D F2 U L D2 F' D2 B L2 R B' R2 U'
125: x D F2 U' L D2 F' R2 U2 R U R D2 R'
126: x D F2 L' R2 U' B L D L2 D' R B L
127: x D F2 R' F U' F2 L' F R' U2 B U2 R
128: x D F' U' L' F2 R' U2 B R F D2 B' D2
129: x D F' U' R F2 L' U2 F R2 U2 R2 B R
130: x D F' U' F2 L' F L2 D2 R' F' D2 L2 R'
131: x D F' U' F2 L' F R' U R' U B U' R
132: x D F' U' F2 L' F B R' B' R' U2 R' B
133: x D F' U' F2 B L' B R' U2 L2 R F R'
134: x D F' U' F' B U2 R F' U2 L2 B' L' F
135: x D2 F D' R' U L B R' D' R2 F L2 B'
136: x D2 F D' R' U' D2 L' R U B U' F' R'
137: x D2 F D' R' D2 R U' L' U B U' F' R'
138: x D2 F2 D2 F' U2 F U D2 L' D' R' F' D
139: x D2 F' R2 D' R' U' F2 L' F' R' B R F2
140: x D' L R F' D B' R' F' U' B' U B' L2
141: x D' L2 D2 L F2 R2 U' F U2 F' B R B'
142: x D' L2 D2 R' B2 L' D' F2 R2 B' L2 R B'
143: x D' L' R' U2 B' U' R2 U2 F' R' F2 U2 B'
144: x D' L' R' U' F B' U R' F2 R2 U R B'
145: x D' R2 U2 F' B2 U2 F2 R U' L F' D2 B2
146: x D' R2 D R' D' L2 D' B L' B2 D' F2 L2
147: x D' R2 D2 B D2 R U' F U L F2 U B2
148: x D' R' D B' U F' R U2 F U B' D F2
149: x D' R' D' F L2 U D L F2 B' R F' B'
150: x D' R' B' R2 B' R U2 B2 U F' D2 B2 R'
151: x D' F' U' D2 F L' F U2 B U2 F2 R' F'
152: x D' F' U' B2 R F B' L' B2 D2 F2 B' R2
153: x D' B D2 L' R' F D L' D F' D L2 F2
154: x D' B' U2 F U2 R' F D2 F2 U' F' B2 R'
155: x D' B' R2 B' R U2 B2 U F U2 F2 D2 R'
156: x D' B' R2 B' R D2 F2 U' D2 F' D2 B2 R'
157: x L U D R' U' D2 F L U D2 L2 F L'
158: x L D L2 R2 B' D B2 L' D' R F U F
159: x L D L2 R2 B' D B2 L' D' R F U2 F
160: x L D L2 R2 B' D B2 L' D' R F U' F
161: x L D L' F' U' F2 L' U2 F R2 B R U
162: x L D L' F' U' F2 L' U2 F R2 B R U2
163: x L D L' F' U' F2 L' U2 F R2 B R U'
164: x L D L' F' R' U' F2 L' U2 F R' B R
165: x L D R2 B' D B L2 B L' D' L R F2
166: x L D2 R' D F B L U D2 B2 L2 F L'
167: x L D2 B2 L' U D L2 D2 L' D' B L2 R
168: x L D2 B2 L' U' D R2 U2 L D' B L2 R
169: x L D' L' D2 F' U' F L' F U2 F B R
170: x L D' L' D' L2 D' B L' R2 B D' L2 F2
171: x L D' L' R F' U' F2 L' F U' B U' R2
172: x L D' L' F' U' F D2 L' F U2 F B R
173: x L D' L' F' U' F2 L' F2 R F' U2 B R2
174: x L R D2 B2 L' F2 U D L D' B L2 R
175: x L R' F U2 L F U D F2 U2 B' L D'
176: x L R' F U2 F R' F U F D L R' F2
177: x L R' F2 R D2 L U' D' L' D' B L2 R
178: x L F2 R U R U' B2 L' U' L B L2 R
179: x L F2 R' U L' U' L D B L' B2 D' L2
180: x L F' U2 D' R U' F R D2 B' R F2 R'
181: x L F' D2 F' L B2 D' R' U' D L B' R
182: x L F' B2 U2 D' F R' D F2 U L B' R'
183: x L F' B2 D F' L' U' L2 B L F2 R F2
184: x L B2 D' F B L U R2 B' R D2 B' L
185: x L B2 L' D F2 U L B L2 R' B2 R2 B2
186: x L2 U D' F' R' U' R2 B R2 F L F B2
187: x L2 U2 B2 R B2 D L F R' U' L2 D L2
188: x L2 R2 B' U' B' U D' R' B L R2 F2 B2
189: x L' R F L' D B' L U F U' D' R D
190: x L' R2 F U' D L B' D2 L2 D F R B
191: x L' R' F U' D L B' D2 L2 D F B U
192: x L' R' F U' D L B' D2 L2 D F B U2
193: x L' R' F U' D L B' D2 L2 D F B U'
194: x L' R' F U' D L B' D2 L2 D B U F
195: x L' R' F U' D L B' D2 L2 D B U2 F
196: x L' R' F U' D L B' D2 L2 D B U' F
197: x L' R' F2 B2 R' U' D L' D' L2 B L2 R
198: x L' F U' D L B' D2 L2 D F2 R' F' B
199: x L' F L' U B' D L F B R B2 U B
200: x L' B L' B2 U2 D2 B D' B U D2 L R
201: x R U D' F D L B L R D L B' R'
202: x R U' D F2 L' U' F U2 B L R' F2 L'
203: x R U' D F2 L' U' F2 U2 F' U2 B R' F'
204: x R U' D2 F D' L' F2 U B L R' F2 L'
205: x R D F' U' F2 L' F D' R' U2 D B R'
206: x R D F' U' F2 L' F B R' B' R' U2 B
207: x R D' R2 D' L2 D' B L' B2 R' D' F2 L2
208: x R F' U' D2 F L' F2 U' R' U2 B U' R2
209: x R F' R' F2 L2 D B U L F B2 U B2
210: x R F' R' F2 L2 D B U2 L B2 U F B2
211: x R2 U L F' D L B2 R U' D2 B' L F
212: x R2 U L B L2 U2 L' B' R2 D B2 L R'
213: x R2 U L B R D L' F' U' F2 L' B' R'
214: x R2 U2 R' U2 F D' F U' L' B' R' B2 R2
215: x R2 D L2 R D' B L' B2 R2 D' F2 L2 U
216: x R2 D L2 R D' B L' B2 R2 D' F2 L2 U2
217: x R2 D L2 R D' B L' B2 R2 D' F2 L2 U'
218: x R2 D F D L2 U' D L U2 F U2 R' B2
219: x R2 D2 L2 R D' B L' B2 R' D' L' F2 L'
220: x R2 D' L2 D2 B' U2 L D' R F' U2 D F2
221: x R2 D' F D' L2 D B U L F U R' B2
222: x R2 D' B' R' U' L F U L2 F2 U' B2 R2
223: x R2 F D2 L2 B U D L F R' U B2 U
224: x R2 F D2 L2 B U D L F R' U B2 U2
225: x R2 F D2 L2 B U D L F R' U B2 U'
226: x R2 F2 U2 R2 U F' D' L' F B' R' B2 R2
227: x R2 B' R2 B' U2 B2 U D2 L' D' R' F' D
228: x R' U L F' B' L' R D' F L' U' F' B'
229: x R' U L B R D' L D B' L D B' D'
230: x R' U L B2 R B' D' L B' D2 B' D' L
231: x R' D2 F2 R F U' D' F2 L' F U B R'
232: x R' D' L2 D' B L' F B2 D' F L' U L'
233: x R' D' L2 D' B R' D L' R B2 D' F2 L2
234: x R' D' L' B' U R' F2 U' L2 D' F2 L2 B2
235: x R' F D2 L2 B U' D L F2 R' F' U B2
236: x F D L2 B U2 D L U F R B U' B
237: x F D L2 B U2 D F R F' L U F B2
238: x F D L2 B U' D L U F U2 R U2 B2
239: x F D2 L2 R' B R U2 D L U F R' B2
240: x F D2 L2 B U2 D L U F U' R' U B2
241: x F D2 L2 B U' D L F R' F' U F B2
242: x F D2 L2 B D L F R' U B2 R2 U2 R2
243: x F D2 L' B L' U' L2 D F R' U L' B2
244: x F D2 F' R F' U' D' F L' F2 B U' R
245: x F L D F B L2 U2 R U2 L' U L B2
246: x F L2 B D L' B L U L F R U B2
247: x F L' U2 F' B D' R F' D R' F' U' B'
248: x F L' U' L' D B' L F U2 R2 B2 U2 B2
249: x F2 L F2 R' F2 D B U L' U' B2 D' L2
250: x F2 L' F' L' U D L F U2 B U2 R B'
251: x F2 L' F' L' U' D B' L F B2 U2 B2 R2
252: x F2 L' F' L' D B L F U' R B2 U2 B2
253: x F' U D F2 L F' B R F2 L2 U B' U
254: x F' U D F2 L F' B R F2 L2 U B' U2
255: x F' U D F2 L F' B R F2 L2 U B' U'
256: x F' U2 B' L2 F B U D2 L' D' R' F' D
257: x F' U' D2 R' D' R F L' F U2 F B R
258: x F' U' D' F L' F2 B U2 R' D B2 D' R'
259: x F' U' R D2 F L' D L2 D' F2 U' R2 B'
260: x F' U' F D F L' F U R2 U B U' R
261: x F' U' F D F L' F U2 B R' B' R2 B
262: x F' U' F D F L' F L2 D2 F' D2 L2 R'
263: x F' U' F D F2 R2 F' L' F U2 B U2 R
264: x F' U' F L D' L2 F2 R U2 B' R2 B2 R'
265: x F' U' F L D' L' D2 L' F U2 F B R
266: x F' U' B R F B L' B2 D L' F2 U' B'
267: x F' D F2 U L F B L2 R2 U R' B' U
268: x F' D F2 U L F B L2 R2 U R' B' U2
269: x F' D F2 U L F B L2 R2 U R' B' U'
270: x F' D2 R' D' R U' F L' F U2 F B R
271: x F' D' R' U F' L' F2 B' R2 F2 U' R' B'
272: x F' D' R' F' U L' F2 B' R2 F2 U' R' B'
273: x F' D' F R' F2 U L' F2 B' R2 F2 R' B'
274: x F' D' F' R F' L2 B D L F R2 U B2
275: x F' R U2 B R2 F' U D L B' U' D' L2
276: x F' R U' D' F2 L' B' U' F B2 R' U B2
277: x F' R2 D2 R2 U' F D L' F2 U R2 B R
278: x F' B' D2 B U' R' D F2 L' F R' U2 B
279: x B R D2 B L2 F2 R F' U D L F B
280: x B R2 F B' L2 B U D L F R' U B2
281: x B R' B2 R U R D L2 U2 B' R' F' D
282: x B' U F' R U2 F U D L' D' B' D F2
283: x B' U F' R U2 F U B' U' L' U D F2
284: x B' U F' R U' B' U' L2 F U L D F2
285: x B' U F' R U' B' U' L2 F L U D F2
286: x B' U F' R U' B' U' L' F U D F2 U
287: x B' U F' R U' B' U' L' F U D F2 U2
288: x B' U F' R U' B' U' L' F U D F2 U'
289: x B' U F' R U' B' U' F L U L2 D F2
290: x B' U F' R U' B' U' F L2 U L D F2
291: x B' U F' R U' B' U' F L' U D F2 U
292: x B' U F' R U' B' U' F L' U D F2 U2
293: x B' U F' R U' B' U' F L' U D F2 U'
294: x B' U F' R' D2 B' D2 R2 U' B' L' D F2
295: x B' D R B L2 D R2 F' R F L R' F2
search finished in 1.470040s
"""