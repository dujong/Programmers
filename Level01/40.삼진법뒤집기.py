def solution(n):
    rev_base = []
    result = 0
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base.append(mod)
    rev_base.reverse()
    a = 1
    for i in range(len(rev_base)):
        result += rev_base[i] * a
        a *= 3

    return result

n = 125
result = solution(n)
print(result)