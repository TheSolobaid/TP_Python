while True:
    V1 = []
    V2 = []
    scal=float(0)
    NmbrMax=int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))
    if 1<=NmbrMax<=10:
        print("Saisie du premier vecteur : ")
        for i in range(NmbrMax):
            temp=int(input(f"V1[{i+1}]"))
            V1.append(temp)
        print("Saisie du second vecteur : ")
        for i in range(NmbrMax):
            temp=int(input(f"V2[{i+1}]"))
            V2.append(temp)
        for i in range(NmbrMax):
            scal=scal+(V1[i]*V2[i])
        print("Le produit scalaire de v1 par v2 vaut 3 ",scal)