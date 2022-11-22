while True:
    Y10=0
    Y1015=0
    Y15=0
    for i in range(1, 11):
        x = float(input(f"{i}e valeur: "))
        if x < 0 or x > 20:
            while x < 0 or x > 20:
                print("valleure fausse")
                x = float(input(f"{i}e valeur: "))
            if x < 10:
                Y10 = Y10 + 1
            elif x >= 15:
                Y15 = Y15 + 1
            else:
                Y1015 = Y1015 + 1
        else:
            if x < 10:
                Y10 = Y10 + 1
            elif x >= 15:
                Y15 = Y15 + 1
            else:
                Y1015 = Y1015 + 1
    print("il y a",Y10,"valleure strictement inferieures à 10",Y1015,"valleure comprisent entre 10 et 15", Y15, "valleure strictement superieure à 15")