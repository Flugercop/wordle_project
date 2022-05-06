"This is a wordle game"

from random import choice
import pandas as pd
from blessed import Terminal
import re
import sys
import os
# Doesn't check for one instance
# Random word gets chosen from wordlists
# Needs to be a way for the player to guess a word
# Needs to be a wordlist(file containing strings)
# needs utf-8 to read and store the strings from the file
# need to be able match the players guess to the chosen word
# Need to categorize each of the letters (match function)
# Keep track of how many guesses a person (max of 6) using a loop
# Game over for when all guesses have been exhuasted, prints out the word that the person got wrong
# If they didn't get it wrong, display a victory message showing how many tries it took the player guess the correct word
# Create a file of scores, and read in from that file and display it to the player

#Regex Expression for 6 letter words: \b^[a-z]{6}\b

TERM = Terminal()

MISPLACED = TERM.yellow3 #Yellow to show the letter is correct but misplaced
INCORRECT = TERM.grey65 #Grey to show the letter is not in the solution
CORRECT = TERM.green2 #Green to show the letter is in the correct position

class Wordle:
    """A program that takes in a user inputs to try to guess a 6 letters word
    6 tries
    
    Attributes:
        name (str): Name of player
        word (str): Random word
    """
        
    def __init__(self, name, filepath):
        """ This initilizes a new Wordle object
        
        Args:
            name (str): players name
            filepath (str): string containing the file path to a wordlist
            
        Side effects:
            Initilizies the name attribute
            Initilizies the word attribute"""
            
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
        """ 
        print("Guess a Word")
        guess = input()
        if guess in self.wordList: 
            self.guesses.append(guess)
            return guess
        else:
            raise ValueError("This is not a valid word")  

    
    def match(self, guess):
        """Matches a users guess to the word the game is thinking of
    
            
        Side effects:
            Prints out whether or not player has guessed a correct letter in the
            word
        """      
        for x in range(len(guess)):
            if guess[x] == self.actual_word[x]:
                print (CORRECT(guess[x]), end=" ")
            elif guess[x] in self.actual_word:
                print (MISPLACED(guess[x]), end=" ")
            else:
                print (INCORRECT(guess[x]), end=" ")
        print()
        
    
    def play(self):
        """
        
        Side Effects:
            Prints out current boards
        """
        with TERM.fullscreen():
            for x in range (0,6):
                while True:
                    try:
                        self.match(self.turn())
                        self.printboard()
                    except ValueError:
                        print("Not a valid word")
                    else:
                        break
                if self.gameover():
                    self.win_lose("score.txt")
                    if not self.replay():
                        sys.exit(0)
                    else:
                        print ("Thanks for Playing")
                    break
        #the next two lines get the users first guess and match it        
        #check to see if the game is over
        
    
    def gameover(self):
        """ Displays the results to the players
        
        Returns:
            Bool: True if the game is over, false if it is not
        
        Side Effects:
            - Prints out whether or not the player guessed the word correctly
            - Will write out the number of tries it took a player to guess the 
            word correctly to a file and store it"""  
    # checks if the users guess it not equal to the actual word
        if self.actual_word != self.guesses[-1]:
    # checking if the user reached the max guess count
            if len(self.guesses) >= 6:
                return True
            else: 
    # this means the user guessed the wrong word but still has turns remaining
                return False
        else: 
    #this means the user guessed the right word
            return True            
        
        #Have statistics for the game in this function (Avg guesses, etc)
        
    def printboard(self):
        """
        
        """
        print(TERM.clear)
        for guess in self.guesses:
            self.match(guess)
        print(TERM.black_on_white(TERM.center('A,B,C,D,E,F,G,H,I,J,K')))
        print(TERM.black_on_white(TERM.center('L,M,N,O,P,Q,R,S,T,U,V')))
        print(TERM.black_on_white(TERM.center('W,X,Y,Z')))
        
    
    def win_lose(self, filepath):
        if self.actual_word == self.guesses[-1]:
            print(TERM.home + TERM.move_y(TERM.height // 2))
            print(TERM.black_on_darkkhaki(TERM.center('You WIN!')))
            score = ("1st" if len(self.guesses) == 1 else
                     "2nd" if len(self.guesses) == 2 else
                     "3rd" if len(self.guesses) == 3 else
                     "4th" if len(self.guesses) == 4 else
                     "5th" if len(self.guesses) == 5 else
                     "6th")
            print (f"You won on the {score} try")
            with open(filepath, "a+", encoding="utf-8") as f:
                f.seek(0)
                lines = [line.strip() for line in f.readlines()]
                f.write("Attempt " + str(len(lines) + 1) +": " + str(len(self.guesses)) + "/6" + "\n")       
        else:
            print("You lose")
            
    def replay(self):
        print()
        while True:
            response = (input("Play Again: (y/n)? "))
            if response not in "yn":
                print("Please type 'y' or 'n'.")
                continue
            return response == "y"

def main():
    player = Wordle("Jonnie","wordlist.txt")
    print(player.actual_word)
    player.play()

  

            
        
            
if __name__ == "__main__": 
    main()
