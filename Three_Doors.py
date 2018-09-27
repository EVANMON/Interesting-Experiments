#Three Doors Problems
#Sep 26, 2018

from random import randint
import numpy as np

THREE_DOORS = [1, 2, 3]

valid_example = 0
behind_selected_door = 0
behind_other_door = 0

while valid_example < 10000:
    car_door = randint(1, 3)
    doors = np.zeros(3, dtype=int)
    doors[car_door-1] = 1

    choice = randint(1, 3)
    left_doors = list(set(THREE_DOORS) - {choice})
    if doors[left_doors[0]-1] == 0:
        open_door = left_doors[0]
    else:
        open_door = left_doors[1]
    """
    Actually, from here, we can see that the open door 
    doesn't have any influence on the result at all.
    So the probability that car behind the first selected door is 1/3! 
    """

    valid_example += 1
    if doors[choice-1] == 1:
        behind_selected_door += 1
    else:
        behind_other_door += 1
assert behind_other_door + behind_selected_door == valid_example
print("The probability of being behind the selected door: %.4f"
      %(behind_selected_door / valid_example))
print("The probability of being behind the other door: %.4f"
      %(behind_other_door / valid_example))