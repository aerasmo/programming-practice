def solution(string,markers):
    statements = string.split('\n')
    words = []
    for statement in statements:
        sentence = ''
        for i in range(len(statement)):
            if statement[i] in markers:
                break
            sentence += statement[i]
        words.append(sentence.strip())
    return '\n'.join(words)

# var result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# // result should == "apples, pears\ngrapes\nbananas"