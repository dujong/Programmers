def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
    return answer

x = 2
n = 5
result = solution(x,n)
print(result)
