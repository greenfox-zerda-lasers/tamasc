# not working

def search_palindromes(palindrome):
    candidates=[]
    palindromes=[]
    for i in range(0, len(palindrome)):
        for j in range(i, len(palindrome)):
            if palindrome[i] == palindrome [j]:
                candidates.append(palindrome[i:j])
    for x in candidates:
        if x == x[::-1]:
            palindromes.append(x)
    return palindromes

print(search_palindromes('dog goat dad duck doodle never'))
