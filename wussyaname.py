# This project was done 36 days into my Python journey
# Import necessary libraries, initialise list
import os, time
listOfNames = []



def prettyPrint():
  '''
  This function prints out the list of names. The counter is initialised to 1 and used for ordering the list. A for loop is used to iterate over each item in the list (as well as incrementing the counter each time) and each one is printed out using f strings.
  '''
  counter = 1
  print("\33[35m" + "LIST OF NAMES" + "\33[0m")
  for name in listOfNames:
    print(f"{counter}. {name} \n")
    counter+=1
  time.sleep(3)
  os.system("clear")



while True:
  # Ask for first and last names, strip away whitespace and capitalize
  firstName = input("What's your first name?: ").strip().capitalize()
  print()
  lastName = input("What's your last name?: ").strip().capitalize()

  # Concatenate first and last name with an f string
  userName = f"{firstName} {lastName}"

  # Check if name already exists in the list of names, if it exists, tell user to proceed, if it doesn't, add it to the list.
  if userName not in listOfNames:
    listOfNames.append(userName)
    print()
    print(f"Welcome, {firstName} {lastName}, you're on the list now.")    
  else:
    print()
    print(f"{userName} is already on the list, please proceed.")

  # Clear screen, call pretty print function
  time.sleep(3)
  os.system("clear")  
  prettyPrint()



# Writing code is fun!!!!!!!
# Comments, not so much +_+