def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst


lst1 = [0,1,2]
lst2 = ajouter_elt(lst1 , len(lst1))

print(f"{lst1} est de type {type(lst1)} à pour id {id(lst1)}")
print(f"{lst2} est de type {type(lst2)} à pour id {id(lst2)}")