def solution(strings, n):
    answer = list()
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()

    for i in range(len(strings)):
        answer.append(strings[i][1:])
    return answer

strings = ["sun", "bed", "car"]
n = 1
result = solution(strings, n)
print(result)