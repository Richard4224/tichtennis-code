import sys

def main():

    player_count = get_player_count()

    players = get_players(player_count)

    print_matches(players)

    players, results = input_results(players)

    print_results(players, results)

    save_result(results)

def get_player_count():  

    # Überprüfen ob ein Argument eingegeben wurde
    if len(sys.argv) > 2:
        print("Usage: 'python tischtennis_turnier.py player_count'")
        sys.exit(1)

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

    return player_count


def get_players(player_count):

    # return players[{"name": string, "wins": int, "losses": int}, {"name": string, "wins": int, "losses": int}, etc]
    # Ein dictionary pro Spieler in Players packen

    players = []

    for i in range(player_count):
        player_name = input(f"Player {i + 1} name: ")
        players.append({"name": player_name, "wins": 0, "losses": 0})

    return players

def print_matches(players):

    # Jedes matchup in den Terminal printen 
    pass

def input_results(players):

    # Nach jedem ergebnis für jedes Matchup fragen
    # Return updatet players mit wins und losses, sowie results[{"match": int, "playerA": string, "playerB": string}, {}]
    return players, results
    pass

def print_results(players, results):

    # Printe alle spieler mit deren Punktzahl (3 Punkte pro win), sortiert und verkünde die Gewinner (die mit höhster Punktzahl)
    pass

def save_result(results):

    # Speichere die Ergebnisse in einer .txt
    pass

if __name__ == "__main__":
    main()
