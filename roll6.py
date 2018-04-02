## Roll 6
## Rolls a 6-sided die to produce the numbers 1-10 as possible outputs
## with equal probability
## Afton Coombs
## aftoncoombs@gmail.com
import random

def roll6():
    firstRoll = random.randint(1, 6)
    while (firstRoll > 5):
        firstRoll = random.randint(1, 6)
    secondRoll = random.randint(1, 6)
    finalRoll = firstRoll * 2 - secondRoll % 2
    return finalRoll
