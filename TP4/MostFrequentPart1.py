L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
a = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /"""
while True:
    Total=0
    valtemp=0
    temp=copy(L1)
    temp.sort()
    temp.reverse()
    L1=a
    grandnombre=temp[0]
    print(L1)
    print(grandnombre)
    for i in range(len(L1)-1):
        j=i+1
        if L1[i]==L1[j]:
            valtemp=L1[i]
            Total=Total+1
    print("Le nombre le plus frequent dans la liste est le : ", valtemp, "(", Total, "x)")
    break








""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
