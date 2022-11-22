from random import *
while True:
    x=int(randint(0,100))
    if x>50:
        print("PILE!")
        suit=input("on continue?  ")
        if suit == "non":
            print("ciao")
            break
    else:
        print("FACE!")
        suit = input("on continue?  ")
        if suit == "non":
            print("ciao")
            break