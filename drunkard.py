# Drunkard Problem
# Sep 26, 2018
import random
import numpy as np

BARS = 3
HOME_PROB = 0.1
BAR_PROB = (1 - HOME_PROB) / BARS

valid_example = 0
at_home = 0
at_bar = 0

# print(HOME_PROB + BARS * BAR_PROB)
# assert (HOME_PROB + BARS * BAR_PROB) == 1.0
while valid_example < 100000:
    drunkard_status = np.zeros(BARS+1, dtype=int)
    prob = random.uniform(0, 1)
    if prob <= HOME_PROB:
        drunkard_status[0] = 1 #at home
    else:
        bar_N = 1
        while bar_N <= BARS:
            if prob <= HOME_PROB + bar_N * BAR_PROB:
                drunkard_status[bar_N] = 1 #at bar N
                break
            bar_N += 1 #!!!!

    if drunkard_status[0] == 1:
        valid_example += 1
        at_home += 1
    elif drunkard_status[-1] == 1:
        valid_example += 1
        at_bar += 1
    else:
        continue

assert at_home + at_bar == valid_example
print("The probability of being at home is %.2f" %(at_home / valid_example))
print("The probability of being at bar is %.2f" %(at_bar / valid_example))