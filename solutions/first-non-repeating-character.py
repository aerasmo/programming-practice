def first_non_repeating_letter(string):
    for char in string:
        if string.lower().count(char.lower()) == 1:
            return char
    else:
        return ''

# Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.