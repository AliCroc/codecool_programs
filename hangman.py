import random, time, sys

words = ['PROGRAM', 'VARIABLE', 'CONSOLE', 'FUNCTION', 'LOOP', 'LAMBDA', 'DICTIONARY', 'CODECOOL', 'COMPUTER']

hangman_img = [
    """
        ________
        |       |
        |       O
        |      \\|/
        |      / \\ 
        |       
        |      
    """,
    """
        ________
        |       |
        |       O
        |      \\|/
        |      /
        |       
        |       
    """,
    """
        ________
        |       |
        |       O
        |      \\|/
        |      
        |       
        |       
    """,
    """
        ________
        |       |
        |       O
        |       |/
        |       
        |       
        |       
    """,
    """
        ________
        |       |
        |       O
        |       |
        |       
        |       
        |       
    """,
    """
        ________
        |       |
        |       
        |       
        |       
        |      
        |      
    """,
    """

        |       
        |       
        |       
        |       
        |      
        |      
    """,
    """







    """
]


def start():
    print("Welcome to our HANGMAN!\n")
    time.sleep(1)
    wanted_word = random.choice(words)  # picks random word from words list
    n = 0
    to_guess = {}
    blanks = {}
    for o in wanted_word:  # writes word into dict and creates second dict with as many blanks as there are letters in word
        to_guess[n] = str(o)
        blanks[n] = "_"
        n += 1
    chances = len(wanted_word) - 1  # chances the player get to guess the word
    print("You have", chances, "chances to guess the word!")
    time.sleep(3)
    tryouts = []
    while chances > 0:
        if "_" not in blanks.values():
            print("Congratulations! You have guessed the whole word", wanted_word, "correctly! :)\n")
            break
        print("\n" * 80)
        print(hangman_img[chances], "\n")
        for l in blanks.values():
            print(l, end=" ")
        print("\n\n")
        if len(tryouts) > 0:
            print("Letters which were tried out so far: ")
            for i in tryouts:
                sys.stdout.write(i)
                sys.stdout.write(" ")
        else:
            print("Letters which were tried out so far: ")
        input_letter = input("\nType in a letter you think is in wanted word\n").upper()
        if input_letter.isalpha() == False or len(input_letter) > 1:
            print("You can type in only one LETTER at a time\n")
            time.sleep(1)
            continue
        if input_letter in tryouts:
            print("You have tried this letter already!\n")
            time.sleep(1)
            continue
        elif input_letter in to_guess.values():
            letters_in_word = []
            for k in to_guess:
                if str(to_guess[k]) == input_letter:
                    letters_in_word.append(int(k))
            for l in letters_in_word:
                blanks[l] = input_letter  # replacing blanks with input letter
            letters_in_word *= 0
            tryouts.append(input_letter)
            continue
        else:
            print("There is no", input_letter, "in this word!")
            tryouts.append(input_letter)
            time.sleep(1)
        chances -= 1
    if chances == 0:
        print(hangman_img[chances])
        print("You used all your chances, you lose!\n The wanted word was:", wanted_word)
        time.sleep(3)
    while True:
        yn = str(input("Would you like to play again? Y/N\n").upper())
        if yn == "Y":
            start()
            break
        if yn == "N":
            print("Thank you for playing! See you next time!")
            time.sleep(3)
            sys.exit(0)
        else:
            print("Wrong input! Type y or n")
            continue


start()


