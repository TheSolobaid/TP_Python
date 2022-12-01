import time
from copy import *
L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 6, 7]
#L1 = [1,2,1,22,1,5,4,5,1,2,6,4,1,4,1,1,1,1]
temp1=0
""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /"""
while True:
    L1B=copy(L1)
    L1B.sort()
    L1B.reverse()
    gn=L1B[0]
    print(gn)
    for i in range(len(L1)):
        for j in range(gn+1):
            if j in L1:
                temp=L1.count(j)
                if temp1<temp:
                    temp1=temp
                    nbr=j
    print("Le nombre le plus frequent dans la liste est le : ",nbr,"(",temp1,"x)")
    break


""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
