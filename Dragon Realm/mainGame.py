import time
import random
def showIntro():
    print('''
You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.
''')

def chooseCave():
    cave = 0
    while cave != 1 and cave != 2:
        print("Which cave will you go into? (1 or 2)")
        cave = int(input())
        if cave > 2 or cave == 0:
            print("Invalid choice!! Please try again")
    return  cave

def checkCave(choosenCave):
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)

    friendlyCave = random.randint(1,2)
    if choosenCave == friendlyCave:
        print("Gives you his treasure!")
    else:
        print("Gobbles you down in one bite!")

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    showIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print("Do you want to play again? (yes or any key...)")
    playAgain = input()