def solution(s):
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = s[i].lower()
        s[i] = s[i].capitalize()
    answer = ' '.join(s)
    return answer

s = "3people unFollowed me"
print(solution(s))