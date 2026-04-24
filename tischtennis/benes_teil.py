import sys


def main():

    player_count = get_player_count()

    players = get_players(player_count)

    matches = print_matches(players)

    players, results = input_results(players, matches)

    print_results(players, results)

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

    # Nach jedem ergebnis für jedes Matchup fragen
    # Return updatet players mit wins und losses, sowie results[{"match": int, "Gewinner": string, "Verlierer": string}, {}]

    results = []
    counter = 1
    choice = None

    print()

    for match in matches:
        print(f"Spiel {counter}: \n {match[0]} vs {match[1]} \n Wer hat gewonnen? \n \t {match[0]} - 1 \n \t {match[1]} - 2")
        while True:
            try:
                choice = int(input("Geben Sie ein: "))
                if choice == 1 or choice == 2:
                    break
                print("Geben Sie 1 oder 2 ein!")
            except ValueError:
                print("Geben Sie 1 oder 2 ein!")

        gewinner = match[choice-1]
        verlierer = match[2-choice]

        for pl in players:
            if pl["name"] == gewinner:
                pl["Matchpoints"] = pl.get("Matchpoints", 0) + 3

        results.append({"match": counter, "Gewinner": gewinner, "Verlierer": verlierer})

        counter += 1

    return players, results


def print_results(players):

    print()

    # Printe alle spieler mit deren Punktzahl (3 Punkte pro win, sortiert und verkünde die Gewinner (die mit höhster Punktzahl)
    players.sort(key=lambda x: (x["Matchpoints"], x["Gamepoints"]), reverse=True)
    for i in range(len(players)):
        print(f"{i + 1}. Place: {players[i]["name"]}\nMatchpoints: {players[i]["Matchpoints"]}\nGamepoints:  {players[i]["Gamepoints"]}")
        print()
    


def save_result(results):

    # Speichere die Ergebnisse in einer .txt
    with open("ergebnisse.txt", "w") as file:
        for i in range(len(results)):
            file.write(f"{i + 1}. Match: Gewinner: {results[i]["Gewinner"]}, Verlierer: {results[i]["Verlierer"]}\n")


if __name__ == "__main__":
    main()
