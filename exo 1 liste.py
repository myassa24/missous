TAILLE_LISTE = 10
notes = []

somme = 0

nbNsupm = 0

for i in range(TAILLE_LISTE):
    print("Entrez la note", (i+1),":",end="")
    note = float(input())
    notes.append(note)
    somme+=note

moyenne=somme/TAILLE_LISTE

for i in range(TAILLE_LISTE):
    if notes[i]> moyenne:
        nbNsupm += 1


print ("la moyenne de la classe est: ", moyenne)
print("le nombre de notes superieures à la moyenne est: ", nbNsupm)

