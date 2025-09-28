# collection: Counter, namedtuple, OrderedDict, deafultdict, deque
from collections import Counter
a = "aaaaaabbbbcccc"
my_counter = Counter(a) # counter Dictionary
print(my_counter)
        # .keys() look out the keys
        # .values() look out values

print(my_counter.most_common()) # To show the most common values
print(my_counter.most_common(1)[0][0]) # To see Elements 
 # [0] to see First Tuple
 # Second [0] to see First Element from First Tuple

print(list(my_counter.elements()))

from collections import namedtuple
point = namedtuple('POint', 'x,y')
pt = point(1, -4)
print(pt)
print(pt.x, pt.y) #print only the value

from collections import OrderedDict
Ordered_dict = OrderedDict()
Ordered_dict['d'] = 4
Ordered_dict['b'] = 2
Ordered_dict['a'] = 1
Ordered_dict['c'] = 3
print(Ordered_dict)

from collections import defaultdict
d = defaultdict(int) # (float) (list)
d['a'] = 1
d['b'] = 2
print(d['d'])

from collections import deque
d = deque()

d.append(1)
d.append(2)
d.appendleft(3)
print(d)

d.pop() #remove the last elemnt or d.popleft or d.clear to clear element
print(d)

d.extendleft([3, 5])  
d.rotate(3)
print(d)