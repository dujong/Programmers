def solution(a, b):
    c = 0
    for i in range(min(a,b),max(a,b)+1):
        c += i
    return c

a = 5
b = 3
c = solution(a,b)
print(c)