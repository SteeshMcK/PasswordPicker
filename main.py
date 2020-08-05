import random
import string

adjectives = ['attractive', 'agreeable', 'angry', 'big', 'flabby', 'kind', 'lazy', 'microscopic', 'skinny', 'witty', 'scary', 'tall', 'jolly', 'zealous', 'gentle']

nouns = ['people', 'history', 'way', 'art', 'world', 'youth', 'uncle', 'trainer', 'throat', 'tale', 'love', 'internet', 'television', 'science', 'library']

print("Welcome to the Password Picker!")

#Use choice() from the random module to make a random choice from the two arrays
adjective = random.choice(adjectives)
noun = random.choice(nouns)