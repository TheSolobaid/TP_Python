import os.path
from datetime import datetime, timedelta
def sec2rest(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    months, days = divmod(days, 30)
    return months, days, hours, minutes, seconds
def find_date(sec):
    epoch = datetime(1970, 1, 1)
    date = epoch + timedelta(seconds=sec)
    return date.strftime("%d-%m-%Y")

while True:
    Fich1 = str(input("nom du premier fichier à chercher: "))
    Fich2 = str(input("nom du deuxieme fichier à chercher: "))
    if os.path.isfile(Fich1) == True:
        print()
        print(f"la taille de {Fich1} est: {os.path.getsize(Fich1)} octet(s)")
        print(f"{Fich1} à été modifié pour la dernière fois le {find_date(os.path.getmtime(Fich1))}")
        print()
    elif os.path.isfile(Fich1) == False:
        print(f"{Fich1} n'existe pas")
        print()
    if os.path.isfile(Fich2) == True:
        print(f"La taille de {Fich2} est: {os.path.getsize(Fich2)} octet(s)")
        print(f"{Fich2} à été modifié pour la dernière fois le {find_date(os.path.getmtime(Fich2))}")
        print()
    elif os.path.isfile(Fich2) == False:
        print(f"{Fich2} n'existe pas")
        print()