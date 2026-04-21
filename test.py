def print_results(players):

    # Printe alle spieler mit deren Punktzahl (3 Punkte pro win, Unentschieden 1 Punkt), sortiert und verkünde die Gewinner (die mit höhster Punktzahl)
    players.sort(key=lambda x: (x["Matchpoints"], x["Gamepoints"]), reverse=True)

    for i in range(len(players)):
        print(i)

print_results([{"name": 'strig', "Matchpoints": 6, "Gamepoints": 12}, {"name": 'strin', "Matchpoints": 4, "Gamepoints": 9}])
