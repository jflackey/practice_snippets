def myfunc(a, b):
    return a + b

funcs = myfunc

# <function myfunc at 0x010C70B8>
print(funcs)

# <function myfunc at 0x00CF70B8>
print(myfunc)

# prints 5
print(funcs(2, 3))
