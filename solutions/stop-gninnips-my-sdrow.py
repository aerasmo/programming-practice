def spin_words(sentence):
    return " ".join([ w[::-1] if len(w) >= 5 else w for w in sentence.split(" ")])

# Write a function that takes in a string of one or more words, and returns the same string,
#   but with all five or more letter words reversed (like the name of this kata).


# spinWords("Hey fellow warriors") => "Hey wollef sroirraw" 
# spinWords("This is a test") => "This is a test" 
# spinWords("This is another test") => "This is rehtona test"