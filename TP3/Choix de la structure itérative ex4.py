while True:
    tmp=0
    total=0
    n=int(input("valeur superieure à 1:  "))
    if n<1:
        n = int(input("valeur SUPERIEURE à 1:  "))
    for i in range(n):
        tmp=tmp+i
        if tmp<=n:
            total=i
        else:
            print(n, "est composé de l'adition des ", total, "permiers entiers")
            break