def ajouter_elt(lst=[0,1,2], elt=3):
    lst.append(elt)
    return lst


print(f'le resultat de la commade "print(ajouter_elt())" est: {ajouter_elt()}')
print(f'le 2e resultat de la commade "print(ajouter_elt())" est: {ajouter_elt()}')