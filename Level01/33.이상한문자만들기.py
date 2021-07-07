def solution(s):
    answer = s.split(' ')
    for i in range(len(answer)):
        word = list(answer[i])
        for j in range(len(word)):
            if j % 2 == 0:
                word[j] = word[j].upper()
            else:
                word[j] = word[j].lower()
        answer[i] = ''.join(word)
    return ' '.join(answer)

s = "try hello world"
result = solution(s)
print(result)