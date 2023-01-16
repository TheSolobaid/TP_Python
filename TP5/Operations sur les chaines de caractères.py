while True:
    P1=[]
    P2=[]
    P1.append(str.capitalize(input("Prénom de la première personne:  ")))
    P1.append(str.upper(input("Nom de la première personne:  ")))
    P2.append(str.capitalize(input("Prénom de la deuxième personne:  ")))
    P2.append(str.upper(input("Nom de la deuxième personne:  ")))
    if P1[1]>P2[1]:
        print(P1[0], P1[1])
        print(P2[0], P2[1])
    elif P1[1]<P2[1]:
        print(P2[0], P2[1])
        print(P1[0], P1[1])
    elif P1[1] == P2[1]:
        if P1[0] > P2[0]:
            print(P1[0], P1[1])
            print(P2[0], P2[1])
        elif P1[0] < P2[0]:
            print(P2[0], P2[1])
            print(P1[0], P1[1])
        else:
            print("ce sont les même nom/prenoms")