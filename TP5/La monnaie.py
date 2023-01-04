while True:
    somme = int(input("votre somme à décomposer "))
    b100 = (somme-somme%100)/100
    somme = somme - b100*100
    b50 = (somme-somme%50)/50
    somme = somme - b50*50
    b10 = (somme-somme%10)/10
    somme = somme - b10*10
    p2 = (somme-somme%2)/2
    somme = somme-p2*2
    p1 = somme
    print(f"{somme} euros, c’est donc {b100} billets de 100, {b50} de 50, {b10} de 10, {p2} pièces de 2 et {p1} pièce 1.")