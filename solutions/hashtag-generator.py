def generate_hashtag(s):
    if not s: return False

    l = [w.strip().capitalize() for w in s.split(" ")]
    hashtag = "#" + "".join(l)

    if len(hashtag) >= 140: 
        return False
    
    return hashtag



s = input()
print(generate_hashtag(s))