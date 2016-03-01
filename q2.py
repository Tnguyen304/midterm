# This is a very simple game of sticks. There are 21 sticks, first the user picks number of sticks between 1-4, then the computer picks sticks(1-4). Who ever will pick the last stick will lose.
# Look for the TODO blocks as an indication of when you have to add your own code.

import random
sticks = 21

def playGame():
    # you do not need to modify code in this function
    print('There are 21 sticks. You can pick from 1 to 4 sticks at a time, and the computer will then pick from 1 to 4 sticks at a time. Whoever picks the last stick loses!')
    while True:
        print('Current sticks: ' + str(sticks))
        userChoice = askUserChoice()
        if subtractSticks( userChoice ):
            print('You lost!')
            break
        
        computerChoice = determineComputerChoice()
        print('Computer picked: ' + str(computerChoice) )
        if subtractSticks( computerChoice ):
            print('Computer lost!')
            break
        

def askUserChoice():
    userChoice = int(input('Please input a value between 1 and 4:'))
    while userChoice < 1 or userChoice > 4:
        print('This is not between 1 and 4!')
        userChoice = int(input('Please input a value between 1 and 4:'))
        print(userChoice)

    return userChoice



def subtractSticks( number ):
    global sticks 
    sticks = sticks - number
    if sticks > 0:
        return False
    elif sticks <= 0:
        return True
    
def determineComputerChoice():
    computerChoice = random.randint(1,4)
    return computerChoice

