# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <Chandler Lawrence>
# Creation Date: <02 December 2021>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time
#Below, the intro is missing a couple words for cohesive purposes of language
def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. In the other cave, the other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
#Below it should say return cave not caves          
    return cave


#The parameter passed into the checkCave function should be chooseCave not chosenCave
def checkCave(chooseCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)
    
    friendlyCave = random.randint(1, 2)
 #Instead of the str it should be int for variable type below
 #ChosenCave should be chooseCave below
    if chooseCave == int(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')
        
playAgain = 'yes'
#Instead of = it should be == for consistency of the operators
while playAgain == 'yes' or playAgain == 'y':
    
    displayIntro()
 #The function assigned to the caveNumber variable is supposed to be chooseCave not choosecave   
    caveNumber = chooseCave()
    
    checkCave(caveNumber)

    
    print('Do you want to play again? (yes or no)')
    playAgain = input()
    if playAgain == "no":
#Corrected the spelling of the word playing below
        print("Thanks for playing")
