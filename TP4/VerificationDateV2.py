mois = [4,6,9,11]
while True:
    date = input("votre date")
    jj=int(date[0]+date[1])
    mm=int(date[2]+date[3])
    aaaa=int(date[4]+date[5]+date[6]+date[7])
    if 0>jj or jj>31:
        print("veuillez respecter le format jour [jj]")
    else:
        if 0 > mm or mm > 12:
            print("veuillez respecter le format mois [mm]")
        else:
            if aaaa%4==0:
                if mm == 2:
                    if jj>29:
                            print("cette date n'existe pas")
                    else:
                        print("Le", jj, mm, aaaa, "est un jour qui existe")
                elif mm in mois:
                    if jj > 3:
                        print("cette date n'existe pas")
                    else:
                        print("Le", jj, mm, aaaa, "est un jour qui existe")
                else:
                    print("Le", jj, mm, aaaa, "est un jour qui existe")
            else:
                if mm == 2:
                    if jj>28:
                            print("cette date n'existe pas")
                    else:
                        print("Le", jj, mm, aaaa, "est un jour qui existe")
                elif mm in mois:
                    if jj > 3:
                        print("cette date n'existe pas")
                    else:
                        print("Le", jj, mm, aaaa, "est un jour qui existe")
                else:
                    print("Le", jj, mm, aaaa, "est un jour qui existe")