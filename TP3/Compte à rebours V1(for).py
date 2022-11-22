import time
while True:
    x=int(input("Nombre positif"))
    if x>= 0:
        for i in range(x+1):
            print(x-i)
            time.sleep(0.5)
        break
    else:
        x = int(input("Nombre POSITIF"))