def solution(n):
    n1 = list(map(int, str(n)))
    n1.sort(reverse=True)
    n2 = ''.join(map(str, n1))
    return int(n2)

n = 118372
result = solution(n)
print(result)