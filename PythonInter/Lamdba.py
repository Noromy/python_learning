# lamdba arguments: expression
add10 = lambda x: x + 10
print(add10(5))
# this is just a short function
def add10_func(x):
    return x + 10

mult = lambda x,y: x*y
print(mult(2, 7))

point2SD = [(1,2), (15,4), (3,8), (8, 16)]

point2SD_sorted = sorted(point2SD, key=lambda x: x[1])

print(point2SD_sorted)

#map (func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2 ,a)
print(list(b))

#better use this
c = [x*2 for x in a]
print(c)

#filter (func, seq)

a = [1, 2, 3, 4, 5]
b = filter(lambda x: x%2==0 ,a) #only show the value True
print(list(b))

c =[x for x in a if x%2==0]
print(c)

#reduce (func, seq)

from functools import reduce

a = [1, 2, 3, 4, 5]

product_a = reduce(lambda x,y: x*y, a) 
print(product_a) 
