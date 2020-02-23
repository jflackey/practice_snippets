def palindrome(word):
    """Return True if the given word is a palindrome."""
    return word == word[::-1]

# Is RACECAR a palindrome?: True
print('Is RACECAR a palindrome?:', palindrome('RACECAR'))

# Is UNICORN a palindrome?: False
print('Is UNICORN a palindrome?:', palindrome('UNICORN'))

# 'Return True if the given word is a palindrome.'
print(repr(palindrome.__doc__))
