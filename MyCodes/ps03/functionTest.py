def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    Result = 1
    new_word = word.lower()
    new_hand = hand.copy()
    
    #Test whether word exists in list or not
    for i,word_in_list in enumerate(word_list):
        if len(new_word)==len(word_in_list):
            test = len(new_word)
            for i,c in enumerate(new_word):
                if (c == '*') or (c == word_in_list[i]):
                    test -=1
                else:
                    break
            if test == 0:
                break
        elif i == len(word_list)-1:
            return False
        else:
            pass



    #If the character of the word doesn't exists in hand, return 0
    for c in new_word:
        try:
            if new_hand[c] > 0:
                new_hand[c] -= 1
                print(c,new_hand[c])
            if new_hand[c] == 0:
                del new_hand[c]
        except:
            Result = 0
    
    return bool(Result)  # TO DO... Remove this line when you implement this function
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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

word_list = load_words()
word = 'h*ney'
hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}

print(is_valid_word(word, hand, word_list))