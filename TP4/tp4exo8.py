while True:
    dico={"firstname":"Samuel","name":"Rolli","promo":"2022","group":"RT111"}
    dico2={"firstname":"Toto","name":"Titi","promo":"2022","group":"RT113"}
    binome={1:dico,2:dico2}
    print(f'votre nom est {dico["name"]}, votre prénom est {dico["firstname"]}, vous faites parti de la promo {dico["promo"]} dans le groupe {dico["group"]}')
    print("Les clés du dictionnaire sont :")
    for i in dico.keys():
        print(f"- {i}")
    print("Les valeurs du dictionnaire sont :")
    for i in dico.values():
        print(f"- {i}")
    print("Les tuplets du dictionnaire sont :")
    for i in dico.items():
        print(f"- {i}")


    """PART 2"""

    print(f'Son nom est {dico2["name"]}, son prénom est {dico2["firstname"]}, il fait parti de la promo {dico2["promo"]} dans le groupe {dico2["group"]}')
    print("Les clés du dictionnaire sont :")
    for i in dico2.keys():
        print(f"- {i}")
    print("Les valeurs du dictionnaire sont :")
    for i in dico2.values():
        print(f"- {i}")
    print("Les tuplets du dictionnaire sont :")
    for i in dico2.items():
        print(f"- {i}")

    """Part 3"""

    print("Les étudiants formants le binôme sont:")
    for i in binome.values():
        print(f'- L`étudiant {i["firstname"]} {i["name"]} du groupe {i["group"]}')
    break


"""dico["firstname"]=input("votre prénom: ")
    dico["name"]=input("votre nom: ")
    dico["promo"]=input("votre promo: ")
    dico["group"]=input("votre groupe: ")"""
"""dico2["firstname"] = input("son prénom: ")
    dico2["name"] = input("son nom: ")
    dico2["promo"] = input("sa promo: ")
    dico2["group"] = input("son groupe: ")"""