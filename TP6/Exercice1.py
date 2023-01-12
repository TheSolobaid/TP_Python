L1 = [0]*3
print(L1)
print(f"le type de L1 est {type(L1)}")
print(f"l'id de L1 est {id(L1)}\n")
for i in range(len(L1)):
    print(f"le type de la {i+1}e valeur de la liste est {type(L1[i])}")
    print(f"le id de la {i+1}e valeur de la liste est {id(L1[i])}\n")

L1[1]+=1
print(L1)
print(f"le type de L1 est {type(L1)}")
print(f"l'id de L1 est {id(L1)}\n")

for i in range(len(L1)):
    print(f"le id de la {i+1}e valeur de la liste est {id(L1[i])}\n")