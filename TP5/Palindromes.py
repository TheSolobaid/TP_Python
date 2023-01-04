while True:
    test=0
    mot=str(input("entrez un mot ou une phrase: "))
    mot = mot.replace(",", "")
    mot = mot.replace(";", "")
    mot = mot.replace("/", "")
    mot = mot.replace(" ", "")
    mot = mot.replace("'", "")
    mot = mot.replace("?", "")
    mot = mot.replace("!", "")
    mot = mot.replace('"', "")
    mot = mot.replace("."," ")
    mot = mot.lower()
    mot = mot.replace("", " ")
    mot = mot.strip()
    m = (mot.split(" "))
    if len(m)%2 == 1:
        for i in range(len(m)):
            if m[i] == m[len(m)-i-1]:
                test=test+1
            else:
                print("ce mot/phrase n'est pas un palindrome")
                test=0
                break
        if test != 0:
            print("ce mot/phrase est un palindrome")
    else:
        for i in range(int(len(m)/2)):
            if m[i] == m[len(m)-i-1]:
                test=test+1
            else:
                print("ce mot/phrase n'est pas un palindrome")
                test=0
                break
        if test != 0:
            print("ce mot/phrase est un palindrome")