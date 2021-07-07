def f(n,m):
    if m>n:
        tmp = n
        n = m
        m = tmp
    while m > 0:
        c = m
        m = n % m
        n = c
    return n
def g(n,m):
    return n * m // f(n,m)
    
def solution(n, m):
    a = f(n,m)
    b = g(n,m)
    return a, b

n = 3
m = 12

a, b = solution(n,m)
print(a,b)