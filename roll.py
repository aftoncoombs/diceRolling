## Roll
## Rolls an n-sided die to produce the numbers 1-k as possible outputs
## with equal probability.
## To do this in two rolls, as in this program, k must be <= n^2.
## Afton Coombs
## aftoncoombs@gmail.com
import random
    
def roll(n, k):
    ## n = number of die faces
    ## k = max of output numbers with equal probability
    if (k > n^2):
        print("k must be <= n^2")
        break
    j = k // n + int(k % n > 0)
    ## Calculate j, representing the number n would need to multipled by
    ## to produce a value >= k. That is how n will map to k.
    ## j is k/n if k/n is evenly divisible, and k/n + 1 else
    maxFirst = k / j
    firstRoll = random.randint(1, n)
    ## Do not accept values that would potentialy yield a finalRoll > k
    while (firstRoll > maxFirst):
        firstRoll = random.randint(1, n)
    secondRoll = random.randint(1, n)
    finalRoll = firstRoll * j - secondRoll % j
    return finalRoll
