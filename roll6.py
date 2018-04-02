## Roll 6
## Rolls a 6-sided die to produce the numbers 1-10 as possible outputs
## with equal probability
## Afton Coombs
## aftoncoombs@gmail.com
import random

def roll6():
    ## Map from 6 sides to 10 possibilities
    ## Since 6 must be multiplied by 2 to get an number >= 10,
    ## a second roll will use the value 2 to map from 6 to 10. 
    firstRoll = random.randint(1, 6)
    ## Don't allow potential rolls greater than 10
    while (firstRoll > 5):
        firstRoll = random.randint(1, 6)
    secondRoll = random.randint(1, 6)
    finalRoll = firstRoll * 2 - secondRoll % 2
    return finalRoll
