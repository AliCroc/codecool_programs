import os
import time
import sys
import random

gamemode_nr = 0
# vibe_check = 0
board_ships_1 = {}
board_ships_2 = {}
board_hits_1 = {}
board_hits_2 = {}
fields_val = 0
nr_of_rows = 0
emergency_exit_word = "quit"
player_name = ""
player_name1 = ""
player_name2 = ""
cell_values = []

def erase_previous_data():
    global gamemode_nr, fields_val, board_ships_1, board_ships_2, board_hits_1, board_hits_2, nr_of_rows, player_name, player_name1, player_name2    # vibe_check,
    gamemode_nr = 0
    # vibe_check = 0
    nr_of_rows = 0
    board_ships_1 = {}
    board_ships_2 = {}
    board_hits_1 = {}
    board_hits_2 = {}
    player_name = ""
    cell_values = []
    fields_val = 0


def start():
    print("Hello and welcome to our Battleship game!\nAre you ready for real battle?")
    time.sleep(2.5)
    main_menu() #menu startowe z wyborem między single i multiplayer


def instructions():
    pass
        # 1. główne założenia gry
        # 2. typy statków
        # 3. poziomy trudności przeciwnika
        # 4. rozstawianie statków


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
    global gamemode_nr, selection_phase_picks
    if func in selection_phase_picks.values():
        func()
    if func == "7":
        instructions()
    gamemode_nr = int(gamemode)
    main_menu_picks[func]()


def one_player_game(num): #tryb jednoosobowy (trudne)
    global player_name
    player_name = input("Type in your nickname, capitan!")
    cls()
    print("Alright", player_name + ", it's time to set your fleet")
    time.sleep(2.5)
    cls()
    arrange_ships(num)


def two_player_game(num): #tryb dwuosobowy (średnie)
    print("Two")


def selection_phase():
    cls()
    global gamemode_nr, emergency_exit_word, fields_val
    option_nr = input("\nSelect game preset you want to use:\n(1) Long Battle\n(2) Quick Joust\n(3) Custom Game\n(4) Go back to main menu\n")
    if option_nr in selection_phase_picks.keys():
        if (str(selection_phase_picks[option_nr])).isdigit() == True:
            board_create(selection_phase_picks[option_nr])
        else:
            try:
                init(selection_phase_picks[option_nr], selection_phase_picks[option_nr])
            except:
                error("Type of game is neither of available picks, please check how it went past 'if option_nr in selection_phase_picks.keys()' statement")
        if option_nr in ["1","2"]:
            # fields_val = selection_phase_picks[option_nr]
            gamemode_choice = (two_player_game if gamemode_nr == 2 else one_player_game)
            gamemode_choice(selection_phase_picks[option_nr])
    elif option_nr == emergency_exit_word:
            exit_game()
    else:
        print("Wrong input, please try again")
        time.sleep(1)


def main_menu():
    erase_previous_data()
    while True:
        cls()
        selection = input("Select one of available options:\n(1) One player\n(2) Two players\n(3) Instructions\n(4) Exit\n")
        if selection in main_menu_picks.keys():
            init(selection, selection) #wywołuje odpowiednią funkcje z opcji
            break
        elif selection == emergency_exit_word:
            exit_game()
        else:
            print("Wrong input, please try again")
            time.sleep(1)


def board_create(count):
    global alphabet, fields_val, board_ships_1, board_ships_2, board_hits_1, board_hits_2, nr_of_rows, cell_values
    nr_of_rows = count
    for rows_n_cols in range(int(count)):
        for letter in alphabet[0:count]:
            dict_key_input = letter + str(rows_n_cols+1)
            board_ships_1[dict_key_input] = " 0 "
            board_ships_2[dict_key_input] = " 0 "
            board_hits_1[dict_key_input] = " 0 "
            board_hits_2[dict_key_input] = " 0 "
            cell_values.append(0)



def print_board(dict, count): #słownik do drukowania oraz liczba komórek na wiersz
    global alphabet
    current_row = []
    current_row_nr = 1
    print("   "+'  '.join(letter for letter in alphabet))
    for cell in dict.values():
        current_row.append(cell)
        if len(current_row) % count == 0:
            print(current_row_nr, " "+(' '.join(str(x) for x in current_row)))
            current_row_nr += 1
            current_row.clear()


def custom():
    global gamemode_nr, emergency_exit_word
    while True:
        cls()
        nr_of_rows_and_cols = input("\nType in a number of custom rows and columns you would like to play with (minimum is 5 and maximum is 20)\n")
        if nr_of_rows_and_cols.isdigit() == True:
            if int(nr_of_rows_and_cols) > 20 or int(nr_of_rows_and_cols) < 5:
                print("Sorry, but max rows and columns count is 20 and minimum is 5, please readjust your pick")
                time.sleep(1.5)
                continue
            board_create(int(nr_of_rows_and_cols))
            gamemode_choice = (two_player_game if gamemode_nr == 2 else one_player_game)
            print(gamemode_nr, str(gamemode_choice))
            gamemode_choice(nr_of_rows_and_cols)
        elif nr_of_rows_and_cols == emergency_exit_word:
            exit_game()
        else:
            print("Wrong input")
            time.sleep(1.5)


# def set_logic(num, list, level):
#     available_spaces = int(((int(num))**2)*level) #
#
#     return list


def arrange_ships(num):
    ship_picks = []
    game_settings = game_difficulty(num)
    # ship_picks = set_logic(game_settings[0])


def game_difficulty(num):
    global density_levels_menu, bot_difficulty_levels
    while True:
        cls()
        dif_preset = input("Choose game preset or select \"custom\" option for custom settings:\n(1) Easy (almost 1 in 2 chance for hit and a baby as an opponent(not recommanded for small boards!))\n(2) Medium (normal hit chance and focused opponent)\n(3) Hard (a challanging opponent with well hidden fleet)\n(4) Master (fight against experienced capitan and WW2 veteran, who won't give you a chance)\n(5) Godlike (your enemy litterly have a sonar and you are outnumbered)\n(6) Custom ship density and opponent difficulty\n(7) Instructions")
        if dif_preset == "7":
            init(dif_preset, dif_preset)
            break
        elif dif_preset in ["1","2","3","4","5"]:
            settings = available_spaces_calc(num, density_levels_menu[dif_preset], int(dif_preset))
            return settings
        elif dif_preset == emergency_exit_word:
            exit_game()
        elif dif_preset == "6":
            settings = custom_difficulty(num)
            return settings
        else:
            print("Wrong input, please try again")
            time.sleep(1)


def available_spaces_calc(num, preset, bot):
    available_spaces = int(((int(num))**2)*preset)
    if bot in bot_difficulty_levels.keys():
        if bot in [3, 4, 5]:
            bot -= 1
    else:
        error("Invalid dif_preset value, please check code for defects")
    return available_spaces, bot_difficulty_levels[bot]


def custom_difficulty(num):
    while True:
        cls()
        cus_dif = input("Choose a level ship density and their count:\n(1) Tremendous (>50% of space)\n(2) Extensive (>40% of space)\n(1) Moderate (>30% of space)\n(1) Rare (>20% of space)\n")
        if int(cus_dif) in density_levels_menu.keys():
            break
        else:
            print("Wrong input, please try again")
            time.sleep(1)
    while True:
        cls()
        level_of_bot = input("Choose a level of your opponents difficulty:\n(1) Easy (shoots almost randomly)\n(2) Medium (follows hits with shots next to them)\n(3) Hard (has 1000 tactics to win and 0 mercy for you)\n(4) Extremly hard (challange a god, suffer for trying)")
        if int(level_of_bot) in bot_difficulty_levels.keys():
            break
        else:
            print("Wrong input, please try again")
            time.sleep(1)
    settings = available_spaces_calc(num, density_levels_menu[cus_dif], bot_difficulty_levels[level_of_bot])
    return settings

# def l_o_d():
#     input("Choose a level ship density and their count:\n(1) Tremendous (>50% of space)\n(2) Extensive (>40% of space)\n(1) Moderate (>30% of space)\n(1) Rare (>20% of space)\n")
#     return

main_menu_picks = {"1": selection_phase, "2": selection_phase, "3": instructions, "4": exit_game} #dict z opcjami menu, umiejscowione tu dla pewności, że program nie wywali się przez brak zdefiniowania którejś opcji z menu
selection_phase_picks = {"1": 10, "2": 5, "3": custom, "4": main_menu} #dict z opcjami menu, umiejscowione tu dla pewności, że program nie wywali się przez brak zdefiniowania którejś opcji z menu
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "Q", "P", "R", "S", "T"]
density_levels_menu = {"1": 0.5, "2": 0.4, "3": 0.4, "4": 0.3, "5": 0.2, "7": instructions}
bot_difficulty_levels = {1: "easy", 2: "medium", 3: "hard", 4: "very hard"}
ships = {"1": 5, "2": 4, "3": 3, "4": 3, "5": 2}

def cls():
    os.system('cls')


def error(str):
    raise Exception(str)


start()