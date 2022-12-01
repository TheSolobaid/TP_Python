from copy import *
L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 6, 7]
appa=[]
chiff=[]
while True:
    for i in range(len(L1)):
        if L1[i] not in chiff:
            chiff.append(L1[i])
            appa.append(L1.count(i))
    max = copy(appa)
    max.sort()
    max.reverse()
    print(f"Le nombre le plus frequent dans la liste est le : {L1[appa.index(max[0])]} ({max[0]}x)")
    break