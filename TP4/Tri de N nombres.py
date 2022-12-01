from random import *
while True:
    Ln=[]
    x=int(input("Longeure de votre liste: "))
    for i in range(x):
#       temp1=int(input(f"votre {i+1}e valleure: "))
        temp1 = randint(0,20)
        Ln.append(temp1)
    print("votre liste: ", Ln)
    print(sorted(Ln))
    Ln.sort()
    print("2e manière : ", Ln)
    for i in range(x):
        for j in range(x):
            if Ln[i]<Ln[j]:
                temp2=Ln[j]
                Ln[j]=Ln[i]
                Ln[i]=temp2
        print(Ln)