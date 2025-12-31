import random, time, pandas as pd, os
from athletes import Athlete, athletes_list
from tabulate import tabulate

def choice(option_list):
    while True:
        option = input("Your choice: ").lower().strip()
        if option not in (option_list):
            print("Selecione uma opção válida!")
        else:
            return option

def clean_screen(text): # the name is self-explanatory
    os.system("cls" if os.name == "nt" else "clear")
    if text:
        print(text)

def show_scoreboard(games: dict, j1: Athlete, j2: Athlete):
    clean_screen("---- TABLE TENNIS SIMULATOR ----")

    scoreboard = {
        j1.name: [],
        j2.name: []
    }
    columns = ["Sets"]
    for game in games.items():
        sets, points = game
        scoreboard[j1.name].append(points[0])
        scoreboard[j2.name].append(points[1])
        columns.append(str(sets))

    df_scoreboard = pd.DataFrame.from_dict(scoreboard, orient="index")
    scoreboard = tabulate(df_scoreboard, headers=columns, stralign="center", 
                          numalign="right", tablefmt="rounded_outline")
    print(scoreboard)


def service_rotation(deuce, count_to_serve, players, to_serve, to_receive):
    """
    Handles service rotation in table tennis.

    The serve alternates every 2 points, regardless of who scored.
    At deuce (10–10), the serve alternates every point.

    :param deuce: True if the match is in deuce
    :param count_to_serve: point counter for serve rotation
    :param players: list containing both players
    :param to_serve: player to serve
    :param to_receive: player to receive
    """
    should_switch = deuce or count_to_serve == 2

    if should_switch:
        to_serve, to_receive = (players[1], players[0]) if to_serve == players[0] else (players[0], players[1])
        count_to_serve = 0

    return to_serve, to_receive, count_to_serve

def match_simulation(j1, j2):
    games = {}

    game_j1, game_j2 = 0, 0
    points_j1 = 0
    points_j2 = 0

    game = 1

    players = [j1, j2]
    random.shuffle(players)
    to_serve, to_receive = players
    count_to_serve = 0

    ATTACK_WEIGHT = 1.3
    DEFENSE_WEIGHT = 1.1
    RANDOM_VARIATION = 8
    BASE_ERROR = 0.05

    while game_j1 < 3 and game_j2 < 3:
        deuce = False
        while True:
            games[game] = (points_j1, points_j2)
            show_scoreboard(games, j1, j2)
            time.sleep(0.4)

            error_chance = (10 - to_serve.serve) / 10
            ace_chance = (to_serve.serve / (to_serve.serve + to_receive.defense)) * 0.15

            if random.random() < error_chance: # missed the serve
                if to_serve == j1:
                    points_j2 += 1
                else:
                    points_j1 += 1
            elif random.random() < ace_chance: # score an ace
                if to_serve == j1:
                    points_j1 += 1
                else:
                    points_j2 += 1
            else: # rally
                random.shuffle(players) # shuffle players to decide who attacks first in the rally

                attack_player, defense_player = players

                attack = attack_player.attack * ATTACK_WEIGHT + random.randint(0, RANDOM_VARIATION)
                defense = defense_player.defense * DEFENSE_WEIGHT + random.randint(0, RANDOM_VARIATION)

                attack_chance = attack / (attack + defense)

                if random.random() < BASE_ERROR:
                    point_winner = defense_player
                else:
                    point_winner = attack_player if random.random() < attack_chance else defense_player

                if point_winner == j1:
                    points_j1 += 1
                else:
                    points_j2 += 1

                if points_j1 == 10 and points_j2 == 10: # Deuce happen when both players scored 10 points in the set/game
                    deuce = True # at deuce, a player must score 2 consecutive points to win the set

            count_to_serve += 1 # counting serves to rotate
            to_serve, to_receive, count_to_serve = service_rotation(deuce, count_to_serve, players, to_serve, to_receive)

            if points_j1 >= 11 and points_j1 - points_j2 >= 2:
                game_j1 += 1
                break

            if points_j2 >= 11 and points_j2 - points_j1 >= 2:
                game_j2 += 1
                break

        games[game] = (points_j1, points_j2)
        points_j1 = 0
        points_j2 = 0
        game += 1

    show_scoreboard(games, j1, j2)

    return j1.name if game_j1 > game_j2 else j2.name

def menu():
    print("""---- TABLE TENNIS SIMULATOR ----
[1] Sim match
""")
    option = choice(("1"))

    if option == "1":
        clean_screen("---- Choose your players ----")

        for athlete in athletes_list:
            print(f"{athletes_list.index(athlete)}. {athlete.name} - OVR: {athlete.overall}")

        len_athletes = len(athletes_list)
        indexes = list(str(i) for i in range(len_athletes))
        j1 = choice(indexes)
        indexes.remove(j1)
        j2 = choice(indexes)

        j1, j2 = int(j1), int(j2)
        j1 = athletes_list[j1]
        j2 = athletes_list[j2]

        match_simulation(j1, j2)

menu()
