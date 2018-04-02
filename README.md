# diceRolling

*Written in Python 2.7.12.*

*I have not tested in Python 3.*

Python functions for rolling an n-sided die to produce 1 through k possible outputs with equal probabilities.

roll6() rolls a 6-sided die to produce 1-10 as possible outputs with equal probabilities.

roll(n, k) rolls an n-sided die to produce 1-k as possible outputs. However, n and k are constrained such that k must be <= n^2.

rollAny(n, k) rolls an n-sided die to produce 1-k as possible outputs, for any n and k -- or at least I think it does. If k is exponentially larger than n, this could require a lot of die rolls.
