while True:
    test=0
    Total1e=0
    Total2e=0
    nbrTemp=0
    #test
    while test==0:
        strt = int(input("Heure de début"))
        end = int(input("Heure de fin  (toute heure entamée est due!)"))
        if strt>end:
            print("Attention ! le début de la location est après la fin...")
        elif strt<0 or end<0 or strt>24 or end>24:
            print("Les heures doivent être comprises entre 0 et 24 !")
        elif strt==end:
            print("Attention ! l’heure de fin est identique à l’heure de début.")
        else:
            test=1
    nbr=(end-strt)
    # savoir le prix dans ca commence en 1e et fini en 1e matin
    if 0<=strt<=7 and 0<=end<=7:
        total=nbr
        print("Vous avez loué votre vélo pendant:")
        print(nbr," heure(s) au tarif horaire de 1.0 euro(s)")
        print("Le montant total à payer est de ",total," euro(s)")
        break
    # savoir le prix dans ca commence en 1e et fini en 1e soir
    elif 17<=strt<=24 and 17<=end<=24:
        total = nbr
        print("Vous avez loué votre vélo pendant:")
        print(nbr, " heure(s) au tarif horaire de 1.0 euro(s)")
        print("Le montant total à payer est de ", total, " euro(s)")
        break
    # savoir le prix dans ca commence en 2e et fini en 2e
    elif 7<strt<17 and 7<end<17:
        total=nbr*2
        print("Vous avez loué votre vélo pendant:")
        print(nbr, " heure(s) au tarif horaire de 2.0 euro(s)")
        print("Le montant total à payer est de ", total, " euro(s)")
        break
    else:
        # savoir le prix dans ca commence en 1e et fini en 1e (avec du 2e entre)
        if strt<=7 and end>=17:
            nbrTemp=0
            for i in range(strt, 7):
                Total1e=Total1e+1
                nbrTemp=nbrTemp+1
            strt = nbrTemp + strt
            nbrTemp=0
            for i in range(strt,17):
                Total2e=Total2e+1
                nbrTemp = nbrTemp + 1
            strt = nbrTemp + strt
            for i in range(strt,end):
                Total1e=Total1e+1
            total=Total1e+(Total2e*2)
            print("Vous avez loué votre vélo pendant:")
            print(Total1e, " heure(s) au tarif horaire de 1.0 euro(s)")
            print(Total2e, " heure(s) au tarif horaire de 2.0 euro(s)")
            print("Le montant total à payer est de ", total, " euro(s)")
            break
        #savoir le prix quand ca commance en 1e et fini en 2e
        elif strt<=7 and end<17:
            for i in range(strt, 7):
                Total1e = Total1e + 1
                nbrTemp = nbrTemp + 1
            strt = nbrTemp + strt
            nbrTemp = 0
            for i in range(strt, end ):
                Total2e = Total2e + 1
            total = Total1e + (Total2e * 2)
            print("Vous avez loué votre vélo pendant:")
            print(Total1e, " heure(s) au tarif horaire de 1.0 euro(s)")
            print(Total2e, " heure(s) au tarif horaire de 2.0 euro(s)")
            print("Le montant total à payer est de ", total, " euro(s)")
            break
        #savoir le prix quand ca commance en 2e et fini en 1e
        else:
            for i in range(strt, 17):
                Total2e = Total2e + 1
                nbrTemp = nbrTemp + 1
            strt = nbrTemp + strt
            nbrTemp = 0
            for i in range(strt, end):
                Total1e = Total1e + 1
            total = Total1e + (Total2e * 2)
            print("Vous avez loué votre vélo pendant:")
            print(Total1e, " heure(s) au tarif horaire de 1.0 euro(s)")
            print(Total2e, " heure(s) au tarif horaire de 2.0 euro(s)")
            print("Le montant total à payer est de ", total, " euro(s)")
            break