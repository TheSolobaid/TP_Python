L1 = [2, 7, 5, 6, 7, 1, 6, 25, 1, 7, 6]
a = [2, 7, 5, 6, 7, 1, 6, 25, 1, 7, 6]
""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /"""
while True:
    temp=L1
    temp.sort()
    temp.reverse()
    L1=a
    grandnombre=temp[0]
    print(L1)
    print(grandnombre)
    for i in range(len(L1)):
        for i in range(grandnombre+1):
            testTemp=L1.index(i)

    break







""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
