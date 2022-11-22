from random import *
while True:
    x=int(randint(0,90))
    if x<60:
        print("PILE!")
        suit=input("on continue?  ")
        if suit == "non":
            break
    else:
        print("FACE!")
        suit = input("on continue?  ")
        if suit == "non":
            break