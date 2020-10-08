import os
import time
import sys


gamemode_nr = 0
vibe_check = 0
board_1 = {}
board_2 = {}
entry_field_val = 0


def erase_previous_data():
    global gamemode_nr, vibe_check, board_1, board_2
    gamemode_nr = 0
    vibe_check = 0
    board_1 = {}
    board_2 = {}

# from pynput.keyboard import Key, Listener


# def emergency_escape(key):
#     if key == Key.esc:
#         yn = input("Wciśnięto awaryjny przycisk wyjścia; czy na pewno chcesz wyjść? Y/N").upper()
#         if yn == "Y":
#             sys.exit(0)
#
#
# # nasłuchiwacz przycisku "Escape"
#
# with Listener(
#         on_release=emergency_escape) as listener:
#     listener.join()


def start():
    print("Hello and welcome to our Battleship game!")
    time.sleep(1.5)
    main_menu() #menu startowe z wyborem między single i multiplayer


def instructions():
    pass


def exit_game():
    cls()
    yn = input("\nAre you sure you want to exit? Y/N").upper()
    if yn == "Y":
        print("See you next time!")
        time.sleep(2)
        sys.exit(0)
    else:
        main_menu()




def init(func, gamemode):
    global gamemode_nr
    gamemode_nr = int(gamemode)
    main_menu_picks[func]()


def one_player_game(): #tryb jednoosobowy (trudne)
    selection_phase(1)


def two_player_game(): #tryb dwuosobowy (średnie)
    selection_phase(2)


def selection_phase():
    cls()
    global gamemode_nr
    option_nr = input("\nSelect game preset you want to use:\n(1) Long Battle\n(2) Quick Joust\n(3) Custom Game\n(4) Go back to main menu\n")
    if option_nr in selection_phase_picks.keys():
        if (str(selection_phase_picks[option_nr])).isdigit() == True:
            if gamemode_nr == 1:
                one_player_game(selection_phase_picks[option_nr])
            elif gamemode_nr == 2:
                two_player_game(selection_phase_picks[option_nr])
            else:
                error("Type of game is neither single- or multiplayer, please check data cohesion")
        else:
            try:
                init(selection_phase_picks[option_nr], selection_phase_picks[option_nr])
            except:
                error("Type of game is neither of available picks, please check it went past 'if option_nr in selection_phase_picks.keys()' statement")
    else:
        print("Wrong input, please try again")
        time.sleep(1)



def main_menu():
    erase_previous_data()
    while True:
        cls()
        selection = input("Select one of available options:\n(1)One player\n(2) Two players\n(3) Instructions\n(4) Exit\n")
        if selection in main_menu_picks.keys():
            init(selection, selection) #wywołuje odpowiednią funkcje z opcji
            break
        else:
            print("Wrong input, please try again")
            time.sleep(1)



def custom():
    global board_1, board_2, alphabet, entry_field_val
    while True:
        cls()
        nr_of_rows_and_cols = input("\nType in a number of custom rows and columns you would like to play with (maximum is 20)")
        if nr_of_rows_and_cols.isdigit() == True & len(nr_of_rows_and_cols) > 0:
            if int(nr_of_rows_and_cols) > 20:
                print("Sorry, but max rows and columns count is 20, please readjust your pick")
                time.sleep(1.5)
                continue
            current_nr=1
            for rows_n_cols in range(int(nr_of_rows_and_cols)+1):
                dict_key_input = str(alphabet[current_nr-1]+rows_n_cols)
                board_1[dict_key_input]=f"[ {entry_field_val} ]"





main_menu_picks = {"1": selection_phase, "2": selection_phase, "3": instructions, "4": exit_game} #dict z opcjami menu, umiejscowione tu dla pewności, że program nie wywali się przez brak zdefiniowania którejś opcji z menu
selection_phase_picks = {"1": 10, "2": 5, "3": custom, "4": main_menu} #dict z opcjami menu, umiejscowione tu dla pewności, że program nie wywali się przez brak zdefiniowania którejś opcji z menu
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","Q","P","R","S","T"]

def cls():
    os.system('cls')


def error(str):
    raise Exception(str)


start()



