import string
import random
voy=["a","e","i","o","u","y","A","E","I","O","U","Y"]
x=int(random.randint(0,99))
T=list(string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase)[:x]
random.shuffle(T)
T.append(0)
print(T)
s=int(1)
test = 0
VoyCont=0
wagon = 0
potemp = 0
po = 0
potest = 0
while test == 0:
    if T[s]!=0:
        s += 1
        if T[s] in voy:
            VoyCont+=1
        if T[s] == 'W' or T[s]== 'w':
            potemp = s
            potest += 1
            if T[s] =='A' or T[s]=='a':
                if T[s]=='G' or T[s]=='g':
                    if T[s]=='O' or T[s]=='o':
                        if T[s]=='N' or T[s]=='n':
                            wagon +=1
                            if potest == 1:
                                po = potemp
                        else:
                            potemp = 0
                            potest = 0
                    else:
                        potemp = 0
                        potest = 0
                else:
                    potemp = 0
                    potest = 0
            else:
                potemp = 0
                potest = 0
    else:
        test=1
        print(f"la taille de la liste est de {s} valeures")
        break
moyen = (VoyCont/s)*100
print(f"les voyelles occupent {moyen:.3f}% de la liste")
if wagon != 0:
    print(f'Le mot "wagon" apparet {wagon}x dans la liste, la première fois étant à la {po}e place')
else:
    print("le mot wagon n'apparet pas dans cette liste")
