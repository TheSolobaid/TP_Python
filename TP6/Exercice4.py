import random

# Fonction generer(nbr, vmin, vmax) pour générer un tableau de 'nbr'
# valeurs comprises entre 'vmin' et 'vmax'

def generer(nbr, vmin, vmax):
    lst = []
    for i in range(nbr):
        lst.append(random.randint(vmin, vmax))
    return lst

# Fonction combienInferieur(table, vseuil) pour compter le nombre de
# valeurs d'un tableau 'table' inférieures à la valeur 'vseuil'

def combienInferieur(table, vseuil):
    test = True
    step = 0
    while test:
        if table[step]<vseuil:
            step += 1
        else:
            test = False
    return step



nb = int(input('longeure de la liste a générer: '))
vmin = int(input('valeur min: '))
vmax = int(input('valeur max: '))
tab = generer(nb, vmin, vmax)
tab.sort()
print(tab)
choice = input('voulez vous choisir une valeure à un nombre (o pour OUI / n pour NON) (si non, la valeure sera 30): ')
if choice == 'o':
    val = int(input('quel est cette valeure ? '))
    total = combienInferieur(tab, val)
else:
    val = 30
    total = combienInferieur(tab, 30)
print(f"Il y en a {total} inférieurs à {val}")