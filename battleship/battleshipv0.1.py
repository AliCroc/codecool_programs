import os
import time
import sys
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


def main_menu():
    while True:
        cls()
        selection = input("Select one of available options:\n1.One player\n2. Two players\n3. Instructions\n4. Exit\n")
        if selection in main_menu.keys():
            init(selection) #wywołuje odpowiednią funkcje z opcji
            break
        else:
            print("Wrong input, please try again")
            time.sleep(1)


def singleplayer(): #tryb jednoosobowy (trudne)
    selection_phase(1)


def multiplayer(): #tryb dwuosobowy (średnie)
    selection_phase(1)


def instructions():  #instrukcje
    pass


def exit_game():
    yn = input("\nAre you sure you want to exit? Y/N").upper()
    if yn == "Y":
        print("See you next time!")
        time.sleep(2)
        sys.exit(0)
    else:
        main_menu()


def cls():
    os.system('cls')

main_menu = {"1": singleplayer, "2": multiplayer, "3": instructions, "4": exit_game} #dict z opcjami menu, umiejscowione tu dla pewności, że program nie wywali się przez brak zdefiniowania którejś opcji z menu

def selection_phase():
    pass

def init(func):
    main_menu[func]()

start()