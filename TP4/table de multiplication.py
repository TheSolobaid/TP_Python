
while True:
    result = []
    arg=float(input("Vous cherchez la table de multiplication de quel nombre ?"))
    for i in range(11):
        temp=i*arg
        temp=round(temp,3)
        result.append(temp)
    for i in range(11):
        print(arg,"*",i,"=",result[i])