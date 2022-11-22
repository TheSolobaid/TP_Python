from random import *
i=0
x = randint(0, 100)
n = int(input("valeur entre 0 et 100:  "))
while True:
    while n!=x:
        if n<x:
            i = i + 1
            print("La valeur est plus grande")
            n=int(input("votre valeur"))
        elif n>x:
            print("La valeur est plus petite")
            n=int(input("votre valeur"))
            i=i+1
    print('BRAVOOOOOOOO ça ne vous a pris "que"',i, "tentative(s)")
    break