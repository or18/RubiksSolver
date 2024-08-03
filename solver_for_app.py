import sys
import io
import RubiksSolver.solver as sv

def main(operation, scramble, rot, op1, op2, op3, op4, length, r):
    if operation=='F2L_solver':
        scramble1=sv.solve_F2L(scramble, rot, op1, op2, op3, op4, length, True, 1, "", r)
    elif operation=='LL_substep_solver':
        scramble1=sv.solve_LL_substep(scramble, rot, op1, op2, op3, op4, length, True, 1, "", r)
    elif operation=='LL_solver':
        scramble1=sv.solve_LL(scramble, rot, length, True, 1, "", r)
    elif operation=='LL_AUF_solver':
        scramble1=sv.solve_LL_AUF(scramble, rot, length, True, 1, "", r)
    
if __name__=="__main__":
    operation=sys.argv[1]
    scramble=sys.argv[2]
    rot=sys.argv[3] if sys.argv[3]!="N" else ""
    op1=True if sys.argv[4]=="True" else False
    op2=True if sys.argv[5]=="True" else False
    op3=True if sys.argv[6]=="True" else False
    op4=True if sys.argv[7]=="True" else False
    length=int(sys.argv[8])
    r=[]
    for m in sys.argv[9]:
        r.append(m)
        r.append(m+"2")
        r.append(m+"'")
    main(operation, scramble, rot, op1, op2, op3, op4, length, r)
