def is_isogram(s):
    string = s.lower()
    return len(set(string)) == len(string)

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that
# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false # -- ignore letter case