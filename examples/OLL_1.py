import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#OLL search
scramble="L U2 L B' D' F R' D R2 U B2 D' L2 U' B2 D R2 B2 D F' D"
scramble=sv.solve_F2L(scramble, "", True, True, True, True, 15, False, 5, "xxxxcross", mv.move_UDLRFB)
scramble=sv.solve_LL_substep(scramble, "", False, True, False, True, 12, True, 1, "OLL", mv.move_UDLRFB)

"""
F2 L U2 L' D2 L2 F L2 F U' D' B' U F'  // xxxxcross No.5
start creating single cp move table
created single cp move table in 0.015567s and save to RubiksSolver/table/single_cp_move_table
start creating single ep move table
created single ep move table in 0.000000s and save to RubiksSolver/table/single_ep_move_table
start creating co move table
created co move table in 0.062543s and save to RubiksSolver/table/co_move_table
start creating eo move table
created eo move table in 0.046796s and save to RubiksSolver/table/eo_move_table
start creating multi move table
created multi move table in 0.078223s and save to RubiksSolver/table/cp_move_table
start creating multi move table
created multi move table in 0.124896s and save to RubiksSolver/table/ep_move_table
1: L' B' U' B U L
2: R B U B' U' R'
3: U F R U R' U' F'
4: U B' R' U' R U B
5: U2 L F U F' U' L'
6: U2 R' F' U' F U R
7: U' F' L' U' L U F
8: U' B L U L' U' B'
9: L' B' U' B U L U
10: L' B' U' B U L U2
11: L' B' U' B U L U'
12: R B U B' U' R' U
13: R B U B' U' R' U2
14: R B U B' U' R' U'
15: U F R U R' U' F' U
16: U F R U R' U' F' U2
17: U F R U R' U' F' U'
18: U B' R' U' R U B U
19: U B' R' U' R U B U2
20: U B' R' U' R U B U'
21: U2 L F U F' U' L' U
22: U2 L F U F' U' L' U2
23: U2 L F U F' U' L' U'
24: U2 R' F' U' F U R U
25: U2 R' F' U' F U R U2
26: U2 R' F' U' F U R U'
27: U' F' L' U' L U F U
28: U' F' L' U' L U F U2
29: U' F' L' U' L U F U'
30: U' B L U L' U' B' U
31: U' B L U L' U' B' U2
32: U' B L U L' U' B' U'
33: D L' B' U' B U L D'
34: D R B U B' U' R' D'
35: D2 L' B' U' B U L D2
36: D2 R B U B' U' R' D2
37: D' L' B' U' B U L D
38: D' R B U B' U' R' D
39: U D F R U R' U' F' D'
40: U D B' R' U' R U B D'
41: U D2 F R U R' U' F' D2
42: U D2 B' R' U' R U B D2
43: U D' F R U R' U' F' D
44: U D' B' R' U' R U B D
45: U2 D L F U F' U' L' D'
46: U2 D R' F' U' F U R D'
47: U2 D2 L F U F' U' L' D2
48: U2 D2 R' F' U' F U R D2
49: U2 D' L F U F' U' L' D
50: U2 D' R' F' U' F U R D
51: U' D F' L' U' L U F D'
52: U' D B L U L' U' B' D'
53: U' D2 F' L' U' L U F D2
54: U' D2 B L U L' U' B' D2
55: U' D' F' L' U' L U F D
56: U' D' B L U L' U' B' D
57: D L' B' U' B U L U D'
58: D L' B' U' B U L U2 D'
59: D L' B' U' B U L U' D'
60: D R B U B' U' R' U D'
61: D R B U B' U' R' U2 D'
62: D R B U B' U' R' U' D'
63: D2 L' B' U' B U L U D2
64: D2 L' B' U' B U L U2 D2
65: D2 L' B' U' B U L U' D2
66: D2 R B U B' U' R' U D2
67: D2 R B U B' U' R' U2 D2
68: D2 R B U B' U' R' U' D2
69: D' L' B' U' B U L U D
70: D' L' B' U' B U L U2 D
71: D' L' B' U' B U L U' D
72: D' R B U B' U' R' U D
73: D' R B U B' U' R' U2 D
74: D' R B U B' U' R' U' D
75: U D F R U R' U' F' U D'
76: U D F R U R' U' F' U2 D'
77: U D F R U R' U' F' U' D'
78: U D B' R' U' R U B U D'
79: U D B' R' U' R U B U2 D'
80: U D B' R' U' R U B U' D'
81: U D2 F R U R' U' F' U D2
82: U D2 F R U R' U' F' U2 D2
83: U D2 F R U R' U' F' U' D2
84: U D2 B' R' U' R U B U D2
85: U D2 B' R' U' R U B U2 D2
86: U D2 B' R' U' R U B U' D2
87: U D' F R U R' U' F' U D
88: U D' F R U R' U' F' U2 D
89: U D' F R U R' U' F' U' D
90: U D' B' R' U' R U B U D
91: U D' B' R' U' R U B U2 D
92: U D' B' R' U' R U B U' D
93: U2 D L F U F' U' L' U D'
94: U2 D L F U F' U' L' U2 D'
95: U2 D L F U F' U' L' U' D'
96: U2 D R' F' U' F U R U D'
97: U2 D R' F' U' F U R U2 D'
98: U2 D R' F' U' F U R U' D'
99: U2 D2 L F U F' U' L' U D2
100: U2 D2 L F U F' U' L' U2 D2
101: U2 D2 L F U F' U' L' U' D2
102: U2 D2 R' F' U' F U R U D2
103: U2 D2 R' F' U' F U R U2 D2
104: U2 D2 R' F' U' F U R U' D2
105: U2 D' L F U F' U' L' U D
106: U2 D' L F U F' U' L' U2 D
107: U2 D' L F U F' U' L' U' D
108: U2 D' R' F' U' F U R U D
109: U2 D' R' F' U' F U R U2 D
110: U2 D' R' F' U' F U R U' D
111: U' D F' L' U' L U F U D'
112: U' D F' L' U' L U F U2 D'
113: U' D F' L' U' L U F U' D'
114: U' D B L U L' U' B' U D'
115: U' D B L U L' U' B' U2 D'
116: U' D B L U L' U' B' U' D'
117: U' D2 F' L' U' L U F U D2
118: U' D2 F' L' U' L U F U2 D2
119: U' D2 F' L' U' L U F U' D2
120: U' D2 B L U L' U' B' U D2
121: U' D2 B L U L' U' B' U2 D2
122: U' D2 B L U L' U' B' U' D2
123: U' D' F' L' U' L U F U D
124: U' D' F' L' U' L U F U2 D
125: U' D' F' L' U' L U F U' D
126: U' D' B L U L' U' B' U D
127: U' D' B L U L' U' B' U2 D
128: U' D' B L U L' U' B' U' D
129: L' U2 L F U' F' U2 L' U L
130: L' B2 D' B U' B' D B2 U L
131: L' B' R B2 D B D' R' B2 L
132: R U2 R' F' U F U2 R U' R'
133: R B L' B2 D' B' D L B2 R'
134: R B2 D B' U B D' B2 U' R'
135: B U B' R' U2 F' U2 F U R
136: B U2 L F U' F' U' L' U' B'
137: B L B' R B L' U B' U' R'
138: B' U2 R' F' U F U R U B
139: B' U' B L U2 F U2 F' U' L'
140: B' R' B L' B' R U' B U L
141: U R U R' F' U2 L' U2 L U F
142: U R U2 B L U' L' U' B' U' R'
143: U R B R' F R B' U R' U' F'
144: U R' U2 F' L' U L U F U R
145: U R' U' R B U2 L U2 L' U' B'
146: U R' F' R B' R' F U' R U B
147: U F U2 F' L' U L U2 F U' F'
148: U F R B' R2 D' R' D B R2 F'
149: U F R2 D R' U R D' R2 U' F'
150: U B' U2 B L U' L' U2 B' U B
151: U B' R2 D' R U' R' D R2 U B
152: U B' R' F R2 D R D' F' R2 B
153: U2 L U2 L' B' U B U2 L U' L'
154: U2 L F R' F2 D' F' D R F2 L'
155: U2 L F2 D F' U F D' F2 U' L'
156: U2 R' U2 R B U' B' U2 R' U R
157: U2 R' F2 D' F U' F' D F2 U R
158: U2 R' F' L F2 D F D' L' F2 R
159: U2 F U F' L' U2 B' U2 B U L
160: U2 F U2 R B U' B' U' R' U' F'
161: U2 F R F' L F R' U F' U' L'
162: U2 F' U2 L' B' U B U L U F
163: U2 F' U' F R U2 B U2 B' U' R'
164: U2 F' L' F R' F' L U' F U R
165: U' L U L' B' U2 R' U2 R U B
166: U' L U2 F R U' R' U' F' U' L'
167: U' L F L' B L F' U L' U' B'
168: U' L' U2 B' R' U R U B U L
169: U' L' U' L F U2 R U2 R' U' F'
170: U' L' B' L F' L' B U' L U F
171: U' F' U2 F R U' R' U2 F' U F
172: U' F' L2 D' L U' L' D L2 U F
173: U' F' L' B L2 D L D' B' L2 F
174: U' B U2 B' R' U R U2 B U' B'
175: U' B L F' L2 D' L' D F L2 B'
176: U' B L2 D L' U L D' L2 U' B'
177: L U L2 B L2 U L' U' B2 U2 B
178: L U F2 B' R' F' R F' B U' L'
179: L D L D' B' L2 U' L' B U L
180: L D2 R2 F R2 D2 L2 U' B U L
181: L2 R D' B D L2 R' U F U2 F'
182: L2 B' U B U' B' U' B2 L B' L
183: L2 B' L2 U' F' L F L2 B U L
184: L' U D' R' U' B' R D L U B
185: L' U2 L F U' F' U2 L' U L U
186: L' U2 L F U' F' U2 L' U L U2
187: L' U2 L F U' F' U2 L' U L U'
188: L' U2 L2 F' D F' D' F2 L2 U2 L
189: L' U' L' B2 D' B' D L B' U L
190: L' D B' U' B U L U L' D' L
191: L' D2 B' U' B U L U L' D2 L
192: L' D' B' U' B U L U L' D L
193: L' R B U' B' U L B U B' R'
194: L' R B L U B' U' R' B' U B
195: L' R B' U B U' R' B' U' B L
196: L' R B' R' U' B U L B U' B'
197: L' R2 D B' D' L R2 U' F' U2 F
198: L' B2 D' B U' B' D B2 U L U
199: L' B2 D' B U' B' D B2 U L U2
200: L' B2 D' B U' B' D B2 U L U'
201: L' B' U R' F' U F U2 R B L
202: L' B' U' B L F U2 R U R' F'
203: L' B' U' B L2 F' D' L D L2 F
204: L' B' R U B U' B' R' U' B L
205: L' B' R B2 D B D' R' B2 L U
206: L' B' R B2 D B D' R' B2 L U2
207: L' B' R B2 D B D' R' B2 L U'
208: R U R B2 D B D' R' B U' R'
209: R U2 R2 F D' F D F2 R2 U2 R'
210: R U2 R' F' U F U2 R U' R' U
211: R U2 R' F' U F U2 R U' R' U2
212: R U2 R' F' U F U2 R U' R' U'
213: R U' D L U B L' D' R' U' B'
214: R D B U B' U' R' U' R D' R'
215: R D2 B U B' U' R' U' R D2 R'
216: R D' B U B' U' R' U' R D R'
217: R B U B' R2 F D R' D' R2 F'
218: R B U B' R' F' U2 L' U' L F
219: R B U' L F U' F' U2 L' B' R'
220: R B L' U' B' U B L U B' R'
221: R B L' B2 D' B' D L B2 R' U
222: R B L' B2 D' B' D L B2 R' U2
223: R B L' B2 D' B' D L B2 R' U'
224: R B2 D B' U B D' B2 U' R' U
225: R B2 D B' U B D' B2 U' R' U2
226: R B2 D B' U B D' B2 U' R' U'
227: R2 B U' B' U B U B2 R' B R'
228: R2 B R2 U F R' F' R2 B' U' R'
229: R' U' R2 B' R2 U' R U B2 U2 B'
230: R' U' F2 B L F L' F B' U R
231: R' D2 L2 F' L2 D2 R2 U B' U' R'
232: R' D' R' D B R2 U R B' U' R'
233: B U B' R' U2 F' U2 F U R U
234: B U B' R' U2 F' U2 F U R U2
235: B U B' R' U2 F' U2 F U R U'
236: B U2 L F U' F' U' L' U' B' U
237: B U2 L F U' F' U' L' U' B' U2
238: B U2 L F U' F' U' L' U' B' U'
239: B L B' R B L' U B' U' R' U
240: B L B' R B L' U B' U' R' U2
241: B L B' R B L' U B' U' R' U'
242: B R U R B' R' U' B R' U' B'
243: B' U2 R' F' U F U R U B U
244: B' U2 R' F' U F U R U B U2
245: B' U2 R' F' U F U R U B U'
246: B' U' B L U2 F U2 F' U' L' U
247: B' U' B L U2 F U2 F' U' L' U2
248: B' U' B L U2 F U2 F' U' L' U'
249: B' L' U' L' B L U B' L U B
250: B' R' B L' B' R U' B U L U
251: B' R' B L' B' R U' B U L U2
252: B' R' B L' B' R U' B U L U'
253: U R U R' F' U2 L' U2 L U F U
254: U R U R' F' U2 L' U2 L U F U2
255: U R U R' F' U2 L' U2 L U F U'
256: U R U2 B L U' L' U' B' U' R' U
257: U R U2 B L U' L' U' B' U' R' U2
258: U R U2 B L U' L' U' B' U' R' U'
259: U R F U F R' F' U' R F' U' R'
260: U R B R' F R B' U R' U' F' U
261: U R B R' F R B' U R' U' F' U2
262: U R B R' F R B' U R' U' F' U'
263: U R' U2 F' L' U L U F U R U
264: U R' U2 F' L' U L U F U R U2
265: U R' U2 F' L' U L U F U R U'
266: U R' U' R B U2 L U2 L' U' B' U
267: U R' U' R B U2 L U2 L' U' B' U2
268: U R' U' R B U2 L U2 L' U' B' U'
269: U R' F' R B' R' F U' R U B U
270: U R' F' R B' R' F U' R U B U2
271: U R' F' R B' R' F U' R U B U'
272: U R' B' U' B' R B U R' B U R
273: U F U F R2 D R D' F' R U' F'
274: U F U2 F2 L D' L D L2 F2 U2 F'
275: U F U2 F' L' U L U2 F U' F' U
276: U F U2 F' L' U L U2 F U' F' U2
277: U F U2 F' L' U L U2 F U' F' U'
278: U F U' D B U R B' D' F' U' R'
279: U F D R U R' U' F' U' F D' F'
280: U F D2 R U R' U' F' U' F D2 F'
281: U F D' R U R' U' F' U' F D F'
282: U F R U R' F2 L D F' D' F2 L'
283: U F R U R' F' L' U2 B' U' B L
284: U F R U' B L U' L' U2 B' R' F'
285: U F R B' U' R' U R B U R' F'
286: U F R B' R2 D' R' D B R2 F' U
287: U F R B' R2 D' R' D B R2 F' U2
288: U F R B' R2 D' R' D B R2 F' U'
289: U F R2 D R' U R D' R2 U' F' U
290: U F R2 D R' U R D' R2 U' F' U2
291: U F R2 D R' U R D' R2 U' F' U'
292: U F B2 D' R D F' B2 U L U2 L'
293: U F B' R U' R' U B R U R' F'
294: U F B' R B U R' U' F' R' U R
295: U F B' R' U R U' F' R' U' R B
296: U F B' R' F' U' R U B R U' R'
297: U F2 R U' R' U R U R2 F' R F'
298: U F2 R F2 U L F' L' F2 R' U' F'
299: U F2 B' D R' D' F2 B U' L' U2 L
300: U F' U' L2 R B L B' L R' U F
301: U F' U' F2 R' F2 U' F U R2 U2 R'
302: U F' D2 B2 L' B2 D2 F2 U R' U' F'
303: U F' D' F' D R F2 U F R' U' F'
304: U B U L2 R' F' L' F L' R U' B'
305: U B U B2 R B2 U B' U' R2 U2 R
306: U B D B D' R' B2 U' B' R U B
307: U B D2 F2 L F2 D2 B2 U' R U B
308: U B2 R' U R U' R' U' R2 B R' B
309: U B2 R' B2 U' L' B L B2 R U B
310: U B' U D' F' U' R' F D B U R
311: U B' U2 B L U' L' U2 B' U B U
312: U B' U2 B L U' L' U2 B' U B U2
313: U B' U2 B L U' L' U2 B' U B U'
314: U B' U2 B2 L' D L' D' L2 B2 U2 B
315: U B' U' B' R2 D' R' D B R' U B
316: U B' D R' U' R U B U B' D' B
317: U B' D2 R' U' R U B U B' D2 B
318: U B' D' R' U' R U B U B' D B
319: U B' R2 D' R U' R' D R2 U B U
320: U B' R2 D' R U' R' D R2 U B U2
321: U B' R2 D' R U' R' D R2 U B U'
322: U B' R' U F' L' U L U2 F R B
323: U B' R' U' R B L U2 F U F' L'
324: U B' R' U' R B2 L' D' B D B2 L
325: U B' R' F U R U' R' F' U' R B
326: U B' R' F R2 D R D' F' R2 B U
327: U B' R' F R2 D R D' F' R2 B U2
328: U B' R' F R2 D R D' F' R2 B U'
329: U2 L U L F2 D F D' L' F U' L'
330: U2 L U2 L2 B D' B D B2 L2 U2 L'
331: U2 L U2 L' B' U B U2 L U' L' U
332: U2 L U2 L' B' U B U2 L U' L' U2
333: U2 L U2 L' B' U B U2 L U' L' U'
334: U2 L U' D R U F R' D' L' U' F'
335: U2 L D F U F' U' L' U' L D' L'
336: U2 L D2 F U F' U' L' U' L D2 L'
337: U2 L D' F U F' U' L' U' L D L'
338: U2 L R2 D' F D L' R2 U B U2 B'
339: U2 L R' F U' F' U R F U F' L'
340: U2 L R' F R U F' U' L' F' U F
341: U2 L R' F' U F U' L' F' U' F R
342: U2 L R' F' L' U' F U R F U' F'
343: U2 L F U F' L2 B D L' D' L2 B'
344: U2 L F U F' L' B' U2 R' U' R B
345: U2 L F U' R B U' B' U2 R' F' L'
346: U2 L F R' U' F' U F R U F' L'
347: U2 L F R' F2 D' F' D R F2 L' U
348: U2 L F R' F2 D' F' D R F2 L' U2
349: U2 L F R' F2 D' F' D R F2 L' U'
350: U2 L F2 D F' U F D' F2 U' L' U
351: U2 L F2 D F' U F D' F2 U' L' U2
352: U2 L F2 D F' U F D' F2 U' L' U'
353: U2 L2 R' D F' D' L2 R U' B' U2 B
354: U2 L2 F U' F' U F U F2 L' F L'
355: U2 L2 F L2 U B L' B' L2 F' U' L'
356: U2 L' U' L2 F' L2 U' L U F2 U2 F'
357: U2 L' U' F B2 R B R' F' B U L
358: U2 L' D2 R2 B' R2 D2 L2 U F' U' L'
359: U2 L' D' L' D F L2 U L F' U' L'
360: U2 R U R2 F R2 U R' U' F2 U2 F
361: U2 R U F' B2 L' B' L F B' U' R'
362: U2 R D R D' F' R2 U' R' F U R
363: U2 R D2 L2 B L2 D2 R2 U' F U R
364: U2 R2 F' U F U' F' U' F2 R F' R
365: U2 R2 F' R2 U' B' R B R2 F U R
366: U2 R' U D' L' U' F' L D R U F
367: U2 R' U2 R B U' B' U2 R' U R U
368: U2 R' U2 R B U' B' U2 R' U R U2
369: U2 R' U2 R B U' B' U2 R' U R U'
370: U2 R' U2 R2 B' D B' D' B2 R2 U2 R
371: U2 R' U' R' F2 D' F' D R F' U R
372: U2 R' D F' U' F U R U R' D' R
373: U2 R' D2 F' U' F U R U R' D2 R
374: U2 R' D' F' U' F U R U R' D R
375: U2 R' F2 D' F U' F' D F2 U R U
376: U2 R' F2 D' F U' F' D F2 U R U2
377: U2 R' F2 D' F U' F' D F2 U R U'
378: U2 R' F' U L' B' U B U2 L F R
379: U2 R' F' U' F R B U2 L U L' B'
380: U2 R' F' U' F R2 B' D' R D R2 B
381: U2 R' F' L U F U' F' L' U' F R
382: U2 R' F' L F2 D F D' L' F2 R U
383: U2 R' F' L F2 D F D' L' F2 R U2
384: U2 R' F' L F2 D F D' L' F2 R U'
385: U2 F U F' L' U2 B' U2 B U L U
386: U2 F U F' L' U2 B' U2 B U L U2
387: U2 F U F' L' U2 B' U2 B U L U'
388: U2 F U2 R B U' B' U' R' U' F' U
389: U2 F U2 R B U' B' U' R' U' F' U2
390: U2 F U2 R B U' B' U' R' U' F' U'
391: U2 F L U L F' L' U' F L' U' F'
392: U2 F R F' L F R' U F' U' L' U
393: U2 F R F' L F R' U F' U' L' U2
394: U2 F R F' L F R' U F' U' L' U'
395: U2 F' U2 L' B' U B U L U F U
396: U2 F' U2 L' B' U B U L U F U2
397: U2 F' U2 L' B' U B U L U F U'
398: U2 F' U' F R U2 B U2 B' U' R' U
399: U2 F' U' F R U2 B U2 B' U' R' U2
400: U2 F' U' F R U2 B U2 B' U' R' U'
401: U2 F' L' F R' F' L U' F U R U
402: U2 F' L' F R' F' L U' F U R U2
403: U2 F' L' F R' F' L U' F U R U'
404: U2 F' R' U' R' F R U F' R U F
405: U' L U L' B' U2 R' U2 R U B U
406: U' L U L' B' U2 R' U2 R U B U2
407: U' L U L' B' U2 R' U2 R U B U'
408: U' L U2 F R U' R' U' F' U' L' U
409: U' L U2 F R U' R' U' F' U' L' U2
410: U' L U2 F R U' R' U' F' U' L' U'
411: U' L F L' B L F' U L' U' B' U
412: U' L F L' B L F' U L' U' B' U2
413: U' L F L' B L F' U L' U' B' U'
414: U' L B U B L' B' U' L B' U' L'
415: U' L' U2 B' R' U R U B U L U
416: U' L' U2 B' R' U R U B U L U2
417: U' L' U2 B' R' U R U B U L U'
418: U' L' U' L F U2 R U2 R' U' F' U
419: U' L' U' L F U2 R U2 R' U' F' U2
420: U' L' U' L F U2 R U2 R' U' F' U'
421: U' L' F' U' F' L F U L' F U L
422: U' L' B' L F' L' B U' L U F U
423: U' L' B' L F' L' B U' L U F U2
424: U' L' B' L F' L' B U' L U F U'
425: U' F U L' R2 B' R' B L R' U' F'
426: U' F U F2 L F2 U F' U' L2 U2 L
427: U' F D F D' L' F2 U' F' L U F
428: U' F D2 B2 R B2 D2 F2 U' L U F
429: U' F2 L' U L U' L' U' L2 F L' F
430: U' F2 L' F2 U' R' F R F2 L U F
431: U' F2 B D' L D F2 B' U R U2 R'
432: U' F' U D' B' U' L' B D F U L
433: U' F' U2 F R U' R' U2 F' U F U
434: U' F' U2 F R U' R' U2 F' U F U2
435: U' F' U2 F R U' R' U2 F' U F U'
436: U' F' U2 F2 R' D R' D' R2 F2 U2 F
437: U' F' U' F' L2 D' L' D F L' U F
438: U' F' D L' U' L U F U F' D' F
439: U' F' D2 L' U' L U F U F' D2 F
440: U' F' D' L' U' L U F U F' D F
441: U' F' L2 D' L U' L' D L2 U F U
442: U' F' L2 D' L U' L' D L2 U F U2
443: U' F' L2 D' L U' L' D L2 U F U'
444: U' F' L' U B' R' U R U2 B L F
445: U' F' L' U' L F R U2 B U B' R'
446: U' F' L' U' L F2 R' D' F D F2 R
447: U' F' L' B U L U' L' B' U' L F
448: U' F' L' B L2 D L D' B' L2 F U
449: U' F' L' B L2 D L D' B' L2 F U2
450: U' F' L' B L2 D L D' B' L2 F U'
451: U' F' B L U' L' U F L U L' B'
452: U' F' B L F U L' U' B' L' U L
453: U' F' B L' U L U' B' L' U' L F
454: U' F' B L' B' U' L U F L U' L'
455: U' F' B2 D L' D' F B2 U' R' U2 R
456: U' B U B L2 D L D' B' L U' B'
457: U' B U2 B2 R D' R D R2 B2 U2 B'
458: U' B U2 B' R' U R U2 B U' B' U
459: U' B U2 B' R' U R U2 B U' B' U2
460: U' B U2 B' R' U R U2 B U' B' U'
461: U' B U' D F U L F' D' B' U' L'
462: U' B D L U L' U' B' U' B D' B'
463: U' B D2 L U L' U' B' U' B D2 B'
464: U' B D' L U L' U' B' U' B D B'
465: U' B L U L' B2 R D B' D' B2 R'
466: U' B L U L' B' R' U2 F' U' F R
467: U' B L U' F R U' R' U2 F' L' B'
468: U' B L F' U' L' U L F U L' B'
469: U' B L F' L2 D' L' D F L2 B' U
470: U' B L F' L2 D' L' D F L2 B' U2
471: U' B L F' L2 D' L' D F L2 B' U'
472: U' B L2 D L' U L D' L2 U' B' U
473: U' B L2 D L' U L D' L2 U' B' U2
474: U' B L2 D L' U L D' L2 U' B' U'
475: U' B2 L U' L' U L U L2 B' L B'
476: U' B2 L B2 U R B' R' B2 L' U' B'
477: U' B' U' L R2 F R F' L' R U B
478: U' B' U' B2 L' B2 U' B U L2 U2 L'
479: U' B' D2 F2 R' F2 D2 B2 U L' U' B'
480: U' B' D' B' D L B2 U B L' U' B'
481: D L' U2 L F U' F' U2 L' U L D'
482: D L' B2 D' B U' B' D B2 U L D'
483: D L' B' R B2 D B D' R' B2 L D'
484: D R U2 R' F' U F U2 R U' R' D'
485: D R B L' B2 D' B' D L B2 R' D'
486: D R B2 D B' U B D' B2 U' R' D'
487: D B U B' R' U2 F' U2 F U R D'
488: D B U2 L F U' F' U' L' U' B' D'
489: D B L B' R B L' U B' U' R' D'
490: D B' U2 R' F' U F U R U B D'
491: D B' U' B L U2 F U2 F' U' L' D'
492: D B' R' B L' B' R U' B U L D'
493: D2 L2 R2 U2 D2 L2 R F' U' F U R
494: D2 L2 R2 U2 D2 L' R2 F U F' U' L'
495: D2 L' U2 L F U' F' U2 L' U L D2
496: D2 L' B2 D' B U' B' D B2 U L D2
497: D2 L' B' U' B U L' R2 U2 D2 L2 R2
498: D2 L' B' R B2 D B D' R' B2 L D2
499: D2 R U2 R' F' U F U2 R U' R' D2
500: D2 R B U B' U' L2 R U2 D2 L2 R2
501: D2 R B L' B2 D' B' D L B2 R' D2
502: D2 R B2 D B' U B D' B2 U' R' D2
503: D2 B U B' R' U2 F' U2 F U R D2
504: D2 B U2 L F U' F' U' L' U' B' D2
505: D2 B L B' R B L' U B' U' R' D2
506: D2 B' U2 R' F' U F U R U B D2
507: D2 B' U' B L U2 F U2 F' U' L' D2
508: D2 B' R' B L' B' R U' B U L D2
509: D' L' U2 L F U' F' U2 L' U L D
510: D' L' B2 D' B U' B' D B2 U L D
511: D' L' B' R B2 D B D' R' B2 L D
512: D' R U2 R' F' U F U2 R U' R' D
513: D' R B L' B2 D' B' D L B2 R' D
514: D' R B2 D B' U B D' B2 U' R' D
515: D' B U B' R' U2 F' U2 F U R D
516: D' B U2 L F U' F' U' L' U' B' D
517: D' B L B' R B L' U B' U' R' D
518: D' B' U2 R' F' U F U R U B D
519: D' B' U' B L U2 F U2 F' U' L' D
520: D' B' R' B L' B' R U' B U L D
521: L U L2 B L2 U L' U' B2 U2 B U
522: L U L2 B L2 U L' U' B2 U2 B U2
523: L U L2 B L2 U L' U' B2 U2 B U'
524: L U L' U2 B' U' R' F' U2 F R B
525: L U F U2 F' U2 F R U R' F' L'
526: L U F2 U' L' U2 R' F' R F' U' F2
527: L U F2 B' R' F' R F' B U' L' U
528: L U F2 B' R' F' R F' B U' L' U2
529: L U F2 B' R' F' R F' B U' L' U'
530: L U B L' D F' L F D2 B D B2
531: L U2 L R' F' D F' D' L' F2 L' R
532: L U2 F R2 U B U' B' R2 U2 F' L'
533: L D L D' B' L2 U' L' B U L U
534: L D L D' B' L2 U' L' B U L U2
535: L D L D' B' L2 U' L' B U L U'
536: L D2 R2 F R2 D2 L2 U' B U L U
537: L D2 R2 F R2 D2 L2 U' B U L U2
538: L D2 R2 F R2 D2 L2 U' B U L U'
539: L R2 F2 B2 L2 R2 F2 B U' B U L
540: L R2 F' D' F R2 B2 L2 U' L2 B2 L'
541: L F2 D F D' F2 U F' U' L2 U2 L
542: L B L2 B' U' B U L U' L B' L'
543: L B2 L2 B' U' B U L U' L B2 L'
544: L B' L2 B' U' B U L U' L B L'
545: L2 U D' B R' U' R U B' U' D L2
546: L2 U L' R' U F U' F' L U' L2 R
547: L2 U L' B' U F U' F' B L U' L2
548: L2 U2 D2 R F' U' F U R' U2 D2 L2
549: L2 U' D F L' U' L U F' U D' L2
550: L2 D F' L' U R U' L R' F D' L2
551: L2 R D2 R2 F' R2 D2 L2 U B' U' R'
552: L2 R D' B D L2 R' U F U2 F' U
553: L2 R D' B D L2 R' U F U2 F' U2
554: L2 R D' B D L2 R' U F U2 F' U'
555: L2 R2 U2 D2 L2 R F' U' F U R D2
556: L2 R2 U2 D2 L' R2 F U F' U' L' D2
557: L2 R' F D F' L2 B2 R2 U R2 B2 R
558: L2 R' F2 B2 L2 R2 F2 B' U B' U' R'
559: L2 F2 B2 R B' D' B D R' F2 B2 L2
560: L2 B L B' U' L2 F' L2 U' L U F
561: L2 B R2 B' L B R2 B2 U' B U L
562: L2 B' U B U' B' U' B2 L B' L U
563: L2 B' U B U' B' U' B2 L B' L U2
564: L2 B' U B U' B' U' B2 L B' L U'
565: L2 B' L2 U' F' L F L2 B U L U
566: L2 B' L2 U' F' L F L2 B U L U2
567: L2 B' L2 U' F' L F L2 B U L U'
568: L' U D' R' U' B' R D L U B U
569: L' U D' R' U' B' R D L U B U2
570: L' U D' R' U' B' R D L U B U'
571: L' U L D' B D F' D' L' B' D F
572: L' U L2 U F U' F' L' U2 L' U L
573: L' U2 L2 F' D F' D' F2 L2 U2 L U
574: L' U2 L2 F' D F' D' F2 L2 U2 L U2
575: L' U2 L2 F' D F' D' F2 L2 U2 L U'
576: L' U2 L2 F' L' F2 U' F' U L' U2 L
577: L' U2 F' U' F R U' L B U B' R'
578: L' U' L U' F' L F L' U L' U L
579: L' U' L2 F' D' L D L U' L U F
580: L' U' L2 F' D' L2 U' L' D L2 U F
581: L' U' L' B L B' U' L U L' U L
582: L' U' L' B L' D L D' B' L U L
583: L' U' L' B2 D' B' D L B' U L U
584: L' U' L' B2 D' B' D L B' U L U2
585: L' U' L' B2 D' B' D L B' U L U'
586: L' U' B2 D' B' D B' L2 U' L2 U2 L
587: L' D B' U' B U L U L' D' L U
588: L' D B' U' B U L U L' D' L U2
589: L' D B' U' B U L U L' D' L U'
590: L' D2 B' U' B U L U L' D2 L U
591: L' D2 B' U' B U L U L' D2 L U2
592: L' D2 B' U' B U L U L' D2 L U'
593: L' D' B' U' B U L U L' D L U
594: L' D' B' U' B U L U L' D L U2
595: L' D' B' U' B U L U L' D L U'
596: L' D' B' L U' B U B' L' B D L
597: L' R F L B U B' U' L' F' L R'
598: L' R F R' B' U' B U R F' L R'
599: L' R F2 L B U B' U' L' F2 L R'
600: L' R F2 R' B' U' B U R F2 L R'
601: L' R F' L B U B' U' L' F L R'
602: L' R F' R' B' U' B U R F L R'
603: L' R B U R B' R' U' B' R' U2 L
604: L' R B U' B' U L U2 R' F' U F
605: L' R B U' B' U L B U B' R' U
606: L' R B U' B' U L B U B' R' U2
607: L' R B U' B' U L B U B' R' U'
608: L' R B U' B' L' B L U B' L R'
609: L' R B D B D' R' B2 L B U' B'
610: L' R B D B L B' L' D' B' L R'
611: L' R B D' R' B R D B L B2 R'
612: L' R B L U B' U' R' B' U B U
613: L' R B L U B' U' R' B' U B U2
614: L' R B L U B' U' R' B' U B U'
615: L' R B R D L B' L' B D' L R2
616: L' R B R B D' R D R' B' L R2
617: L' R B2 L' B' D' B D L B2 L R'
618: L' R B2 R B D B' D' R' B2 L R'
619: L' R B' U B U' R' U2 L F U' F'
620: L' R B' U B U' R' B' U' B L U
621: L' R B' U B U' R' B' U' B L U2
622: L' R B' U B U' R' B' U' B L U'
623: L' R B' U B R B' R' U' B L R'
624: L' R B' U' L' B L U B L U2 R'
625: L' R B' D L B' L' D' B' R' B2 L
626: L' R B' D' B' D L B2 R' B' U B
627: L' R B' D' B' R' B R D B L R'
628: L' R B' L' D' R' B R B' D L2 R'
629: L' R B' L' B' D L' D' L B L2 R'
630: L' R B' R' U' B U L B U' B' U
631: L' R B' R' U' B U L B U' B' U2
632: L' R B' R' U' B U L B U' B' U'
633: L' R2 D B' D' L R2 U' F' U2 F U
634: L' R2 D B' D' L R2 U' F' U2 F U2
635: L' R2 D B' D' L R2 U' F' U2 F U'
636: L' R2 D2 L2 F L2 D2 R2 U' B U L
637: L' F U2 F' B' U F B U2 F' U L
638: L' F2 B U2 D2 F2 B2 U D2 B U L
639: L' F' U' R U B' U' B R' U F L
640: L' B U D' R2 U' R2 U' D B' U L
641: L' B U2 D2 F2 U' F2 U2 D2 B' U L
642: L' B U' D L2 U' L2 U D' B' U L
643: L' B R D B' D' B2 R' U' B2 U L
644: L' B2 D' B U B' D B U2 B U L
645: L' B2 L' F2 L B U' B U L' F2 L2
646: L' B2 R' U2 F' U' F R U2 B2 U L
647: L' B' U D2 F2 B2 U2 D2 F2 B' U L
648: L' B' U R' F' U F U2 R B L U
649: L' B' U R' F' U F U2 R B L U2
650: L' B' U R' F' U F U2 R B L U'
651: L' B' U F U R U' R' F' U2 B L
652: L' B' U F B U' B' U F' U2 B L
653: L' B' U F B' R2 B R2 F' B U' L
654: L' B' U F2 B2 D2 B D2 F2 B2 U' L
655: L' B' U F' B L2 B L2 F B' U' L
656: L' B' U B' D' F R2 F' D B2 U L
657: L' B' U B' D' B U2 B' D B2 U L
658: L' B' U2 L U F U' F' L' U B L
659: L' B' U2 L U' R' U L' U2 R B L
660: L' B' U2 B L U2 F U F' L' U' L
661: L' B' U2 B2 L' D' B D B2 L U2 L
662: L' B' U' R B R2 U F R' F' L R2
663: L' B' U' R2 D' R' D B R2 U L R
664: L' B' U' R' B L B' R B L' U L
665: L' B' U' F B U F2 L D F' D' F2
666: L' B' U' F2 B R' F' R U F2 L F
667: L' B' U' F2 B' U2 D2 F2 B2 U' D2 L
668: L' B' U' B U L' R2 U2 D2 L2 R2 D2
669: L' B' U' B U2 B L2 D L D' B' L2
670: L' B' U' B U' D2 L2 R2 U2 D2 L' R2
671: L' B' U' B U' L R' F2 L F2 L' R
672: L' B' U' B U' L2 R2 D2 L D2 L2 R2
673: L' B' U' B U' L' R B2 L B2 L R'
674: L' B' U' B U' B' R' U R U2 B L
675: L' B' U' B L F U2 R U R' F' U
676: L' B' U' B L F U2 R U R' F' U2
677: L' B' U' B L F U2 R U R' F' U'
678: L' B' U' B L2 F' D' L D L2 F U
679: L' B' U' B L2 F' D' L D L2 F U2
680: L' B' U' B L2 F' D' L D L2 F U'
681: L' B' U' B2 D B' U' B D' B' U2 L
682: L' B' D B2 U' D' B' U D B2 D' L
683: L' B' L R U B' U' R' U' B U2 B
684: L' B' L F L' F' U' B U F L F'
685: L' B' R U B U' B' R' U' B L U
686: L' B' R U B U' B' R' U' B L U2
687: L' B' R U B U' B' R' U' B L U'
688: L' B' R B L R' U' B L U L' B'
689: L' B' R B' R D' R' D B R' B L
690: L' B' R B' R' B U R' U' R B L
691: L' B' R2 D' R' B' D L B R' U B
692: L' B' R' U F R' F' R U' R B L
693: R U R B2 D B D' R' B U' R' U
694: R U R B2 D B D' R' B U' R' U2
695: R U R B2 D B D' R' B U' R' U'
696: R U R B' R D' R' D B R' U' R'
697: R U R B' R' B U R' U' R U' R'
698: R U R2 F D R2 U R D' R2 U' F'
699: R U R2 F D R' D' R' U R' U' F'
700: R U R' U F R' F' R U' R U' R'
701: R U B2 D B D' B R2 U R2 U2 R'
702: R U2 R2 F D' F D F2 R2 U2 R' U
703: R U2 R2 F D' F D F2 R2 U2 R' U2
704: R U2 R2 F D' F D F2 R2 U2 R' U'
705: R U2 R2 F R F2 U F U' R U2 R'
706: R U2 F U F' L' U R' B' U' B L
707: R U' D L U B L' D' R' U' B' U
708: R U' D L U B L' D' R' U' B' U2
709: R U' D L U B L' D' R' U' B' U'
710: R U' R2 U' F' U F R U2 R U' R'
711: R U' R' D B' D' F D R B D' F'
712: R D B U B' U' R' U' R D' R' U
713: R D B U B' U' R' U' R D' R' U2
714: R D B U B' U' R' U' R D' R' U'
715: R D B R' U B' U' B R B' D' R'
716: R D2 B U B' U' R' U' R D2 R' U
717: R D2 B U B' U' R' U' R D2 R' U2
718: R D2 B U B' U' R' U' R D2 R' U'
719: R D' B U B' U' R' U' R D R' U
720: R D' B U B' U' R' U' R D R' U2
721: R D' B U B' U' R' U' R D R' U'
722: R F U L' U' B U B' L U' F' R'
723: R F2 B' U2 D2 F2 B2 U' D2 B' U' R'
724: R F' U2 F B U' F' B' U2 F U' R'
725: R B U L B' R' B L' B' R U' R'
726: R B U L2 D L D' B' L2 U' L' R'
727: R B U L' B' L2 U' F' L F L2 R'
728: R B U F2 B U2 D2 F2 B2 U D2 R'
729: R B U F2 B' L F L' U' F2 R' F'
730: R B U F' B' U' F2 R' D' F D F2
731: R B U B2 D' B U B' D B U2 R'
732: R B U B' U D2 L2 R2 U2 D2 L2 R
733: R B U B' U L R' F2 R' F2 L' R
734: R B U B' U L2 R2 D2 R' D2 L2 R2
735: R B U B' U L' R B2 R' B2 L R'
736: R B U B' U B L U' L' U2 B' R'
737: R B U B' U2 B' R2 D' R' D B R2
738: R B U B' U' L2 R U2 D2 L2 R2 D2
739: R B U B' R2 F D R' D' R2 F' U
740: R B U B' R2 F D R' D' R2 F' U2
741: R B U B' R2 F D R' D' R2 F' U'
742: R B U B' R' F' U2 L' U' L F U
743: R B U B' R' F' U2 L' U' L F U2
744: R B U B' R' F' U2 L' U' L F U'
745: R B U2 R' U L U' R U2 L' B' R'
746: R B U2 R' U' F' U F R U' B' R'
747: R B U2 B2 R D B' D' B2 R' U2 R'
748: R B U2 B' R' U2 F' U' F R U R'
749: R B U' D2 F2 B2 U2 D2 F2 B U' R'
750: R B U' L F U' F' U2 L' B' R' U
751: R B U' L F U' F' U2 L' B' R' U2
752: R B U' L F U' F' U2 L' B' R' U'
753: R B U' F B' R2 B' R2 F' B U R'
754: R B U' F2 B2 D2 B' D2 F2 B2 U R'
755: R B U' F' U' L' U L F U2 B' R'
756: R B U' F' B L2 B' L2 F B' U R'
757: R B U' F' B' U B U' F U2 B' R'
758: R B U' B D F' L2 F D' B2 U' R'
759: R B U' B D B' U2 B D' B2 U' R'
760: R B D' B2 U D B U' D' B2 D R'
761: R B L U' F' L F L' U L' B' R'
762: R B L2 D L B D' R' B' L U' B'
763: R B L' U' B' U B L U B' R' U
764: R B L' U' B' U B L U B' R' U2
765: R B L' U' B' U B L U B' R' U'
766: R B L' R' U' B U L U B' U2 B'
767: R B L' B L B' U' L U L' B' R'
768: R B L' B L' D L D' B' L B' R'
769: R B L' B' L R' U B' R' U' R B
770: R B R' F' R F U B' U' F' R' F
771: R B2 D B' U' B D' B' U2 B' U' R'
772: R B2 L U2 F U F' L' U2 B2 U' R'
773: R B2 R F2 R' B' U B' U' R F2 R2
774: R B' U D' R2 U R2 U' D B U' R'
775: R B' U2 D2 F2 U F2 U2 D2 B U' R'
776: R B' U' D L2 U L2 U D' B U' R'
777: R B' L' D' B D B2 L U B2 U' R'
778: R2 U D' F' R U R' U' F U' D R2
779: R2 U2 D2 L' F U F' U' L U2 D2 R2
780: R2 U' D B' L U L' U' B U D' R2
781: R2 U' L R U' F' U F R' U L' R2
782: R2 U' R B U' F' U F B' R' U R2
783: R2 D' F R U' L' U L R' F' D R2
784: R2 F2 B2 L' B D B' D' L F2 B2 R2
785: R2 B U' B' U B U B2 R' B R' U
786: R2 B U' B' U B U B2 R' B R' U2
787: R2 B U' B' U B U B2 R' B R' U'
788: R2 B R2 U F R' F' R2 B' U' R' U
789: R2 B R2 U F R' F' R2 B' U' R' U2
790: R2 B R2 U F R' F' R2 B' U' R' U'
791: R2 B' L2 B R' B' L2 B2 U B' U' R'
792: R2 B' R' B U R2 F R2 U R' U' F'
793: R' U2 L R' F D' F D R F2 L' R
794: R' U2 F' L2 U' B' U B L2 U2 F R
795: R' U' R U2 B U L F U2 F' L' B'
796: R' U' R2 B' R2 U' R U B2 U2 B' U
797: R' U' R2 B' R2 U' R U B2 U2 B' U2
798: R' U' R2 B' R2 U' R U B2 U2 B' U'
799: R' U' F2 U R U2 L F L' F U F2
800: R' U' F2 B L F L' F B' U R U
801: R' U' F2 B L F L' F B' U R U2
802: R' U' F2 B L F L' F B' U R U'
803: R' U' F' U2 F U2 F' L' U' L F R
804: R' U' B' R D' F R' F' D2 B' D' B2
805: R' D2 L2 F' L2 D2 R2 U B' U' R' U
806: R' D2 L2 F' L2 D2 R2 U B' U' R' U2
807: R' D2 L2 F' L2 D2 R2 U B' U' R' U'
808: R' D' R' D B R2 U R B' U' R' U
809: R' D' R' D B R2 U R B' U' R' U2
810: R' D' R' D B R2 U R B' U' R' U'
811: R' F2 D' F' D F2 U' F U R2 U2 R'
812: R' B R2 B U B' U' R' U R' B' R
813: R' B2 R2 B U B' U' R' U R' B2 R
814: R' B' R2 B U B' U' R' U R' B R
815: F U R U2 R' F2 D' B L B' D F
816: F U2 F' L' B' R' U2 R U' B U L
817: F U' B' U F' U' B2 L U L' U' B'
818: F L F' D' L' B' U' L' B U D L
819: F R U' R2 U' F' U F R2 U R' F'
820: F R B U2 B' R' U' F' U2 L' U L
821: F' U B U' F U B2 R' U' R U B
822: F' U2 F R B L U2 L' U B' U' R'
823: F' U' L' U2 L F2 D B' R' B D' F'
824: F' L' U L2 U F U' F' L2 U' L F
825: F' L' B' U2 B L U F U2 R U' R'
826: F' R' F D R B U R B' U' D' R'
827: B U R2 F R F' U' R2 U B' U' R'
828: B U B' R' F B' R2 F' R2 B U R
829: B U B' R' F' U' F' L F L' F R
830: B U' L U' F' L F L' U2 L' U' B'
831: B U' L' U L U F2 B' R' F' R F'
832: B U' L' B L B' U' L U2 L' U' B'
833: B D B' U B' R' U' R U B2 D' B'
834: B D2 B' U B' R' U' R U B2 D2 B'
835: B D' B' U B' R' U' R U B2 D B'
836: B L' D' B' U' B D L B' L' U L
837: B L' B' L U F' L U' L2 U L F
838: B L' B' L U B' U R' U2 R U B
839: B R U R B' R' U' B R' U' B' U
840: B R U R B' R' U' B R' U' B' U2
841: B R U R B' R' U' B R' U' B' U'
842: B R D' B U B' D R' B' R U' R'
843: B2 U R B' R' B2 U' L' U' B U L
844: B2 U' L' B L B2 U R U B' U' R'
845: B2 L' B' R B L U B2 U' B R' B'
846: B2 L' B' R B2 L U B U' B2 R' B'
847: B2 R B L' B2 R' U' B' U B2 L B
848: B2 R B L' B' R' U' B2 U B' L B
849: B' U R U' R' U' F2 B L F L' F
850: B' U R B' R' B U R' U2 R U B
851: B' U R' U F R' F' R U2 R U B
852: B' U' L2 F' L' F U L2 U' B U L
853: B' U' B L F U F R' F' R F' L'
854: B' U' B L F' B L2 F L2 B' U' L'
855: B' D B U' B L U L' U' B2 D' B
856: B' D2 B U' B L U L' U' B2 D2 B
857: B' D' B U' B L U L' U' B2 D B
858: B' L' U' L' B L U B' L U B U
859: B' L' U' L' B L U B' L U B U2
860: B' L' U' L' B L U B' L U B U'
861: B' L' D B' U' B D' L B L' U L
862: B' R D B U B' D' R' B R U' R'
863: B' R B R' U' F R' U R2 U' R' F'
864: B' R B R' U' B U' L U2 L' U' B'
search finished in 28.720736s
"""