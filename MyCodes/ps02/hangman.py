# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # If i == len(sWord) that means
    # all the letters in list are included in secret_word
    i = 0
    for sWord in secret_word:
        for gWord in letters_guessed:
            if sWord == gWord:
                i += 1
                break

    if i == len(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guess = ''
    if len(letters_guessed) == 0:
        for i in range(len(secret_word)):
            guess += "_ "
        return guess

    for sWord in secret_word:
        # iteration count for each loop
        i = 0
        for gWord in letters_guessed:
            i += 1
            if sWord == gWord:
                guess += sWord
                break
            elif i == len(letters_guessed):
                guess += "_ "
    return guess


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    guess_letters = string.ascii_lowercase
    for gLetter in letters_guessed:
        guess_letters = guess_letters.replace(gLetter, "")
    return guess_letters


def is_word_correct(user_input, secret_word):
    for letter in secret_word:
        if user_input == letter:
            return True
    return False

def win_or_lose(guessed_words):
    i = 1
    for char in guessed_words:
        i *= int(str.isalpha(char))
        if i != 1:
            return False
    return True

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # number of guesses at the start.
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    print("Welcome to the game Hangman! \n" +
          "I am thinking of a word that is " + str(len(secret_word)) + " letters long.\n" +
          "-------------")

    while (guesses_remaining >= 0):
        print("You have " + str(guesses_remaining) + " guesses left.")
        print("Available letters: " + get_available_letters(letters_guessed))
        '''
        Validate input whether 
        1. it is alphabet
        2. it is already guessed
        and if not valid -1 warnings when warning reached 3, -1 guesses
        '''

        # validate input
        user_input = input("Please guess a letter: ")

        # case 1. is alphabet
        if not str.isalpha(user_input):
            print("Oops! That is not a valid letter.")
            if warnings_remaining < 0:
                print("You have no warnings left so you lose one guess: ")
                guesses_remaining -= 1
            else:
                print("You have " + str(warnings_remaining) + " warning left")
                warnings_remaining -= 1
            continue

        # case 2. is already guessed
        if is_word_guessed(user_input, letters_guessed):
            print("The letter already guessed")
            if warnings_remaining < 0:
                print("You have no warnings left so you lose one guess: ")
                guesses_remaining -= 1
            else:
                print("You have " + str(warnings_remaining) + " warning left: ")
                warnings_remaining -= 1
            continue

        # turn into lower case
        user_input = user_input.lower()
        print(user_input)
        # as the input is validated, put it into list
        letters_guessed.append(user_input)
        # and show the available letters
        print("Available letters: " + get_available_letters(letters_guessed))

        '''
        check `is word correct`
        if correct, guess as it is. otherwise lose guess depends on vowel or not
        '''
        if is_word_correct(user_input, secret_word):
            print("Good guess: ")
        else:
            print("Oops! That letter is not in my word: ")
            # check vowel
            # is vowel? -2 guess
            if user_input in ("a", "e", "i", "o", "u"):
                guesses_remaining -= 2
            # else -1 guess
            else:
                guesses_remaining -= 1

        '''
        show the result
        '''
        guessed_words = get_guessed_word(secret_word, letters_guessed)
        print(guessed_words)
        print("-----------------")

        '''
        Win or lose
        '''
        if win_or_lose(guessed_words):
            print("Congratulations, you won!")
            print("Your total score for this game is: " + str(guesses_remaining
                                                              *len(''.join(set(guessed_words)))))
            break
        else:
            print("Sorry, you ran out of guesses. The word was " + secret_word + ".")

        # # if the word is guessed, guesscount remains as it is otherwise -1
        # letters_guessed.append(user_input)
        # if is_word_guessed(secret_word, letters_guessed):
        #     guesscount = guesscount
        # else:
        #     guesscount -= 1
        # # print the remaining count of guesses
        # print("You have "+ str(guesscount)+" guesses left")
        # # shows the available letters
        # print(letters_guessed)
        # print("Available letters: " + get_available_letters(letters_guessed))
        # print(get_guessed_word(secret_word, letters_guessed)+ "\n")

    return None


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)
