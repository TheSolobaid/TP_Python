while True:
    temptable=[]
    note=[]
    coef=[]
    total=0
    count=0
    test=0
    for i in range(5):
        temp=str(input(f"votre {i+1}e note et son coef: "))
        temptable=temp.split(" ")
        if len(temptable) != 2:
            print("les valleure ou la syntaxe sont faussent!")
            break
        note.append(temptable[0])
        coef.append(temptable[1])
    for i in range(5):
        total=total+(int(note[i])*int(coef[i]))
        count=count+1
    total=total/count
    if total >= 10:
        for i in range(5):
            if int(note[i])<8:
                print("you're rejected")
                test=1
        if test==0:
            print("you're admitted!!!!!")
    else:
        print("you're rejected")