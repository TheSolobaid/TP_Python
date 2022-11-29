while True:
    nbrEtud=int(input("Donnez le nombre d'etudiants : "))
    moyenne=float(0.0)
    notes=[]
    ecartMoy=[]
    for i in range(nbrEtud):
        noteTemp = 0
        noteTemp=float(input(f"note du {i+1}e étudiant : "))
        notes.append(noteTemp)
    for i in range(nbrEtud):
        moyenne=moyenne+notes[i]
    moyenne=moyenne/nbrEtud
    for i in range(nbrEtud):
        moyTemp = 0
        moyTemp = notes[i] - moyenne
        moyTemp=round(moyTemp,2)
        ecartMoy.append(moyTemp)
    print("Moyenne de classe : ",moyenne)
    print("Numéro de l’Etudiant | note | ecart a la moyenne")
    for i in range(nbrEtud):
        print(i+1," | ",notes[i]," | ",ecartMoy[i])