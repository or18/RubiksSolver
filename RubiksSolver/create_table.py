import RubiksSolver.move as move
import RubiksSolver.function as function
import time
import array
import os
def create_edge_move_table():
    path="RubiksSolver/table/edge_move_table"
    if not os.path.exists(path):
        print(f"start creating edge move table")
        t=time.time()
        move_table=array.array('i',[0 for i in range(24*18)])
        for i in range(24):
            ep=[-1]*12
            eo=[-1]*12
            co=[0]*8
            cp=[0]*8
            ep[i//2]=i//2
            eo[i//2]=i%2
            state=move.State(cp, co, ep, eo)
            for j in range(18):
                new_state=state.apply_move_edge(move.moves[move.move_names[j]], i//2)
                index=new_state.ep.index(i//2)
                move_table[18*i+j]=2*index+new_state.eo[index]
        with open(path, 'wb') as f:
            move_table.tofile(f)
        print(f"created edge move table in {time.time()-t:.6f}s and save to {path}")
        return move_table
    else:
        move_table = array.array('i')
        with open(path, 'rb') as f:
            move_table.fromfile(f, 18*24)
        return move_table
            
def create_corner_move_table():
    path="RubiksSolver/table/corner_move_table"
    if not os.path.exists(path):
        print(f"start creating corner move table")
        t=time.time()
        move_table=array.array('i',[0 for i in range(24*18)])
        for i in range(24):
            ep=[0]*12
            eo=[0]*12
            co=[-1]*8
            cp=[-1]*8
            cp[i//3]=i//3
            co[i//3]=i%3
            state=move.State(cp, co, ep, eo)
            for j in range(18):
                new_state=state.apply_move_corner(move.moves[move.move_names[j]], i//3)
                index=new_state.cp.index(i//3)
                move_table[18*i+j]=3*index+new_state.co[index]
        with open(path, 'wb') as f:
            move_table.tofile(f)
        print(f"created corner move table in {time.time()-t:.6f}s and save to {path}")
        return move_table
    else:
        move_table = array.array('i')
        with open(path, 'rb') as f:
            move_table.fromfile(f, 18*24)
        return move_table
    
def create_multi_move_table(n, c, pn, size, table, path):
    if not os.path.exists(path):
        print(f"start creating multi move table")
        tmp_table={i: v for i, v in enumerate(table)}
        tmp=0
        t=time.time()
        move_table=array.array('i', [-1 for i in range(size*18)])
        for i in range(size):
            for j in range(18):
                a=function.index_to_array(i, n, c, pn)
                if move_table[18*i+j]!=-1:
                    continue
                a=function.index_to_array(i, n, c, pn)
                tmp=function.array_to_index([tmp_table[18*k+j] for k in a], n, c, pn)
                move_table[18*i+j]=tmp
                move_table[18*tmp+3*(j//3)+2-j%3]=i
        with open(path, "wb") as f:
            move_table.tofile(f)
        print(f"created multi move table in {time.time()-t:.6f}s and save to {path}")
        return move_table
    else:
        move_table = array.array('i')
        with open(path, 'rb') as f:
            move_table.fromfile(f, size*18)
        return move_table

def create_prune_table(index1, index2, size1, size2, depth, table1, table2, path):
    if not os.path.exists(path):
        print(f"start creating prune table")
        t=time.time()
        size=size1*size2
        prune_table=array.array('i',[-1 for i in range(size)])
        start=index1*size2+index2
        loop_index=[i for i in range(start, size)]
        loop_index.extend(range(0, start))
        prune_table[start]=0
        num_filled=1
        for d in range(0, depth):
            for i in loop_index:
                if prune_table[i]==d:
                    for j in range(18):
                        next_i=table1[(i//size2)*18+j]*size2+table2[(i%size2)*18+j]
                        if prune_table[next_i]==-1:
                            prune_table[next_i]=d+1
                            num_filled+=1
            print(f"d={d}, {100*num_filled/size:.6f}%")
        with open(path, "wb") as f:
            prune_table.tofile(f)
        print(f"created prune table in {time.time()-t:.6f}s and saved to {path}")
        return prune_table
    else:
        prune_table = array.array('i')
        with open(path, 'rb') as f:
            prune_table.fromfile(f, size1*size2)
        return prune_table
    
def create_eo_move_table():
    path="RubiksSolver/table/eo_move_table"
    if not os.path.exists(path):
        print(f"start creating eo move table")
        t=time.time()
        move_table=array.array('i',[0 for i in range(2**11*18)])
        for i in range(2**11):
            ep=[0]*12
            eo=function.index_to_o(i, 2, 12)
            co=[0]*8
            cp=[0]*8
            state=move.State(cp, co, ep, eo)
            for j in range(18):
                new_state=state.apply_move(move.moves[move.move_names[j]])
                move_table[18*i+j]=function.o_to_index(new_state.eo, 2, 12)
        with open(path, 'wb') as f:
            move_table.tofile(f)
        print(f"created eo move table in {time.time()-t:.6f}s and save to {path}")
        return move_table
    else:
        move_table = array.array('i')
        with open(path, 'rb') as f:
            move_table.fromfile(f, 2**11*18)
        return move_table
    
def create_co_move_table():
    path="RubiksSolver/table/co_move_table"
    if not os.path.exists(path):
        print(f"start creating co move table")
        t=time.time()
        move_table=array.array('i',[0 for i in range(3**7*18)])
        for i in range(3**7):
            ep=[0]*12
            eo=[0]*12
            cp=[0]*8
            co=function.index_to_o(i, 3, 8)
            state=move.State(cp, co, ep, eo)
            for j in range(18):
                new_state=state.apply_move(move.moves[move.move_names[j]])
                move_table[18*i+j]=function.o_to_index(new_state.co, 3, 8)
        with open(path, 'wb') as f:
            move_table.tofile(f)
        print(f"created co move table in {time.time()-t:.6f}s and save to {path}")
        return move_table
    else:
        move_table = array.array('i')
        with open(path, 'rb') as f:
            move_table.fromfile(f, 3**7*18)
        return move_table
    
def create_ep_move_table():
    path="RubiksSolver/table/single_ep_move_table"
    if not os.path.exists(path):
        print(f"start creating single ep move table")
        t=time.time()
        move_table=array.array('i',[0 for i in range(12*18)])
        for i in range(12):
            ep=[-1]*12
            eo=[-1]*12
            co=[0]*8
            cp=[0]*8
            ep[i]=i
            eo[i]=0
            state=move.State(cp, co, ep, eo)
            for j in range(18):
                new_state=state.apply_move_edge(move.moves[move.move_names[j]], i)
                move_table[18*i+j]=new_state.ep.index(i)
        with open(path, 'wb') as f:
            move_table.tofile(f)
        print(f"created single ep move table in {time.time()-t:.6f}s and save to {path}")
        return move_table
    else:
        move_table = array.array('i')
        with open(path, 'rb') as f:
            move_table.fromfile(f, 12*18)
        return move_table
    
def create_cp_move_table():
    path="RubiksSolver/table/single_cp_move_table"
    if not os.path.exists(path):
        print(f"start creating single cp move table")
        t=time.time()
        move_table=array.array('i',[0 for i in range(8*18)])
        for i in range(8):
            ep=[0]*12
            eo=[0]*12
            co=[-1]*8
            cp=[-1]*8
            cp[i]=i
            co[i]=0
            state=move.State(cp, co, ep, eo)
            for j in range(18):
                new_state=state.apply_move_corner(move.moves[move.move_names[j]], i)
                move_table[18*i+j]=new_state.cp.index(i)
            
        with open(path, 'wb') as f:
            move_table.tofile(f)
        print(f"created single cp move table in {time.time()-t:.6f}s and save to {path}")
        return move_table
    else:
        move_table = array.array('i')
        with open(path, 'rb') as f:
            move_table.fromfile(f, 8*18)
        return move_table
    
def create_ma_table():
    ret={prev*18+i: (i//3==prev//3 or ((i//3)//2==(prev//3)//2 and (prev//3)%2>(i//3)%2)) if prev<18 else False for prev in range(19) for i in range(18)}
    return ret
            
