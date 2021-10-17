# https://www.youtube.com/watch?v=KzqSDvzOFNA&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=27&ab_channel=CoreySchafer

import random

# returns a number between 0 and 1, example: 0.10781027820424316
value = random.random()

# if we want a floating point value between 1 and 10, example: 6.459325954342391
value = random.uniform(1, 10)

# random integer between 1 and 6 (includes both values)
value = random.randint(1, 6)

# suppose we want to get a random value out of a list
greetins = ["hello", "howdy", "wassup", "hola", "hallo"]
value = random.choice(greetins)

# if we want more than one choice, in this case we asked for two. A value could be picked more than once.
colors = ["red", "blue", "green", "black", "white", "pink", "yellow"]
results = random.choices(colors, k=3)

# if we want to give more weight to each option, that is define a probability
# the chance is the value of the choice out of the sum of all choices. 
# in this case, the green has a probability of 2 out of 30
colors = ["red", "blue", "green"]
results = random.choices(colors, weights=[18, 10, 2], k=3)

# let's create a deck of cards, the range will return us 52 number
deck = list(range(1, 53))

# now let's shuffle the order of the items in the list
random.shuffle(deck)

# if we to get a random sample out of a list
# that is, to get an x amount of random non-repeatable (that is, unique) items
deck = list(range(1, 53))
hand = random.sample(deck, k=3)

print(hand)