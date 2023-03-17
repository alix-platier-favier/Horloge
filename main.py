import time

print("Bonjour !")
heures = 11
minutes = 29
secondes = 57

def afficher_heure(heures, minutes, secondes):
    print("\033c", end="")
    print(f"Heure actuelle: {heures:02d}:{minutes:02d}:{secondes:02d}")
    secondes += 1
    if secondes == 60:
            secondes = 0
            minutes += 1
            if minutes == 60:
                minutes = 0
                heures += 1
                if heures == 24:
                    heures = 0
    time.sleep(1)
    
def afficher_alarme():
    global heures, minutes, secondes
    alarme_heures, alarme_minutes, alarme_secondes = input("Heures de l'alarme (hh:mm:ss) : ").split(":")
    alarme_heures, alarme_minutes, alarme_secondes = int(alarme_heures), int(alarme_minutes), int(alarme_secondes)

    while True:
        secondes += 1
        if secondes >= 60:
            secondes = 0
            minutes += 1
            if minutes >= 60:
                minutes = 0
                heures += 1
                if heures >= 24:
                    heures = 0
        if heures == alarme_heures and minutes == alarme_minutes and secondes == alarme_secondes:
            print("Ring, ring! C'est l'heure! ")
            break

        afficher_heure(heures, minutes, secondes)
        time.sleep(1)

while True:
    print("Que voulez-vous faire ?")
    print("1 - Afficher l'heure")
    print("2 - Ajouter une alarme")
    print("3 - Quitter")
    choice = input("> ")
    if choice == "1":
        print("\033c", end="")
        print(f"Heure actuelle: {heures:02d}:{minutes:02d}:{secondes:02d}")
    elif choice == "2":
        afficher_alarme()
    elif choice == "3":
        break
    else:
        print("Choix invalide.")