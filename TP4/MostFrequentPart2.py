import time

L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
#L1 = [1,2,1,22,1,5,4,5,1,2,6,4,1,4,1,1,1,1]
temp1=0
""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /"""
while True:
    for i in range(len(L1)):
        if i in L1:
            temp=L1.count(i)
            if temp1<temp:
                temp1=temp
                nbr=i
    print("Le nombre le plus frequent dans la liste est le : ",nbr,"(",temp1,"x)")
    break








""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
