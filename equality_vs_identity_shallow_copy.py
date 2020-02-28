# comparison operators - equality vs identity (shallow copy)

a = [1, 2, 3,]
b = a

print(a == b) # True
print(a is b) # True

c = [1, 2, 3,]
d = list(c) # create

print(c == d) # True
print(c is d) # False
