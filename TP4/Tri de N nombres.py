from random import *
from copy import *
while True:
    Ln=[]
    x=int(input("Longeure de votre liste: "))
    for i in range(x):
#       temp1=int(input(f"votre {i+1}e valleure: "))
        temp1 = randint(0,20)
        Ln.append(temp1)
    Ln1=copy(Ln)
    print("votre liste: ", Ln)
    print("1e manière : ",sorted(Ln1))
    Ln1.sort()
    print("2e manière : ", Ln1)
    print("3e manière : ")
    for i in range(x):
        for j in range(x):
            if Ln[i]<Ln[j]:
                temp2=Ln[j]
                Ln[j]=Ln[i]
                Ln[i]=temp2
        print(Ln)