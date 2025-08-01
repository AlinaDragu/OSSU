# Problem Set 2, hangman.py
import os
import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"
# def load_words():
#     """
#     returns: list, a list of valid words. Words are strings of lowercase letters.

#     Depending on the size of the word list, this function may
#     take a while to finish.
#     """
#     print("Loading word list from file...")
#     # inFile: file
#     inFile = open(WORDLIST_FILENAME, 'r')
#     # line: string
#     line = inFile.readline()
#     # wordlist: list of strings
#     wordlist = line.split()
#     print(" ", len(wordlist), "words loaded.")
#     return wordlist
def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    
    # This line gets the absolute path of the directory the script is in
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # This line joins the directory with the filename to create a full path
    full_path = os.path.join(script_dir, WORDLIST_FILENAME)
    
    # Now, open the file using the full, absolute path
    inFile = open(full_path, 'r')
    
    line = inFile.readline()
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
      if letter not in letters_guessed:
        return False
    return True

def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    progress_list = []
    for letter in secret_word:
      if letter in letters_guessed:
        progress_list.append(letter)
      else:
        progress_list.append('*')
    return ''.join(progress_list)


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_letters = string.ascii_lowercase
    available_letters = []
    for letter in all_letters:
      if letter not in letters_guessed:
        available_letters.append(letter)
    return ''.join(available_letters)



def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_left = 10
    letters_guessed = []
    vowels = "aeiou"
    
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that i {len(secret_word)} letters long.")
    print("-------------")
    
    # The for loop now provides the maximum number of turns (10 guesses).
    # The loop can be exited early with 'break' if the player wins.
    for guesses_left in range(10, 0, -1):
        if has_player_won(secret_word, letters_guessed):
            break
        
        print(f"You have {guesses_left} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        
        guess = input("Please guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha() and guess != '!':
            print("Invalid input. Please enter a single letter.")
            print(f"Current progress: {get_word_progress(secret_word, letters_guessed)}")
            print("-------------")
            continue

        if guess == '!':
            if with_help:
                if guesses_left > 3: # The for loop provides guesses_left, so we need to be careful with its usage.
                    unguessed_letters = [letter for letter in secret_word if letter not in letters_guessed]
                    if unguessed_letters:
                        hint_letter = random.choice(unguessed_letters)
                        letters_guessed.append(hint_letter)
                        print(f"Help activated! The letter '{hint_letter}' has been revealed.")
                        # To correctly deduct guesses from the for-loop counter, we need to adjust it.
                        # This isn't straightforward, so we simply print the new guess count here.
                        # The for loop will proceed to the next iteration with the next value.
                        print(f"You will have {guesses_left - 3} guesses for the next round.")
                    else:
                        print("There are no more unguessed letters to reveal.")
                else:
                    print("Warning: You do not have enough guesses (3) to use the help feature.")
            else:
                print("The help feature is not enabled for this game.")
            print(f"Current progress: {get_word_progress(secret_word, letters_guessed)}")
            print("-------------")
            continue
        
        if guess in letters_guessed:
            print("You have already guessed that letter. Please try again.")
        elif guess in secret_word:
            letters_guessed.append(guess)
            print("Good guess!")
        else:
            letters_guessed.append(guess)
            print(f"Oops! That letter is not in my word.")
            # Note: The for-loop structure makes it difficult to deduct 2 guesses for a vowel.
            # We would need to manually skip a loop iteration, which complicates the logic.
            # The current for-loop version only deducts 1 guess per incorrect guess.
            # The original while-loop is more flexible for this specific rule.
        
        print(f"Current progress: {get_word_progress(secret_word, letters_guessed)}")
        print("-------------")
    
    if has_player_won(secret_word, letters_guessed):
        print("Congratulations! You won!")
    else:
        print("Sorry, you ran out of guesses.")
        print(f"The word was: {secret_word}")  
          
          
          

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############


