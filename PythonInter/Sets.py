myset = {1, 2, 3, 4, 5} or set([1, 2, 3, 4, 5]) #Creating a set

#set not allow duplicate

myset = set()

myset.add(1) #Adding item to a set
myset.add(2)
myset.add(3)

# myset.remove(2) #Removing item from a set # IF you put 4 it will be error
myset.discard(4) #Removing item from a set #nothing will be re
myset.pop() #Removes and returns an arbitrary set item

print(myset)

for i in myset: #Looping through a set
    print(i)

odds = {1, 3, 5}
evens = {2, 4, 6}
primes = {2, 3, 5, 7}

 # u = odds.union(evens) #Union of two sets
# print(u)

i = odds.intersection(primes) #Intersection of two sets
print(i) # {3}


setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3, 6, 7, 8}
diff = setA.difference(setB) #Difference of two sets
print(diff) # {4, 5}

# diff = setB.symmetric_difference(setA) #Symmetric difference of two sets
# print(diff) # {6, 7, 8}

# setA.update(setB) #Update setA with setB
# print(setA)

# setA.intersection_update(setB) #Update setA with intersection of setB
# print(setA) # {1, 2, 3}

# setA.difference_update(setB) #Update setA with difference of setB
# print(setA) # {4, 5}

# setA.symmetric_difference_update(setB) #Update setA with symmetric difference of setB
 #print(setA) # {4, 5, 6, 7, 8}

setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3}
setC = {6, 7, 8}

print(setB.issubset(setA)) #Check if setB is subset of setA #True

print(setB.issuperset(setA)) #Check if setA is superset of setB #True

print(setA.isdisjoint(setC)) #Check if setA and setB have no common elements #False

# Becarefull !!!!
# setB = set(setA) or setB = setA.copy() #Copying a set

a = frozenset([1, 2, 3, 4, 5]) #Creating a frozenset (immutable set)    
# remove or add (Update) will not work except Uni. Inter. Diff.
print(a) #frozenset({1, 2, 3, 4, 5})