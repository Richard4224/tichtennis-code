import sys


def main():

    player_count = get_player_count()

    players = get_players(player_count)

    matches = print_matches(players)

    players, results = input_results(players, matches)

    print_results(players)

    save_result(results)


def get_player_count():  

    # Überprüfen ob ein Argument eingegeben wurde
    if len(sys.argv) > 2:
        # Überprüfe ob Argv ein integer ist
        try:
            player_count = int(sys.argv[1])
        except ValueError:
            print("Info: player_count argument must be an int")
            sys.exit(1)
        # Überprüfe ob Argument ein positiver Integer ist
        if player_count < 1:
            print("Info: player_count must be a positive integer")
            sys.exit(1)
    else:

        while True:
            try:
                player_count = int(input("How many players: "))
                break

            except ValueError:
                print("Info: player_count must be a positive integer")

    return player_count


def get_players(player_count):

    # Ein dictionary pro Spieler in Players packen

    players = []

    for i in range(player_count):
        player_name = input(f"Player {i + 1} name: ")
        players.append({"name": player_name, "Matchpoints": 0, "Gamepoints": 0})

    return players


def print_matches(players):

    matches = []
    counter = 1

    print()

    for pl1 in range(len(players)):
        for pl2 in range(pl1+1, len(players)):
            name1 = players[pl1]["name"]
            name2 = players[pl2]["name"]
            matches.append([name1, name2])
            print(f"Spiel {counter}: \n {name1} vs {name2}")
            counter += 1

    return matches


def input_results(players, matches):

    results = []
    counter = 1

    print()

    for match in matches:
        print(f"Spiel {counter}: \n {match[0]} vs {match[1]}")
        
        while True:
            try:
                punkte0 = int(input(f" Punkte für {match[0]}: "))
                punkte1 = int(input(f" Punkte für {match[1]}: "))
                if punkte0 < 0 or punkte1 < 0:
                    print("Punkte können nicht negativ sein!")
                    continue
                if punkte0 == punkte1:
                    print("Unentschieden nicht möglich. Bitte erneut eingeben!")
                    continue
                break
            except ValueError:
                print("Bitte nur ganze Zahlen eingeben!")

        if punkte0 > punkte1:
            gewinner  = match[0]
            verlierer = match[1]
            punkte_gewinner  = punkte0
            punkte_verlierer = punkte1
        else:
            gewinner  = match[1]
            verlierer = match[0]
            punkte_gewinner  = punkte1
            punkte_verlierer = punkte0


        for pl in players:
            if pl["name"] == gewinner:
                pl["Matchpoints"] = pl.get("Matchpoints", 0) + 3
                pl["Gamepoint ratio"] = pl.get("Gamepoint ratio", 0) + (punkte_gewinner - punkte_verlierer)
            elif pl["name"] == verlierer:
                pl["Gamepoint ratio"] = pl.get("Gamepoint ratio", 0) + (punkte_verlierer - punkte_gewinner)


        results.append({"match": counter, "Gewinner": gewinner, "Verlierer": verlierer, "Punkte_Gewinner": punkte_gewinner, "Punkte_Verlierer": punkte_verlierer,})

        counter += 1

    return players, results


def print_results(players):

    print()

    # Printe alle spieler mit deren Punktzahl (3 Punkte pro win, sortiert und verkünde die Gewinner (die mit höhster Punktzahl)
    players.sort(key=lambda x: (x["Matchpoints"], x["Gamepoint ratio"]), reverse=True)
    for i in range(len(players)):
        print(f"{i + 1}. Platz: {players[i]["name"]}\nMatchpoints: {players[i]["Matchpoints"]}\nPunkteverhältnis: {players[i]["Gamepoint ratio"]}")
        print()
    


def save_result(results):

    # Speichere die Ergebnisse in einer .txt
    with open("ergebnisse.txt", "w") as file:
        for i in range(len(results)):
            file.write(f"{i + 1}. Match: Gewinner: {results[i]["Gewinner"]}, Verlierer: {results[i]["Verlierer"]}, Punkte Gewinner: {results[i]["Punkte_Gewinner"]}, Punkte Verlierer: {results[i]["Punkte_Verlierer"]}\n")


if __name__ == "__main__":
    main()