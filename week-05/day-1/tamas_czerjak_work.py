import string

def anagramm(string1, string2):
    if not isinstance(string1, str) or not isinstance(string2, str):
        raise TypeError("Don't be silly, input parameters must be a strings")
    string1 = [item for item in sorted(string1.lower()) if item != ' ']
    string2 = [item for item in sorted(string2.lower()) if item != ' ']
    return string1 == string2

def count_letters(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Don't be silly, input parameter must be a string")
    input_string = [item for item in input_string if item in string.ascii_letters]
    dictionary = {}
    for character in input_string:
        if character.lower() in dictionary:
            dictionary[character.lower()] += 1
        else:
            dictionary[character.lower()] = 1
    return dictionary
