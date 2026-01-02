import random
import time
import pandas as pd
import os
import db # __init__.py --> get_connection, init_db
from athletes import Athlete
from tabulate import tabulate
from repository.athletes_repository import get_all_athletes, create_athlete

def choice(option_list, text="Your choice: "):
    """
    Prompt the user to select an option from a given list.

    :param option_list (list): A list of valid options.
    :param (str, optional): The prompt message displayed to the user. Default is "Your choice: ".

    Returns:
    - str: The option chosen by the user (always valid).
    
    The function keeps asking until the user enters a valid option.
    """
    while True:
        option = input(text).lower().strip()
        if option not in (option_list):
            print("Invalid! Choose again!!")
        else:
            return option
        
def clean_screen(text=None): # the name is self-explanatory
    os.system("cls" if os.name == "nt" else "clear")
    if text:
        print(text)

def show_scoreboard(games: dict, j1: Athlete, j2: Athlete):
    clean_screen("---- TABLE TENNIS SIMULATOR ----")

    scoreboard = {
        j1.name: [],
        j2.name: []
    }
    columns = ["Games"]
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

    MATCH_SPEED = 0.5

    while game_j1 < 3 and game_j2 < 3:
        deuce = False
        while True:
            games[game] = (points_j1, points_j2)
            show_scoreboard(games, j1, j2)
            time.sleep(MATCH_SPEED)

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
    athletes_list = get_all_athletes()
    while True:
        clean_screen()
        print("""---- TABLE TENNIS SIMULATOR ----
    [1] Sim match
    [2] Create athlete
    """)
        option = choice(("1", "2"))

        match option:
            case "1":
                clean_screen("---- Choose your players ----")

                for athlete in athletes_list:
                    print(f"{athletes_list.index(athlete)}. {athlete.name} - OVR: {athlete.overall}")

                print()

                len_athletes = len(athletes_list)
                indexes = list(str(i) for i in range(len_athletes))
                j1 = choice(indexes)
                indexes.remove(j1) # removes the selected athlete from the list
                j2 = choice(indexes)

                j1, j2 = int(j1), int(j2)
                j1 = athletes_list[j1]
                j2 = athletes_list[j2]

                # the match allways starts and after that the user will be asked for a rematch
                while True: 
                    match_simulation(j1, j2)
                    option = choice(("y","n"), "Rematch: (y/n) ")
                    if option == "n":
                        break
            case "2":
                clean_screen("---- Create your athlete ----")
                options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                           "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
                name = input("Name: ")

                attack = choice(options, "Attack: (1-20) ")
                attack = int(attack)

                defense = choice(options, "Defense: (1-20) ")
                defense = int(defense)

                serve = choice(options, "Serve: (1-20) ")
                serve = int(serve)

                athletes_list = create_athlete(name, attack, defense, serve)
                
                print("Athlete created, good luck!")

                enter = input("Press Enter: ")
                

db.init_db() # starts the database if it not exists
menu()
