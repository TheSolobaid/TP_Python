while True:
    date = []
    temp=int(input("Jour voulu [format jj]"))
    if temp<1 or 31<temp:
        print("veuillez respecter le format")
    else:
        date.append(temp)
        temp = int(input("Mois voulu [format mm]"))
        if temp < 1 or 12 < temp:
            print("veuillez respecter le format")
        else:
            date.append(temp)
            temp = int(input("Année voulu [format aaaa]"))
            if temp < 0 or 3000 < temp:
                print("veuillez respecter le format")
            else:
                date.append(temp)
                if date[2]%4==0:
                    if date[1]==2:
                        if date[0]>29:
                            print("veuillez respecter le format")
                        else:
                            print("le", date[0], date[1], date[2], "est un jour qui existe")
                    elif date[1]==1 or date[1]==3 or date[1]==5 or date[1]==7 or date[1]==8 or date[1]==10 or date[1]==12:
                        if date[0]>31:
                            print("veuillez respecter le format")
                        else:
                            print("le",date[0],date[1],date[2],"est un jour qui existe")
                    else:
                        if date[0]>30:
                            print("veuillez respecter le format")
                        else:
                            print("le",date[0],date[1],date[2],"est un jour qui existe")
                else:
                    if date[1]==2:
                        if date[0]>28:
                            print("veuillez respecter le format")
                        else:
                            print("le",date[0],date[1],date[2],"est un jour qui existe")
                    elif date[1]==1 or date[1]==3 or date[1]==5 or date[1]==7 or date[1]==8 or date[1]==10 or date[1]==12:
                        if date[0]>31:
                            print("veuillez respecter le format")
                        else:
                            print("le",date[0],date[1],date[2],"est un jour qui existe")
                    else:
                        if date[0]>30:
                            print("veuillez respecter le format")
                        else:
                            print("le", date[0], date[1], "de l'année", date[2], "est un jour qui existe")