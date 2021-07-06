

def solution(a, b):
    result = 0
    for i in range(len(a)):
        result +=  a[i] * b[i] 
    return result

a = [-1,0,1]
b = [1,0,-1]

result = solution(a,b)
print(result)