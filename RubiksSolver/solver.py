import RubiksSolver.search as search
import RubiksSolver.function as function
import RubiksSolver.create_table as create_table
import RubiksSolver.move as mv
import time
import os
import array

    
def solve_cross(scramble, rotation, max_length, full_search, sol_index, name, move_restrict):
    if not scramble:
        return False
    if not os.path.exists('RubiksSolver/table'):
        os.makedirs('RubiksSolver/table')
    table1_path='RubiksSolver/table/2edges_move_table'
    edge_move_table=create_table.create_edge_move_table()
    table1=create_table.create_multi_move_table(2, 2, 12, 24*22, edge_move_table, table1_path)
    prune_path1='RubiksSolver/table/edge1618_edge2022_prune_table'
    index1=416
    index2=520
    prune_table1=create_table.create_prune_table(index1, index2, 24*22, 24*22, 8, table1, table1, prune_path1)
    alg=function.AlgRotation(function.StringToAlg(scramble), rotation)
    for move in alg:
        index1=table1[index1*18+move]
        index2=table1[index2*18+move]
        
    move_restrict=array.array('i',[mv.move_names.index(i) for i in move_restrict])
    ma=create_table.create_ma_table()
    a=search.cross_search(table1, prune_table1, rotation, full_search, sol_index, move_restrict, ma)
    t=time.time()
    n=a.start_search(index1, index2, max_length)
    t=time.time()-t
    if full_search:
        if n>0:
            print(f"search finished in {t:.6f}s")
            return False
        else:
            print("No solution found")
            return False
    else:
        if n:
            if n!=" ":
                if rotation!="":
                    print(f"{rotation} {n} // {name} No.{sol_index}")
                else:
                    print(f"{n} // {name} No.{sol_index}")
                n=function.AlgToString(alg)+n
                return n
            else:
                print(f"// {name}")
                return function.AlgToString(alg)
        else:
            print(f"// No solution for {name}")
            return function.AlgToString(alg)
        
def solve_xcross(scramble, rotation, slot1, max_length, full_search, sol_index, name, move_restrict):
    if not scramble:
        return False
    if not os.path.exists('RubiksSolver/table'):
        os.makedirs('RubiksSolver/table')
    slot_set=["BL", "BR", "FR", "FL"]
    if (slot1 not in set(slot_set)):
        print(f"slot error")
    else:
        alg=function.AlgRotation(function.StringToAlg(scramble), rotation)
        edge_move_table=create_table.create_edge_move_table()
        corner_move_table=create_table.create_corner_move_table()
        table1_path='RubiksSolver/table/5edges_move_table'
        table1=create_table.create_multi_move_table2(5, 2, 12, 24*22*20*18*16, edge_move_table, table1_path)
    
        prune_path_set=['RubiksSolver/table/edge016182022_corner12_prune_table', 'RubiksSolver/table/edge216182022_corner15_prune_table', 'RubiksSolver/table/edge416182022_corner18_prune_table', 'RubiksSolver/table/edge616182022_corner21_prune_table']
        edge_solved_set=[2989056, 2989088, 2989120, 2989152]
        corner_solved_set=[12, 15, 18, 21]
        
        index1=edge_solved_set[slot_set.index(slot1)]
        index2=corner_solved_set[slot_set.index(slot1)]
        prune_table1=create_table.create_prune_table2(index1, index2, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[slot_set.index(slot1)])
        table1=array.array('i', [24*i for i in table1])
        index1*=24
        for move in alg:
            index1=table1[index1+move]
            index2=corner_move_table[index2*18+move]
            
        move_restrict=array.array('i',[mv.move_names.index(i) for i in move_restrict])
        ma=create_table.create_ma_table()
        a=search.xcross_search(table1, corner_move_table, prune_table1, rotation, full_search, sol_index, move_restrict, ma)
        t=time.time()
        n=a.start_search(index1, index2, max_length)
        t=time.time()-t
        if full_search:
            if n>0:
                print(f"search finished in {t:.6f}s")
                return False
            else:
                print("No solution found")
                return False
        else:
            if n:
                if n!=" ":
                    if rotation!="":
                        print(f"{rotation} {n} // {name} No.{sol_index}")
                    else:
                        print(f"{n} // {name} No.{sol_index}")
                    n=function.AlgToString(alg)+n
                    return n
                else:
                    print(f"//{name}")
                    return function.AlgToString(alg)
            else:
                print(f"// No solution for {name}")
                return function.AlgToString(alg)
        
def solve_xxcross(scramble, rotation, slot1, slot2, max_length, full_search, sol_index, name, move_restrict):
    if not scramble:
        return False
    if not os.path.exists('RubiksSolver/table'):
        os.makedirs('RubiksSolver/table')
    slot_set=["BL", "BR", "FR", "FL"]
    if (slot1 not in set(slot_set)) or (slot2 not in set(slot_set)) or slot1==slot2:
        print(f"slot error")
    else: 
        alg=function.AlgRotation(function.StringToAlg(scramble), rotation)
        edge_move_table=create_table.create_edge_move_table()
        corner_move_table=create_table.create_corner_move_table()
        table1_path='RubiksSolver/table/5edges_move_table'
        table1=create_table.create_multi_move_table2(5, 2, 12, 24*22*20*18*16, edge_move_table, table1_path)
        prune_path_set=['RubiksSolver/table/edge016182022_corner12_prune_table', 'RubiksSolver/table/edge216182022_corner15_prune_table', 'RubiksSolver/table/edge416182022_corner18_prune_table', 'RubiksSolver/table/edge616182022_corner21_prune_table']
        edge_solved_set=[2989056, 2989088, 2989120, 2989152]
        corner_solved_set=[12, 15, 18, 21]
        
        index1=edge_solved_set[slot_set.index(slot1)]
        index2=corner_solved_set[slot_set.index(slot1)]
        prune_table1=create_table.create_prune_table2(index1, index2, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[slot_set.index(slot1)])
        
        index3=edge_solved_set[slot_set.index(slot2)]
        index4=corner_solved_set[slot_set.index(slot2)]
        prune_table2=create_table.create_prune_table2(index3, index4, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[slot_set.index(slot2)])
        table1=array.array('i', [24*i for i in table1])
        
        index1*=24
        index3*=24
        for move in alg:
            index1=table1[index1+move]
            index2=corner_move_table[index2*18+move]
            index3=table1[index3+move]
            index4=corner_move_table[index4*18+move]
            
        move_restrict=array.array('i',[mv.move_names.index(i) for i in move_restrict])
        ma=create_table.create_ma_table()
        a=search.xxcross_search(table1, corner_move_table, prune_table1, prune_table2, rotation, full_search, sol_index, move_restrict, ma)
        t=time.time()
        n=a.start_search(index1, index2, index3, index4, max_length)
        t=time.time()-t
        if full_search:
            if n>0:
                print(f"search finished in {t:.6f}s")
                return False
            else:
                print("No solution found")
                return False
        else:
            if n:
                if n!=" ":
                    if rotation!="":
                        print(f"{rotation} {n} // {name} No.{sol_index}")
                    else:
                        print(f"{n} // {name} No.{sol_index}")
                    n=function.AlgToString(alg)+n
                    return n
                else:
                    print(f"//{name}")
                    return function.AlgToString(alg)
            else:
                print(f"// No solution for {name}")
                return function.AlgToString(alg)
            
def solve_xxxcross(scramble, rotation, slot1, slot2, slot3, max_length, full_search, sol_index, name, move_restrict):
    if not scramble:
        return False
    if not os.path.exists('RubiksSolver/table'):
        os.makedirs('RubiksSolver/table')
    slot_set=["BL", "BR", "FR", "FL"]
    if (slot1 not in set(slot_set)) or (slot2 not in set(slot_set)) or (slot3 not in set(slot_set)) or slot1==slot2 or slot1==slot2 or slot2==slot3:
        print(f"slot error")
    else: 
        alg=function.AlgRotation(function.StringToAlg(scramble), rotation)
        edge_move_table=create_table.create_edge_move_table()
        corner_move_table=create_table.create_corner_move_table()
        table1_path='RubiksSolver/table/5edges_move_table'
        table1=create_table.create_multi_move_table2(5, 2, 12, 24*22*20*18*16, edge_move_table, table1_path)
        prune_path_set=['RubiksSolver/table/edge016182022_corner12_prune_table', 'RubiksSolver/table/edge216182022_corner15_prune_table', 'RubiksSolver/table/edge416182022_corner18_prune_table', 'RubiksSolver/table/edge616182022_corner21_prune_table']
        edge_solved_set=[2989056, 2989088, 2989120, 2989152]
        corner_solved_set=[12, 15, 18, 21]
        
        index1=edge_solved_set[slot_set.index(slot1)]
        index2=corner_solved_set[slot_set.index(slot1)]
        prune_table1=create_table.create_prune_table2(index1, index2, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[slot_set.index(slot1)])
        
        index3=edge_solved_set[slot_set.index(slot2)]
        index4=corner_solved_set[slot_set.index(slot2)]
        prune_table2=create_table.create_prune_table2(index3, index4, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[slot_set.index(slot2)])
        
        index5=edge_solved_set[slot_set.index(slot3)]
        index6=corner_solved_set[slot_set.index(slot3)]
        prune_table3=create_table.create_prune_table2(index5, index6, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[slot_set.index(slot3)])
        table1=array.array('i', [24*i for i in table1])
        
        index1*=24
        index3*=24
        index5*=24
        for move in alg:
            index1=table1[index1+move]
            index2=corner_move_table[index2*18+move]
            index3=table1[index3+move]
            index4=corner_move_table[index4*18+move]
            index5=table1[index5+move]
            index6=corner_move_table[index6*18+move]
        
        move_restrict=array.array('i',[mv.move_names.index(i) for i in move_restrict])
        ma=create_table.create_ma_table()
        a=search.xxxcross_search(table1, corner_move_table, prune_table1, prune_table2, prune_table3, rotation, full_search, sol_index, move_restrict, ma)
        t=time.time()
        n=a.start_search(index1, index2, index3, index4, index5, index6, max_length)
        t=time.time()-t
        if full_search:
            if n>0:
                print(f"search finished in {t:.6f}s")
                return False
            else:
                print("No solution found")
                return False
        else:
            if n:
                if n!=" ":
                    if rotation!="":
                        print(f"{rotation} {n} // {name} No.{sol_index}")
                    else:
                        print(f"{n} // {name} No.{sol_index}")
                    n=function.AlgToString(alg)+n
                    return n
                else:
                    print(f"//{name}")
                    return function.AlgToString(alg)
            else:
                print(f"// No solution for {name}")
                return function.AlgToString(alg)
            
def solve_xxxxcross(scramble, rotation, max_length, full_search, sol_index, name, move_restrict):
    if not scramble:
        return False
    if not os.path.exists('RubiksSolver/table'):
        os.makedirs('RubiksSolver/table')
    alg=function.AlgRotation(function.StringToAlg(scramble), rotation)
    edge_move_table=create_table.create_edge_move_table()
    corner_move_table=create_table.create_corner_move_table()
    table1=create_table.create_multi_move_table2(5, 2, 12, 24*22*20*18*16, edge_move_table, 'RubiksSolver/table/5edges_move_table')
    prune_path_set=['RubiksSolver/table/edge016182022_corner12_prune_table', 'RubiksSolver/table/edge216182022_corner15_prune_table', 'RubiksSolver/table/edge416182022_corner18_prune_table', 'RubiksSolver/table/edge616182022_corner21_prune_table']
    edge_solved_set=[2989056, 2989088, 2989120, 2989152]
    corner_solved_set=[12, 15, 18, 21]
        
    index1=edge_solved_set[0]
    index2=corner_solved_set[0]
    prune_table1=create_table.create_prune_table2(index1, index2, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[0])
        
    index3=edge_solved_set[1]
    index4=corner_solved_set[1]
    prune_table2=create_table.create_prune_table2(index3, index4, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[1])
        
    index5=edge_solved_set[2]
    index6=corner_solved_set[2]
    prune_table3=create_table.create_prune_table2(index5, index6, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[2])
        
    index7=edge_solved_set[3]
    index8=corner_solved_set[3]
    prune_table4=create_table.create_prune_table2(index7, index8, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[3])
    table1=array.array('i', [24*i for i in table1])
    index1*=24
    index3*=24
    index5*=24
    index7*=24
    for move in alg:
        index1=table1[index1+move]
        index2=corner_move_table[index2*18+move]
        index3=table1[index3+move]
        index4=corner_move_table[index4*18+move]
        index5=table1[index5+move]
        index6=corner_move_table[index6*18+move]
        index7=table1[index7+move]
        index8=corner_move_table[index8*18+move]
    
    move_restrict=array.array('i',[mv.move_names.index(i) for i in move_restrict])
    ma=create_table.create_ma_table()
    a=search.xxxxcross_search(table1, corner_move_table, prune_table1, prune_table2, prune_table3, prune_table4, rotation, full_search, sol_index, move_restrict, ma)
    t=time.time()
    n=a.start_search(index1, index2, index3, index4, index5, index6, index7, index8, max_length)
    t=time.time()-t
    if full_search:
        if n>0:
            print(f"search finished in {t:.6f}s")
            return False
        else:
            print("No solution found")
            return False
    else:
        if n:
            if n!=" ":
                if rotation!="":
                    print(f"{rotation} {n} // {name} No.{sol_index}")
                else:
                    print(f"{n} // {name} No.{sol_index}")
                n=function.AlgToString(alg)+n
                return n
            else:
                print(f"// {name}")
                return function.AlgToString(alg)
        else:
            print(f"// No solution for {name}")
            return function.AlgToString(alg)
        
def solve_F2L(scramble, rotation, solve_BL, solve_BR, solve_FR, solve_FL, max_length, full_search, sol_index, name, move_restrict):
    if not scramble:
        return False
    slot=[]
    if solve_BL:
        slot.append("BL")
    if solve_BR:
        slot.append("BR")
    if solve_FR:
        slot.append("FR")
    if solve_FL:
        slot.append("FL")
    if len(slot)==0:
        return solve_cross(scramble, rotation, max_length, full_search, sol_index, name, move_restrict)
    elif len(slot)==1:
        return solve_xcross(scramble, rotation, slot[0], max_length, full_search, sol_index, name, move_restrict)
    elif len(slot)==2:
        return solve_xxcross(scramble, rotation, slot[0], slot[1], max_length, full_search, sol_index, name, move_restrict)
    elif len(slot)==3:
        return solve_xxxcross(scramble, rotation, slot[0], slot[1], slot[2], max_length, full_search, sol_index, name, move_restrict)
    elif len(slot)==4:
        return solve_xxxxcross(scramble, rotation, max_length, full_search, sol_index, name, move_restrict)
    
def solve_LL_substep(scramble, rotation, solve_cp, solve_co, solve_ep, solve_eo, max_length, full_search, sol_index, name, move_restrict):
    if not scramble:
        return False
    if not os.path.exists('RubiksSolver/table'):
        os.makedirs('RubiksSolver/table')
    alg=function.AlgRotation(function.StringToAlg(scramble), rotation)
    edge_move_table=create_table.create_edge_move_table()
    corner_move_table=create_table.create_corner_move_table()
    table1=create_table.create_multi_move_table2(5, 2, 12, 24*22*20*18*16, edge_move_table, 'RubiksSolver/table/5edges_move_table')
    prune_path_set=['RubiksSolver/table/edge016182022_corner12_prune_table', 'RubiksSolver/table/edge216182022_corner15_prune_table', 'RubiksSolver/table/edge416182022_corner18_prune_table', 'RubiksSolver/table/edge616182022_corner21_prune_table']
    edge_solved_set=[2989056, 2989088, 2989120, 2989152]
    corner_solved_set=[12, 15, 18, 21]
    single_cp_move_table=create_table.create_cp_move_table()
    single_ep_move_table=create_table.create_ep_move_table()
    co_table=create_table.create_co_move_table()
    eo_table=create_table.create_eo_move_table()
    cp_table=create_table.create_multi_move_table(4, 1, 8, 8*7*6*5, single_cp_move_table, 'RubiksSolver/table/cp_move_table')
    ep_table=create_table.create_multi_move_table(4, 1, 12, 12*11*10*9, single_ep_move_table, 'RubiksSolver/table/ep_move_table')
    cp_table=array.array('i', [18*i for i in cp_table])
    ep_table=array.array('i', [18*i for i in ep_table])
        
    index1=edge_solved_set[2]
    index2=corner_solved_set[2]
    prune_table1=create_table.create_prune_table2(index1, index2, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[2])
        
    index3=edge_solved_set[1]
    index4=corner_solved_set[1]
    prune_table2=create_table.create_prune_table2(index3, index4, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[1])
        
    index5=edge_solved_set[3]
    index6=corner_solved_set[3]
    prune_table3=create_table.create_prune_table2(index5, index6, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[3])
        
    index7=edge_solved_set[0]
    index8=corner_solved_set[0]
    prune_table4=create_table.create_prune_table2(index7, index8, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[0])
    table1=array.array('i', [24*i for i in table1])
    index1*=24
    index3*=24
    index5*=24
    index7*=24
    index_cp=0
    index_co=0
    index_ep=5860*18
    index_eo=0
    for move in alg:
        index1=table1[index1+move]
        index2=corner_move_table[index2*18+move]
        index3=table1[index3+move]
        index4=corner_move_table[index4*18+move]
        index5=table1[index5+move]
        index6=corner_move_table[index6*18+move]
        index7=table1[index7+move]
        index8=corner_move_table[index8*18+move]
        index_cp=cp_table[index_cp+move]
        index_co=co_table[index_co+move]
        index_ep=ep_table[index_ep+move]
        index_eo=eo_table[index_eo+move]
        
    move_restrict=array.array('i',[mv.move_names.index(i) for i in move_restrict])
    ma=create_table.create_ma_table()
    a=search.LL_substep_search(solve_cp, solve_co, solve_ep, solve_eo, table1, corner_move_table, cp_table, co_table, ep_table, eo_table, prune_table1, prune_table2, prune_table3, prune_table4, rotation, full_search, sol_index, move_restrict, ma)
    t=time.time()
    n=a.start_search(index1, index2, index3, index4, index5, index6, index7, index8, index_cp, index_co, index_ep, index_eo, max_length)
    t=time.time()-t
    if full_search:
        if n>0:
            print(f"search finished in {t:.6f}s")
            return False
        else:
            print("No solution found")
            return False
    else:
        if n:
            if n!=" ":
                if rotation!="":
                    print(f"{rotation} {n} // {name} No.{sol_index}")
                else:
                    print(f"{n} // {name} No.{sol_index}")
                n=function.AlgToString(alg)+n
                return n
            else:
                print(f"// {name}")
                return function.AlgToString(alg)
        else:
            print(f"// No solution for {name}")
            return function.AlgToString(alg)
        
def solve_LL(scramble, rotation, max_length, full_search, sol_index, name, move_restrict):
    if not scramble:
        return False
    if not os.path.exists('RubiksSolver/table'):
        os.makedirs('RubiksSolver/table')
    alg=function.AlgRotation(function.StringToAlg(scramble), rotation)
    edge_move_table=create_table.create_edge_move_table()
    corner_move_table=create_table.create_corner_move_table()
    table1=create_table.create_multi_move_table2(5, 2, 12, 24*22*20*18*16, edge_move_table, 'RubiksSolver/table/5edges_move_table')
    prune_path_set=['RubiksSolver/table/edge016182022_corner12_prune_table', 'RubiksSolver/table/edge216182022_corner15_prune_table', 'RubiksSolver/table/edge416182022_corner18_prune_table', 'RubiksSolver/table/edge616182022_corner21_prune_table']
    edge_solved_set=[2989056, 2989088, 2989120, 2989152]
    corner_solved_set=[12, 15, 18, 21]
    single_cp_move_table=create_table.create_cp_move_table()
    single_ep_move_table=create_table.create_ep_move_table()
    co_table=create_table.create_co_move_table()
    eo_table=create_table.create_eo_move_table()
    cp_table=create_table.create_multi_move_table(4, 1, 8, 8*7*6*5, single_cp_move_table, 'RubiksSolver/table/cp_move_table')
    ep_table=create_table.create_multi_move_table(4, 1, 12, 12*11*10*9, single_ep_move_table, 'RubiksSolver/table/ep_move_table')
    cp_table=array.array('i', [18*i for i in cp_table])
    ep_table=array.array('i', [18*i for i in ep_table])
    
    index1=edge_solved_set[2]
    index2=corner_solved_set[2]
    prune_table1=create_table.create_prune_table2(index1, index2, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[2])
        
    index3=edge_solved_set[1]
    index4=corner_solved_set[1]
    prune_table2=create_table.create_prune_table2(index3, index4, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[1])
        
    index5=edge_solved_set[3]
    index6=corner_solved_set[3]
    prune_table3=create_table.create_prune_table2(index5, index6, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[3])
        
    index7=edge_solved_set[0]
    index8=corner_solved_set[0]
    prune_table4=create_table.create_prune_table2(index7, index8, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[0])
    table1=array.array('i', [24*i for i in table1])
    
    index1*=24
    index3*=24
    index5*=24
    index7*=24
    index_cp=0
    index_co=0
    index_ep=5860*18
    index_eo=0
    for move in alg:
        index1=table1[index1+move]
        index2=corner_move_table[index2*18+move]
        index3=table1[index3+move]
        index4=corner_move_table[index4*18+move]
        index5=table1[index5+move]
        index6=corner_move_table[index6*18+move]
        index7=table1[index7+move]
        index8=corner_move_table[index8*18+move]
        index_cp=cp_table[index_cp+move]
        index_co=co_table[index_co+move]
        index_ep=ep_table[index_ep+move]
        index_eo=eo_table[index_eo+move]
        
    move_restrict=array.array('i',[mv.move_names.index(i) for i in move_restrict])
    ma=create_table.create_ma_table()
    a=search.LL_search(table1, corner_move_table, cp_table, co_table, ep_table, eo_table, prune_table1, prune_table2, prune_table3, prune_table4, rotation, full_search, sol_index, move_restrict, ma)
    t=time.time()
    n=a.start_search(index1, index2, index3, index4, index5, index6, index7, index8, index_cp, index_co, index_ep, index_eo, max_length)
    t=time.time()-t
    if full_search:
        if n>0:
            print(f"search finished in {t:.6f}s")
            return False
        else:
            print("No solution found")
            return False
    else:
        if n:
            if n!=" ":
                if rotation!="":
                    print(f"{rotation} {n} // {name} No.{sol_index}")
                else:
                    print(f"{n} // {name} No.{sol_index}")
                n=function.AlgToString(alg)+n
                return n
            else:
                print(f"// {name}")
                return function.AlgToString(alg)
        else:
            print(f"// No solution for {name}")
            return function.AlgToString(alg)
        
def solve_LL_AUF(scramble, rotation, max_length, full_search, sol_index, name, move_restrict):
    if not scramble:
        return False
    if not os.path.exists('RubiksSolver/table'):
        os.makedirs('RubiksSolver/table')
    alg=function.AlgRotation(function.StringToAlg(scramble), rotation)
    edge_move_table=create_table.create_edge_move_table()
    corner_move_table=create_table.create_corner_move_table()
    table1=create_table.create_multi_move_table2(5, 2, 12, 24*22*20*18*16, edge_move_table, 'RubiksSolver/table/5edges_move_table')
    prune_path_set=['RubiksSolver/table/edge016182022_corner12_prune_table', 'RubiksSolver/table/edge216182022_corner15_prune_table', 'RubiksSolver/table/edge416182022_corner18_prune_table', 'RubiksSolver/table/edge616182022_corner21_prune_table']
    edge_solved_set=[2989056, 2989088, 2989120, 2989152]
    corner_solved_set=[12, 15, 18, 21]
    single_cp_move_table=create_table.create_cp_move_table()
    single_ep_move_table=create_table.create_ep_move_table()
    co_table=create_table.create_co_move_table()
    eo_table=create_table.create_eo_move_table()
    cp_table=create_table.create_multi_move_table(4, 1, 8, 8*7*6*5, single_cp_move_table, 'RubiksSolver/table/cp_move_table')
    ep_table=create_table.create_multi_move_table(4, 1, 12, 12*11*10*9, single_ep_move_table, 'RubiksSolver/table/ep_move_table')
    cp_table=array.array('i', [18*i for i in cp_table])
    ep_table=array.array('i', [18*i for i in ep_table])
    
    index1=edge_solved_set[2]
    index2=corner_solved_set[2]
    prune_table1=create_table.create_prune_table2(index1, index2, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[2])
        
    index3=edge_solved_set[1]
    index4=corner_solved_set[1]
    prune_table2=create_table.create_prune_table2(index3, index4, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[1])
        
    index5=edge_solved_set[3]
    index6=corner_solved_set[3]
    prune_table3=create_table.create_prune_table2(index5, index6, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[3])
        
    index7=edge_solved_set[0]
    index8=corner_solved_set[0]
    prune_table4=create_table.create_prune_table2(index7, index8, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[0])
    table1=array.array('i', [24*i for i in table1])
    index1*=24
    index3*=24
    index5*=24
    index7*=24
    index_cp=0
    index_co=0
    index_ep=5860*18
    index_eo=0
    for move in alg:
        index1=table1[index1+move]
        index2=corner_move_table[index2*18+move]
        index3=table1[index3+move]
        index4=corner_move_table[index4*18+move]
        index5=table1[index5+move]
        index6=corner_move_table[index6*18+move]
        index7=table1[index7+move]
        index8=corner_move_table[index8*18+move]
        index_cp=cp_table[index_cp+move]
        index_co=co_table[index_co+move]
        index_ep=ep_table[index_ep+move]
        index_eo=eo_table[index_eo+move]
        
    move_restrict=array.array('i',[mv.move_names.index(i) for i in move_restrict])
    ma=create_table.create_ma_table()
    a=search.LL_AUF_search(table1, corner_move_table, cp_table, co_table, ep_table, eo_table, prune_table1, prune_table2, prune_table3, prune_table4, rotation, full_search, sol_index, move_restrict, ma)
    t=time.time()
    n=a.start_search(index1, index2, index3, index4, index5, index6, index7, index8, index_cp, index_co, index_ep, index_eo, max_length)
    t=time.time()-t
    if full_search:
        if n>0:
            print(f"search finished in {t:.6f}s")
            return False
        else:
            print("No solution found")
            return False
    else:
        if n:
            if n!=" ":
                if rotation!="":
                    print(f"{rotation} {n} // {name} No.{sol_index}")
                else:
                    print(f"{n} // {name} No.{sol_index}")
                n=function.AlgToString(alg)+n
                return n
            else:
                print(f"// {name}")
                return function.AlgToString(alg)
        else:
            print(f"// No solution for {name}")
            return function.AlgToString(alg)
