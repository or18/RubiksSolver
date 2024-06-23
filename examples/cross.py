import RubiksSolver.solver as sv
import RubiksSolver.move as mv

#cross search
scramble="F2 U L2 F2 D2 U' B2 D2 F2 U' B2 D R F2 D U' B' R' D2 U"
scramble=sv.solve_F2L(scramble, "", False, False, False, False, 5, True, 1, "cross", mv.move_UDLRFB)

"""
start creating edge move table
created edge move table in 0.000000s and save to RubiksSolver/table/edge_move_table
start creating multi move table
created multi move table in 0.056589s and save to RubiksSolver/table/2edges_move_table
start creating prune table
d=0, 0.005739%
d=1, 0.062414%
d=2, 0.562443%
d=3, 4.080937%
d=4, 20.717832%
d=5, 55.602904%
d=6, 68.145231%
d=7, 68.181818%
created prune table in 0.053587s ans saved to RubiksSolver/table/edge1618_edge2022_prune_table
1: D R' D' L B2
2: D R' D' B2 L
3: L D R' D' B2
4: L B2 D R' D'
5: R' D' L R B2
6: R' D' R B2 L
7: B2 D R' D' L
8: B2 L D R' D'
search finished in 0.000000s
"""