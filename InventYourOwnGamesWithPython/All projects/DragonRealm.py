import random
import time

def displayIntro():
    print('You are in a land full of dragons. Int front of you there are two caves. In one cave, the dragon is friendly and will share his treasure with you. the other dragon is greedy and hungry and will gobble you on sight.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approch the cave...')
    time.sleep(2)
    print('It is dark and spooky...') 
    time.sleep(2)
    print('A large dragon appears in front of you! He opens his jaws...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure! You are now rich! Lucky!')
    else:
        print('Gobbles you down in one bite! You are now dead! Unlucky!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

print('do you want to play again? (yes//no)')
playAgain = input()