import os
import RubiksSolver.function as function
import RubiksSolver.create_table as create_table
import RubiksSolver.move as mv
import array
if not os.path.exists('RubiksSolver/table'):
      os.makedirs('RubiksSolver/table')
edge_move_table=create_table.create_edge_move_table()
table1=create_table.create_multi_move_table(2, 2, 12, 24*22, edge_move_table, 'RubiksSolver/table/2edges_move_table')
prune_path1='RubiksSolver/table/edge1618_edge2022_prune_table'
index1=416
index2=520
create_table.create_prune_table(index1, index2, 24*22, 24*22, 8, table1, table1, prune_path1)
corner_move_table=create_table.create_corner_move_table()
table1=create_table.create_multi_move_table2(5, 2, 12, 24*22*20*18*16, edge_move_table, 'RubiksSolver/table/5edges_move_table')
prune_path_set=['RubiksSolver/table/edge016182022_corner12_prune_table', 'RubiksSolver/table/edge216182022_corner15_prune_table', 'RubiksSolver/table/edge416182022_corner18_prune_table', 'RubiksSolver/table/edge616182022_corner21_prune_table']
edge_solved_set=[2989056, 2989088, 2989120, 2989152]
corner_solved_set=[12, 15, 18, 21]
single_cp_move_table=create_table.create_cp_move_table()
single_ep_move_table=create_table.create_ep_move_table()
create_table.create_co_move_table()
create_table.create_eo_move_table()
create_table.create_multi_move_table(4, 1, 8, 8*7*6*5, single_cp_move_table, 'RubiksSolver/table/cp_move_table')
create_table.create_multi_move_table(4, 1, 12, 12*11*10*9, single_ep_move_table, 'RubiksSolver/table/ep_move_table')
index1=edge_solved_set[2]
index2=corner_solved_set[2]
create_table.create_prune_table2(index1, index2, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[2])
index3=edge_solved_set[1]
index4=corner_solved_set[1]
create_table.create_prune_table2(index3, index4, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[1])
index5=edge_solved_set[3]
index6=corner_solved_set[3]
create_table.create_prune_table2(index5, index6, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[3])
index7=edge_solved_set[0]
index8=corner_solved_set[0]
create_table.create_prune_table2(index7, index8, 24*22*20*18*16, 24, 12, table1, corner_move_table, prune_path_set[0])
