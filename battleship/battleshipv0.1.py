import os
import time
import sys


gamemode_nr = 0
vibe_check = 0
board_ships_1 = {}
board_ships_2 = {}
board_hits_1 = {}
board_hits_2 = {}
entry_field_val = 0
nr_of_rows = 0

def erase_previous_data():
    global gamemode_nr, vibe_check, board_ships_1, board_ships_2, board_hits_1, board_hits_2, nr_of_rows
    gamemode_nr = 0
    vibe_check = 0
    nr_of_rows = 0
    board_ships_1 = {}
    board_ships_2 = {}
    board_hits_1 = {}
    board_hits_2 = {}

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
    if func in selection_phase_picks.values():
        func()
    gamemode_nr = int(gamemode)
    main_menu_picks[func]()


def one_player_game(num): #tryb jednoosobowy (trudne)
    pass


def two_player_game(num): #tryb dwuosobowy (średnie)
    pass


def selection_phase():
    cls()
    global gamemode_nr
    option_nr = input("\nSelect game preset you want to use:\n(1) Long Battle\n(2) Quick Joust\n(3) Custom Game\n(4) Go back to main menu\n")
    if option_nr in selection_phase_picks.keys():
        if (str(selection_phase_picks[option_nr])).isdigit() == True:
            board_create(selection_phase_picks[option_nr])
            # if gamemode_nr == 1:
            #     one_player_game(selection_phase_picks[option_nr])
            # elif gamemode_nr == 2:
            #     two_player_game(selection_phase_picks[option_nr])
            # else:
            #     error("Type of game is neither single- or multiplayer, please check data cohesion")
        else:
            try:
                init(selection_phase_picks[option_nr], selection_phase_picks[option_nr])
            except:
                error("Type of game is neither of available picks, please check how it went past 'if option_nr in selection_phase_picks.keys()' statement")
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


def board_create(count):
    global alphabet, entry_field_val, board_ships_1, board_ships_2, board_hits_1, board_hits_2, nr_of_rows
    nr_of_rows = count
    for rows_n_cols in range(int(count)):
        for letter in alphabet[0:count]:
            dict_key_input = letter + str(rows_n_cols+1)
            board_ships_1[dict_key_input] = " 0 "
            board_ships_2[dict_key_input] = " 0 "
            board_hits_1[dict_key_input] = " 0 "
            board_hits_2[dict_key_input] = " 0 "


def print_board(dict, count): #słownik do drukowania oraz liczba komórek na wiersz
    global alphabet
    current_row = []
    print(" "+'  '.join(letter for letter in alphabet))
    for cell in dict.values():
        current_row.append(cell)
        if len(current_row) % count == 0:
            print(' '.join(str(x) for x in current_row))
            current_row.clear()


def custom():
    while True:
        cls()
        nr_of_rows_and_cols = input("\nType in a number of custom rows and columns you would like to play with (maximum is 20)")
        if nr_of_rows_and_cols.isdigit() == True & len(nr_of_rows_and_cols) > 0:
            if int(nr_of_rows_and_cols) > 20:
                print("Sorry, but max rows and columns count is 20, please readjust your pick")
                time.sleep(1.5)
                continue
            board_create(int(nr_of_rows_and_cols))
        else:
            print("Wrong input")
            time.sleep(1.5)





main_menu_picks = {"1": selection_phase, "2": selection_phase, "3": instructions, "4": exit_game} #dict z opcjami menu, umiejscowione tu dla pewności, że program nie wywali się przez brak zdefiniowania którejś opcji z menu
selection_phase_picks = {"1": 10, "2": 5, "3": custom, "4": main_menu} #dict z opcjami menu, umiejscowione tu dla pewności, że program nie wywali się przez brak zdefiniowania którejś opcji z menu
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","Q","P","R","S","T"]

def cls():
    os.system('cls')


def error(str):
    raise Exception(str)


start()



