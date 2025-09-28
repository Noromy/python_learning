def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()


# for i in g:
  #  print(i)
'''
value = next(g)
print(value) # 1 (Output) #You have to use next() to run the generator or you can use for loop

value = next(g)
print(value) # 2

value = next(g)
print(value) # 3
'''
# print(sum(g)) # Output : 6
print(sorted(g))

def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)

print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))

#for i in cd:
 #   print(i)

import sys
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


myList = firstn(10)
print(myList)


def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1
    
myList_G = firstn_generator(10)
print(next(myList_G))

print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000))) # Generator is samller


def fibonacci(limit):
    # 0 1 1 2 3 5 8 13 21
    a, b =0, 1
    while a <limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)

for i in fib:
    print(i) 



def TriangleFib(rows):
    fib = [0,1]
    while len(fib) < rows * (rows +1) // 2:
        fib.append(fib[-1] + fib[-2])
    Index = 0
    for r in range(1, rows + 1):
        line = fib[Index: Index + r]
        Index += r
        print(" " * (rows -r) * 2, *line)
    
TriangleFib(7)


