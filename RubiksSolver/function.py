import RubiksSolver.move as move

def AlgToString(alg):
    String=""
    for i in alg:
        String+=move.move_names[i]+" "
    return String

def StringToAlg(String):
    alg=[]
    for name in String.split(" "):
        if name!="":
            alg.append(move.move_names.index(name))  
    return alg

def AlgConvertRotation(alg, rotation):
    if rotation=="":
        return alg
    face_list_0=[0, 1, 2, 3, 4, 5]
    if rotation=="x":
        face_list=[5, 4, 2, 3, 0, 1]
    elif rotation=="x2":
        face_list=[1, 0, 2, 3, 5, 4]
    elif rotation=="x'":
        face_list=[4, 5, 2, 3, 1, 0]
    elif rotation=="y":
        face_list=[0, 1, 5, 4, 2, 3]
    elif rotation=="y2":
        face_list=[0, 1, 3, 2, 5, 4]
    elif rotation=="y'":
        face_list=[0, 1, 4, 5, 3, 2]
    elif rotation=="z":
        face_list=[3, 2, 0, 1, 4, 5]
    elif rotation=="z2":
        face_list=[1, 0, 3, 2, 4, 5]
    elif rotation=="z'":
        face_list=[2, 3, 1, 0, 4, 5]
        
    for i in range(len(alg)):
        alg[i]=3*face_list[alg[i]//3]+alg[i]%3
    return alg

def AlgRotation(alg, rotation_algString):
    for rot in rotation_algString.split(" "):
        alg=AlgConvertRotation(alg, rot)
    return alg

def array_to_index(a, n, c, pn):
    p=[i//c for i in a]
    index=0
    base=1
    for i in range(n):
        tmp=0
        for j in range(i):
            if p[j]<p[i]:
                tmp+=1
        index+=(p[i]-tmp)*base
        base *= pn-i
    index*=c**n
    for i in range(n):
        index+=(a[i]%c)*c**(n-i-1)
    return index

def index_to_array(index, n, c, pn):
    p_index=index//(c**n)
    o_index=index%(c**n)
    p=[0 for i in range(n)]
    base=pn
    for i in range(n):
        p[i]=p_index%base
        p_index//=base
        for j in sorted(p[:i]):
            if j<=p[i]:
                p[i]+=1
        base-=1
    for i in range(n):
        p[n-i-1]=c*p[n-i-1]+o_index%c
        o_index//=c
    return p

def o_to_index(o, c, pn):
    o_index=0
    for i in range(pn-1):
        o_index+=o[i]*c**(pn-i-2)
    return o_index

def index_to_o(index, c, pn):
    o=[0 for i in range(pn-1)]
    count=0
    for i in range(pn-1):
        o[pn-i-2]=index%c
        count+=o[pn-i-2]
        index//=c
    o+=[(-count)%c]
    return o