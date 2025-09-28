from itertools import product # for Searching how many combination
a = [1, 2]
b = [2, 4]
prod = product(a,b) # , repeat=2)
print(list(prod))

from itertools import permutations

a = [1, 2, 3]
perm = permutations(a) # ,2 )  specify the second argument (limitting the lenght)
print(list(perm))

from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
comb_wr = combinations_with_replacement (a, 2)
print(list(comb_wr))

from itertools import accumulate
import operator
a = [1, 2, 3,4]
acc = accumulate(a) # func=operator.mul) #Change to be MUltiple instead of Plus
 # func=max) The number after the biggest will change to it and on
print(a)
print(list(acc))

from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_by = groupby(a, key=smaller_than_3) # key=lambda x: x,3) short key
for key, value in group_by:
    print(key, list(value))

person = [{'name': 'Tim', 'age': 25}, {'name': 'Ton', 'age': 25}, 
          {'name': 'Tim', 'age': 28}, {'name': 'Son', 'age': 23}]


group_by = groupby(person, key=lambda x: x['age']) # key=lambda x: x,3) short key
for key, value in group_by:
    print(key, list(value))

from itertools import count, cycle, repeat

# infinate loop
for i in count(10):
    print(i)
    if i == 15:
        break

a = [1, 2, 3]
for i in repeat(1, 4):
    print(i)
