import os
import time



def start():
    print("Hello and welcome to our Battleship game!")
    time.sleep(1.5)
    main_menu() #menu startowe z wyborem między single i multiplayer



def singleplayer(): #tryb jednoosobowy (trudne)
    pass


def multiplayer(): #tryb dwuosobowy (średnie)
    pass


def instructions():  #instrukcje
    pass


def exit_game():
    pass


def cls():
    os.system('cls')

menu_choices = {"1": singleplayer, "2": multiplayer, "3": instructions, "4": exit_game} #dict z opcjami menu, umiejscowione tu dla pewności, że program nie wywali się przez brak zdefiniowania którejś opcji z menu


def main_menu():
    while True:
        cls()
        selection = input("Select one of available options:\n1.One player\n2. Two players\n3. Instructions\n4. Exit\n")
        if selection in menu_choices.keys():
            init(selection) #wywołuje odpowiednią funkcje z opcji
            break
        else:
            print("Wrong input, please try again")
            time.sleep(1)





def init(func):
    menu_choices[func]()

start()