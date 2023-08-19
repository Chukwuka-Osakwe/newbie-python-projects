# This project was done maybe 14 days into my Python journey. Can't quite remember but it was pretty early
# It's a game based off the Monty Hall Problem (for more info about that: https://en.wikipedia.org/wiki/Monty_Hall_problem)



#Importing libraries
import random, os, time

# Welcome message, a lil fancy maybe, it's a game after all
print("\033[31m" + "WELCOME." + "\033[0m")
print()
time.sleep(2)
print("\033[32m" + "THERE ARE 3 DOORS IN THIS GAME, BEHIND EACH ONE LIES SOMETHING." + "\033[0m")
print()
time.sleep(2)
print("\033[33m" + "BEHIND 2 DOORS THERE ARE GOATS, AND BEHIND ONE DOOR, A MAGIC JEWEL." + "\033[0m")
time.sleep(10)
os.system("clear")
print("\033[34m" + "YOUR CHALLENGE, SHOULD YOU CHOOSE TO ACCEPT IT, IS TO SEE HOW MANY TIMES YOU PICK THE DOOR WITH THE JEWEL BEHIND IT." + "\033[0m")
print()
time.sleep(2)
print("\033[35m" + "GOODLUCK!" + "\033[0m")
time.sleep(10)
os.system("clear")

# Initialising counters
# One counter will keep track of the number of times user has played, the other for the number of times they won
counter = 0
counter1 = 1

# Firing up the while loop
while True:
  # I'm going to set the values of the 3 doors, then shuffle them and reassignn them at random
  Door1 = "goat" 
  Door2 = "goat"
  Door3 = "jewel"
  values = [Door1, Door2, Door3]
  random.shuffle(values)
  Door1, Door2, Door3 = values
  # Now I ask the user to pick a door
  UserChoice1 = input("There are three doors, 1, 2, and 3. Choose one: ")
  print() 

  # Everything beyond this point is what happens when a user picks a door
  # No matter the door they pick, I use an if statement to check which other door corresponds to "goat"
  # Then I show them that door and ask if they want to switch
  # Rinse and repeat for all possible choices

  # For example, if they pick Door 1 and Door 2 == goat, this runs
  if UserChoice1 == "1" and Door2 == "goat":
    os.system("clear")
    print("Before we open your door, here's a peek behind another door.")
    time.sleep(1)
    print()
    print("\033[31m" + "THERE IS A GOAT BEHIND DOOR 2" + "\033[0m")
    print()
    print("Now, before we open your door, do you want to switch doors?")
    print()
    UserChoice2 = input("Yes or No?: ")
    if UserChoice2 == "Yes" or UserChoice2 == "yes":
      os.system("clear")
      print("Alright then, you've chosen Door 3. There is a", Door3, "behind your door.")
      print()
      UserContinue = input("Would you like to keep playing?: ")
      if UserContinue == "Yes" or UserContinue == "yes":
        if Door3 == "jewel":
          counter+=1
          counter1+=1
          os.system("clear")
          continue
        else:
          counter1+=1
          os.system("clear")
          continue
      elif UserContinue == "No" or UserContinue == "no":
        if Door3 == "jewel":
          counter+=1
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")
          break
        else:
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")
          break
      else:
        print("we're sorry, something went wrong unexpectedly, please start again.")
        break
    elif UserChoice2 == "No" or UserChoice2 == "no":
      os.system("clear")
      print("Brave of you sticking with your first choice, there is a", Door1, "behind your door.")
      print()
      UserContinue = input("Would you like to keep playing?: ")
      if UserContinue == "Yes" or UserContinue == "yes":
        if Door1 == "jewel":
          counter+=1
          counter1+=1
          os.system("clear")
          continue
        else:
          counter1+=1
          os.system("clear")
          continue
      elif UserContinue == "No" or UserContinue == "no":
        if Door1 == "jewel":
          counter+=1
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")        
          break
        else:
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")
          break
      else:
        print("we're sorry, something went wrong unexpectedly, please start again.")
        break
    else:
      print("we're sorry, something went wrong unexpectedly, please start again.")        

  

  # But if they pick Door 1 and it's a goat, but Door 2 is the jewel, what then? Well, this runs, because Door 3 == goat then
  elif UserChoice1 == "1" and Door3 == "goat":
    os.system("clear")
    print("Before we open your door, here is a peek behind one of the other doors.")
    time.sleep(1)
    print()
    print("\033[31m" + "THERE IS A GOAT BEHIND DOOR 3" + "\033[0m")
    print()
    print("Now, before we open your door, would you like to switch doors?")
    print()
    UserChoice2 = input("Yes or No?: ")
    if UserChoice2 == "Yes" or UserChoice2 == "yes":
      os.system("clear")
      print("Alright then, you've switched to Door 2, there is a", Door2, "behind your door!")
      print()
      UserContinue = input("Would you like to keep playing?: ")
      if UserContinue == "Yes" or UserContinue == "yes":
        if Door2 == "jewel":
          counter+=1
          counter1+=1
          os.system("clear")
          continue
        else:
          counter1+=1
          os.system("clear")
          continue
      elif UserContinue == "No" or UserContinue == "no":
        if Door2 == "jewel":
          counter+=1
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")        
          break
        else:
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")        
          break          
    elif UserChoice2 == "No" or UserChoice2 == "no":
      os.system("clear")
      print("Brave choice sticking with your original choice, there is a", Door1, "behind that door!")
      print()
      UserContinue = input("Would you like to keep playing?: ")
      if UserContinue == "Yes" or UserContinue == "yes":
        if Door1 == "jewel":
          counter+=1
          counter1+=1
          os.system("clear")
          continue
        else:
          counter1+=1
          os.system("clear")
          continue
      elif UserContinue == "No" or UserContinue == "no":
        if Door1 == "jewel":
          counter+=1
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")        
          break
        else:
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")
          break
      else:
        print("we're sorry, something went wrong unexpectedly, please start again.")
        break
    else:
      print("we're sorry, something went wrong unexpectedly, please start again.")



  elif UserChoice1 == "2" and Door1 == "goat":
    os.system("clear")
    print("Before we open your door, here's a peek behind another door.")
    time.sleep(1)
    print()
    print("\033[31m" + "THERE IS A GOAT BEHIND DOOR 1" + "\033[0m")
    print()
    print("Now, before we open your door, do you want to switch doors?")
    print()
    UserChoice2 = input("Yes or No?: ")
    if UserChoice2 == "Yes" or UserChoice2 == "yes":
      os.system("clear")
      print("Alright then, you've chosen Door 3. There is a", Door3, "behind your door.")
      print()
      UserContinue = input("Would you like to keep playing?: ")
      if UserContinue == "Yes" or UserContinue == "yes":
        if Door3 == "jewel":
          counter+=1
          counter1+=1
          os.system("clear")
          continue
        else:
          counter1+=1
          os.system("clear")
          continue
      elif UserContinue == "No" or UserContinue == "no":
        if Door3 == "jewel":
          counter+=1
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")
          break
        else:
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")
          break
      else:
        print("we're sorry, something went wrong unexpectedly, please start again.")
        break
    elif UserChoice2 == "No" or UserChoice2 == "no":
      os.system("clear")
      print("Brave of you sticking with your first choice, there is a", Door2, "behind your door.")
      print()
      UserContinue = input("Would you like to keep playing?: ")
      if UserContinue == "Yes" or UserContinue == "yes":
        if Door2 == "jewel":
          counter+=1
          counter1+=1
          os.system("clear")
          continue
        else:
          counter1+=1
          os.system("clear")
          continue
      elif UserContinue == "No" or UserContinue == "no":
        if Door2 == "jewel":
          counter+=1
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")        
          break
        else:
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")
          break
      else:
        print("we're sorry, something went wrong unexpectedly, please start again.")
        break
    else:
      print("we're sorry, something went wrong unexpectedly, please start again.")



  elif UserChoice1 == "2" and Door3 == "goat":
    os.system("clear")
    print("Before we open your door, here's a peek behind another door.")
    time.sleep(1)
    print()
    print("\033[31m" + "THERE IS A GOAT BEHIND DOOR 3" + "\033[0m")
    print()
    print("Now, before we open your door, do you want to switch doors?")
    print()
    UserChoice2 = input("Yes or No?: ")
    if UserChoice2 == "Yes" or UserChoice2 == "yes":
      os.system("clear")
      print("Alright then, you've chosen Door 1. There is a", Door1, "behind your door.")
      print()
      UserContinue = input("Would you like to keep playing?: ")
      if UserContinue == "Yes" or UserContinue == "yes":
        if Door1 == "jewel":
          counter+=1
          counter1+=1
          os.system("clear")
          continue
        else:
          counter1+=1
          os.system("clear")
          continue
      elif UserContinue == "No" or UserContinue == "no":
        if Door1 == "jewel":
          counter+=1
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")
          break
        else:
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")
          break
      else:
        print("we're sorry, something went wrong unexpectedly, please start again.")
        break
    elif UserChoice2 == "No" or UserChoice2 == "no":
      os.system("clear")
      print("Brave of you sticking with your first choice, there is a", Door2, "behind your door.")
      print()
      UserContinue = input("Would you like to keep playing?: ")
      if UserContinue == "Yes" or UserContinue == "yes":
        if Door2 == "jewel":
          counter+=1
          counter1+=1
          os.system("clear")
          continue
        else:
          counter1+=1
          os.system("clear")
          continue
      elif UserContinue == "No" or UserContinue == "no":
        if Door2 == "jewel":
          counter+=1
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")        
          break
        else:
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")
          break
      else:
        print("we're sorry, something went wrong unexpectedly, please start again.")
        break
    else:
      print("we're sorry, something went wrong unexpectedly, please start again.")



  elif UserChoice1 == "3" and Door1 == "goat":
    os.system("clear")
    print("Before we open your door, here's a peek behind another door.")
    time.sleep(1)
    print()
    print("\033[31m" + "THERE IS A GOAT BEHIND DOOR 1" + "\033[0m")
    print()
    print("Now, before we open your door, do you want to switch doors?")
    print()
    UserChoice2 = input("Yes or No?: ")
    if UserChoice2 == "Yes" or UserChoice2 == "yes":
      os.system("clear")
      print("Alright then, you've chosen Door 2. There is a", Door2, "behind your door.")
      print()
      UserContinue = input("Would you like to keep playing?: ")
      if UserContinue == "Yes" or UserContinue == "yes":
        if Door2 == "jewel":
          counter+=1
          counter1+=1
          os.system("clear")
          continue
        else:
          counter1+=1
          os.system("clear")
          continue
      elif UserContinue == "No" or UserContinue == "no":
        if Door2 == "jewel":
          counter+=1
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")
          break
        else:
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")
          break
      else:
        print("we're sorry, something went wrong unexpectedly, please start again.")
        break
    elif UserChoice2 == "No" or UserChoice2 == "no":
      os.system("clear")
      print("Brave of you sticking with your first choice, there is a", Door3, "behind your door.")
      print()
      UserContinue = input("Would you like to keep playing?: ")
      if UserContinue == "Yes" or UserContinue == "yes":
        if Door3 == "jewel":
          counter+=1
          counter1+=1
          os.system("clear")
          continue
        else:
          counter1+=1
          os.system("clear")
          continue
      elif UserContinue == "No" or UserContinue == "no":
        if Door3 == "jewel":
          counter+=1
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")        
          break
        else:
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")
          break
      else:
        print("we're sorry, something went wrong unexpectedly, please start again.")
        break
    else:
      print("we're sorry, something went wrong unexpectedly, please start again.")



  elif UserChoice1 == "3" and Door2 == "goat":
    os.system("clear")
    print("Before we open your door, here's a peek behind another door.")
    time.sleep(1)
    print()
    print("\033[31m" + "THERE IS A GOAT BEHIND DOOR 2" + "\033[0m")
    print()
    print("Now, before we open your door, do you want to switch doors?")
    print()
    UserChoice2 = input("Yes or No?: ")
    if UserChoice2 == "Yes" or UserChoice2 == "yes":
      os.system("clear")
      print("Alright then, you've chosen Door 1. There is a", Door1, "behind your door.")
      print()
      UserContinue = input("Would you like to keep playing?: ")
      if UserContinue == "Yes" or UserContinue == "yes":
        if Door1 == "jewel":
          counter+=1
          counter1+=1
          os.system("clear")
          continue
        else:
          counter1+=1
          os.system("clear")
          continue
      elif UserContinue == "No" or UserContinue == "no":
        if Door1 == "jewel":
          counter+=1
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")
          break
        else:
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")
          break
      else:
        print("we're sorry, something went wrong unexpectedly, please start again.")
        break
    elif UserChoice2 == "No" or UserChoice2 == "no":
      os.system("clear")
      print("Brave of you sticking with your first choice, there is a", Door3, "behind your door.")
      print()
      UserContinue = input("Would you like to keep playing?: ")
      if UserContinue == "Yes" or UserContinue == "yes":
        if Door3 == "jewel":
          counter+=1
          counter1+=1
          os.system("clear")
          continue
        else:
          counter1+=1
          os.system("clear")
          continue
      elif UserContinue == "No" or UserContinue == "no":
        if Door3 == "jewel":
          counter+=1
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")        
          break
        else:
          os.system("clear")
          print("WE'RE SORRY TO SEE YOU GO. COME BACK SOON")
          print()
          print("\033[33m" + "YOU PLAYED " + str(counter1) + " TIMES " + "AND WON " + str(counter) + " TIMES" + "\033[0m")
          break
      else:
        print("we're sorry, something went wrong unexpectedly, please start again.")
        break
    else:
      print("we're sorry, something went wrong unexpectedly, please start again.")