# Various ways to print

name = "John"
age = 40

# Hello, John. You are 40.
print(f"Hello, {name}. You are {age}.")

# john is funny.
print(f"{name.lower()} is funny.")

# Multi-line print
message = f"Hi {name}. " \
f"You are {age}. "
print(message)

person_example= {'name': 'Joe', 'age': 40}
f"The name is {person_example['name']}, aged {person_example['age']}."

# Hello, John. You are 40.
print("Hello, {}. You are {}.".format(name, age))

# Hello, John. You are 40.
print("Hello, {1}. You are {0}.".format(age, name))

# Hello, Jane. You are 41.
person = {'name': 'Jane', 'age': 41}
print("Hello, {name}. You are {age}.".format(
    name=person['name'], age=person['age']))

# Hello, Jane. You are 41.
print("Hello, {name}. You are {age}.".format(**person))

first_name = "Joe"
last_name = "Person"

# Hello, Joe Person.
print("Hello, {first_name} {last_name}.".format(
    first_name=first_name, last_name=last_name))
