def solution(s):
    answer = list(map(int, s.split(' ')))
    return str(min(answer)) + ' ' + str(max(answer))

s = "-11 -21 -31 -41"
print(solution(s))