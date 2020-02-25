def incrementer():
    i = 1
    while True:
        yield i
        i += 1

inc = incrementer()

print(next(inc)) # yeilds 1
print(next(inc)) # yeilds 2
print(next(inc)) # yeilds 3
