while True:
    nbr=int(input("Entrez un nombre entier:"))
    if nbr%2==0:
        if nbr>0:
            print(nbr,"est pair et positif")
        elif nbr==0:
            print(nbr, "est egale a zero!")
        else:
            print(nbr, "est pair et negatif")
    else:
        if nbr > 0:
            print(nbr, "est impair et positif")
        elif nbr == 0:
            print(nbr, "est egale a zero!")
        else:
            print(nbr, "est impair et negatif")
