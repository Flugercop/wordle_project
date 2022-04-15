"This is a wordle game"

class Player:
    """Instantiates a player"""
    
    def __init__(self, name):
        
    def turn(self, state):
        

class Wordle:
    """A program that takes in a user inputs to try to guess a 6 letters word
    6 tries
    
    """
        
    def __init__(self, name, wordlist):
    
        
    def guess(self, guess):
        """There will be a guess function that takes in a user’s guess 
        and then based on that it outputs a colored answer using “from blessed”.
        Use for blessed to give letters colors example: if a letter is in the 
        correct spot, it will be green if it is a correct letter but not in the 
        right spot it will be yellow, if the letter is not in the solution, 
        then it will grey out. 
        
        Raises:
            ValueError: If user enters a word that does not exist in the list
            
        Side effects:
            Prints out whether or not player has guessed a correct letter in the
            word
        """
            
class WordleState:
    """Provides information on the current state of the worlde game
    
    Attributes:
        max_tries (int): Max amount of attempts
        bad_guesses(set of characters): set containing characters not in the word
        good_guesses(set of characetrs): set containing characters that are in
        the word
        length(int, 7): Length of word
        letters_guessed(set of characters): set containing the amount of letters guessed
        
        
    """
    def __init__(self, word, guesses):
        