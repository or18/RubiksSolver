class State:
    def __init__(self, cp, co, ep, eo):
        self.cp=cp
        self.co=co
        self.ep=ep
        self.eo=eo
    def apply_move_edge(self, move, e):
        new_ep=[-1]*12
        new_eo=[-1]*12
        index=self.ep.index(e)
        index_next=move.ep.index(e)
        new_ep[index_next]=e
        new_eo[index_next]=(self.eo[index]+move.eo[index_next])%2
        return State(self.cp, self.co, new_ep, new_eo)
    def apply_move_corner(self, move, c):
        new_cp=[-1]*8
        new_co=[-1]*8
        index=self.cp.index(c)
        index_next=move.cp.index(c)
        new_cp[index_next]=c
        new_co[index_next]=(self.co[index]+move.co[index_next])%3
        return State(new_cp, new_co, self.ep, self.eo)
    def apply_move(self, move):
        new_cp=[self.cp[p] for p in move.cp]
        new_co=[(self.co[p]+move.co[i])%3 for i, p in enumerate(move.cp)]
        new_ep=[self.ep[p] for p in move.ep]
        new_eo=[(self.eo[p]+move.eo[i])%2 for i, p in enumerate(move.ep)]
        return State(new_cp, new_co, new_ep, new_eo)

moves = {
   "U": State([3, 0, 1, 2, 4, 5, 6, 7], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 7, 4, 5, 6, 8, 9, 10, 11], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
   "U2": State([2, 3, 0, 1, 4, 5, 6, 7], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 6, 7, 4, 5, 8, 9, 10, 11], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
   "U'": State([1, 2, 3, 0, 4, 5, 6, 7], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 5, 6, 7, 4, 8, 9, 10, 11], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
   "D": State([0, 1, 2, 3, 5, 6, 7, 4], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 8], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
   "D2": State([0, 1, 2, 3, 6, 7, 4, 5], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 8, 9], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
   "D'": State([0, 1, 2, 3, 7, 4, 5, 6], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7, 11, 8, 9, 10], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
   "L": State([4, 1, 2, 0, 7, 5, 6, 3], [2, 0, 0, 1, 1, 0, 0, 2], [11, 1, 2, 7, 4, 5, 6, 0, 8, 9, 10, 3], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
   "L2": State([7, 1, 2, 4, 3, 5, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0], [3, 1, 2, 0, 4, 5, 6, 11, 8, 9, 10, 7], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
   "L'": State([3, 1, 2, 7, 0, 5, 6, 4], [2, 0, 0, 1, 1, 0, 0, 2], [7, 1, 2, 11, 4, 5, 6, 3, 8, 9, 10, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
   "R": State([0, 2, 6, 3, 4, 1, 5, 7], [0, 1, 2, 0, 0, 2, 1, 0], [0, 5, 9, 3, 4, 2, 6, 7, 8, 1, 10, 11], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
   "R2": State([0, 6, 5, 3, 4, 2, 1, 7], [0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 1, 3, 4, 9, 6, 7, 8, 5, 10, 11], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
   "R'": State([0, 5, 1, 3, 4, 6, 2, 7], [0, 1, 2, 0, 0, 2, 1, 0], [0, 9, 5, 3, 4, 1, 6, 7, 8, 2, 10, 11], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
   "F": State([0, 1, 3, 7, 4, 5, 2, 6], [0, 0, 1, 2, 0, 0, 2, 1], [0, 1, 6, 10, 4, 5, 3, 7, 8, 9, 2, 11], [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0]),
   "F2": State([0, 1, 7, 6, 4, 5, 3, 2], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 3, 2, 4, 5, 10, 7, 8, 9, 6, 11], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
   "F'": State([0, 1, 6, 2, 4, 5, 7, 3], [0, 0, 1, 2, 0, 0, 2, 1], [0, 1, 10, 6, 4, 5, 2, 7, 8, 9, 3, 11], [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0]),
   "B": State([1, 5, 2, 3, 0, 4, 6, 7], [1, 2, 0, 0, 2, 1, 0, 0], [4, 8, 2, 3, 1, 5, 6, 7, 0, 9, 10, 11], [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]),
   "B2": State([5, 4, 2, 3, 1, 0, 6, 7], [0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 2, 3, 8, 5, 6, 7, 4, 9, 10, 11], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
   "B'": State([4, 0, 2, 3, 5, 1, 6, 7], [1, 2, 0, 0, 2, 1, 0, 0], [8, 4, 2, 3, 0, 5, 6, 7, 1, 9, 10, 11], [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0])
}

move_names=['U', 'U2', "U'", 'D', 'D2', "D'", 'L', 'L2', "L'", 'R', 'R2', "R'", 'F', 'F2', "F'", 'B', 'B2', "B'"]

move_UDLRFB=['U', 'U2', "U'", 'D', 'D2', "D'", 'L', 'L2', "L'", 'R', 'R2', "R'", 'F', 'F2', "F'", 'B', 'B2', "B'"]
move_URF=['U', 'U2', "U'", 'R', 'R2', "R'", 'F', 'F2', "F'"]
move_URFB=['U', 'U2', "U'", 'R', 'R2', "R'", 'F', 'F2', "F'", 'B', 'B2', "B'"]
move_UDR=['U', 'U2', "U'", 'D', 'D2', "D'", 'R', 'R2', "R'"]
move_UDRF=['U', 'U2', "U'", 'D', 'D2', "D'", 'R', 'R2', "R'", 'F', 'F2', "F'"]