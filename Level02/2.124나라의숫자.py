def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        print(n)
        answer = '124'[n%3] + answer
        print(answer)
        n //= 3
    return answer


n = 15
print(solution(n))

