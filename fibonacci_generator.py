def fibonacci_gen():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci_gen()

for i in fib:
    if i > 7:
        break
    else:
        print('Generatated:', i)

# Generatated: 1
# Generatated: 1
# Generatated: 2
# Generatated: 3
# Generatated: 5
