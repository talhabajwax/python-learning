from random import randint
def numberGuess():
    
    number=randint(1,10)
    while True:
        try:
          guess=int(input("Guess a number between 1 and 10: "))
        except ValueError:
          print("Invalid input. Please enter a number.")
          continue
    
    
        if guess<number:
            print("Too low! Try again.")
            continue
        if guess>number:
            print("Too high! Try again.")
            continue
        elif guess==number:
            print("Congratulations! You guessed the number.")
            break
        
numberGuess()        
            
            