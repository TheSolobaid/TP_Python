

def textcleaner(text):
    str.lower(text)
    

    alpha = ""
    for i in text:
        if i.isalpha() :
            alpha = alpha + i
    return alpha


def textreplace(text):
    text = text.replace("é", "e")
    text = text.replace("è", "e")
    text = text.replace("ë", "e")               #replace pour le "e"
    text = text.replace("ê", "e")               

    text = text.replace("à", "a")
    text = text.replace("â", "a")               #replace pour le "a"
    text = text.replace("ä", "a")

    text = text.replace("ç", "c")               #replace pour le "c"

    text = text.replace("ù", "u")
    text = text.replace("ü", "u")               #replace pour le "u"
    text = text.replace("û", "u")

    text = text.replace("ï", "i")               #replace pour le "i"

    text = text.replace("ö", "o")               #replace pour le "o"
    text = text.replace("ô", "o")

    text = text.replace("ÿ", "y")               #replace pour le "y"

    text = text.replace("ñ", "n")               #replace pour le "n"
    return text

while True:
    test = 0
    mot=str(input("entrez un mot ou une phrase: "))
    mot = str(textcleaner(mot))
    mot = str(textreplace(mot))
    mot = mot.replace("", " ")
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