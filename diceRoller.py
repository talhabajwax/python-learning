from random import choice, randint
def diceRoller():
    print("Welcome to the Dice Roller!")
    print('Want to roll a die? (y/n)')
    userChoice = input()
    while userChoice.lower() == 'y':
        dice = [1, 2, 3, 4, 5, 6]
        length =1
        print("Rolling the die...")
        roll = ""
        for d in range(length) :
            roll += str(choice(dice)) + " "
        print("You rolled: " + roll)
        print('Roll again? (y/n)')
        userChoice = input()
    print("Thanks for playing!")
diceRoller()