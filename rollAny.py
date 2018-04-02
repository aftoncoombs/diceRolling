## Roll Any
## Rolls an n-sided die to produce the numbers 1-k as possible outputs
## with equal probability.
## This may require many rolls if k is exponentially larger than n.
## Afton Coombs
## aftoncoombs@gmail.com
import random
import math
    
def rollAny(n, k):
    ## n = number of die faces
    ## k = max of output numbers with equal probability
    if (n<2):
        print("No dice with side counts < 2. That doesn't make sense.")
        return(None)
    ## Get the dimensions of n required to produce k.
    ## This determines the number of times modTrick will need to
    ## be executed to map n back to k (possibly through many dimensions of n).
    j = k // n + int(k % n > 0)
    ## This is how a smaller number is mapped to a larger number.
    ## Calculate j, representing the number n would need to multipled by
    ## to produce a value >= k. That is how n will map to k.
    ## j is k/n if k/n is evenly divisible, and k/n + 1 else.
    ## If j is too big for n, first map from n to j instead of n to k.
    if j > n:
        j = rollAny(n, j)
    maxFirst = math.ceil(k / float(j))
    firstRoll = random.randint(1, n)
    ## Do not accept values that would potentialy yield a finalRoll > k
    while (firstRoll > maxFirst):
        firstRoll = random.randint(1, n)
    secondRoll = random.randint(1, n)
    finalRoll = firstRoll * j - secondRoll % j
    while (finalRoll > k):
        secondRoll = random.randint(1, n)
        finalRoll = firstRoll * j - secondRoll % j
    return finalRoll
