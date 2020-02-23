import collections

c = collections.Counter('hello')

print(c)
# Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

print(c.most_common(3))
# [('l', 2), ('h', 1), ('e', 1)]
