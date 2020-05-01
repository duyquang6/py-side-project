### 4.1. Manually Consuming an Iterator

# with open('/etc/passwd') as f:
#     try:
#         while True:
#             line = next(f)
#             print(line, end='')
#     except StopIteration:
#         pass

### 4.2. Delegating Iteration
# class Node:
#     def __init__(self, value):
#         self._value = value
#         self._children = []
#
#     def __repr__(self):
#         return 'Node({!r})'.format(self._value)
#
#     def add_child(self, node):
#         self._children.append(node)
#
#     def __iter__(self):
#         return iter(self._children)
#
#
# # Example
# if __name__ == '__main__':
#     root = Node(0)
#     child1 = Node(1)
#     child2 = Node(2)
#     root.add_child(child1)
#     root.add_child(child2)
#     for ch in root:
#         print(ch)
#     # Outputs Node(1), Node(2)

### 4.3. Creating New Iteration Patterns with Generators
# def frange(start, stop, increment):
#     x = start
#     while x < stop:
#         yield x
#         x += increment
#
#
# print(list(frange(0, 1, 0.125)))

### 4.4. Implementing the Iterator Protocol
# class Node:
#     def __init__(self, value):
#         self._value = value
#         self._children = []
#
#     def __repr__(self):
#         return 'Node({!r})'.format(self._value)
#
#     def add_child(self, node):
#         self._children.append(node)
#
#     def __iter__(self):
#         return iter(self._children)
#
#     def depth_first(self):
#         yield self
#         for c in self:
#             yield from c.depth_first()
#
#
# # Example
# if __name__ == '__main__':
#     root = Node(0)
#     child1 = Node(1)
#     child2 = Node(2)
#     root.add_child(child1)
#     root.add_child(child2)
#     child1.add_child(Node(3))
#     child1.add_child(Node(4))
#     child2.add_child(Node(5))
#
#     for ch in root.depth_first():
#         print(ch)
#     # Outputs Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)

### 4.5. Iterating in Reverse
# a = [1, 2, 3, 4]
# for x in reversed(a):
#     print(x)
#
#
# class Countdown:
#     def __init__(self, start):
#         self.start = start
#
#     # Forward iterator
#     def __iter__(self):
#         n = self.start
#         while n > 0:
#             yield n
#             n -= 1
#
#     # Reverse iterator
#     def __reversed__(self):
#         n = 1
#         while n <= self.start:
#             yield n
#             n += 1

### 4.6. Defining Generator Functions with Extra State
# from collections import deque
#
#
# class linehistory:
#     def __init__(self, lines, histlen=3):
#         self.lines = lines
#         self.history = deque(maxlen=histlen)
#
#     def __iter__(self):
#         for lineno, line in enumerate(self.lines, 1):
#             self.history.append((lineno, line))
#             yield line
#
#     def clear(self):
#         self.history.clear()


### 4.7. Taking a Slice of an Iterator
# def count(n):
#     while True:
#         yield n
#         n += 1
#
#
# c = count(0)
#
# import itertools
#
# for x in itertools.islice(c, 10, 20):
#     print(x)
#

### 4.8. Skipping the First Part of an Iterable
# from itertools import dropwhile
# with open('/etc/passwd') as f:
#     for line in dropwhile(lambda line: line.startswith('#'), f):
#         print(line, end='')
#
# # know exactly numbers of item to skip
# from itertools import islice
# items = ['a', 'b', 'c', 1, 4, 10, 15]
# for x in islice(items, 3, None):
#     print(x)


### 4.9. Iterating Over All Possible Combinations or Permutations
from itertools import permutations, combinations, combinations_with_replacement

items = ['a', 'b', 'c']
for p in permutations(items):
    print(p)
for p in permutations(items, 2):
    print(p)
for p in combinations(items, 2):
    print(p)
for c in combinations_with_replacement(items, 3):
    print(c)

### 4.10. Iterating Over the Index-Value Pairs of a Sequence
# my_list = ['a', 'b', 'c']
# for idx, val in enumerate(my_list, 1):
#     print(idx, val)
# data = [(1, 2), (3, 4), (5, 6), (7, 8)]
# for n, (x, y) in enumerate(data):
#     print(n, x, y)


### 4.11. Iterating Over Multiple Sequences Simultaneously
# xpts = [1, 5, 4, 2, 10, 7]
# ypts = [101, 78, 37, 15, 62, 99]
# for x, y in zip(xpts, ypts):
#     print(x, y)
#
# from itertools import zip_longest
#
# a = [1, 2, 3]
# b = ['w', 'x', 'y', 'z']
# c = ['x', 'y', 'z']
# for i in zip(a, b, c):
#     print(i)
# for i in zip_longest(a, b):
#     print(i)
#
# for i in zip_longest(a, b, fillvalue=0):
#     print(i)
#
# headers = ['name', 'shares', 'price']
# values = ['ACME', 100, 490.1]
# s = dict(zip(headers, values))


### 4.12. Iterating on Items in Separate Containers
from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)

### 4.13. Creating Data Processing Pipelines
## Very important !
# TODO
