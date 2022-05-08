from random import choice
from blessed import Terminal
import re
import sys

TERM = Terminal()

MISPLACED = TERM.yellow3 #Yellow to show the letter is correct but misplaced
INCORRECT = TERM.grey65 #Grey to show the letter is not in the solution
CORRECT = TERM.green2 #Green to show the letter is in the correct position
VIOLET = TERM.violetred4 #Violet color for player name

class Wordle:
    """A program that takes in a user inputs to try to guess a 6 letters word
    6 tries
    
    Attributes:
        name (str): Name of player
        guesses (list of str): lists holding the player's guesses
        actual_word (str): word that is trying to be guessed
        wordList (list of str): List of words with 6 letters
    """
        
    def __init__(self, name, filepath):
        """ This initilizes a new Wordle object
        
        Args:
            name (str): players name
            filepath (str): string containing the file path to a wordlist
            
        Side effects:
            Initilizies the name attribute
            Inititalizes the guesses attribute 
            Initilizies the actual_word attribute
            Initializes the wordList attribute"""
            
        self.name = name
        self.guesses = list()
        expr = r"\b^[a-z]{6}\b"
        with open(filepath, "r", encoding="utf-8") as f:
            self.wordList = [line.strip().upper() for line in f if re.search(expr, line)]
        self.actual_word = choice(self.wordList)
    
    def turn(self):
        """Simulates a players attempt at guessing the word the Wordle game
        is thinking of
        
        Returns:
            str: Players guess
        
        Raises:
            ValueError: If user enters a word that does not exist in the list
            
        Side effects:
            Appends a user's guess to the self.guesses list
        """ 
        guess = input()
        if guess in self.wordList: 
            self.guesses.append(guess)
            return guess
        else:
            raise ValueError("This is not a valid word")  

    
    def match(self, guess):
        """Matches a users guess to the word the game is thinking of
    
        Args:
            guess (str): A user's guess
            
        Side effects:
            Prints information to the terminal
            
        """      
        freq = {i : [self.actual_word.count(i), {pos for pos, char in enumerate(self.actual_word) if char == i}] for i in set(self.actual_word)}
        guess_freq = {i : [guess.count(i), {pos for pos, char in enumerate(guess) if char == i}] for i in set(guess)}
        for x in range(len(guess)):
            char = guess[x]
            # guessed character not found in targeted word
            if char not in freq.keys():
                print (INCORRECT(guess[x]), end=" ")
            # if the guess correctly guess all index of the targeted word
            elif len(set(freq[char][1].intersection(guess_freq[char][1]))) == freq[char][0]:
                # if this index is one of the correct index then print green
                if x in freq[char][1]:
                    print (CORRECT(guess[x]), end=" ")
                # else not one of the correct index, print grey
                else:
                    print (INCORRECT(guess[x]), end=" ")
            # if there are more instances in targeted word than guess   
            elif freq[char][0] > guess_freq[char][0]:
                if x in freq[char][1]:
                    print (CORRECT(guess[x]), end=" ")
                # else not one of the correct index, print grey
                else:
                    print (MISPLACED(guess[x]), end=" ")
                
            # if there are more instances in guess than targeted word
            elif guess_freq[char][0] > freq[char][0]:
                if x in freq[char][1]:
                    print (CORRECT(guess[x]), end=" ")
                    freq[char][0] -= 1
                # else not one of the correct index, print grey
                elif freq[char][0] > 0:
                    print (MISPLACED(guess[x]), end=" ")
                    freq[char][0] -= 1
                # extra instances
                else:
                    print (INCORRECT(guess[x]), end=" ")
            elif char == self.actual_word[x]:
                print (CORRECT(guess[x]), end=" ")
            else:
                print (MISPLACED(guess[x]), end=" ") 
        print()      

        
    
    def play(self):
        """ Simulates a full Wordle Game
        
        Side Effects:
            Prints information to the terminal
            
        """
        with TERM.fullscreen():
            self.printboard()
            for x in range (0,6):
                while True:
                    try:
                        self.match(self.turn())
                        self.printboard()
                    except ValueError:
                        print(TERM.red("Not a valid word"))
                    else:
                        break
                if self.gameover():
                    self.win_lose("score.txt")
                    if not self.replay():
                        sys.exit(0)
        #the next two lines get the users first guess and match it        
        #check to see if the game is over
        
    
    def gameover(self):
        """ Determines whether or not the game is over
        
        Returns:
            Bool: True if the game is over, false if it is not
        
        """  
        if self.actual_word != self.guesses[-1]:
            if len(self.guesses) >= 6:
                return True
            else: 
                return False
        else: 
            return True            
        
    def printboard(self):
        """ Displays the current contents of the board
        
        Side effects:
            Prints information to the terminal
        
        """
        print(TERM.clear)
        print(VIOLET(f"{self.name}"))
        print(self.actual_word)
        for guess in self.guesses:
            self.match(guess)
        print()
        print(TERM.white(TERM.center('A,B,C,D,E,F,G,H,I,J,K')))
        print(TERM.white(TERM.center('L,M,N,O,P,Q,R,S,T,U,V')))
        print(TERM.white(TERM.center('W,X,Y,Z')))
        
    
    def win_lose(self, filepath):
        """Determines what happens if the player wins or loses

        Args:
            filepath (str): String containing file path to scores
            
        Side effects:
            Adds a players score to score.txt
            Prints information to the terminal
        """
        if self.actual_word == self.guesses[-1]:
            print(TERM.home + TERM.move_y(TERM.height // 2))
            print(TERM.black_on_darkkhaki(TERM.center('You WIN!')))
            score = ("1st" if len(self.guesses) == 1 else
                     "2nd" if len(self.guesses) == 2 else
                     "3rd" if len(self.guesses) == 3 else
                     "4th" if len(self.guesses) == 4 else
                     "5th" if len(self.guesses) == 5 else
                     "6th")
            print (TERM.black_on_white(TERM.center(f"You won on the {score} try")))
            with open(filepath, "a+", encoding="utf-8") as f:
                f.seek(0)
                lines = [line.strip() for line in f.readlines()]
                f.write("Attempt " + str(len(lines) + 1) +": " + str(len(self.guesses)) + "/6" + "\n")       
        else:
            print(TERM.black_on_darkkhaki(TERM.center('You Lose! The Correct Word Was: ' + self.actual_word)))
            
    def replay(self):
        """ Asks user if they want to play again
        
        Returns:
            Bool: True if the user wants to keep playing, false if otherwise 
            
        Side effects:
            Prints information to the terminal
        """
        print()
        while True:
            response = (input("Play Again: (y/n)? "))
            if response not in "yn":
                print("Invalid. Type 'y' or 'n'.")
                continue
            return response == "y"

def main():
    player = Wordle("Chigozie","wordlist.txt")
    player.play()

  

                       
if __name__ == "__main__": 
    main()
