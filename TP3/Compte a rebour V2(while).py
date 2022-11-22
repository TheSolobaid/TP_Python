import time
while True:
    i=0
    x=int(input("Nombre positif"))
    if x>= 0:
        while i<=x:
            print(x-i)
            i=i+1
            time.sleep(0.5)
        break
    else:
        x = int(input("Nombre POSITIF"))