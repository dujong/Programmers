def solution(n):
    answer = list(map(int, str(n)))
    answer.reverse()
    return answer
    

n = 12345
result = solution(n)
print(result)