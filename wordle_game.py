"This is a wordle game"

import random as choice
import pandas as pd
from blessed import Terminal
import re
import sys
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
        self.wordList = list()
        expr = r"\b^[a-z]{6}\b"
        with open(filepath, "r", encoding="utf-8") as f:
            wordList = [line.strip() for line in f if re.search(expr, line)]
        self.actual_word = choice(wordList) 
        
    def turn(self):
        """Simulates a players attempt at guessing the word the Wordle game
        is thinking of
        
        Returns:
            str: Players guess
        
        Raises:
            ValueError: If user enters a word that does not exist in the list
        """ 
        print("Guess a Letter")
        if guess in self.wordList: 
            guess = input()
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
        guess = self.turn()     
        for x in range(len(self.turn())):
            if guess[x] == self.actual_word[x]:
                print (CORRECT(guess[x]), end=" ")
            elif guess[x] in self.actual_word:
                print (MISPLACED(guess[x]), end=" ")
            else:
                print (INCORRECT(guess[x]), end=" ")
        
    
    def play(self):
        """
        
        Side Effects:
            Prints out current boards
        """
        for x in range (0,6):
            self.match()
            
    
    def gameover(self):
        # Have statistics for the game in this function (Avg guesses, etc)
        """ Displays the results to the players
        
        Returns:
            Bool: True if the game is over, false if it is not
        
        Side Effects:
            - Prints out whether or not the player guessed the word correctly
            - Will write out the number of tries it took a player to guess the 
            word correctly to a file and store it"""  
    
    def printboard(self):
        """
        
        """
        print(self.current_guess)

            
        
            
if __name__ == "__main__": 
