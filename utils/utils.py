import os

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
