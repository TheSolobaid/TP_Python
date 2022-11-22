while True:
    fact = 1
    x=int(input("valeur a factorialiser"))
    n=input("quelle type de traitement? (‘while’ ou 'for')")
    i=0
    if n=="while" or n=="‘while’":
        while i!=x:
            fact=fact*(i+1)
            i=i+1
            print(fact)
        print("le factoriel de", x, "est",fact)
    elif n=="for" or n=="‘for’":
        for y in range(x):
            fact = fact * (y + 1)
            print(fact)
        print("le factoriel de", x, "est", fact)
    else:
        print("veuillez bien choisir votre traitement")