import random

ComputerNumber = random.randint(1,100)
guesses = 0
MaxGuesses = 7
Win = False
Play = True


while MaxGuesses > 0:
    print()
    playerNumber = (input("Guess my Number (between 1 and 100):  "))

    guesses += 1
    if playerNumber.isdigit():
      playerNumber = int(playerNumber)
      if playerNumber < 0 or playerNumber > 100:
        print("Bad number")
      if  playerNumber < ComputerNumber:
          print("Too low")
          MaxGuesses -= 1
          print("You have {} guesses left." .format(MaxGuesses))
      if playerNumber > ComputerNumber:
          print("Too high")
          MaxGuesses -= 1
          print("You have {} guesses left." .format  (MaxGuesses))
          print(ComputerNumber)
      if playerNumber == ComputerNumber:
          Win = True
          break
    else:
      print("please enter a number! ")


if Win == True:
  print("Congrats!  You won! It took you {} guesses to win!".format(guesses)) 
else:
  print("game over. No more tries.")
  print("the number was {}.".format(ComputerNumber))
