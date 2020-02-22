def palindrome(s):
    return s == s[::-1]

print('Is palindrome?')
print('toot', palindrome('toot'))
print('hoot', palindrome('hoot'))
