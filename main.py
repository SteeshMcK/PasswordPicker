"""
This program:
1. Asks the user how many passwords they 
   would like generated for them.
2. Chooses one word randomly, from 3 different 
   arrays, as well as a number between 0 and 100
   and a special character.
3. Strings words and number together.
3. Repeats to satisfy user input.
4. Prints concatenated string to run field.
5. Asks user if they would like to create more passwords.
6. If the user types 'y', condition remains 'true' and 
   password producing operation repeats.
7. If user types 'n', condition changes to 'false',
   and there is a break in the program, ending it.
Coded by Stesha McKindle
Last updated 9/09/20
"""

import random
import string

adjectives = ['attractive', 'agreeable', 'angry', 'big', 'flabby', 'kind', 'lazy', 'microscopic', 'skinny', 'witty', 'scary', 'tall', 'jolly', 'zealous', 'gentle']

colors = ['Cotton', 'Sand', 'Banana', 'Cantaloupe', 'Garnet', 'Rouge', 'Violet', 'Cerulean', 'Pine', 'Hickory', 'Dove', 'Fog', 'Flint', 'Raven', 'Spider']

nouns = ['People', 'History', 'Way', 'Art', 'World', 'Youth', 'Uncle', 'Trainer', 'Throat', 'Tale', 'Love', 'Internet', 'Television', 'Science', 'Library', 'Bookstand']

print("Welcome to the Password Picker!")

howMany = int(input("How many passwords would you like? "))

while True:
  for num in range(howMany):
    #Use choice() from the random module to make a random choice from the two arrays
    adjective = random.choice(adjectives)
    color = random.choice(colors)
    noun = random.choice(nouns)

    #Use randrange() from random module to choose a random number within the range given
    number = random.randrange(0, 100)

    #string.punctuation is a constant variable
    #It holds a string of punctuation characters
    special_char = random.choice(string.punctuation)

    password = adjective + color + noun + str(number) + special_char
    print("Your new password is: "  + password)

  response = input("Would you me to create more passwords? Type y or n: ")
  if response.lower() == 'n':
    break

