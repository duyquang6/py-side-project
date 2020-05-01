# 1.10. Removing Duplicates from a Sequence while Maintaining Order
# a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
#
#
# def dedupe(items, key=None):
#     seen = set()
#     for item in items:
#         val = item if key is None else key(item)
#         if val not in seen:
#             yield item
#             seen.add(val)
#
#
# print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))

# 1.11. Naming a Slice
# ######    0123456789012345678901234567890123456789012345678901234567890'
# record = '....................100          .......513.25     ..........'
# cost = int(record[20:32]) * float(record[40:48])
# SHARES = slice(20, 32)
# PRICE = slice(40, 48)
#
# cost = int(record[SHARES]) * float(record[PRICE])

# 1.12. Determining the Most Frequently Occurring Items in a Sequence
# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
#     'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
#     'my', 'eyes', "you're", 'under'
# ]
#
# from collections import Counter
#
# word_counts = Counter(words)
# top_three = word_counts.most_common(3)
# print(top_three)
#
# # update
# more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
# word_counts.update(more_words)
#
# # perform operations
# a = Counter(words)
# b = Counter(more_words)
# a + b
# a - b


# 1.13. Sorting a List of Dictionaries by a Common Key
# rows = [
#     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
#     {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#     {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
#     {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
# ]
#
# from operator import itemgetter
#
# rows_by_name = sorted(rows, key=itemgetter('fname'))
# rows_by_uid = sorted(rows, key=itemgetter('uid'))
# rows_by_name
# rows_by_uid
#
# rows_by_name = sorted(rows, key=lambda d: d['fname'])
# rows_by_uid = sorted(rows, key=lambda d: d['uid'])
# rows_by_name
# rows_by_uid
#
# rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
# rows_by_lfname
#
# rows_by_lfname = sorted(rows, key=lambda d: (d['lname'], d['fname']))
# rows_by_lfname


# 1.14. Sorting Objects Without Native Comparison Support
# class User:
#     def __init__(self, user_id):
#         self.user_id = user_id
#
#     def __repr__(self):
#         return 'User({})'.format(self.user_id)
#
#
# users = [User(23), User(3), User(99)]
# users
# sorted(users, key=lambda u: u.user_id)
#
# from operator import attrgetter
# sorted(users, key=attrgetter('user_id'))


# 1.15. Grouping Records Together Based on a Field
# rows = [
#     {'address': '5412 N CLARK', 'date': '07/01/2012'},
#     {'address': '5148 N CLARK', 'date': '07/04/2012'},
#     {'address': '5800 E 58TH', 'date': '07/02/2012'},
#     {'address': '2122 N CLARK', 'date': '07/03/2012'},
#     {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
#     {'address': '1060 W ADDISON', 'date': '07/02/2012'},
#     {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
#     {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
# ]
#
# from operator import itemgetter
# from itertools import groupby
#
# # Sort by the desired field first
# rows.sort(key=itemgetter('date'))
#
# # Iterate in groups
# for date, items in groupby(rows, key=itemgetter('date')):
#     print(date)
#     for i in items:
#         print('    ', i)

# 1.16. Filtering Sequence Elements
# mylist = [1, 4, -5, 10, -7, 2, 3, -1]
# [n for n in mylist if n > 0]
# pos = (n for n in mylist if n > 0)
# pos
# next(pos)
#
# values = ['1', '2', '-3', '-', '4', 'N/A', '5']
# def is_int(val):
#     try:
#         x = int(val)
#         return True
#     except ValueError:
#         return False
#
# ivals = list(filter(is_int, values))
# print(ivals)

# 1.17. Extracting a Subset of a Dictionary
# prices = {
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75
# }
#
# # Make a dictionary of all prices over 200
# p1 = {key: prices[key] for key in prices.keys() if prices[key] > 200}
# p1 = {key: value for key, value in prices.items() if value > 200}
#
# # Make a dictionary of tech stocks
# tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
# p2 = {key: value for key, value in prices.items() if key in tech_names}


# 1.18. Mapping Names to Sequence Elements
# from collections import namedtuple
#
# Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
# sub = Subscriber('jonesy@example.com', '2012-10-19')
# sub
# sub.addr
# sub.joined
# len(sub)
#
# Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# # Create a prototype instance
# stock_prototype = Stock('', 0, 0.0, None, None)
# # Function to convert a dictionary to a Stock
# def dict_to_stock(s):
#     return stock_prototype._replace(**s)
#
# a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
# dict_to_stock(a)


# 1.19. Transforming and Reducing Data at the Same Time
# nums = [1, 2, 3, 4, 5]
# # bad performance
# s = sum([x * x for x in nums])
# # recommend
# s = sum(x * x for x in nums)  # equivalent to sum((x * x for x in nums))


# 1.20. Combining Multiple Mappings into a Single Mapping
# from collections import ChainMap
#
# a = {'x': 1, 'z': 3}
# b = {'y': 2, 'z': 4}
# c = ChainMap(a, b)
# c
# c['z'] = 10
# c['w'] = 40
# del c['x']
# a
#
# values = ChainMap()
# values['x'] = 1
# # Add a new mapping
# values = values.new_child()
# values['x'] = 2
# # Add a new mapping
# values = values.new_child()
# values['x'] = 3
# values
# ChainMap({'x': 3}, {'x': 2}, {'x': 1})
# values['x']  # 3
# # Discard last mapping
# values = values.parents
# values['x']  # 2
# # Discard last mapping
# values = values.parents
# values['x']  # 1
# values
# ChainMap({'x': 1})
