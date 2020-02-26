# Functions are first-class
def yell(text):
    return text.upper() + '!'

print(yell('hello'))

# Assign yell function to bark
bark = yell
print(bark('woof'))

# Delete yell, bark references yell
del yell
print(bark('hey'))
print('Function "bark"references:', bark.__name__)

# Pass function to function
def greet(func):
    greeting = func('Hi, I am a Python programmer')
    print(greeting)


greet(bark)

# Map function to list
print(list(map(bark, ['hello', 'hey', 'hi'])))

# Nested function


def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)


print(speak('Hello world'))
