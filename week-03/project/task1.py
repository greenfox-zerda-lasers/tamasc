def create_palindrome(word):
    return word + word[::-1]

print(create_palindrome('pear'))
