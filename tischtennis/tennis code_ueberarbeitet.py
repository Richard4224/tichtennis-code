import random


# Turnierergebnisse absteigend speichern
def speichern(file, wörterbuch):
    with open(file, "w", encoding="utf-8") as f:
        for name, points in sorted(wörterbuch.items(), key=lambda s: s[1], reverse=True):
            f.write(f"{name}, {points}\n")


eingabedaten = 2 # Eingabebestätigung (1 = korrekt)

# Spieleranzahl und Namen eingeben, bei Bestätigung Schleife beenden
while eingabedaten != 1:
    spieler_anzahl = None
    print("Bitte geben sie die Spielerzahl an:")
    while type(spieler_anzahl) != int:
        try:
            spieler_anzahl = int(input())
        except ValueError:
            print("Bitte eine ganze Zahl eingeben.")

    print("Perfekt!")
    print("\n-------------------\n")

    spieler_liste = []

    for i in range(spieler_anzahl):
        print("Bitte geben sie nacheinander die Namen aller Spieler einzeln ein:")
        spieler_liste.append(input())

    print("\n-------------------\n")

    print(f"Erledigt!\nInsgesamt {len(spieler_liste)} Spieler\nNamen aller Spieler:")

    for x in spieler_liste:
        print("-" + x)

    print("\n-------------------\n")
    print("Bitte prüfen Sie, ob alle Namen korrekt eingegeben wurden:")
    print("- 1 - Ja, alles ist korrekt")
    print("- 2 - Nein, ich muss die Daten erneut eingeben")

    while True:
        try:
            eingabedaten = int(input("Eingabe:"))
            if eingabedaten == 1 or eingabedaten == 2:
                break
            print("Bitte nur 1 oder 2 eingeben!")
        except ValueError:
            print("Bitte nur 1 oder 2 eingeben!")

print("\n-------------------\n")
print("Perfekt! Die Spielerliste wurde bestätigt.")


paare = [] # Alle Spielerpaare erstellen
for i in range(len(spieler_liste)):
    for j in range(i+1, len(spieler_liste)):
        paare.append([spieler_liste[i], spieler_liste[j]])

random.shuffle(paare) # Spielreihenfolge zufällig mischen

# Spielplan ausgeben
print ("\nDer Spielplan und die teilnehmenden Paare:\n")
for i in range(len(paare)):
    print (f"Spiel {i+1}:")
    print (paare[i][0], "und", paare[i][1], "\n")

print("\n-------------------\n")

print("Das Turnier beginnt!")

print("\n-------------------\n")

results = {name: 0 for name in spieler_liste} # Punktestand initialisieren (alle = 0)


# Spiele durchführen, Sieger bekommt 3 Punkte
for i in range(len(paare)):
    print(f"Spiel {i+1}:")
    print("Es spielen:")
    print(f"    1 - {paare[i][0]}")
    print(f"    2 - {paare[i][1]}")
    auswahl = 0
    while True:
        try:
            auswahl = int(input("Bitte die Nummer des Gewinners eingeben:"))
            if auswahl == 1 or auswahl == 2:
                break
            print("Bitte nur 1 oder 2 eingeben!")
        except ValueError:
            print("Bitte nur 1 oder 2 eingeben!")
    results[paare[i][auswahl-1]] += 3
    print("\n-------------------\n")

print("Das Turnier ist beendet!\n")
print("Turnierergebnisse:\n")

# Ergebnisse absteigend ausgeben
nummer = 0 # Platznummer
last_result = 0 # Vergleich, gleiche Punktzahl = gleicher Platz
for key, value in sorted(results.items(), key = lambda s: s[1], reverse = True):
    if value != last_result:
        nummer += 1
    print (f"Platz {nummer}:")
    print (f"{key}: {value} Punkte")

    last_result = value

print("\n-------------------\n")

# Ergebnisse in Datei speichern, schreiben ohne .txt
print("Wollen sie die Turnierergebnisse speichern?")
print(f"    1 - Ja")
print(f"    2 - Nein")
while True:
        try:
            auswahl = int(input("Antwort:"))
            if auswahl == 1 or auswahl == 2:
                break
            print("Bitte nur 1 oder 2 eingeben!")
        except ValueError:
            print("Bitte nur 1 oder 2 eingeben!")
if auswahl == 1:
    filename = str(input("Gib dem Turnier einen Namen: ")+".txt")
    speichern(filename, results)
    print (f"Turnierergebnisse wurde gespeichert als {filename}")