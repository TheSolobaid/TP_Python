while True:
    x=float(input("Entrez un nombre décimal :  "))
    if x<0:
        if x < -10:
            print(x," n'appartient pas à I")
        elif x<-2 or x==-2:
            print(x," appartient à I")
        else:
            print(x,"n'appartient pas à I")
    elif x == 0:
        print(x, " n'appartient pas à I")
    elif x<1:
        print(x," appartient à I")
    elif x<3:
        if x<2 or x==2:
            print(x," n'appartient pas à I")
        else:
            print(x," appartient à I")
    else:
        print(x," n'appartient pas à I")