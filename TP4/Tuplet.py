while True:
    T=('Login1','Login2')
    print(f"L’étudiant {T[0]} est en binome avec l’étudiant {T[1]}")
    test=input("pour ajouter un étudient au groupe tappez 'oui' : ")



""" Test Modif 1 élément 1    
    test=input("voulz vous changer? ")
    if test == 'oui':
        Login1 = input("avec qui voulez vous changer le 1er étudient? ")
        Login2 = input("avec qui voulez vous changer le 2e étudient? ")
        T[0]=Login1
        T[1]=Login2
        'tuple' object does not support item assignment"""

""" Test suppr 1 élément fonction del
    del (T[1])
    print(T)"""


""" test ajout tuplet
    if test == "oui" :
        test.__add__(input("tappez son nom: "))
        print(T)
        print(f"l'étudient {T[2]} est le nouveau membre du groupe! ")"""

"""J'en déduit qu'un tuplet et non modifiable, une fois créé il restera tjrs comme ça"""