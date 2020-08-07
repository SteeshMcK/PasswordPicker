import random
import string

adjectives = ['attractive', 'agreeable', 'angry', 'big', 'flabby', 'kind', 'lazy', 'microscopic', 'skinny', 'witty', 'scary', 'tall', 'jolly', 'zealous', 'gentle']

nouns = ['People', 'History', 'Way', 'Art', 'World', 'Youth', 'Uncle', 'Trainer', 'Throat', 'Tale', 'Love', 'Internet', 'Television', 'Science', 'Library']

print("Welcome to the Password Picker!")

while True:
  #Use choice() from the random module to make a random choice from the two arrays
  adjective = random.choice(adjectives)
  noun = random.choice(nouns)

  #Use randrange() from random module to choose a random number within the range given
  number = random.randrange(0, 100)

  #string.punctuation is a constant variable
  #It holds a string of punctuation characters
  special_char = random.choice(string.punctuation)

  password = adjective + noun + str(number) + special_char
  print("Your new password is: "  + password)

  response = input("Would you me to create another password? Type y or n: ")
  if response.lower() == 'n':
    break