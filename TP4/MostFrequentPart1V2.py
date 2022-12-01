from copy import *
chiff=[]
appa=[]
L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 6, 7]
max = []
while True:
    cnt=0
    L2=copy(L1)
    L2.sort()
    L2.reverse()
    grn=L2[0]
    for i in range(len(L1)):
        test = 1
        for j in range(len(L1)):
            if j!=i:
                if L1[i] == L1[j]:
                    test=test+1
        if L1[i] not in chiff:
            chiff.append(L1[i])
            appa.append(test)
    max = copy(appa)
    max.sort()
    max.reverse()
    print(f"Le nombre le plus frequent dans la liste est le : {chiff[appa.index(max[0])]} ({max[0]}x)")
    break