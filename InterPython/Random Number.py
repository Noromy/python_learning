import random

a = random.random()
    # random.uniform(1, 10) Range 1 to 10 (Decimal : 3,5..)
    # random.randint(1, 10) Range 1 to 10 (Integral : 3 )
    # random.randrage(1,10) The last number is excluded (1 to 9)
    # random.normalvariate(0, 1) Random number with normal distribution (mean, standard deviation) Gaussian

print(a)

mylist = list ("ABCDEFGH")
a = random.choice(mylist)  # Pick a random element from the list
    #random.choices(mylist, k=3) Pick multiple random elements from the list (with replacement)
    #random.sample(mylist, k=3) Pick multiple random elements from the list (without replacement)
print(a)

mylist1 = list ("ABCDEFGH")
b = random.shuffle(mylist1)  # Shuffle the list
print(mylist1)

random.seed(1)  # Set the seed for reproducibility
c = random.random()
c = random.randint(1,100)
print(c)
random.seed(1)  # Set the seed for reproducibility
d = random.random()
d = random.randint(1,100)
print(d)


import secrets

a = secrets.randbelow(10) # Random number below 10
 # secrets.randbits(4) # Random number with 4 bits (0 to 15)
 # secrets.choice(mylist) # Pick a random element from the list (cryptographically secure)
print(a)

import numpy as np

a = np.random.rand(3)  # Array of 3 random numbers (Decimal : 0.234, 0.567, 0.890)
    # np.random.randint(1, 10, size=3) Array of 3 random numbers (Integral : 3, 5, 7) to make a tuple (3, 4)
    # np.random.randn(3) Array of 3 random numbers with normal distribution (mean=0, std=1)

print(a)

np.random.seed(1)
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr)  # Shuffle the array along the first axis
print(arr)