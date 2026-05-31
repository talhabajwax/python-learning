from random import choice
def toss():
    choose = input ("Do you want to swing a Toss")
    if choose not in ("yes","no"):
        print ("Please choose y or n")
        return
    if choose in ('yes'):
        print ("Swinging the Toss")
        swing = ("Heads","tails")
        swing2 = input ("Please choose Heads or Tails")
        toSs = choice(swing)
        if swing2 == toSs:
            print ("You win")
        else:
            print (f"You lose the toss, it was {toSs}")
    else:
            print ("Maybe next time")
            return
        
  
toss()
    