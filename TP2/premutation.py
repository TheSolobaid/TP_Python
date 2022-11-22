import time

print("quel est votre X?")
Var1=input()
print("quel est votre Y?")
Var2=input()
print("permutation en cour")
print("...")
time.sleep(0.5)
VarTemp=Var1
Var1=Var2
Var2=VarTemp
print("...")
time.sleep(0.5)
print("...")
time.sleep(0.5)
print("avant permutation")
print("X=",Var2)
print("Y=",Var1)
print("après permutation")
print("X=",Var1)
print("Y=",Var2)
