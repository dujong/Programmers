def solution(n):

    N = bin(n).count('1')
    b = n + 1

    while True:
        M = bin(b).count('1')

        if N == M:
            return b

        b = b + 1

n = 78

print(solution(n))