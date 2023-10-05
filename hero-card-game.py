'''
I think I made this because I was trying to wrap my head around using dictionaries in Python. Anyway it's a little fun game. Pick a character, pick an atrribute, the computer picks a character at random and compares the value of the attribute you've picked for both characters. Larger number wins, simple. 

You can also add characters and give them custom attributes if you want. Enjoy.
'''

import random

print(f"🌟Top Trumps🌟 \n")

# Gots to add some explanations of how this game works amafrade
# Dictionary = {name: {speed, strength, special ability}}
charDict = {'Jonn': {'Speed': 70, 'Strength': 78, 'Special': 49}, 'Flash': {'Speed': 400, 'Strength': 34, 'Special': 344}, 'Batman': {'Speed': 20, 'Strength': 200, 'Special': 30}}



def addCharacter():
  '''
  This is a simple function call to add a new user-generated character to the  dictionary.
  '''
  charName = input("\nWhat's the character's name? > ")
  charName = charName.strip().capitalize()
  charSpeed = int(input("How quick is your character? > "))
  charStrength = int(input("How strong is this character? > "))
  charSpecial = int(input("What's the character's special ability? > "))
  print()

  charDict[charName] = {'Speed': charSpeed, 'Strength': charStrength, 'Special': charSpecial}



def randomCharacter():
  '''
  This function generates a random character for the computer to play with. All the dictionary's keys (the character names) are put into a list at random. Then one name is picked at random from the list by using the random library to generate a random number between index 0 and the length of the list.
  '''
  values = []
  for key, value in charDict.items():
    values.append(key)
  listLength = len(values)
  listLength-=1
  random.shuffle(values)
  x = random.randint(0, listLength)
  computerValue = values[x]
  return computerValue



def playGame():
  '''
  This is where the magic happens. User picks a character and an attribute and then the program shows the value of that attribute for the user's character and the computer's character and compares the value of their attributes to determine a winner.
  '''
  print("\nPick a character:")
  for key, value in charDict.items():
    print(f"- {key}")
  userChoice = input("> ")
  userChoice = userChoice.strip().capitalize()

  userAttribute = input("\nOkay, now pick an attribute: \n- Speed\n- Strength\n- Special\n> ")
  userAttribute = userAttribute.strip().capitalize()

  print(f"\n{userChoice} has a {userAttribute} of {charDict[userChoice][userAttribute]}")

  # And now for the random selection by Computer
  computerChoice = randomCharacter()
  print(f"{computerChoice} has a {userAttribute} of {charDict[computerChoice][userAttribute]}")

  print()
  if charDict[userChoice][userAttribute] > charDict[computerChoice][userAttribute]:
    print(f"{userChoice} wins this round!")
  elif charDict[userChoice][userAttribute] < charDict[computerChoice][userAttribute]:
    print(f"{computerChoice} wins this round!")
  else:
    print("It's a tie fellas.")




while True:
  userCharacter = input("Would you like to add a character? y/n > ")
  userCharacter = userCharacter.strip().lower()

  if userCharacter == 'y':
    addCharacter()
    playGame()

    userContinue = input("\nWould you like to keep going? y/n > ")
    userContinue = userContinue.strip().lower()
    if userContinue == 'y':
      continue
    elif userContinue == 'n':
      print("\nCome back again and play soon!")
      break    

  elif userCharacter == 'n':
    playGame()

    userContinue = input("\nWould you like to keep going? y/n > ")
    userContinue = userContinue.strip().lower()
    if userContinue == 'y':
      continue
    elif userContinue == 'n':
      print("\nCome back again and play soon!")
      break