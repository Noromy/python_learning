# Immutable Object
org = 5
cpy = org
cpy = 6 #This will be independent 
print(cpy)
print(org)

# Mutable Object
org1 = [0, 1, 2, 3, 4]
cpy1 = org1
cpy1[0] = -10 # This is not make a new copy it just inside
print(cpy1)
print(org1)


# - shallow copy: one level deep, only refrences of nested child object
# - deep copy: full independent copy

#Shallow Copy
import copy
org2 = [0, 1, 2, 3, 4]
cpy2 = copy.copy(org2)
# Other way
# cpy2 = org2.copy()
# cpy2 = list[org2]
# cpy2 = org[:]
cpy2 = -10 # This is not make a new copy it just inside
print(cpy2)
print(org2) # The original didn't get affected

# Shallow copy is only one level deep cant be in Nested object like :
# org2 = [[0, 1, 2, 3, 4], [1, 2, 3]] or the original will be affected

#If you want to copy a nested you need a deep copy
org3 = [[0, 1, 2, 3, 4], [1, 2, 3]]
cpy3 = copy.deepcopy(org3)
# Other way
# cpy2 = org2.copy()
cpy3[0][1] = -10 # This is not make a new copy it just inside
print(cpy3)
print(org3)

# The use of copy in nested object   
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

p1 = Person('Alex', 27)
p2 = Person('Jo mama', 50)

company = Company(p1, p2)

Company_code = copy.deepcopy(company)
Company_code.boss.age = 76

print(company.boss.age)
print(Company_code.boss.age)
