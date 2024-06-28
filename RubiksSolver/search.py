import RubiksSolver.function as function

class cross_search:
    def __init__(self, table1, prune_table, rotation, full_search, sol_index, move_restrict, ma):
        self.sol=[]
        self.count=0
        self.table1=table1
        self.prune_table=prune_table
        self.rotation=rotation
        self.full_search=full_search
        self.sol_index=sol_index
        self.move_restrict=move_restrict
        self.ma=ma
        self.index1_tmp=0
        self.index2_tmp=0
        self.prune_tmp=0
        
    def depth_limited_search(self, index1, index2, depth, prev):
        for i in self.move_restrict:
            if self.ma[prev+i]:
                continue
            self.index1_tmp=self.table1[index1+i]
            self.index2_tmp=self.table1[index2+i]
            self.prune_tmp=self.prune_table[self.index1_tmp*528+self.index2_tmp]
            if self.prune_tmp>=depth:
                continue
            self.sol.append(i)
            if depth==1:
                if self.prune_tmp==0:
                    self.count+=1
                    if self.full_search:
                        if self.rotation!="":
                            print(f"{self.count}: {self.rotation} {function.AlgToString(self.sol)}")
                        else:
                            print(f"{self.count}: {function.AlgToString(self.sol)}")
                    else:
                        if self.count==self.sol_index:
                            return True
            elif self.depth_limited_search(self.index1_tmp*18, self.index2_tmp*18, depth-1, i*18):
                return True
            self.sol.pop()
        
    def start_search(self, index1, index2, max_length):
        self.prune_tmp=self.prune_table[index1*528+index2]
        if self.prune_tmp==0:
            if self.full_search:
                print("already solved")
                return 0
            else:
                return " "
        index1*=18
        index2*=18
        for depth in range(1, max_length+1):
            if self.depth_limited_search(index1, index2, depth, 324):
                return function.AlgToString(self.sol)
        if self.full_search:
            return self.count
        else:
            return False
    
class xcross_search:
    def __init__(self, table1, corner_move_table, prune_table1, rotation, full_search, sol_index, move_restrict, ma):
        self.sol=[]
        self.count=0
        self.table1=table1
        self.corner_move_table=corner_move_table
        self.prune_table1=prune_table1
        self.rotation=rotation
        self.full_search=full_search
        self.sol_index=sol_index
        self.move_restrict=move_restrict
        self.ma=ma
        self.index1_tmp=0
        self.index2_tmp=0
        self.prune_tmp=0
        
    def depth_limited_search(self, index1, index2, depth, prev):
        for i in self.move_restrict:
            if self.ma[prev+i]:
                continue
            self.index1_tmp=self.table1[index1+i]
            self.index2_tmp=self.corner_move_table[index2+i]
            self.prune_tmp=self.prune_table1[self.index1_tmp*24+self.index2_tmp]
            if self.prune_tmp>=depth:
                continue
            self.sol.append(i)
            if depth==1:
                if self.prune_tmp==0:
                    self.count+=1
                    if self.full_search:
                        if self.rotation!="":
                            print(f"{self.count}: {self.rotation} {function.AlgToString(self.sol)}")
                        else:
                            print(f"{self.count}: {function.AlgToString(self.sol)}")
                    else:
                        if self.count==self.sol_index:
                            return True
            elif self.depth_limited_search(self.index1_tmp*18, self.index2_tmp*18, depth-1, i*18):
                return True
            self.sol.pop()
        
    def start_search(self, index1, index2, max_length):
        self.prune_tmp=self.prune_table1[index1*24+index2]
        if self.prune_tmp==0:
            if self.full_search:
                print("already solved")
                return 0
            else:
                return " "
        index1*=18
        index2*=18
        for depth in range(1, max_length+1):
            if self.depth_limited_search(index1, index2, depth, 324):
                return function.AlgToString(self.sol)
        if self.full_search:
            return self.count
        else:
            return False
    
class xxcross_search:
    def __init__(self, table1, corner_move_table, prune_table1, prune_table2, rotation, full_search, sol_index, move_restrict, ma):
        self.sol=[]
        self.count=0
        self.table1=table1
        self.corner_move_table=corner_move_table
        self.prune_table1=prune_table1
        self.prune_table2=prune_table2
        self.rotation=rotation
        self.full_search=full_search
        self.sol_index=sol_index
        self.move_restrict=move_restrict
        self.ma=ma
        self.index1_tmp=0
        self.index2_tmp=0
        self.index3_tmp=0
        self.index4_tmp=0
        self.prune1_tmp=0
        self.prune2_tmp=0
        
    def depth_limited_search(self, index1, index2, index3, index4, depth, prev):
        for i in self.move_restrict:
            if self.ma[prev+i]:
                continue
            self.index1_tmp=self.table1[index1+i]
            self.index2_tmp=self.corner_move_table[index2+i]
            self.prune1_tmp=self.prune_table1[self.index1_tmp*24+self.index2_tmp]
            if self.prune1_tmp>=depth:
                continue
            self.index3_tmp=self.table1[index3+i]
            self.index4_tmp=self.corner_move_table[index4+i]
            self.prune2_tmp=self.prune_table2[self.index3_tmp*24+self.index4_tmp]
            if self.prune2_tmp>=depth:
                continue
            self.sol.append(i)
            if depth==1:
                if self.prune1_tmp==0 and self.prune2_tmp==0:
                    self.count+=1
                    if self.full_search:
                        if self.rotation!="":
                            print(f"{self.count}: {self.rotation} {function.AlgToString(self.sol)}")
                        else:
                            print(f"{self.count}: {function.AlgToString(self.sol)}")
                    else:
                        if self.count==self.sol_index:
                            return True
            elif self.depth_limited_search(self.index1_tmp*18, self.index2_tmp*18, self.index3_tmp*18, self.index4_tmp*18, depth-1, i*18):
                return True
            self.sol.pop()
        
    def start_search(self, index1, index2, index3, index4, max_length):
        self.prune1_tmp=self.prune_table1[index1*24+index2]
        self.prune2_tmp=self.prune_table2[index3*24+index4]
        if self.prune1_tmp==0 and self.prune2_tmp==0:
            if self.full_search:
                print("already solved")
                return 0
            else:
                return " "
        index1*=18
        index2*=18
        index3*=18
        index4*=18
        for depth in range(1, max_length+1):
            if self.depth_limited_search(index1, index2, index3, index4, depth, 324):
                return function.AlgToString(self.sol)
        if self.full_search:
            return self.count
        else:
            return False
    
class xxxcross_search:
    def __init__(self, table1, corner_move_table, prune_table1, prune_table2, prune_table3, rotation, full_search, sol_index, move_restrict, ma):
        self.sol=[]
        self.count=0
        self.table1=table1
        self.corner_move_table=corner_move_table
        self.prune_table1=prune_table1
        self.prune_table2=prune_table2
        self.prune_table3=prune_table3
        self.rotation=rotation
        self.full_search=full_search
        self.sol_index=sol_index
        self.move_restrict=move_restrict
        self.ma=ma
        self.index1_tmp=0
        self.index2_tmp=0
        self.index3_tmp=0
        self.index4_tmp=0
        self.index5_tmp=0
        self.index6_tmp=0
        self.prune1_tmp=0
        self.prune2_tmp=0
        self.prune3_tmp=0
        
    def depth_limited_search(self, index1, index2, index3, index4, index5, index6, depth, prev):
        for i in self.move_restrict:
            if self.ma[prev+i]:
                continue
            self.index1_tmp=self.table1[index1+i]
            self.index2_tmp=self.corner_move_table[index2+i]
            self.prune1_tmp=self.prune_table1[self.index1_tmp*24+self.index2_tmp]
            if self.prune1_tmp>=depth:
                continue
            self.index3_tmp=self.table1[index3+i]
            self.index4_tmp=self.corner_move_table[index4+i]
            self.prune2_tmp=self.prune_table2[self.index3_tmp*24+self.index4_tmp]
            if self.prune2_tmp>=depth:
                continue
            self.index5_tmp=self.table1[index5+i]
            self.index6_tmp=self.corner_move_table[index6+i]
            self.prune3_tmp=self.prune_table3[self.index5_tmp*24+self.index6_tmp]
            if self.prune3_tmp>=depth:
                continue
            self.sol.append(i)
            if depth==1:
                if self.prune1_tmp==0 and self.prune2_tmp==0 and self.prune3_tmp==0:
                    self.count+=1
                    if self.full_search:
                        if self.rotation!="":
                            print(f"{self.count}: {self.rotation} {function.AlgToString(self.sol)}")
                        else:
                            print(f"{self.count}: {function.AlgToString(self.sol)}")
                    else:
                        if self.count==self.sol_index:
                            return True
            elif self.depth_limited_search(self.index1_tmp*18, self.index2_tmp*18, self.index3_tmp*18, self.index4_tmp*18, self.index5_tmp*18, self.index6_tmp*18, depth-1, i*18):
                return True
            self.sol.pop()
        
    def start_search(self, index1, index2, index3, index4, index5, index6, max_length):
        self.prune1_tmp=self.prune_table1[index1*24+index2]
        self.prune2_tmp=self.prune_table2[index3*24+index4]
        self.prune3_tmp=self.prune_table3[index5*24+index6]
        if self.prune1_tmp==0 and self.prune2_tmp==0 and self.prune3_tmp==0:
            if self.full_search:
                print("already solved")
                return 0
            else:
                return " "
        index1*=18
        index2*=18
        index3*=18
        index4*=18
        index5*=18
        index6*=18
        for depth in range(1, max_length+1):
            if self.depth_limited_search(index1, index2, index3, index4, index5, index6, depth, 324):
                return function.AlgToString(self.sol)
        if self.full_search:
            return self.count
        else:
            return False
    
class xxxxcross_search:
    def __init__(self, table1, corner_move_table, prune_table1, prune_table2, prune_table3, prune_table4, rotation, full_search, sol_index, move_restrict, ma):
        self.sol=[]
        self.count=0
        self.table1=table1
        self.corner_move_table=corner_move_table
        self.prune_table1=prune_table1
        self.prune_table2=prune_table2
        self.prune_table3=prune_table3
        self.prune_table4=prune_table4
        self.rotation=rotation
        self.full_search=full_search
        self.sol_index=sol_index
        self.move_restrict=move_restrict
        self.ma=ma
        self.index1_tmp=0
        self.index2_tmp=0
        self.index3_tmp=0
        self.index4_tmp=0
        self.index5_tmp=0
        self.index6_tmp=0
        self.index7_tmp=0
        self.index8_tmp=0
        self.prune1_tmp=0
        self.prune2_tmp=0
        self.prune3_tmp=0
        self.prune4_tmp=0
        
    def depth_limited_search(self, index1, index2, index3, index4, index5, index6, index7, index8, depth, prev):
        for i in self.move_restrict:
            if self.ma[prev+i]:
                continue
            self.index1_tmp=self.table1[index1+i]
            self.index2_tmp=self.corner_move_table[index2+i]
            self.prune1_tmp=self.prune_table1[self.index1_tmp*24+self.index2_tmp]
            if self.prune1_tmp>=depth:
                continue
            self.index3_tmp=self.table1[index3+i]
            self.index4_tmp=self.corner_move_table[index4+i]
            self.prune2_tmp=self.prune_table2[self.index3_tmp*24+self.index4_tmp]
            if self.prune2_tmp>=depth:
                continue
            self.index5_tmp=self.table1[index5+i]
            self.index6_tmp=self.corner_move_table[index6+i]
            self.prune3_tmp=self.prune_table3[self.index5_tmp*24+self.index6_tmp]
            if self.prune3_tmp>=depth:
                continue
            self.index7_tmp=self.table1[index7+i]
            self.index8_tmp=self.corner_move_table[index8+i]
            self.prune4_tmp=self.prune_table4[self.index7_tmp*24+self.index8_tmp]
            if self.prune4_tmp>=depth:
                continue
            self.sol.append(i)
            if depth==1:
                if self.prune1_tmp==0 and self.prune2_tmp==0 and self.prune3_tmp==0 and self.prune4_tmp==0:
                    self.count+=1
                    if self.full_search:
                        if self.rotation!="":
                            print(f"{self.count}: {self.rotation} {function.AlgToString(self.sol)}")
                        else:
                            print(f"{self.count}: {function.AlgToString(self.sol)}")
                    else:
                        if self.count==self.sol_index:
                            return True
            elif self.depth_limited_search(self.index1_tmp*18, self.index2_tmp*18, self.index3_tmp*18, self.index4_tmp*18, self.index5_tmp*18, self.index6_tmp*18, self.index7_tmp*18, self.index8_tmp*18, depth-1, i*18):
                return True
            self.sol.pop()
        
    def start_search(self, index1, index2, index3, index4, index5, index6, index7, index8, max_length):
        self.prune1_tmp=self.prune_table1[index1*24+index2]
        self.prune2_tmp=self.prune_table2[index3*24+index4]
        self.prune3_tmp=self.prune_table3[index5*24+index6]
        self.prune4_tmp=self.prune_table4[index7*24+index8]
        if self.prune1_tmp==0 and self.prune2_tmp==0 and self.prune3_tmp==0 and self.prune4_tmp==0:
            if self.full_search:
                print("already solved")
                return 0
            else:
                return " "
        index1*=18
        index2*=18
        index3*=18
        index4*=18
        index5*=18
        index6*=18
        index7*=18
        index8*=18
        for depth in range(1, max_length+1):
            if self.depth_limited_search(index1, index2, index3, index4, index5, index6, index7, index8, depth, 324):
                return function.AlgToString(self.sol)
        if self.full_search:
            return self.count
        else:
            return False
    
class LL_substep_search:
    def __init__(self, solve_cp, solve_co, solve_ep, solve_eo, table1, corner_move_table, cp_table, co_table, ep_table, eo_table, prune_table1, prune_table2, prune_table3, prune_table4, rotation, full_search, sol_index, move_restrict, ma):
        self.sol=[]
        self.count=0
        self.solve_cp=not solve_cp
        self.solve_co=not solve_co
        self.solve_ep=not solve_ep
        self.solve_eo=not solve_eo
        self.table1=table1
        self.corner_move_table=corner_move_table
        self.cp_table=cp_table
        self.co_table=co_table
        self.ep_table=ep_table
        self.eo_table=eo_table
        self.prune_table1=prune_table1
        self.prune_table2=prune_table2
        self.prune_table3=prune_table3
        self.prune_table4=prune_table4
        self.rotation=rotation
        self.full_search=full_search
        self.sol_index=sol_index
        self.move_restrict=move_restrict
        self.ma=ma
        self.index1_tmp=0
        self.index2_tmp=0
        self.index3_tmp=0
        self.index4_tmp=0
        self.index5_tmp=0
        self.index6_tmp=0
        self.index7_tmp=0
        self.index8_tmp=0
        self.index_cp_tmp=0
        self.index_co_tmp=0
        self.index_ep_tmp=0
        self.index_eo_tmp=0
        self.prune1_tmp=0
        self.prune2_tmp=0
        self.prune3_tmp=0
        self.prune4_tmp=0
        
    def depth_limited_search(self, index1, index2, index3, index4, index5, index6, index7, index8, index_cp, index_co, index_ep, index_eo, depth, prev):
        for i in self.move_restrict:
            if self.ma[prev+i]:
                continue
            self.index1_tmp=self.table1[index1+i]
            self.index2_tmp=self.corner_move_table[index2+i]
            self.prune1_tmp=self.prune_table1[self.index1_tmp*24+self.index2_tmp]
            if self.prune1_tmp>=depth:
                continue
            self.index3_tmp=self.table1[index3+i]
            self.index4_tmp=self.corner_move_table[index4+i]
            self.prune2_tmp=self.prune_table2[self.index3_tmp*24+self.index4_tmp]
            if self.prune2_tmp>=depth:
                continue
            self.index5_tmp=self.table1[index5+i]
            self.index6_tmp=self.corner_move_table[index6+i]
            self.prune3_tmp=self.prune_table3[self.index5_tmp*24+self.index6_tmp]
            if self.prune3_tmp>=depth:
                continue
            self.index7_tmp=self.table1[index7+i]
            self.index8_tmp=self.corner_move_table[index8+i]
            self.prune4_tmp=self.prune_table4[self.index7_tmp*24+self.index8_tmp]
            if self.prune4_tmp>=depth:
                continue
            self.index_cp_tmp=self.cp_table[index_cp+i]
            self.index_co_tmp=self.co_table[index_co+i]
            self.index_ep_tmp=self.ep_table[index_ep+i]
            self.index_eo_tmp=self.eo_table[index_eo+i]
            self.sol.append(i)
            if depth==1:
                if self.prune1_tmp==0 and self.prune2_tmp==0 and self.prune3_tmp==0 and self.prune4_tmp==0 and (self.solve_ep or (self.index_ep_tmp==5860 or self.index_ep_tmp==5863 or self.index_ep_tmp==5886 or self.index_ep_tmp==6005)) and (self.solve_cp or (self.index_cp_tmp==0 or self.index_cp_tmp==3 or self.index_cp_tmp==18 or self.index_cp_tmp==65)) and (self.solve_co or self.index_co_tmp==0) and (self.solve_eo or self.index_eo_tmp==0):
                    self.count+=1
                    if self.full_search:
                        if self.rotation!="":
                            print(f"{self.count}: {self.rotation} {function.AlgToString(self.sol)}")
                        else:
                            print(f"{self.count}: {function.AlgToString(self.sol)}")
                    else:
                        if self.count==self.sol_index:
                            return True
            elif self.depth_limited_search(self.index1_tmp*18, self.index2_tmp*18, self.index3_tmp*18, self.index4_tmp*18, self.index5_tmp*18, self.index6_tmp*18, self.index7_tmp*18, self.index8_tmp*18, self.index_cp_tmp*18, self.index_co_tmp*18, self.index_ep_tmp*18, self.index_eo_tmp*18, depth-1, i*18):
                return True
            self.sol.pop()
        
    def start_search(self, index1, index2, index3, index4, index5, index6, index7, index8, index_cp, index_co, index_ep, index_eo, max_length):
        self.prune1_tmp=self.prune_table1[index1*24+index2]
        self.prune2_tmp=self.prune_table2[index3*24+index4]
        self.prune3_tmp=self.prune_table3[index5*24+index6]
        self.prune4_tmp=self.prune_table4[index7*24+index8]
        if self.prune1_tmp==0 and self.prune2_tmp==0 and self.prune3_tmp==0 and self.prune4_tmp==0 and (self.solve_ep or (index_ep==5860 or index_ep==5863 or index_ep==5886 or index_ep==6005)) and (self.solve_cp or (index_cp==0 or index_cp==3 or index_cp==18 or index_cp==65)) and (self.solve_co or index_co==0) and (self.solve_eo or index_eo==0):
            if self.full_search:
                print("already solved")
                return 0
            else:
                return " "
        index1*=18
        index2*=18
        index3*=18
        index4*=18
        index5*=18
        index6*=18
        index7*=18
        index8*=18
        index_cp*=18
        index_co*=18
        index_ep*=18
        index_eo*=18
        for depth in range(1, max_length+1):
            if self.depth_limited_search(index1, index2, index3, index4, index5, index6, index7, index8, index_cp, index_co, index_ep, index_eo, depth, 324):
                return function.AlgToString(self.sol)
        if self.full_search:
            return self.count
        else:
            return False
    
class LL_search:
    def __init__(self, table1, corner_move_table, cp_table, co_table, ep_table, eo_table, prune_table1, prune_table2, prune_table3, prune_table4, rotation, full_search, sol_index, move_restrict, ma):
        self.sol=[]
        self.count=0
        self.table1=table1
        self.corner_move_table=corner_move_table
        self.cp_table=cp_table
        self.co_table=co_table
        self.ep_table=ep_table
        self.eo_table=eo_table
        self.prune_table1=prune_table1
        self.prune_table2=prune_table2
        self.prune_table3=prune_table3
        self.prune_table4=prune_table4
        self.rotation=rotation
        self.full_search=full_search
        self.sol_index=sol_index
        self.move_restrict=move_restrict
        self.ma=ma
        self.index1_tmp=0
        self.index2_tmp=0
        self.index3_tmp=0
        self.index4_tmp=0
        self.index5_tmp=0
        self.index6_tmp=0
        self.index7_tmp=0
        self.index8_tmp=0
        self.index_cp_tmp=0
        self.index_co_tmp=0
        self.index_ep_tmp=0
        self.index_eo_tmp=0
        self.prune1_tmp=0
        self.prune2_tmp=0
        self.prune3_tmp=0
        self.prune4_tmp=0
    
    def depth_limited_search(self, index1, index2, index3, index4, index5, index6, index7, index8, index_cp, index_co, index_ep, index_eo, depth, prev):
        for i in self.move_restrict:
            if self.ma[prev+i]:
                continue
            self.index1_tmp=self.table1[index1+i]
            self.index2_tmp=self.corner_move_table[index2+i]
            self.prune1_tmp=self.prune_table1[self.index1_tmp*24+self.index2_tmp]
            if self.prune1_tmp>=depth:
                continue
            self.index3_tmp=self.table1[index3+i]
            self.index4_tmp=self.corner_move_table[index4+i]
            self.prune2_tmp=self.prune_table2[self.index3_tmp*24+self.index4_tmp]
            if self.prune2_tmp>=depth:
                continue
            self.index5_tmp=self.table1[index5+i]
            self.index6_tmp=self.corner_move_table[index6+i]
            self.prune3_tmp=self.prune_table3[self.index5_tmp*24+self.index6_tmp]
            if self.prune3_tmp>=depth:
                continue
            self.index7_tmp=self.table1[index7+i]
            self.index8_tmp=self.corner_move_table[index8+i]
            self.prune4_tmp=self.prune_table4[self.index7_tmp*24+self.index8_tmp]
            if self.prune4_tmp>=depth:
                continue
            self.index_cp_tmp=self.cp_table[index_cp+i]
            self.index_co_tmp=self.co_table[index_co+i]
            self.index_ep_tmp=self.ep_table[index_ep+i]
            self.index_eo_tmp=self.eo_table[index_eo+i]
            self.sol.append(i)
            if depth==1:
                if self.prune1_tmp==0 and self.prune2_tmp==0 and self.prune3_tmp==0 and self.prune4_tmp==0 and ((self.index_ep_tmp==5860 and self.index_cp_tmp==0) or (self.index_ep_tmp==5886 and self.index_cp_tmp==18) or (self.index_ep_tmp==6005 and self.index_cp_tmp==65) or (self.index_ep_tmp==5863 and self.index_cp_tmp==3)) and self.index_co_tmp==0 and self.index_eo_tmp==0:
                    self.count+=1
                    if self.full_search:
                        if self.rotation!="":
                            print(f"{self.count}: {self.rotation} {function.AlgToString(self.sol)}")
                        else:
                            print(f"{self.count}: {function.AlgToString(self.sol)}")
                    else:
                        if self.count==self.sol_index:
                            return True
            elif self.depth_limited_search(self.index1_tmp*18, self.index2_tmp*18, self.index3_tmp*18, self.index4_tmp*18, self.index5_tmp*18, self.index6_tmp*18, self.index7_tmp*18, self.index8_tmp*18, self.index_cp_tmp*18, self.index_co_tmp*18, self.index_ep_tmp*18, self.index_eo_tmp*18, depth-1, i*18):
                return True
            self.sol.pop()
        
    def start_search(self, index1, index2, index3, index4, index5, index6, index7, index8, index_cp, index_co, index_ep, index_eo, max_length):
        self.prune1_tmp=self.prune_table1[index1*24+index2]
        self.prune2_tmp=self.prune_table2[index3*24+index4]
        self.prune3_tmp=self.prune_table3[index5*24+index6]
        self.prune4_tmp=self.prune_table4[index7*24+index8]
        if self.prune1_tmp==0 and self.prune2_tmp==0 and self.prune3_tmp==0 and self.prune4_tmp==0 and ((index_ep==5860 and index_cp==0) or (index_ep==5886 and index_cp==18) or (index_ep==6005 and index_cp==65) or (index_ep==5863 and index_cp==3)) and index_co==0 and index_eo==0:
            if self.full_search:
                print("already solved")
                return 0
            else:
                return " "
        index1*=18
        index2*=18
        index3*=18
        index4*=18
        index5*=18
        index6*=18
        index7*=18
        index8*=18
        index_cp*=18
        index_co*=18
        index_ep*=18
        index_eo*=18
        for depth in range(1, max_length+1):
            if self.depth_limited_search(index1, index2, index3, index4, index5, index6, index7, index8, index_cp, index_co, index_ep, index_eo, depth, 324):
                return function.AlgToString(self.sol)
        if self.full_search:
            return self.count
        else:
            return False
    
class LL_AUF_search:
    def __init__(self, table1, corner_move_table, cp_table, co_table, ep_table, eo_table, prune_table1, prune_table2, prune_table3, prune_table4, rotation, full_search, sol_index, move_restrict, ma):
        self.sol=[]
        self.count=0
        self.table1=table1
        self.corner_move_table=corner_move_table
        self.cp_table=cp_table
        self.co_table=co_table
        self.ep_table=ep_table
        self.eo_table=eo_table
        self.prune_table1=prune_table1
        self.prune_table2=prune_table2
        self.prune_table3=prune_table3
        self.prune_table4=prune_table4
        self.rotation=rotation
        self.full_search=full_search
        self.sol_index=sol_index
        self.move_restrict=move_restrict
        self.ma=ma
        self.index1_tmp=0
        self.index2_tmp=0
        self.index3_tmp=0
        self.index4_tmp=0
        self.index5_tmp=0
        self.index6_tmp=0
        self.index7_tmp=0
        self.index8_tmp=0
        self.index_cp_tmp=0
        self.index_co_tmp=0
        self.index_ep_tmp=0
        self.index_eo_tmp=0
        self.prune1_tmp=0
        self.prune2_tmp=0
        self.prune3_tmp=0
        self.prune4_tmp=0
    
    def depth_limited_search(self, index1, index2, index3, index4, index5, index6, index7, index8, index_cp, index_co, index_ep, index_eo, depth, prev):
        for i in self.move_restrict:
            if self.ma[prev+i]:
                continue
            self.index1_tmp=self.table1[index1+i]
            self.index2_tmp=self.corner_move_table[index2+i]
            self.prune1_tmp=self.prune_table1[self.index1_tmp*24+self.index2_tmp]
            if self.prune1_tmp>=depth:
                continue
            self.index3_tmp=self.table1[index3+i]
            self.index4_tmp=self.corner_move_table[index4+i]
            self.prune2_tmp=self.prune_table2[self.index3_tmp*24+self.index4_tmp]
            if self.prune2_tmp>=depth:
                continue
            self.index5_tmp=self.table1[index5+i]
            self.index6_tmp=self.corner_move_table[index6+i]
            self.prune3_tmp=self.prune_table3[self.index5_tmp*24+self.index6_tmp]
            if self.prune3_tmp>=depth:
                continue
            self.index7_tmp=self.table1[index7+i]
            self.index8_tmp=self.corner_move_table[index8+i]
            self.prune4_tmp=self.prune_table4[self.index7_tmp*24+self.index8_tmp]
            if self.prune4_tmp>=depth:
                continue
            self.index_cp_tmp=self.cp_table[index_cp+i]
            self.index_co_tmp=self.co_table[index_co+i]
            self.index_ep_tmp=self.ep_table[index_ep+i]
            self.index_eo_tmp=self.eo_table[index_eo+i]
            self.sol.append(i)
            if depth==1:
                if self.prune1_tmp==0 and self.prune2_tmp==0 and self.prune3_tmp==0 and self.prune4_tmp==0 and (self.index_ep_tmp==5860 and self.index_cp_tmp==0) and self.index_co_tmp==0 and self.index_eo_tmp==0:
                    self.count+=1
                    if self.full_search:
                        if self.rotation!="":
                            print(f"{self.count}: {self.rotation} {function.AlgToString(self.sol)}")
                        else:
                            print(f"{self.count}: {function.AlgToString(self.sol)}")
                    else:
                        if self.count==self.sol_index:
                            return True
            elif self.depth_limited_search(self.index1_tmp*18, self.index2_tmp*18, self.index3_tmp*18, self.index4_tmp*18, self.index5_tmp*18, self.index6_tmp*18, self.index7_tmp*18, self.index8_tmp*18, self.index_cp_tmp*18, self.index_co_tmp*18, self.index_ep_tmp*18, self.index_eo_tmp*18, depth-1, i*18):
                return True
            self.sol.pop()
        
    def start_search(self, index1, index2, index3, index4, index5, index6, index7, index8, index_cp, index_co, index_ep, index_eo, max_length):
        self.prune1_tmp=self.prune_table1[index1*24+index2]
        self.prune2_tmp=self.prune_table2[index3*24+index4]
        self.prune3_tmp=self.prune_table3[index5*24+index6]
        self.prune4_tmp=self.prune_table4[index7*24+index8]
        if self.prune1_tmp==0 and self.prune2_tmp==0 and self.prune3_tmp==0 and self.prune4_tmp==0 and index_ep==5860 and index_cp==0 and index_co==0 and index_eo==0:
            if self.full_search:
                print("already solved")
                return 0
            else:
                return " "
        index1*=18
        index2*=18
        index3*=18
        index4*=18
        index5*=18
        index6*=18
        index7*=18
        index8*=18
        index_cp*=18
        index_co*=18
        index_ep*=18
        index_eo*=18
        for depth in range(1, max_length+1):
            if self.depth_limited_search(index1, index2, index3, index4, index5, index6, index7, index8, index_cp, index_co, index_ep, index_eo, depth, 324):
                return function.AlgToString(self.sol)
        if self.full_search:
            return self.count
        else:
            return False
