def search_palindromes(palindrome):
    palindromes=[]
    for chars in range(3,len(palindrome), 1):
        for i in range(0,len(palindrome)-chars+1):
            test_word=palindrome[i:i+chars]
            if test_word == test_word[::-1]:
                palindromes.append(test_word)
    return palindromes

print(search_palindromes('101dog goat dad duck dad doodle neveroomoor'))

# it outputs every palindrome, even those which are part of bigger palindrome :(
