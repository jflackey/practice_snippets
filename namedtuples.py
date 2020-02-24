from collections import namedtuple

Car = namedtuple('Car', 'make model color')

my_car = Car('Mercedes', 'S', 'Silver')

print(my_car.make)
print(my_car.model)
print(my_car.color)
