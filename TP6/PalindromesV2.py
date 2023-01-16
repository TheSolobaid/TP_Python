while True:
    test=0
    mot=str(input("entrez un mot ou une phrase: "))
    mot = mot.replace(",", "")
    mot = mot.replace(";", "")
    mot = mot.replace("/", "")
    mot = mot.replace(" ", "")
    mot = mot.replace("'", "")
    mot = mot.replace("&", "")
    mot = mot.replace("~", "")
    mot = mot.replace("?", "")
    mot = mot.replace("!", "")
    mot = mot.replace('"', "")
    mot = mot.replace("-", "")
    mot = mot.replace("#", "")
    mot = mot.replace("|", "")
    mot = mot.replace("{", "")
    mot = mot.replace("}", "")
    mot = mot.replace("`", "")
    mot = mot.replace("@", "a")
    mot = mot.lower()
    mot = mot.replace("é", "e")
    mot = mot.replace("è", "e")
    mot = mot.replace("ë", "e")
    mot = mot.replace("ê", "e")
    mot = mot.replace("à", "a")
    mot = mot.replace("â", "a")
    mot = mot.replace("ä", "a")
    mot = mot.replace("ç", "c")
    mot = mot.replace("ù", "u")
    mot = mot.replace("ü", "u")
    mot = mot.replace("û", "u")
    mot = mot.replace("ï", "i")
    mot = mot.replace("ö", "o")
    mot = mot.replace("ÿ", "y")
    mot = mot.replace("ñ", "n")
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