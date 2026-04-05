import os
import pandas as pd
from tabulate import tabulate
from schemas.athlete_schema import Athlete

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